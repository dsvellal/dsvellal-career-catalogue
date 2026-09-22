# TakingThingsToConclusion LoggingLibraryChanges July28th2014

> Converted from document `TakingThingsToConclusion_LoggingLibraryChanges_July28th2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Cc:
Subject:

Anuroop V. Gaonkar
Monday, July 28, 2014 7:11 PM
Suraj Rajaram Prabhu; Arun Panattu Chacko; Rajeev Joshi; Dattatreya Subramanya Vellal
Krishnamurthy Hegde; Chowlur Vijendra Nagendra Sharma; Chandrashekhar
Surendranath
RE: svn://172.17.10.60/onegate/branches/3.3.2.9-hotfix03-vt-ebf

Thanks Datta, Suraj, and Arun. Neatly done.
Thanks Rajeev for teaching Suraj how to build the PlanService with right jars using JDeveloper.
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Suraj Rajaram Prabhu
Sent: Monday, July 28, 2014 7:07 PM
To: Arun Panattu Chacko
Cc: Krishnamurthy Hegde; Anuroop V. Gaonkar; Dattatreya Subramanya Vellal; Chowlur Vijendra Nagendra Sharma
Subject: RE: svn://172.17.10.60/onegate/branches/3.3.2.9-hotfix03-vt-ebf

Hi Arun,
ONEGATECORE-20895 is the deployment JIRA related with new OneGatePlansService movement to
3.3.2.9HF3VTEBF.
Regards,
Suraj Prabhu | E X E T E R
Skype ID : s7.sunshine | Mobile : 9481871177
From: Anuroop V. Gaonkar
Sent: 28 July 2014 13:02
To: Dattatreya Subramanya Vellal; Suraj Rajaram Prabhu
Cc: Krishnamurthy Hegde
Subject: RE: svn://172.17.10.60/onegate/branches/3.3.2.9-hotfix03-vt-ebf

Suraj,
Could you please pick up Datta’s changes and move forward with PlanService build?
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Dattatreya Subramanya Vellal
Sent: Monday, July 28, 2014 12:52 PM
To: Anuroop V. Gaonkar
Subject: RE: svn://172.17.10.60/onegate/branches/3.3.2.9-hotfix03-vt-ebf

Hello Anuroop,
The og-api has been ported and built.
1

It can be downloaded from here: http://egbuild:8080/artifactory/libs-snapshotlocal/com/armedica/onegate/api/og-api/3.3.2.9-HF02-SNAPSHOT/og-api-3.3.2.9-HF02-20140728.072058-61.jar
I have created a job: http://172.17.0.77:8080/hudson/view/3.3.2.9 HF VT/job/3.3.2.9 HF3 VT og-api to build og-api’s
for the VT 3.3.2.9 HF version.
Commit details:
Revision: 38868
Author: dvellal
Date: Monday, July 28, 2014 12:41:12 PM
Message:
The following revisions were merged: 37566, 37801, 38037, 38041, 38048, 38059, 38080, 38082
From branch: svn://172.17.10.60/onegate/branches/3.3.2.9-hotfix03-ebf1/lib/og-api/
To branch: svn://172.17.10.60/onegate/branches/3.3.2.9-hotfix03-vt-ebf/lib/og-api/
This shall take care of OgLogger issues, and the og-api movement from log4j to slf4j.
---Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/og-api
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/og-api/pom.xml
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/caching/AsyncLazyTimeCache.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/caching/BaseCache.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/caching/LazyTimeCache.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/caching/LazyTimeCacheByKey.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/CarrierNames.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/og-api/src/main/java/com/armedica/onegate/api/client/Clinics.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/GroupPolicies.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/HouseholdCompositionEngine.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/Households.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/MasterCaseToContactInfo.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/OgPlans.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/PlanTemplates.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/PlanTypes.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/ProgramBenefitsAdmin.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/Providers.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/og-api/src/main/java/com/armedica/onegate/api/client/Rating.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/Regions.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/SpecialEnrollment.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/client/TierCategories.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/common/OgApiPackageInfo.java
2

Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/common/OpaUtils.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/common/SiebelUtils.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/ChangeCaptureEngine.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/ChangeCaptureResults.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/EmployerContributionConfig.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/GroupPolicyCoverages.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/IndividualPolicyCoverages.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgCaseAccess.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgEntity.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgEntityAttribute.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgEntityDefinition.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgEntityElement.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgEntityField.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgEntityLink.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgEntityNode.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgEntityValue.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgEntityXPath.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgFieldDefinition.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgHealthServiceCostMetaData.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgLinkDefinition.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgNavBrokerCases.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgOpenEnrollment.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgParameters.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgPlan.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgPlanTemplates.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgPolicyHealthServiceCost.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgProgramBenefitsAdminBenefit.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgProgramBenefitsAdminProgram.java
3

Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OgRateBand.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/OracleAllTabColumns.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/SiebelAuditTrail.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/SiebelBusinessComponentLinksMetaData.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/SiebelBusinessComponentMetaData.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/SiebelEntities.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/SiebelEntity.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/SiebelEntityDefinitions.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/SiebelEntityLink.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/SiebelEntityLinkAssoc.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/SiebelEntityLinkDisassoc.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/SiebelLOV.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/datamodel/SiebelTimezone.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/logging/OgDbLogger.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/logging/OgFileLogger.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/logging/OgLogConfig.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/logging/OgLogger.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/logging/OgLoggerFactory.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/service/ContactServiceOutputCache.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/service/ECMClientHeaderHandler.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/service/ECMEaiInterfaceService.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/service/ECMProgramBenefitsService.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/service/ERPlanSelectionServiceImpl.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/service/HealthPlanSiebelServiceImpl.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/service/MasterCaseService.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/service/OneGateAdminHixLocaleService.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/service/OneGateAdminTierCategoryProcessService.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/service/OneGateHealthInsurancePlanTemplatesService.java
4

Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/service/OneGatePlanSelectionMetadataServiceImpl.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/service/OnegateCOCPlanSelectionServiceImpl.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/og-api/src/main/java/com/armedica/onegate/api/util/Cloner.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/main/java/com/armedica/onegate/api/util/DateUtils.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/client/AppTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/client/HouseholdCompositionEngineUnitTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/common/OgApiPackageInfoUnitTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/common/OpaUtilsFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/common/SiebelUtilsFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/ChangeCaptureEngineFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/ChangeCaptureEngineUnitTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/EmployerContributionConfigFunctionalOff.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/FlowDecisionsFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/OgEntityNodeUnitTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/OgEntityXPathFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/OgEntityXPathUnitTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/OgNavBrokerCasesFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/OracleAllTabColumnsFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/SiebelAuditTrailFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/SiebelAuditTrailUnitTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/SiebelBusinessComponentLinksMetaDataFunctionalTest.ja
va
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/SiebelBusinessComponentMetaDataFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/SiebelBusinessComponentMetaDataUnitTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/SiebelEntitiesFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/SiebelLOVFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/datamodel/SiebelTimezoneFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/logging/OgLoggerFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/service/ECMGroupPolicyImplFunctionalTest.java
5

Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/service/OnegateCOCPlanSelectionServiceImplFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/service/SiebelCaseServiceFunctionalTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/test/ParallelTesting.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/testcaching/CacheTesting.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/util/DateUtilsUnitTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/util/GlobUtilityUnitTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/util/MapUtilityUnitTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/util/ServerInfoUnitTest.java
Modified : /branches/3.3.2.9-hotfix03-vt-ebf/lib/ogapi/src/test/java/com/armedica/onegate/api/util/StringUtilityUnitTest.java

Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Anuroop V. Gaonkar
Sent: Monday, July 28, 2014 11:00 AM
To: Dattatreya Subramanya Vellal
Subject: FW: svn://172.17.10.60/onegate/branches/3.3.2.9-hotfix03-vt-ebf

Datta,
The branch where the Logger related corrections need to be made.
svn://172.17.10.60/onegate/branches/3.3.2.9-hotfix03-vt-ebf
Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

From: Anuroop V. Gaonkar
Sent: Monday, July 28, 2014 10:42 AM
To: Suraj Rajaram Prabhu; Abhishek Ramesh Babu
Cc: Krishnamurthy Hegde
Subject: svn://172.17.10.60/onegate/branches/3.3.2.9-hotfix03-vt-ebf

Regards,
Anuroop V. Gaonkar, +919845183528, Skype: ag_theone
E X E T E R | 6th floor, Nitesh Timesquare, 8, M.G. Road| Bangalore 560001 | India

6

