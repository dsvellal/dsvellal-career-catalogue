"""Batch ingest ~/Downloads/Career into the digital twin knowledge graph.

Classifies files based on filename + folder context (no LLM calls needed).
The folder structure and filenames are extremely descriptive.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from twin.db import get_connection, init_schema
from twin.ingestion.extractors import extract
from twin.ingestion.pipeline import ingest_pre_classified

CAREER_DIR = Path.home() / "Downloads" / "Career"
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "knowledge.duckdb"

# Sensitive file patterns to skip
SENSITIVE_PATTERNS = re.compile(
    "|".join([
        r"compensation", r"salary", r"payslip", r"pay_slip", r"hike",
        r"F&F", r"settlement", r"tax", r"PF.?transfer",
        r"RSU", r"bonus", r"CTC", r"LTI", r"form.?12BB", r"insurance",
        r"ITCS", r"encashment", r"12BB", r"american.?express",
        r"payslip_details", r"F16_FY", r"PHL_LTI",
        r"PF_Withdrawal", r"Online_PF",
        r"canceled.?cheque", r"pan.?card", r"passport",
        r"2020-21_Philips-Annual", r"2022_Philips_Compenstation",
        r"2023_Philips_Compenstation", r"Salary.?Confirmation",
        r"2020-21_Philips-AnnualCompensatioin",
    ]),
    re.IGNORECASE,
)

SKIP_EXTENSIONS = {".zip", ".msi", ".wrf"}


def should_skip(path: Path) -> bool:
    if path.name == ".DS_Store":
        return True
    if path.suffix.lower() in SKIP_EXTENSIONS:
        return True
    if SENSITIVE_PATTERNS.search(path.name):
        return True
    if "DocsSubmittedDuringJoining" in str(path):
        return True
    if "/Copy of " in str(path):
        return True
    return False


def classify_from_context(path: Path) -> dict:
    """Derive classification from filename and folder structure."""
    rel = path.relative_to(CAREER_DIR)
    parts = rel.parts
    name = path.stem
    folder = parts[0] if len(parts) > 1 else ""
    subfolder = parts[1] if len(parts) > 2 else ""

    classification = {
        "type": "other",
        "dates": [],
        "projects": [],
        "skills": [],
        "people": [],
        "organizations": [],
        "claims": [],
        "confidence": 0.85,
    }

    # Extract dates from filename (YYYYMMDD or YYYY-MM-DD patterns)
    date_matches = re.findall(r"(\d{4})(\d{2})(\d{2})", name)
    if not date_matches:
        date_matches = re.findall(r"(\d{4})-(\d{2})-(\d{2})", name)
    if not date_matches:
        # Try YYYYMM pattern
        ym = re.findall(r"(\d{4})(\d{2})(?:_|\b)", name)
        if ym and int(ym[0][1]) <= 12:
            date_matches = [(ym[0][0], ym[0][1], "01")]

    for dm in date_matches:
        y, m, d = dm
        if 2000 <= int(y) <= 2026 and 1 <= int(m) <= 12:
            classification["dates"].append({
                "date": f"{y}-{m}-{d}",
                "context": name,
            })

    # Organization from folder
    if folder.startswith("2007 IBM"):
        classification["organizations"].append({"name": "IBM", "role": "employer"})
        _classify_ibm(classification, name, subfolder)
    elif folder.startswith("2013 Exeter"):
        classification["organizations"].append({"name": "Exeter Group / OneGate", "role": "employer"})
        _classify_exeter(classification, name, subfolder, parts)
    elif folder.startswith("2016 Amazon"):
        classification["organizations"].append({"name": "Amazon", "role": "employer"})
        _classify_amazon(classification, name, subfolder, parts)
    elif folder.startswith("2018 Philips"):
        classification["organizations"].append({"name": "Philips", "role": "employer"})
        _classify_philips(classification, name, subfolder, parts)
    elif folder == "Certificates" or folder == "LinkedIn Certificates":
        _classify_certificate(classification, name)
    elif folder == "Feedbacks":
        _classify_feedback(classification, name, subfolder, parts)
    elif folder == "MarksCard":
        _classify_education(classification, name)
    elif folder == "My Talks":
        _classify_talk(classification, name, parts)
    elif folder == "Other Offer Letters":
        _classify_other_offers(classification, name)
    elif folder == "Resume":
        _classify_resume(classification, name, parts)
    elif folder == "Students feedbacks":
        _classify_student_feedback(classification, name)
    elif folder == "Tech Artifacts" or folder == "Tech stuff":
        _classify_tech_artifact(classification, name)
    elif folder == "Yoga Instructors Course SVYASA":
        _classify_yoga(classification, name)
    else:
        _classify_root(classification, name)

    return classification


def _classify_ibm(c: dict, name: str, subfolder: str) -> None:
    if "Offer" in name:
        c["type"] = "other"
        c["claims"].append("Offered Associate Software Engineer position at IBM India")
        c["skills"].extend(["Java", "Software Development"])
        if not c["dates"]:
            c["dates"].append({"date": "2006-08-24", "context": "IBM offer letter"})
    elif "Business Commitment" in name:
        c["type"] = "performance_review"
        c["skills"].extend(["Java", "Software Development", "Expeditor Toolkit"])
        c["projects"].append("Expeditor Toolkit")
        if "2008" in name:
            c["dates"].append({"date": "2008-01-01", "context": "2008 PBC"})
        elif "2009" in name:
            c["dates"].append({"date": "2009-01-01", "context": "2009 PBC"})
    elif "Experience" in name:
        c["type"] = "other"
        c["claims"].append("Worked at IBM from 10/07/2007 to 29/03/2013")
        c["dates"].append({"date": "2013-04-29", "context": "Experience letter issued"})
    elif "Provisional" in name or "Relieving" in name:
        c["type"] = "other"
        c["claims"].append("Resigned from IBM, last date 29/03/2013")
        c["dates"].append({"date": "2013-03-29", "context": "Last working day at IBM"})


def _classify_exeter(c: dict, name: str, subfolder: str, parts: tuple) -> None:
    if "Appreciation" in str(parts) or subfolder == "Exeter - Appreciation Emails":
        c["type"] = "email_appreciation"
        _parse_exeter_appreciation(c, name)
    elif "PPM" in name or "PerformanceReview" in name:
        c["type"] = "performance_review"
        c["claims"].append(f"Performance review at Exeter: {name}")
    elif "Offer" in name:
        c["type"] = "other"
        c["claims"].append("Job offer from Exeter Group")
    elif "Relieving" in name or "Experience Certificate" in name:
        c["type"] = "other"
        c["claims"].append("Relieved from Exeter with experience certificate")
    elif "KRA" in name:
        c["type"] = "project_doc"
        c["claims"].append("Key Result Areas for Exeter 2015-16")
    elif "ID Card" in name:
        c["type"] = "other"
    elif "Name Change" in name:
        c["type"] = "other"
        c["claims"].append("Company name changed from j235 to Exeter")


def _parse_exeter_appreciation(c: dict, name: str) -> None:
    """Parse the highly structured Exeter appreciation email filenames."""
    # Format: Category_Description_DateContext.pdf
    categories = {
        "DoTheRightThing": "doing the right thing",
        "Leadership&Ownership": "leadership and ownership",
        "LeadershipInOrganizingEvents": "leadership in organizing events",
        "Collaboration": "collaboration",
        "TakingThingsToConclusion": "taking things to conclusion",
        "SpreadingKnowledge&Practices": "spreading knowledge and practices",
        "TroubleShooting&DefectOwnership": "troubleshooting and defect ownership",
        "ReleaseSupport": "release support",
        "ClientSuccess": "client success",
        "TeamMentoring": "team mentoring",
        "GiveBack": "giving back to organization",
        "TrustCharacterCredibility": "trust, character, and credibility",
        "RiskEscalation&Mitigation": "risk escalation and mitigation",
        "KeepingStakeHoldersInformed": "keeping stakeholders informed",
        "GeneralThankYouNote": "general thank you",
        "ItsGoodToCelebrate": "celebration",
        "OfficialNotes": "official announcement",
        "TRMS": "TRMS recognition",
    }

    for cat_key, cat_desc in categories.items():
        if name.startswith(cat_key):
            c["claims"].append(f"Recognized for {cat_desc}")
            # Extract the description part
            remainder = name[len(cat_key):].lstrip("_")
            c["skills"].extend(_extract_skills_from_description(remainder))
            break
    else:
        # Try prefix matching for other patterns
        if "PPM" in name:
            c["type"] = "performance_review"
            c["claims"].append("Quarterly performance review at Exeter")

    # Extract people names from description
    people_patterns = {
        "Jonah": "manager",
        "Jonathan": "US counterpart",
        "Krishna": "team lead",
        "Rob": "colleague",
        "Brett": "client",
        "Chevy": "colleague",
        "Kavya": "mentee",
        "Satheesh": "mentee",
    }
    for person, role in people_patterns.items():
        if person in name:
            c["people"].append({"name": person, "role": role})

    # Extract project/technology mentions
    project_mentions = {
        "Edifects": "Edifecs Integration",
        "Edifecs": "Edifecs Integration",
        "Apollo": "Apollo Platform",
        "Liferay": "Liferay Portal",
        "PlanSelection": "Plan Selection Module",
        "OAPC": "OAPC",
        "OPADL": "OPADL Transforms",
        "MyAccounts": "My Accounts Module",
        "GlobalSession": "Global Session Management",
        "AgeOut": "Age Out Feature",
        "AgeOff": "Age Off Feature",
    }
    for key, project in project_mentions.items():
        if key in name:
            c["projects"].append(project)


def _extract_skills_from_description(desc: str) -> list[str]:
    """Extract skills from Exeter appreciation descriptions."""
    skill_keywords = {
        "DesignPattern": "Design Patterns",
        "CodingGuidelines": "Coding Guidelines",
        "CodeQualityMetrics": "Code Quality",
        "AgileProcess": "Agile",
        "Agile": "Agile",
        "ServerBounce": "Server Administration",
        "Logging": "Logging & Observability",
        "Performance": "Performance Optimization",
        "RCA": "Root Cause Analysis",
        "ClearTextPassword": "Security",
        "Yoga": "Yoga Instruction",
        "Recruitment": "Recruitment",
        "TExeter": "Knowledge Sharing",
    }
    skills = []
    for key, skill in skill_keywords.items():
        if key in desc:
            skills.append(skill)
    return skills


def _classify_amazon(c: dict, name: str, subfolder: str, parts: tuple) -> None:
    if "Appreciation" in str(parts):
        c["type"] = "email_appreciation"
        _parse_amazon_appreciation(c, name)
    elif "Annual Review" in name or "ForteReview" in name:
        c["type"] = "performance_review"
        c["claims"].append(f"Annual performance review at Amazon")
    elif "Offer" in name or "Candidate Information" in name:
        c["type"] = "other"
        c["claims"].append("Job application/offer at Amazon")
    elif "Resignation" in name:
        c["type"] = "other"
        c["claims"].append("Resignation from Amazon")
    elif "Relieving" in name:
        c["type"] = "other"
        c["claims"].append("Relieved from Amazon")
    elif "Employment" in name or "employement" in name:
        c["type"] = "other"
        c["claims"].append("Employment at Amazon")
    elif "Profile" in name or "Phonetool" in name:
        c["type"] = "other"
        c["claims"].append("Amazon internal profile")
    elif "Onboarding" in name:
        c["type"] = "other"
        c["claims"].append("Amazon onboarding documentation")
    elif "ExitInterview" in name:
        c["type"] = "other"
        c["claims"].append("Amazon exit interview feedback")
    elif "Project well done" in name:
        c["type"] = "email_appreciation"
        c["claims"].append("Project well done recognition at Amazon")
    elif "ID Card" in name:
        c["type"] = "other"
    elif "Leaves" in name:
        c["type"] = "other"


def _parse_amazon_appreciation(c: dict, name: str) -> None:
    """Parse Amazon appreciation email filenames."""
    appreciations = {
        "MigrationOfMySQLToRDS": ("MySQL to RDS Migration", ["MySQL", "AWS RDS", "Database Migration"]),
        "XML_Parser": ("New XML Parser", ["Java", "XML Parsing"]),
        "XML_Migration_Strategy_SOP": ("XML Migration SOP", ["Technical Writing", "Migration Strategy"]),
        "XML_Migration_SOP": ("XML Migration SOP feedback", ["Process Documentation"]),
        "FindingABugViaUserTesting": ("Bug found via user testing", ["Quality Assurance", "User Testing"]),
        "ACSCS2016_Hackday": ("Won ACSCS 2016 Hackday", ["Innovation", "Hackathon"]),
        "AmazonLinuxMigration": ("Amazon Linux Migration", ["Linux", "Infrastructure Migration"]),
        "ScrumWorkshop": ("Scrum workshop facilitation", ["Scrum", "Agile Coaching"]),
        "InterviewFeedback": ("Interview process improvement", ["Interviewing", "Hiring"]),
        "InterviewQuestions": ("Interview question design", ["Interviewing", "Hiring"]),
        "IP_TradeSecret": ("Intellectual property contribution", ["Innovation", "IP"]),
        "DesignDocumentWellWritten": ("Design document quality", ["Technical Writing", "Software Design"]),
        "OAPC": ("OAPC launch/unblock", ["Java", "Service Development"]),
        "SVA": ("SVA service work", ["Java", "Service Development", "Payments"]),
        "OnBoardingGuide": ("Created onboarding guide", ["Documentation", "Mentoring"]),
        "RiPE": ("RiPE service", ["Java", "API Development"]),
        "BookmarsWikiPage": ("Knowledge documentation", ["Documentation"]),
        "IndiaTechConf": ("India Tech Conference presentation", ["Public Speaking", "Technical Leadership"]),
        "AusterService": ("SVA Auster service error handling", ["Error Handling", "Service Reliability"]),
        "BulkActionTool": ("SVA Bulk Action Tool", ["Java", "Tooling", "Automation"]),
        "TRMS_SHOWTIME": ("TRMS Showtime recognition", ["Innovation"]),
        "PO_Facilitator": ("Product Owner facilitator", ["Product Ownership", "Agile"]),
        "GCOptimisation": ("GC optimisation profiler analysis", ["Java", "Performance Tuning", "JVM"]),
        "HWEfficiency": ("Hardware efficiency dollars saved", ["Cost Optimization", "Infrastructure"]),
        "ProductOwnershipScore": ("Product ownership score", ["Product Ownership", "Agile"]),
        "TeachingAgileProductOwnership": ("Teaching Agile PO workshop", ["Agile Coaching", "Training"]),
        "OncallLoadTicketReduction": ("Oncall ticket reduction", ["Operational Excellence", "Automation"]),
        "VariableComparisonTool": ("Variable Comparison Tool", ["Java", "Tooling"]),
        "Pay2LoadLatencyReduction": ("SVA Pay2Load latency reduction", ["Performance Optimization", "Latency"]),
        "PrimeDay": ("Prime Day SVA Auto Approval bug find", ["Quality Assurance", "Payments"]),
        "ScrumWorkshopHighestScoringTrainer": ("Highest scoring Scrum trainer", ["Scrum", "Training"]),
        "TRMS Spot Award": ("TRMS Spot Award", ["Recognition"]),
        "TRMS ZEUS Award": ("TRMS Zeus Award", ["Recognition"]),
        "TRMS Tech Awards": ("TRMS Tech Awards", ["Technical Leadership"]),
    }

    for key, (claim, skills) in appreciations.items():
        if key in name:
            c["claims"].append(claim)
            c["skills"].extend(skills)
            break
    else:
        c["claims"].append(f"Recognition at Amazon: {name}")

    # People
    amazon_people = {
        "Hari": "colleague",
        "Thiru": "colleague",
        "Harsha": "manager",
        "SDT": "team",
    }
    for person, role in amazon_people.items():
        if person in name:
            c["people"].append({"name": person, "role": role})


def _classify_philips(c: dict, name: str, subfolder: str, parts: tuple) -> None:
    if "Awards" in str(parts) or subfolder == "Awards":
        c["type"] = "email_appreciation"
        _parse_philips_award(c, name)
    elif "PPM" in name:
        c["type"] = "performance_review"
        c["claims"].append(f"Annual performance review at Philips")
    elif "Offer" in name:
        c["type"] = "other"
        c["claims"].append("Job offer from Philips")
    elif "Development Center" in str(parts):
        c["type"] = "other"
        _parse_philips_dev_center(c, name)
    elif "Leadership interview" in str(parts):
        c["type"] = "other"
        c["claims"].append("Leadership interview assessment")
        c["skills"].append("Leadership")
    elif "India Separation" in str(parts):
        c["type"] = "other"
    elif "Employment" in name or "Employement" in name:
        c["type"] = "other"
        c["claims"].append("Employment confirmation at Philips")
    elif "TDCOnline" in name:
        c["type"] = "certificate"
        c["claims"].append("TDC Online 2021 Connections Certificate")
    elif "State of Craftsmanship" in name:
        c["type"] = "project_doc"
        c["claims"].append("State of Craftsmanship report")
        c["skills"].extend(["Software Craftsmanship", "Code Quality"])
    elif "Software-Excellence-Wins" in name:
        c["type"] = "email_appreciation"
        c["claims"].append("Software Excellence wins recognition")
        c["skills"].extend(["Software Quality", "Technical Leadership"])
    elif "AI_Dattatreya" in name:
        c["type"] = "performance_review"
        c["claims"].append("Annual incentive / performance assessment")
    elif "ID Card" in name or "NDA" in name:
        c["type"] = "other"
    elif "Profile" in name or "Grade" in name:
        c["type"] = "other"


def _parse_philips_award(c: dict, name: str) -> None:
    awards = {
        "EagerToImprove": ("Eager to Improve and Inspire award", ["Mentoring", "Interviewing"]),
        "MovingTheNeedleOnCodeQuality": ("Moving the Needle on Code Quality", ["Code Quality", "Technical Leadership"]),
        "DotCraftSuccess": ("DotCraft program success", ["Software Craftsmanship", "Program Management"]),
    }
    for key, (claim, skills) in awards.items():
        if key in name:
            c["claims"].append(claim)
            c["skills"].extend(skills)
            break
    else:
        c["claims"].append(f"Award at Philips: {name}")

    # People
    philips_people = {"Sundar": "manager", "Viswa": "colleague"}
    for person, role in philips_people.items():
        if person in name:
            c["people"].append({"name": person, "role": role})


def _parse_philips_dev_center(c: dict, name: str) -> None:
    c["type"] = "other"
    c["claims"].append("Philips Development Center assessment")
    c["skills"].extend(["Leadership", "Decision Making"])
    assessments = {
        "360Degree": "360-degree feedback assessment",
        "Leadership Development": "Leadership development report",
        "BeTalent_Strengths": "Strengths assessment",
        "Decision_Styles": "Decision styles assessment",
        "Situation_Analysis": "Situation analysis assessment",
        "Executive_Aptitude": "Executive aptitude assessment",
        "Resilience": "Resilience assessment",
    }
    for key, desc in assessments.items():
        if key in name:
            c["claims"].append(desc)
            break


def _classify_certificate(c: dict, name: str) -> None:
    c["type"] = "certificate"
    certs = {
        "CodeScene-Developer-Course-Foundation": ("CodeScene Developer Course Foundation", ["CodeScene", "Code Quality"]),
        "CodeScene-Developer-Course-Intermediate": ("CodeScene Developer Course Intermediate", ["CodeScene", "Code Quality", "Technical Debt"]),
        "Google-Prompt-Engineering": ("Google Prompt Engineering Essentials", ["Prompt Engineering", "AI", "LLM"]),
        "Mastering-Technical-Debt": ("Mastering Technical Debt by CodeScene", ["Technical Debt", "Code Quality"]),
        "Consolidated-Certificates": ("CodeScene Academy consolidated", ["CodeScene", "Code Quality"]),
        "TypeScript Essential": ("TypeScript Essential Training", ["TypeScript"]),
    }
    for key, (claim, skills) in certs.items():
        if key in name:
            c["claims"].append(f"Completed: {claim}")
            c["skills"].extend(skills)
            c["organizations"].append({"name": "CodeScene" if "CodeScene" in key else "LinkedIn Learning", "role": "issuer"})
            break


def _classify_feedback(c: dict, name: str, subfolder: str, parts: tuple) -> None:
    if subfolder == "Evaluation":
        c["type"] = "performance_review"
        c["organizations"].append({"name": "Philips", "role": "employer"})
        # Parse year and org from filename like "2019-Philips-PPM-Datta-Final"
        year_match = re.match(r"(\d{4})", name)
        if year_match:
            c["dates"].append({"date": f"{year_match.group(1)}-01-01", "context": "Annual review"})
        if "Exeter" in name:
            c["organizations"] = [{"name": "Exeter Group / OneGate", "role": "employer"}]
        elif "Amazon" in name:
            c["organizations"] = [{"name": "Amazon", "role": "employer"}]
    elif subfolder == "Informal":
        c["type"] = "email_appreciation"
        c["organizations"].append({"name": "Philips", "role": "employer"})
        _parse_philips_informal_feedback(c, name)
    elif subfolder == "Sessions":
        c["type"] = "other"
        c["organizations"].append({"name": "Philips", "role": "employer"})
        _parse_session_feedback(c, name)
    else:
        # Root level feedbacks
        c["organizations"].append({"name": "Philips", "role": "employer"})
        if "Anytime-Feedback" in name:
            c["type"] = "email_appreciation"
            c["claims"].append("Peer feedback collection")
        elif "360-Degree" in name:
            c["type"] = "performance_review"
            c["claims"].append("360-degree feedback assessment")
        elif "HeartStyles" in name:
            c["type"] = "other"
            c["claims"].append("HeartStyles leadership feedback assessment")
            c["skills"].append("Leadership")
        elif "PPM" in name:
            c["type"] = "performance_review"
        elif "Profile" in name:
            c["type"] = "other"


def _parse_philips_informal_feedback(c: dict, name: str) -> None:
    """Parse Philips informal feedback filenames."""
    feedbacks = {
        "JUnit_OfflineInstrumentation_Powermock": ("JUnit and PowerMock expertise", ["JUnit", "PowerMock", "Java Testing"]),
        "SWCoEConference": ("SW CoE Conference participation", ["Software Excellence", "Conference"]),
        "CleanCode_CleanTest_Workshop": ("Clean Code/Test workshop", ["Clean Code", "Testing", "Training"]),
        "CodeDuplication_JSCPD": ("Code duplication analysis with JSCPD", ["Code Quality", "JSCPD"]),
        "CICDRefArchitecture": ("CI/CD Reference Architecture", ["CI/CD", "DevOps", "Architecture"]),
        "QualityAtDesk": ("Quality at Desk initiative", ["Code Quality", "Shift Left"]),
        "SWExcellence_Dashboard": ("Software Excellence Dashboard", ["Metrics", "Software Quality"]),
        "Microservices": ("Microservices session", ["Microservices", "Architecture"]),
        "HackerNoon": ("HackerNoon Finals Judge", ["Technical Leadership", "Judging"]),
        "CulturalBehaviours": ("Cultural behaviours recognition", ["Leadership"]),
        "SkillRaisers": ("Skill Raisers training", ["Training", "Mentoring"]),
        "RoleModelling": ("Role modelling recognition", ["Leadership", "Mentoring"]),
        "BarRaisers": ("Bar Raisers hiring program", ["Interviewing", "Hiring"]),
        "IWillCode": ("I Will Code initiative", ["Coding", "Training", "Initiative"]),
        "dotTune": ("dotTune program", ["Code Quality", "Mentoring"]),
        "dotCraft": ("dotCraft assessment", ["Software Craftsmanship", "Assessment"]),
        "PECFinals": ("PEC Finals presentation", ["Technical Leadership", "Innovation"]),
        "FeatureTimeline": ("Feature Timeline pilot", ["Product Management", "Tooling"]),
        "Observability": ("Observability for Customer Delight", ["Observability", "Monitoring"]),
        "ReverseMentor": ("Reverse mentoring", ["Mentoring", "Leadership"]),
        "OutstandingTechnicalAchievement": ("Outstanding Technical Achievement Award", ["Technical Excellence"]),
        "HPM-Release-Workflows": ("HPM Release Workflows", ["Release Engineering", "GitHub"]),
        "MR-Feedback": ("Merge Request feedback", ["Code Review"]),
        "StateOfCraftsmanship": ("State of Craftsmanship report", ["Software Craftsmanship"]),
        "CMDK-Code-Review": ("CMDK Code Review feedback", ["Code Review"]),
        "Interview-With-Janar": ("Interview facilitation", ["Interviewing"]),
        "Kubernets": ("Kubernetes expertise", ["Kubernetes", "Cloud Native"]),
        "Ultrasound": ("Ultrasound Virtualization", ["Cloud Migration", "Virtualization"]),
        "GitHub": ("GitHub expertise", ["GitHub", "Git"]),
        "SOLID": ("SOLID Principles teaching", ["SOLID Principles", "OOP"]),
        "Innovation-Forum": ("Innovation Forum presentation", ["Innovation", "Technical Leadership"]),
        "Scanner-In-Cloud": ("Scanner in Cloud Migration Playbook", ["Cloud Migration", "Architecture"]),
        "Competency_to_Skills": ("Competency to Skills mapping", ["Skills Framework", "HR Tech"]),
        "DotNet-Testing-Tool": (".NET Testing tool", [".NET", "Testing", "Tooling"]),
        "Mentoring": ("Mentoring recognition", ["Mentoring", "Leadership"]),
    }

    for key, (claim, skills) in feedbacks.items():
        if key in name:
            c["claims"].append(claim)
            c["skills"].extend(skills)
            break
    else:
        c["claims"].append(f"Informal feedback: {name}")

    # People
    people = {
        "Nagaraj": "colleague", "Raja": "colleague", "Simao": "manager",
        "David": "colleague", "Lena": "colleague", "Kala": "manager",
        "Caroline": "leadership", "Jegan": "colleague", "Sundar": "manager",
        "Hemant": "colleague", "Pushkar": "colleague", "Richard": "senior leader",
        "Taky": "colleague", "Elwin": "colleague", "Elaine": "colleague",
        "BobD": "colleague", "Fred": "colleague", "Kitty": "colleague",
        "Matt": "colleague", "Neil": "colleague", "Richa": "colleague",
        "Vivek": "colleague", "Brian": "colleague",
    }
    for person, role in people.items():
        if person in name:
            c["people"].append({"name": person, "role": role})


def _parse_session_feedback(c: dict, name: str) -> None:
    """Parse training/session feedback filenames."""
    c["claims"].append("Training/workshop session delivered")
    c["skills"].append("Training & Facilitation")

    sessions = {
        "Java Best Practices": ["Java", "Best Practices"],
        "Unit Testing": ["Unit Testing", "JUnit"],
        "Test driven development": ["TDD", "Clean Code"],
        "Tech Debt": ["Technical Debt"],
        "clean code": ["Clean Code"],
        "Code duplication": ["Code Quality", "JSCPD"],
        "Mutation testing": ["Mutation Testing"],
        "JSCPD": ["Code Duplication", "JSCPD"],
        "Crafting Code Quality": ["Code Quality", "Tooling"],
        "SWCoE": ["Software Excellence"],
        "I will code": ["Coding", "Initiative"],
        "Pair programming": ["Pair Programming"],
        "Interviews": ["Interviewing"],
        "interview": ["Interviewing"],
        "Shift left": ["Shift Left", "Quality"],
        "Back to basics": ["Software Fundamentals"],
        "SOLID": ["SOLID Principles", "OOP"],
        "GitHub": ["GitHub", "Git"],
        "CoPilot": ["GitHub Copilot", "AI-Assisted Development"],
        "Bar_Skill raiser": ["Hiring", "Bar Raising"],
        "hiring culture": ["Hiring", "Culture"],
        "Microservices": ["Microservices"],
        "Program Behavior Metrics": ["Metrics", "Code Quality"],
        "Code dojo": ["Coding Dojo", "Practice"],
        "RVCE": ["Public Speaking"],
        "BMSIT": ["Public Speaking"],
        "SIT": ["Public Speaking"],
        "NIE": ["Public Speaking"],
        "AIT": ["Public Speaking"],
    }
    for key, skills in sessions.items():
        if key.lower() in name.lower():
            c["skills"].extend(skills)

    # Venues
    venues = {
        "RVCE": "RV College of Engineering",
        "BMSIT": "BMS Institute of Technology",
        "SIT": "SIT Tumkur",
        "NIE": "NIE Mysore",
        "AIT": "Dr. AIT",
        "Philips": "Philips",
    }
    for key, org in venues.items():
        if key in name:
            if not any(o["name"] == org for o in c["organizations"]):
                c["organizations"].append({"name": org, "role": "client"})


def _classify_education(c: dict, name: str) -> None:
    c["type"] = "certificate"
    if "10th" in name:
        c["claims"].append("10th Standard (SSLC) marks card")
        c["organizations"].append({"name": "Karnataka State Board", "role": "education"})
    elif "PUC" in name or "2nd" in name:
        c["claims"].append("2nd PUC (Pre-University) marks card")
        c["organizations"].append({"name": "Karnataka PUC Board", "role": "education"})
    elif "BE" in name and "VTU" in name:
        c["claims"].append("Bachelor of Engineering (BE) degree from VTU")
        c["organizations"].append({"name": "Visvesvaraya Technological University", "role": "education"})
        c["skills"].append("Computer Science")
    elif "MSc" in name or "Yoga" in name:
        c["claims"].append("MSc Yoga from Annamalai University")
        c["organizations"].append({"name": "Annamalai University", "role": "education"})
        c["skills"].append("Yoga")
    elif "PGDY" in name:
        c["claims"].append("Post Graduate Diploma in Yoga from Annamalai University")
        c["organizations"].append({"name": "Annamalai University", "role": "education"})
        c["skills"].append("Yoga")
    elif "SVYASA" in name or "YIC" in name:
        c["claims"].append("Yoga Instructor Course (YIC) from SVYASA")
        c["organizations"].append({"name": "SVYASA", "role": "education"})
        c["skills"].append("Yoga Instruction")


def _classify_talk(c: dict, name: str, parts: tuple) -> None:
    c["type"] = "presentation"
    c["skills"].append("Public Speaking")

    path_str = "/".join(parts)
    if "Non Technical" in path_str:
        c["skills"].append("Soft Skills Training")
        _classify_non_tech_talk(c, name, parts)
    elif "Technical" in path_str:
        c["skills"].append("Technical Training")
        _classify_tech_talk(c, name, parts)
    elif "Feedbacks" in path_str:
        c["type"] = "other"
        c["claims"].append("Talk feedback data")


def _classify_non_tech_talk(c: dict, name: str, parts: tuple) -> None:
    talks = {
        "Attitude towards learning": (["Soft Skills", "Motivation"], "Attitude towards learning talk"),
        "uncertainty": (["Resilience", "Life Skills"], "How to deal with uncertainty talk"),
        "presentation": (["Presentation Skills"], "How to give a presentation talk"),
        "interviews": (["Interview Preparation"], "How to prepare for interviews talk"),
        "tech report": (["Technical Writing"], "How to write a tech report talk"),
        "26 interviews": (["Resilience", "Interview Preparation"], "I failed 26 interviews - motivational talk"),
        "Intellectual Property": (["IP", "Innovation"], "Intellectual Property Rights talk"),
        "Yoga": (["Yoga", "Wellness"], "Yoga presentation"),
        "TMOD": (["Toastmasters", "Public Speaking"], "Table Topics Master of the Day"),
        "Scaling new heights": (["Motivation", "Career Growth"], "Scaling new heights motivational talk"),
        "Spinning_Web": (["Storytelling", "Public Speaking"], "Storytelling presentation"),
        "Think on your feet": (["Impromptu Speaking", "Communication"], "Think on your feet talk"),
        "Career Development": (["Career Growth", "Mentoring"], "Career development talk"),
        "Hackday": (["Hackathon", "Innovation"], "Hackday information session"),
        "StressManagement": (["Stress Management", "Yoga"], "Stress management through yoga"),
        "PanchakoshaViveka": (["Yoga Philosophy"], "Panchakosha Viveka presentation"),
    }
    for key, (skills, claim) in talks.items():
        if key.lower() in name.lower() or key.lower() in "/".join(parts).lower():
            c["skills"].extend(skills)
            c["claims"].append(claim)
            return
    c["claims"].append(f"Non-technical talk: {name}")


def _classify_tech_talk(c: dict, name: str, parts: tuple) -> None:
    talks = {
        "Design Pattern": (["Design Patterns", "OOP", "Java"], "Design Patterns talk/workshop"),
        "SOLID": (["SOLID Principles", "OOP"], "SOLID Principles talk"),
        "Social Media": (["Microservices", "Social Media"], "Social Media & Microservices talk"),
        "Web2.0": (["Web Technologies", "JavaScript", "Ajax"], "Web 2.0 talk"),
        "JavaScript": (["JavaScript", "Ajax"], "JavaScript/Ajax talk"),
        "J2EE": (["Java EE", "Java"], "J2EE introduction talk"),
        "Java Enterprise": (["Java EE", "Java"], "Java Enterprise Edition talk"),
        "IDE": (["IDEs", "Development Tools"], "IDEs programming platform talk"),
        "4G Internet": (["Networking", "Mobile"], "4G Internet technologies talk"),
        "Face Detection": (["Computer Vision", "Image Processing"], "Face Detection & Recognition project"),
        "Coding dojo": (["TDD", "Pair Programming", "Clean Code"], "Coding Dojo facilitation"),
        "Structured Architecting": (["Software Architecture", "System Design"], "Structured Architecture training"),
        "Visual Component": (["Dependency Management", "IEEE"], "Visual Component Dependency Management (IEEE paper)"),
        "Patent": (["Innovation", "IP"], "US Patent US20120150789A1"),
        "Agile": (["Agile", "Process Improvement"], "Agile adoption talk"),
        "Whitepaper": (["DevOps", "CI/CD"], "End-to-End DevOps whitepaper"),
        "Web programming": (["Web Development"], "Web programming manual"),
        "Android": (["Android", "Mobile Development"], "Android development talk"),
        "TExeter": (["Knowledge Sharing", "Quiz"], "TExeter Thursday tech event"),
    }
    for key, (skills, claim) in talks.items():
        if key.lower() in name.lower() or key.lower() in "/".join(parts).lower():
            c["skills"].extend(skills)
            c["claims"].append(claim)
            return
    c["claims"].append(f"Technical talk: {name}")

    # Venues
    venues = {
        "GMIT": "GMIT College",
        "Jain College": "Jain College",
        "MVJCE": "MVJCE College",
        "VVIT": "VVIT Mysore",
        "Exeter": "Exeter Group",
        "CSI": "Computer Society of India",
        "BMSIT": "BMS Institute of Technology",
        "RVCE": "RV College of Engineering",
    }
    for key, org in venues.items():
        if key in name or key in "/".join(parts):
            c["organizations"].append({"name": org, "role": "client"})


def _classify_other_offers(c: dict, name: str) -> None:
    c["type"] = "other"
    offers = {
        "UHG": "UnitedHealth Group",
        "CarDekho": "CarDekho",
        "Ola": "Ola",
        "OracleAconex": "Oracle Aconex",
        "Sapient": "Publicis Sapient",
        "Tala": "Tala",
    }
    for key, org in offers.items():
        if key in name:
            c["organizations"].append({"name": org, "role": "employer"})
            c["claims"].append(f"Received job offer from {org}")
            break


def _classify_resume(c: dict, name: str, parts: tuple) -> None:
    c["type"] = "other"
    c["claims"].append("Resume/CV version")

    # Extract year
    year_match = re.match(r"(\d{4})", name)
    if year_match:
        c["dates"].append({"date": f"{year_match.group(1)}-01-01", "context": "Resume version"})

    path_str = "/".join(parts)
    if "Job Specific" in path_str:
        # Job-specific applications
        if "Tyler Tech" in path_str:
            c["organizations"].append({"name": "Tyler Technologies", "role": "employer"})
        elif "Autodesk" in path_str:
            c["organizations"].append({"name": "Autodesk", "role": "employer"})
        elif "Microsoft" in path_str:
            c["organizations"].append({"name": "Microsoft", "role": "employer"})
        elif "Oracle" in path_str:
            c["organizations"].append({"name": "Oracle", "role": "employer"})

        if "Cover Letter" in name:
            c["type"] = "other"
            c["claims"].append("Cover letter for job application")
        elif "Job Description" in name:
            c["type"] = "other"
    elif "Cover-Letter" in name:
        c["type"] = "other"
        c["claims"].append("Cover letter template")
    elif "WorkExamples" in name:
        c["type"] = "project_doc"
        c["claims"].append("Amazon work examples document")
        c["organizations"].append({"name": "Amazon", "role": "employer"})


def _classify_student_feedback(c: dict, name: str) -> None:
    c["type"] = "other"
    c["skills"].extend(["Public Speaking", "Training & Facilitation"])
    c["claims"].append("Student feedback for talk/session")

    # Parse venue and topic from filename
    venues = {
        "RVCE": "RV College of Engineering",
        "NIE": "NIE Mysore",
        "VemanaIT": "Vemana IT",
        "BMSIT": "BMS Institute of Technology",
        "SIT": "SIT Tumkur",
        "AIT": "Dr. AIT",
    }
    for key, org in venues.items():
        if key in name:
            c["organizations"].append({"name": org, "role": "client"})


def _classify_tech_artifact(c: dict, name: str) -> None:
    c["type"] = "project_doc"
    if "DevOps" in name or "CI-CD" in name:
        c["skills"].extend(["DevOps", "CI/CD", "Pipeline Design"])
        c["claims"].append("DevOps and CI/CD reference pipeline documentation")
        c["organizations"].append({"name": "Philips", "role": "employer"})
    elif "Bar Raiser" in name:
        c["skills"].extend(["Interviewing", "Hiring", "Bar Raising"])
        c["claims"].append("Bar Raiser program documentation")
        c["organizations"].append({"name": "Philips", "role": "employer"})
    elif "Reference Pipelines" in name:
        c["skills"].extend(["CI/CD", "DevOps", "Architecture"])
        c["organizations"].append({"name": "Philips", "role": "employer"})


def _classify_yoga(c: dict, name: str) -> None:
    c["type"] = "project_doc"
    c["organizations"].append({"name": "SVYASA", "role": "education"})
    c["skills"].extend(["Yoga", "Yoga Instruction", "Research"])
    if "8Step" in name:
        c["claims"].append("8-step method yoga research project")
    elif "StressManagement" in name:
        c["claims"].append("Yoga and Stress Management research project")
    elif "Assignment" in name:
        c["claims"].append("YIC course assignment")
    elif "Telemetry" in name:
        # This seems misplaced
        c["type"] = "project_doc"
        c["skills"] = ["Telemetry", "Observability"]
        c["claims"] = ["Telemetry and Observability document"]
        c["organizations"] = [{"name": "Philips", "role": "employer"}]


def _classify_root(c: dict, name: str) -> None:
    """Classify files at the root of the Career folder."""
    if "Protogonist" in name or "Personality Type" in name:
        c["type"] = "other"
        c["claims"].append("Personality type assessment results")
        c["skills"].append("Self-Awareness")
        c["organizations"].append({"name": "Protagonist", "role": "issuer"})


def run_ingestion() -> None:
    """Main ingestion loop."""
    init_schema(DB_PATH)
    conn = get_connection(DB_PATH)

    all_files = sorted(CAREER_DIR.rglob("*"))
    eligible = [f for f in all_files if f.is_file() and not should_skip(f)]

    print(f"Processing {len(eligible)} files...")
    print()

    processed = 0
    skipped = 0
    errors = 0

    for i, filepath in enumerate(eligible, 1):
        try:
            # Extract text
            extraction = extract(filepath)
            raw_text = extraction.text

            # Classify from filename/folder context
            classification = classify_from_context(filepath)

            # Determine file_type
            file_type = extraction.file_type

            # Ingest
            result = ingest_pre_classified(
                classification_data=classification,
                conn=conn,
                file_name=filepath.name,
                file_type=file_type,
                raw_text=raw_text,
                context=f"Folder: {filepath.relative_to(CAREER_DIR)}",
                channel="batch_career_ingest",
            )

            if result.status == "processed":
                processed += 1
                if i % 50 == 0 or i <= 5:
                    print(f"  [{i}/{len(eligible)}] {result.status}: {filepath.name} "
                          f"(+{result.nodes_created}N, +{result.edges_created}E)")
            elif result.status == "skipped":
                skipped += 1
            else:
                errors += 1
                print(f"  [{i}/{len(eligible)}] ERROR: {filepath.name} - {result.skipped_reason}")

        except Exception as e:
            errors += 1
            print(f"  [{i}/{len(eligible)}] EXCEPTION: {filepath.name} - {e}")

    conn.close()

    print()
    print(f"Done! Processed: {processed}, Skipped (dup): {skipped}, Errors: {errors}")


if __name__ == "__main__":
    run_ingestion()
