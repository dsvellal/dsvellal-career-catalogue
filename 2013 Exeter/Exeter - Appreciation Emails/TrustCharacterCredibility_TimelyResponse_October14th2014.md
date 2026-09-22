# TrustCharacterCredibility TimelyResponse October14th2014

> Converted from document `TrustCharacterCredibility_TimelyResponse_October14th2014.pdf`

Dattatreya Subramanya Vellal
From:
Sent:
To:
Subject:

Krishnamurthy Hegde
Tuesday, October 14, 2014 7:21 PM
Dattatreya Subramanya Vellal; Satheesh Kumar Raju
RE: SLCSLP Error Details

Thank you both for nailing this down in less than an hour. Appreciate the help; it was a struggle for me.
Krishnamurthy Hegde | khegde@exeter.com | Mob: +91-9448505697 | Off: +91-80-33450029 | Skype: khegde
From: Dattatreya Subramanya Vellal
Sent: Tuesday, October 14, 2014 6:37 PM
To: Satheesh Kumar Raju
Cc: Krishnamurthy Hegde
Subject: RE: SLCSLP Error Details

This was accurate. Thanks a lot for the help.
Regards,
Datta
Dattatreya S Vellal | dvellal@exeter.com | Mobile: +91 99723 12693 | Skype: dsvellal
From: Satheesh Kumar Raju
Sent: Tuesday, October 14, 2014 5:44 PM
To: Dattatreya Subramanya Vellal
Subject: SLCSLP Error Details

Hi Datta,
Please find the details for the error happening in SLCSLP call .
Note : The issue is in the Plan service Call which send us wrong Age which is causing the problem.
So I have given explanation for How PLAN SERVICE calculates the age based on the DOB. Please find the
attached files for the complete code snippet in Plan service.
Working Case Explanation :
DOB : 1/10/1993(MM-dd-YYY)
So when we give the above date of birth the age outcome is 21 which is correct. This is because the age is calculated
based on a relative date. In Plan service this relative date is always set to 1st JAN of Next year of Today’s Date (0101-2015 in our Case).so the logic in the util Class (just see highlighted in red and purple )
int year1 = relnow.get(Calendar.YEAR);
int year2 = dob.get(Calendar.YEAR);
int age = year1 - year2; (output = 22)
int month1 = relnow.get(Calendar.MONTH);
int month2 = dob.get(Calendar.MONTH);
//Fix for ONEGATECORE-10956. Switched the variable check.
if (month1 > month2) {(output = false)
age--;
} else if (month1 == month2) {(output = true)
int day1 = relnow.get(Calendar.DAY_OF_MONTH);
int day2 = dob.get(Calendar.DAY_OF_MONTH);
if (day2 > day1) {(output = true)
age--; (output = 21)
1

}
Final output = 21
So the age returned 21 is correct. So API uses this Age and calculates the SLCSLP value which will be correct.
Failing Case Explanation :
DOB : 1/1/1980(MM-dd-YYYY)
So when we give the above date of birth the age outcome is 34 but from plan service the calculated age is 35. This is
because the age is calculated based on a relative date. In Plan service this relative date is always set to 1st JAN of
Next year of Today’s Date (01-01-2015 in our Case).so the logic in the util Class (just see highlighted in red &
purple)
int year1 = relnow.get(Calendar.YEAR);
int year2 = dob.get(Calendar.YEAR);
int age = year1 - year2; (output = 35)
int month1 = relnow.get(Calendar.MONTH);
int month2 = dob.get(Calendar.MONTH);
//Fix for ONEGATECORE-10956. Switched the variable check.
if (month1 > month2) {(output = false)
age--;
} else if (month1 == month2) {(output = false)
int day1 = relnow.get(Calendar.DAY_OF_MONTH);
int day2 = dob.get(Calendar.DAY_OF_MONTH);
if (day2 > day1) {
age--;
}
Final output = 35
So the age returned 35 is in-correct. So API uses this Age and calculates the SLCSLP value which will also result in
wrong output .

This explain when it will work correctly and when it will not work properly.
If you want any further details please feel free to ask
Regards,
Satheesh.
Satheesh kumar raju | Email : sraju@exeter.com | mobile : 9741946268 | skype:Satheesh.kumar839

2

