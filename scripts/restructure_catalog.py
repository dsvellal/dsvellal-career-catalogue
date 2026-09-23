#!/usr/bin/env python3
"""
Career Catalog Restructuring Script
Migrates all files from fragmented top-level folders into a 5-pillar taxonomy.
"""
import os
import shutil
from pathlib import Path

ROOT = Path('/Users/dsvellal/Downloads/Website')

PILLARS = [
    "01_Career_Eras/2013_Exeter",
    "01_Career_Eras/2016_Amazon",
    "01_Career_Eras/2018_2023_Philips",
    "01_Career_Eras/2024_2026_SWCoE",
    "02_Evidence_and_Feedback/Executive_Appreciations",
    "02_Evidence_and_Feedback/360_Peer_Feedbacks",
    "02_Evidence_and_Feedback/Informal_Recognitions",
    "02_Evidence_and_Feedback/Student_and_Mentee_Reviews",
    "03_Executive_Givebacks/Technical_Keynotes_and_Talks",
    "03_Executive_Givebacks/University_and_Community",
    "03_Executive_Givebacks/Overview",
    "04_Architecture_and_Strategy/Whitepapers_and_Pipelines",
    "04_Architecture_and_Strategy/Domain_Assessments",
    "05_Credentials_and_Academics/Executive_Profiles_and_Resumes",
    "05_Credentials_and_Academics/Certifications",
    "05_Credentials_and_Academics/Academic_Records"
]

def run_restructuring():
    print("==> Initializing 5-pillar directory structure...")
    for rel_path in PILLARS:
        dest = ROOT / rel_path
        dest.mkdir(parents=True, exist_ok=True)

    # 1. Pillar 01: Career Eras
    print("==> Moving Pillar 01 (Career Eras)...")
    if (ROOT / "2013 Exeter").exists():
        for item in (ROOT / "2013 Exeter").iterdir():
            shutil.move(str(item), str(ROOT / "01_Career_Eras/2013_Exeter" / item.name))
        (ROOT / "2013 Exeter").rmdir()

    if (ROOT / "2016 Amazon").exists():
        for item in (ROOT / "2016 Amazon").iterdir():
            shutil.move(str(item), str(ROOT / "01_Career_Eras/2016_Amazon" / item.name))
        (ROOT / "2016 Amazon").rmdir()

    dest_philips = ROOT / "01_Career_Eras/2018_2023_Philips"
    if (ROOT / "2018 Philips").exists():
        for item in (ROOT / "2018 Philips").iterdir():
            target = dest_philips / item.name
            if target.exists() and item.is_dir():
                for sub in item.iterdir():
                    shutil.move(str(sub), str(target / sub.name))
                item.rmdir()
            else:
                shutil.move(str(item), str(target))
        (ROOT / "2018 Philips").rmdir()

    if (ROOT / "Philips").exists():
        for item in (ROOT / "Philips").iterdir():
            target = dest_philips / item.name
            if target.exists() and item.is_dir():
                for sub in item.iterdir():
                    sub_target = target / sub.name
                    if sub_target.exists():
                        shutil.move(str(sub), str(target / f"philips_{sub.name}"))
                    else:
                        shutil.move(str(sub), str(sub_target))
                item.rmdir()
            else:
                shutil.move(str(item), str(target))
        (ROOT / "Philips").rmdir()

    dest_swcoe = ROOT / "01_Career_Eras/2024_2026_SWCoE"
    if (ROOT / "2026_SWCoE").exists():
        for item in (ROOT / "2026_SWCoE").iterdir():
            shutil.move(str(item), str(dest_swcoe / item.name))
        (ROOT / "2026_SWCoE").rmdir()

    if (ROOT / "SWCoE_Archive").exists():
        for item in (ROOT / "SWCoE_Archive").iterdir():
            target = dest_swcoe / item.name
            if target.exists() and item.is_dir():
                for sub in item.iterdir():
                    shutil.move(str(sub), str(target / sub.name))
                item.rmdir()
            else:
                shutil.move(str(item), str(target))
        (ROOT / "SWCoE_Archive").rmdir()

    # 2. Pillar 02: Evidence and Feedback
    print("==> Moving Pillar 02 (Evidence & Feedback)...")
    dest_exec = ROOT / "02_Evidence_and_Feedback/Executive_Appreciations"
    old_appr = ROOT / "Dattatreya S Vellal_s appreciation letters and certificates"
    if old_appr.exists():
        for item in old_appr.iterdir():
            shutil.move(str(item), str(dest_exec / item.name))
        old_appr.rmdir()

    dest_feedbacks = ROOT / "02_Evidence_and_Feedback/360_Peer_Feedbacks"
    if (ROOT / "Feedbacks").exists():
        for item in (ROOT / "Feedbacks").iterdir():
            shutil.move(str(item), str(dest_feedbacks / item.name))
        (ROOT / "Feedbacks").rmdir()

    dest_informal = ROOT / "02_Evidence_and_Feedback/Informal_Recognitions"
    if (ROOT / "Philips Office Informal Feedbacks").exists():
        for item in (ROOT / "Philips Office Informal Feedbacks").iterdir():
            shutil.move(str(item), str(dest_informal / item.name))
        (ROOT / "Philips Office Informal Feedbacks").rmdir()

    dest_students = ROOT / "02_Evidence_and_Feedback/Student_and_Mentee_Reviews"
    if (ROOT / "Students feedbacks").exists():
        for item in (ROOT / "Students feedbacks").iterdir():
            shutil.move(str(item), str(dest_students / item.name))
        (ROOT / "Students feedbacks").rmdir()

    # 3. Pillar 03: Executive Givebacks
    print("==> Moving Pillar 03 (Executive Givebacks)...")
    dest_talks = ROOT / "03_Executive_Givebacks/Technical_Keynotes_and_Talks"
    if (ROOT / "My Talks").exists():
        for item in (ROOT / "My Talks").iterdir():
            shutil.move(str(item), str(dest_talks / item.name))
        (ROOT / "My Talks").rmdir()

    dest_univ = ROOT / "03_Executive_Givebacks/University_and_Community"
    if (ROOT / "Givebacks").exists():
        for item in (ROOT / "Givebacks").iterdir():
            shutil.move(str(item), str(dest_univ / item.name))
        (ROOT / "Givebacks").rmdir()

    dest_overview = ROOT / "03_Executive_Givebacks/Overview"
    for loose, target_name in [
        ("Givebacks.md", "Givebacks_Summary.md"),
        ("Professional giving back.md", "Professional_Giving_Back.md"),
        ("Social giving back.md", "Social_Giving_Back.md")
    ]:
        f = ROOT / loose
        if f.exists():
            shutil.move(str(f), str(dest_overview / target_name))

    # 4. Pillar 04: Architecture and Strategy
    print("==> Moving Pillar 04 (Architecture & Strategy)...")
    dest_tech = ROOT / "04_Architecture_and_Strategy/Whitepapers_and_Pipelines"
    if (ROOT / "Tech Artifacts").exists():
        for item in (ROOT / "Tech Artifacts").iterdir():
            shutil.move(str(item), str(dest_tech / item.name))
        (ROOT / "Tech Artifacts").rmdir()

    dest_assess = ROOT / "04_Architecture_and_Strategy/Domain_Assessments"
    f_assess = ROOT / "Assessment Matrix_Ultrasound.md"
    if f_assess.exists():
        shutil.move(str(f_assess), str(dest_assess / "Assessment_Matrix_Ultrasound.md"))

    # 5. Pillar 05: Credentials and Academics
    print("==> Moving Pillar 05 (Credentials & Academics)...")
    dest_res = ROOT / "05_Credentials_and_Academics/Executive_Profiles_and_Resumes"
    if (ROOT / "Resume").exists():
        for item in (ROOT / "Resume").iterdir():
            shutil.move(str(item), str(dest_res / item.name))
        (ROOT / "Resume").rmdir()

    f_proto = ROOT / "20241004 - Protogonist - Dattatreya S Vellal Personality Type Results.md"
    if f_proto.exists():
        shutil.move(str(f_proto), str(dest_res / f_proto.name))

    dest_cert = ROOT / "05_Credentials_and_Academics/Certifications"
    if (ROOT / "Certificates").exists():
        for item in (ROOT / "Certificates").iterdir():
            shutil.move(str(item), str(dest_cert / item.name))
        (ROOT / "Certificates").rmdir()

    dest_acad = ROOT / "05_Credentials_and_Academics/Academic_Records"
    if (ROOT / "MarksCard").exists():
        for item in (ROOT / "MarksCard").iterdir():
            shutil.move(str(item), str(dest_acad / item.name))
        (ROOT / "MarksCard").rmdir()

    f_face = ROOT / "Face Detection & Recognition RVCE 2007.md"
    if f_face.exists():
        shutil.move(str(f_face), str(dest_acad / f_face.name))

    print("==> Restructuring migration completed successfully!")

if __name__ == '__main__':
    run_restructuring()
