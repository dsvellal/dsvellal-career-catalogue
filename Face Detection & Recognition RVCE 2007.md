# Face Detection & Recognition RVCE 2007

> Converted from document `Face Detection & Recognition RVCE 2007.pdf`

VISVESVARAYA TECHNOLOGICAL UNIVERSITY
Machche, Belgaum

2006 - 2007
A project report on

“Face Detection and Recognition”
Submitted in partial fulfillment of the requirements for the award of degree

Bachelor of Engineering
in
Computer Science & Engineering
by
1. Avinash K Gupta, 1RV03CS045
3. Dattatreya S Vellal, 1RV03CS025

2. Balu R, 1RV03CS022
4. Srikanth K M, 1RV03CS046

Under the guidance of
Mrs. Padmashree T
Lecturer
Department of CSE, R.V.C.E.
Carried out at
RVCE,
Bangalore-560059

Department of Computer Science and Engineering,
R. V. College of Engineering,
Bangalore – 560059

Department of Computer Science and Engineering
R.V. College of Engineering,
Bangalore – 560059

CERTIFICATE
This is to certify that the project titled

“Face Detection and Recognition”
has been successfully carried out at R.V.C.E., Bangalore
in partial fulfillment of the requirements for the award of degree of
Bachelor of Engineering in Computer Science and Engineering
of Visvesvaraya Technological University, Belgaum
during the academic year 2006-07
by

Avinash K Gupta, 1RV03CS045
Dattatreya S Vellal, 1RV03CS025

Mrs. Padmashree T
Lecturer,
Department of CSE
R.V.C.E., Bangalore-59

Prof B.I. Khodanpur
Professor and Head,
Department of CSE
R.V.C.E., Bangalore-59

Name of the Examiners
1.
2.

Balu R, 1RV03CS022
Srikanth K M, 1RV03CS046

Dr. S.C. Sharma
Principal,
R.V.C.E.
Bangalore-59

Signature with Date

Acknowledgements
Our project was the result of the encouragement of many people who helped
shape it and provided feedback, direction and valuable support. It is with hearty
gratitude that we acknowledge their contributions to our project.
We would like to thank our internal guide Mrs.Padmashree.T for the constant
help and support extended towards us during the course of the project.
We are also grateful to our HOD, Prof. B. I. Khodanpur, Department of
Computer Science & Engineering, RVCE, for permitting us to take up this project and
his encouragement. We thank our Principal, Dr.S.C.Sharma who has always been a
great source of inspiration.
Last, but not the least, we would like to thank our peers and friends who
provided us with valuable suggestions to improve our project.

1. Avinash K Gupta, 1RV03CS045
2. Balu R, 1RV03CS022
3. Dattatreya S Vellal, 1RV03CS025
4. Srikanth K M, 1RV03CS046

SYNOPSIS
The subject of face recognition is as old as computer vision and both because of the
practical importance of the topic and theoretical interest from cognitive science. Face
recognition is not the only method of recognizing other people. Even humans between each
other use senses in order to recognize others. Machines have a wider range for recognition
purposes, which use things such as fingerprints, or iris scans. Despite the fact that these
methods of identification can be more accurate, face recognition has always remains a major
focus of research because of its non-invasive nature and because it is people's primary
method of person identification
A facial recognition system is a computer-driven application for automatically
identifying a person from a digital image. It does that by comparing selected facial features in
the live image and a facial database.
Face Detection is a necessary pre-requisite for face recognition to detect the presence of
faces in a given image.
It is typically used for security systems and can be compared to other biometrics such
as fingerprint or eye iris recognition systems.
Popular recognition algorithms include eigenface, fisherface, the Hidden Markov
model, and the neuronal motivated Dynamic Link Matching.

i

Contents
Particulars

Page No.

1. Introduction………………………………………………………………………….01

2.

1.1

Introduction………….………………………………………………………01

1.2

Historical Overview…………………………………………………………02

1.3

Stages in Face Recognition……………………………………………….....03

1.4

Purpose……………………………………………………………………...04

1.5

Scope………………………………………………………………………..04

1.6

Motivation…………………………………………………………………..05

1.7

Literature Survey……………………………………………………………06

Software Requirements Specifications…………………………………….……....07
2.1Software Requirements Specification……………………………....................07
2.2

Overall Description………………………………………………..……....07
2.2.1 Product Perspective………………………………………..……….08
2.2.2

Product Functions………………………………………..…………08

2.2.3 User Characteristics………………………………………..……….08
2.2.4

Constraints…….................................................................................09

2.2.5 Assumptions and Dependencies…………………………..………..09
2.3

Specific Requirements…………………………………………..……….…10
2.3.1

Functional Requirements…………………………………..……10

2.3.1.1

Detect the Presence of a Face……………………..……..10

2.3.1.2

Identify the Location of the Face…………………..…….11

2.3.1.3

Recognize the Face……………………………………....11

2.3.2 Performance………………………………………………………..11
2.3.2.1

Detect the Face………………………………………...…11

2.3.2.2
2.3.3

Recognize the Face…………………………………...12

Supportability………………………………………………………13
2.3.3.1

Software should provide option to maintain Database.....13
ii

2.3.4 Interfaces…………………………………………………………...13
2.3.4.1 User Interface…………………………………………..…13
2.3.4.2
3.

Software Interface………………………………………...14

High Level Design…………………………………….………………………..…15
3.1

High Level Design………………………………………………..……....15

3.2

Design Considerations…………………………………………...…..….....16
3.2.1 Assumptions and Dependencies………………………………….....16
3.2.2 General Constraints………………………………………………....16
3.2.3

Development Methods……………………………………...………17

3.3

Architectural Strategies………………………………………………….....18

3.4

System Architecture …………………………………………………….….19

3.5 System Architecture (DFD’s)………………………………………….…....20
3.5.1

4.

DFD’s – Data Flow Diagrams…………………………….…….….20

Detailed Design……………………………………………………………..……26
4.1 Detailed Design…………………………………………..………………..26
4.2 Structured Charts………………………………………………..………...26
4.2.1 Structured Chart for Face Detection and Recognition System.……..27
4.2.2 Structured Chart for Preprocessing…………………………………28
4.2.3 Structured Chart for Noise Reduction………………………………29
4.2.4 Structured Chart for Face Detection………………………………..30
4.2.5 Structured Chart for Face Recognition……………………………..31
4.2.6 Structured Chart for Training……………………………………….32
4.3 Module 1: Face Detection………………………………………………….33
4.3.1 Introduction..……………………………………………………….33
4.3.2 Purpose……………………………………………………………..33
4.3.3 Functionality……………………………………………………….34
4.3.4 Intercomponent relationship………………………………………..35
4.4 Module 2: Face Histogram………….……………………………………...35
4.4.1 Introduction..…………………………………………………….....35
4.4.2 Purpose……………………………………………………………..35
iii

4.4.3 Functionality………………………………………………………..36
4.4.4 Intercomponent relationship………………………………………..36
4.5

Module 3: Converttohsv……………………………………………………37
4.5.1 Introduction..……………………………………………………….37
4.5.2 Purpose……………………………………………………………..37
4.5.3 Functionality……………………………………………………….37

4.6 Module 4: Calculate_Skin…..……………………………………………...39
4.6.1 Introduction..……………………………………………………….39
4.6.2 Purpose……………………………………………………………..39
4.6.3 Functionality……………………………………………………….39
4.6.4 Intercomponent relationship………………………………………..41
4.7 Module 5: Region…………..……………………………………………....41
4.7.1 Introduction..……………………………………………………….41
4.7.2 Purpose……………………………………………………………..41
4.7.3 Functionality……………………………………………………….41
4.8 Module 6: Goldenratio…………….……………………………………….43
4.8.1 Introduction..……………………………………………………….43
4.8.2 Purpose……………………………………………………………..43
4.8.3 Functionality……………………………………………………….43
4.9 Module 7: Pre-process……….…………………………………………….44
4.9.1 Introduction..……………………………………………………….44
4.9.2 Purpose……………………………………………………………..45
4.9.3 Functionality……………………………………………………….45
4.9.4 Intercomponent relationship……………………………………….46
4.10 Module 8: Gray Scale Conversion…………………………………………46
4.10.1 Introduction..……………………………………………………...47
4.10.2 Purpose……………………………………………………………47
4.10.3 Functionality……………………………………………………...47
4.11

Module 9: Histogram Equalization………………………………………..48
4.11.1 Introduction..……………………………………………………...48
4.11.2 Purpose……………………………………………………………48
4.11.3 Functionality……………………………………………………...48
iv

4.12

Module 10: Low Pass Filter……………………………………………….49
4.12.1 Introduction..……………………………………………………...49
4.12.2 Purpose……………………………………………………………50
4.12.3 Functionality……………………………………………………...50

4.13 Module 11: Resize…………………………………………………………51
4.13.1 Introduction..……………………………………………………...51
4.13.2 Purpose……………………………………………………………51
4.13.3 Functionality……………………………………………………...51
4.13.4 Intercomponent relationship………………………………………52
4.14 Module 12: Face Recognition……………………………………………...52
4.14.1 Introduction..……………………………………………………...52
4.14.2 Purpose……………………………………………………………52
4.14.3 Functionality……………………………………………………...53
4.14.4 Intercomponent relationship……………………………………...54
4.15 Module 13: Training…. …………………………………………………...54
4.15.1 Introduction..……………………………………………………...54
4.15.2 Purpose…………………………………………………………....54
4.15.3 Functionality……………………………………………………...55
4.16

Module 14: PCA…………………………………………………………...56
4.16.1 Introduction..……………………………………………………...56
4.16.2 Purpose……………………………………………………………56
4.16.3 Functionality………………………………………………………56

4.17

Module 15: Classification…………………………………………………..57
4.17.1 Introduction..………………………………………………………57
4.17.2 Purpose……………………………………………………………58
4.17.3 Functionality………………………………………………………58

5.

Implementation ………………………….…………………………………………60
5.1

Implementation…………………………………………………………….60

5.2

Programming Language……………………………………………………60
5.2.1

Matlab…………………………………….. ……………………..61

5.2.2

Java………………………………………………………………61
v

6.

5.3

Coding Standards…………………………………………………………..63

5.4

Platform……………………………………………………………………65

Testing……………………………………………………………………………...66
6.1

Testing……………………………………………………………………..66

6.2

Unit Testing………………………………………………………………..67
6.2.1 Face Detection Unit……………………………………………….67
6.2.1.1

Testing Strategy………………………………………….67

6.2.1.2

Test Cases………………………………………………..68

6.2.2 Pre-processing Unit..……………………………………………...70
6.2.2.1 Testing Strategy…………………………………………70
6.2.2.2 Test Cases……………………………………………….71
6.2.3 Face Recognition Unit…………………………………………….72

6.3

6.2.3.1

Testing Strategy………………………………………….72

6.2.3.2

Test Cases………………………………………………..73

Integration Testing………………………………………………………...75
6.3.1 Testing Strategy……………………………………………............75
6.3.2 Test Cases………………………………………………………….77

6.4

Interface Testing…………………………………………………………..78
6.4.1 Software Interface…… …………………………………………..78
6.4.1.1 Testing Strategy………………………………………....78
6.4.1.2 Test Cases……………………………………………….79
6.4.2 User Interface……………………………………………………..79
6.4.2.1 Testing Strategy………………………………………....80
6.4.2.2 Test Cases……………………………………………….81

6.5
7.

Results…………………………………………………………………….83

Conclusion………………………………………………………………………….85
7.1

Summary..…………………………………………………………………85

7.2

Limitations……………………………………………………………...…85

7.3

Further Enhancements...…………………………………………………..86

vi

8.

References………………………………………………………………………….87

9.

Appendices…………………………………………………………………………89
Appendix A Source Code Listing………………………………………………...89
Appendix B

List of Figures...................................................................................114

Appendix C

List of Tables………………………………………………………115

vii

Introduction

Face Detection and Recognition

1. Introduction
1.1. Introduction
As continual research is being conducted in the area of computer vision, one of the
most practical applications under vigorous development is in the construction of a robust
real-time face recognition system. With the recent major terrorist attack, there have been
increasingly substantial interests in the development of intelligent surveillance cameras that
can automatically detect and recognize known criminals as well as suspicious characters.
Due to such uncertain times, humans are beginning to seek support from computer systems to
aid in the process of identification and location of faces in everyday scenes. Smart buildings
can be implemented whereby the presence of unknown dubious individuals can be brought to
the attention of building security for appropriate action, and smart computers can be used to
load personal preferences and needs. Entertainment companies are particularly interested in
systems where specific actors can be searched for and located in a video sequence, so that
their movements can be tracked throughout the entire movie.
The subject of face recognition is as old as computer vision and both because of the
practical importance of the topic and theoretical interest from cognitive science. Face
recognition is not the only method of recognizing other people. Even humans, between each
other use senses in order to recognize others. Machines have a wider range for recognition
purposes, which use things such as fingerprints, or iris scans. Despite the fact that these
methods of identification can be more accurate, face recognition has always remains a major
focus of research because of its non-invasive nature and because it is people's primary
method of person identification[1].

Dept. of CSE, R.V.C.E

Jan-May’ 2007

1

Introduction

Face Detection and Recognition

1.2. Historical Overview
There are two main approaches to face recognition [2]. They are as follows:
! Geometrical approach
! Pictorial approach.
The geometrical approach uses the spatial configuration of facial features. This means
that the main geometrical features of the face such as the eyes, nose and mouth are first
located and then faces are classified on the basis of various geometrical distances and angles
between features. On the other hand, the pictorial approach uses templates of the facial
features. That method is using the templates of the major facial features and entire face to
perform recognition on frontal views of faces. Many of the projects that where based on
those two approaches have some common extensions that handle different poses
backgrounds. Apart from these two techniques we have other recent template-based
approaches, which form templates from the image gradient, and the principal component
analysis approach[3], which can be read as a sub-optimal template approach. Finally we have
the deformable template approach that combines elements of both the pictorial and feature
geometry approaches and has been applied to faces at varying pose and expression.
Since the early start of face recognition there is a strong relation and connection with
the science of neural networks. The most famous early example of a face recognition
"system", using neural networks is the Kohonen model[1]. That system was a simple neural
network that was able to perform face recognition for aligned and normalized face images.
The type of network he employed computed a face description by approximating the
eigenvectors of the face image's auto-correlation matrix; these eigenvectors are now known
as "eigenfaces"[4].
After that there were many other methods that were developed based on older
techniques. The "idea" of face recognition is based on geometrical approach or pictorial
approach, and after that we have methods like eigenfaces, Principal Component Analysis, or
other methods that process images in combination with neural networks or other expert
systems.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

2

Introduction

Face Detection and Recognition

In the recognition stage, the input is compared against all selected model views of
each person. To compare the input against a particular model view, the face is first
geometrically aligned with the model view. An affine transform is applied to the input to
bring the facial features automatically located by the system into correspondence with the
same features on the model.
While solutions to the task of face recognition have been presented, recognition
performances of many systems are heavily dependent upon a strictly constrained
environment. The problem of recognizing faces under gross variations remains largely
unsolved. This project addressed the issue of developing a face recognition system under
reduced constraints.

1.3. Stages in Face Recognition
The design of the face recognition system is based upon “eigenfaces”[4] and has been
separated into three major modules: Preprocessing of Face, Face Detection, and Face
Recognition.
Preprocessing modules account for possible scaling, planar rotational and illumination
differences.
Face detection is accomplished by first performing a skin search of the input image
based on color segmentation[5]. Although skin colors differ from person to person, it was
found that the color remained distributed over a very small region on the chrominance plane.
Normalized cross correlation and face space decomposition are then applied in order to
locate the exact position of the face. The application of eigenfaces to the task of face
recognition requires a perfectly standardized and aligned database of faces.
The outcome is a sophisticated system capable of reliable recognition with reduced
constraints in the position and orientation of the face, as well as the illumination and
background of the image[1].

Dept. of CSE, R.V.C.E

Jan-May’ 2007

3

Introduction

Face Detection and Recognition

1.4. Purpose
The goal of this project is to implement a system capable of Detecting and Recognizing
faces in near real-time. Successfully constructing a real-time face recognition system
naturally leads onto the solution to the problems of extremely constraint testing
environments. The current challenge is when we are presented with faces having many
different possible rotational and illumination conditions.
A system that can accept varying forms of inputs at different sizes and image
resolutions should be implemented, including a well-coded and documented system for easier
future development.
Alongside the design and implementation of the face recognition system, a
mathematical derivation of the eigenface approach, based on the work of Turk and Pentland
[4], has been explored.

1.5. Scope
Scope of a project - is the sum total of all requirements or features.
Keeping this in mind, our Face Detection and Recognition system requires a system to
support the three key features implemented in our system, they are – Preprocessing, Face
Detection and Face Recognition (Detailed explanation of requirements and features to be
done in Chapter 2).
Also, Scope defines the size of the project. Scope can include such areas as
departments, geographic locations, deliverables, features and functions. So we are looking at
applications like 1.Credit card, driver’s license, passport, and personal identification.
2. Bank / store security
3. Crowd surveillance
4. Expert identification
5. Witness face reconstruction

Dept. of CSE, R.V.C.E

Jan-May’ 2007

4

Introduction

Face Detection and Recognition

6. Criminal Databases etc.
And many other such applications in which this system can be used.
Assumptions and Dependencies are mentioned in Chapter 3.

1.6. Motivation
What motivated us to take up this project?
!

The desire to create an application, which has equal social relevance and commercial
usage.

!

Security concern is a major issue in the current scenario; we wanted to develop an
application that addresses this issue.

!

This project helps us in integrating the new technological concepts with the
underlying biological features of the human body, thereby Minimizing the divide
between – “Man and the Machine”.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

5

Introduction

Face Detection and Recognition

1.7. Literature Survey
1. Eigenfaces for Recognition by Turk and Pentland
2. Image Processing in C Second Edition by Dwayne Phillips
3. Real Time Face Recognition by Carlos Leung, University of Queensland
Submitted for the degree of Bachelor of Engineering October 2001.
4. Digital Image Processing by Gonzalez, Woods
5. An Integrated Approach to Software Engineering by Pankaj Jalote, Narosa Publication
6. Programming in Matlab by Herniter
7. www.wikipedia.org – The online Encyclopedia
8. www.face-rec.org/algorithms - Official Face Recognition Site
9. www.mathworks.com – For Matlab tutorials
10. www.google.com – Awesome Searching Power

Dept. of CSE, R.V.C.E

Jan-May’ 2007

6

Software Requirements Specification

Face Detection and Recognition

2. Software Requirement Specification
2.1. Software Requirement Specification
In System Engineering and Software Engineering, requirements analysis[6]
encompasses those tasks that go into determining the requirements of a new or altered
system, taking account of the possibly conflicting requirements of the various stakeholders,
such as users. Requirements analysis is critical to the success of a project. Requirements must
be measurable, testable, related to identified business needs or opportunities, and defined to a
level of detail sufficient for system design.
It's important to note that an SRS contains functional and nonfunctional requirements
only; it doesn't offer design suggestions, possible solutions to technology or business issues,
or any other information other than what the development team understands the customer's
system requirements to be.

2.2. Overall Description
Since the Software Requirement Specification contains both Functional and nonfunctional requirements the following document states both of these requirements according
to IEEE standards[7]. The Face Recognition system is basically an application level project
meant to be used by different kind of end-users. Hence the requirements are oriented towards
not only satisfy technical specifications but also user interface requirements in a satisfactory
manner. The document also explains the product functions and user characteristics in a
comprehensive manner.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

7

Software Requirements Specification

Face Detection and Recognition

2.2.1. Product Perspective
The face detection and recognition system is a relatively new concept, which has only
recently come into commercial domain. Though a number of products are available to
perform face detection or recognition, there is still no definite method, which gives the best
reliability and performance. Different approaches include eigen faces[3], fisher faces, neural
networks[1] etc. Our objective in developing this product is to choose a reasonably accurate
method of face recognition to deliver the expected performance within our constraints.

2.2.2. Product Functions
The basic function of our project in layman terms is to recognize the face of a person
given as input. That is our product tries to simulate the human brain in the sense that humans
can recognize faces, which they have seen before (giving a little leeway to the fact humans
might forget few faces). So our product can be used in all applications where recognizing
people play an important part like security services etc. An important pre-requisite for face
recognition is to detect the presence of the face[5] in the input image as the input might not
contain a human face at all or might contain many faces etc. Hence detection of faces also
forms an important part of our product.

2.2.3. User Characteristics
This project is meant to be an academic project to be used for demonstrating the
viability of Face Recognition to all students and lecturers. However Face Recognition is
general-purpose software, which has wide applications and can be used by different people
across various domains. Hence it may be difficult to generalize the characteristics of people
who might be using the product eventually.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

8

Software Requirements Specification

Face Detection and Recognition

However since the product is expected to be used by people with no expertise in
technical field the following characteristics can be stated:
! The users would prefer a simple user interface with as few inner details revealed as
possible.
! Users would expect the system to be fast and extremely accurate (they may not
realize that 100% accuracy cannot be guaranteed with the current advancement in
technology)[1].

2.2.4. Constraints
During the development of any product, a number of constraints are encountered under
which the product must be developed. Some of the common constraints like time and
resources would be faced by almost all project teams. Some specific constraints under which
face recognition is developed are as follows:
! There is no known recognition algorithm giving close to 100% results[1]. Hence we
have to develop the software with the possibility of wrong result.
! We do not have a standard database of Indian people to test our project against hence
must develop our own test database.

2.2.5. Assumptions and Dependencies
Every project is completed with certain assumptions about users, technology used,
output expected etc and as well dependencies on other components. These assumptions
basically arise from the fact that, no project irrespective of its sophistication level can work
under all conditions. In case of the face recognition system developed by us the important
assumptions arise because of the dependence of the software on the kind of images given as
input, since, a three dimensional face is read as two dimensional image accurate
representation is possible only when the orientation of the face is similar, lighting conditions
are good etc.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

9

Software Requirements Specification

Face Detection and Recognition

Some of our assumptions and dependencies are as follows:
! The user of the system has basic computer knowledge to use it.
! The system satisfies the hardware and software requirements of our product.
! The inputs are given according to our specification - Fairly clear images containing
almost frontal faces.
! The image database is created by us.

2.3. Specific Requirements
While the above sections explain the product perspective and user characteristics they
do not state the actual requirements needed to be satisfied by the software system. The
specific requirements are the actual data over which the customer and software provider can
agree. That is, the final product is expected to satisfy all the requirements mentioned here.

2.3.1. Functional Requirements
The functional requirements for a system describe the functionality or services that
the system is expected to provide. These depend on the type software, which is being
developed, the expected users of the software and the type of system, which is being
developed. The functional requirements describe the system function in detail, its input
output etc.
2.3.1.1. Detect the presence of a face
The basic requirement of our software is given an input image our software should be
able to decide whether a human face exists in the image or not[8]. Further steps in face
recognition can take place only after this function is performed. The software should be able
to detect faces even if multiple faces exist and only human faces[5]. That is, the presence of
nonhuman faces should not be detected.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

10

Software Requirements Specification

Face Detection and Recognition

2.3.1.2. Identify the location of the face
This requirement goes along with previous requirement in the sense that, once the
presence of a face is detected its location needs to be identified and marked. The marked out
portion of the image is sent to face recognition. The marking should ensure that only the
portion of face is selected and not external surroundings and other parts of the body as it ll
reduce the effectiveness of face recognition stage.
2.3.1.3. Recognize the face
This is the primary requirement of our software. Given a face in the database it must
be recognized correctly. For faces not in the database an appropriate message must be
displayed. The recognition should be as accurate as possible under the given conditions and
input specifications. The user need not be aware of the method used to recognize the faces.

2.3.2. Performance
Since there are No. of different approaches to face detection and recognition it is
difficult to decide upon parameters, which determines whether our software is performing
well or not. By studying similar systems, which are already in place the following, the
parameters are approximately fixed as standards of optimal performance.
2.3.2.1. Detect the face
! Response time
Average response time for recognizing one face is 20 seconds.
Maximum response time for recognizing a face is 50 seconds
! Throughput
The system throughput cannot be given in terms of operations per second as
each operation involves complex computations and takes lot of time as given
above

Dept. of CSE, R.V.C.E

Jan-May’ 2007

11

Software Requirements Specification

Face Detection and Recognition

! Capacity
The product does not have a fixed capacity in terms no. of faces that can be
recognized. Given sufficient hard disk space unlimited no. of faces can be
stored in the database.
! Degradation Mode.
Since our product is designed to run on a single system with single user, the
degradation of the main node results in the software being stopped.
! Resource Utilization
The software is computationally expensive and hence requires at least 128
MB Ram and 1 GHz processor.
2.3.2.2 Recognize the face
! Response Time
The average response time is 30 seconds while maximum response time is 50
seconds.
! Throughput
The system throughput cannot be given in terms of operations per second as
each operation involves complex computations and takes lot of time as
mentioned above
! Resource Utilization
The software requires a minimum of 500 MB to store a substantially big face
database.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

12

Software Requirements Specification

Face Detection and Recognition

2.3.3. Supportability
This section indicates any requirements that will enhance the supportability or
maintainability of the system being built, including coding standards, naming conventions,
maintenance access, maintenance utilities etc[7].
2.3.3.1. The software should provide options to maintain the database.
This requirement basically states that, it must be possible for the user to add new faces
into training database as well as clear the current database and create a new one. This feature
is essential because as the software is put into use many new faces may need to be
recognized for which it needs to stored in the database or added freshly. During the next run
of the software these faces can also be recognized.

2.3.4. Interfaces
This section defines the interfaces that must be supported by the application. The
interfaces include, software and hardware interfaces like ports to be used, logical addresses
etc. However the face recognition system developed by us does not require any hardware
interfaces and hence only software requirements are specified.
2.3.4.1. User interfaces
Good user interface design is critical to the success of a system. An interface that is
difficult to use will, at best result in a high level of user errors. At worst, users will simply
refuse to use the software system irrespective of its functionality. If information s presented
in a confusing or misleading way, users may misunderstand the meaning of information.
The product must provide the following user interfaces.
! A separate graphical user interface for training and recognition.
! The UI for training should provide the options to maintain the training database.
! The UI for general user should enable him to upload image for recognition and get
the results back.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

13

Software Requirements Specification

Face Detection and Recognition

2.3.4.2. Software interfaces
The product requires access to JAMA package[9], which is open source software.
JAMA stands for Java Matrix package. This component is required is required to perform
matrix manipulations. JAMA is a basic linear algebra package for Java. It provides user-level
classes for constructing and manipulating real, dense matrices. It is meant to provide
sufficient functionality for routine problems, packaged in a way that is natural and
understandable to non-experts.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

14

High Level Design

Face Detection and Recognition

3. High Level Design
3.1. High Level Design
Software sometimes can be a complex entity. Its development usually follows what is
known as Software Development Life Cycle (SDLC)[7]. The second stage in the SDLC is
the Design Stage. The objective of the design stage is to produce the overall design of the
software. The design stage involves two sub-stages namely:
1. High-Level Design
2. Detailed-Level Design
In the High-Level Design, the Technical Architect of the project will study the
proposed applications functional and non-functional (qualitative) requirements and design
overall solution architecture of the application, which can handle those needs.
High Level Design means precisely that. A high level design discusses an overall view
of how something should work and the top-level components that will comprise the proposed
solution. It should have very little detail on implementation, i.e. no explicit class definitions,
and in some cases not even details such as database type (relational or object) and
programming language and platform.
In our project, the high-level design stage consists of decomposing the project into toplevel modules of face detection, preprocessing and face recognition, which are explained in
further parts of the chapter. The system interacts with the user to get the input and provides
as output the info about recognized person.

Dept. of CSE, R.V.C.E

Jan-May’2007

15

High Level Design

Face Detection and Recognition

3.2. Design Considerations
There are a number of design considerations, which must be taken into account before
design phase is begun. The Issues that we need to address before considering a design for
implementing our system are: ! Position of the Face
! Illumination
! Facial Expression
! Occlusion due to other Objects (E.g. Sunglasses!!)

3.2.1. Assumptions and Dependencies
Every project is completed with certain assumptions about users, technology used,
output expected etc and as well dependencies on other components. These assumptions
basically arise from the fact that no project irrespective of its sophistication level can work
under all conditions. In case of the face recognition system developed by us, important
assumptions arise because of the dependence of the software on the kind of images given as
input. Other assumptions regarding operating systems, hardware requirements are also
specified.
Some of our assumptions and dependencies are as follows:
! The user of the system has basic computer knowledge to use it.
! The system satisfies the hardware and software requirements of our product.
! The inputs are given according to our specification - Fairly clear images containing
almost frontal faces.
! The image database is created by us.

3.2.2. General Constraints
General constraints specify the constraints one has developed the project under. These
constraints can have significant impact on the final system being developed and the
performance of the system. Constraints are limitations while developing the project including
hardware specifications, user interfaces, and interoperatability requirements etc.

Dept. of CSE, R.V.C.E

Jan-May’2007

16

High Level Design

Face Detection and Recognition

! The system in which our application is installed is expected to have minimum of 512
MB hard disk space, this is because we are storing the faces in a file along with
certain information about the face. When everything is done, the values are so stored
that the user cannot exclusively access the information. Doing so requires a lot of
space and hence to make sure that our application works, we need so much space.
! Graphical User Interface is being provided, and every care is taken to see that the UI
is easy to understand and manageable by even a computer layman.
! Since our application does a lot of computations, it is necessary to have a fast
processor (1.7 GHz P4 Processor).
! Everything that is required to be stored, is stored in a file and to these files, the
exclusive access for the user is denied.
! As mentioned above, we require a minimum of 128 MB RAM and 512 MB Hard disk
space to do computation comfortably.
! The system needs to be trained with different faces since we are relying on setting
certain threshold values depending on the information extracted in the training phase.

3.2.3. Development Method
Although we did consider many strategies for developing this system, the one, which
suited us best, was the functional development approach[6]. In this method, we list out the
different functions that we can have in our application and start developing them. The
functional dependencies are maintained throughout this process. Also, to be noted is the input
– output data that flows from one function to another function remains same.

Dept. of CSE, R.V.C.E

Jan-May’2007

17

High Level Design

Face Detection and Recognition

Rapid Application Development
A prototype is an initial version of a software system, which is used to demonstrate
concepts, try out design options and generally to find out more about the problem and its
possible solutions. Since the face detection and recognition is a relatively new field under
research we felt it was necessary to build a prototype of the system before we go ahead with
it final implementation in high level programming language.
Among the available prototyping techniques, rapid prototyping technique[6] was the
most preferable one for our project due to the short time we have at our disposal. Rapid
prototyping techniques are development techniques, which emphasize speed of delivery
rather than other system characteristics such as performance, maintenance or reliability.
Matlab was the tool we decided to use for developing the prototype because of its
inbuilt features for image processing, matrix manipulations etc. The rest of features of the
language are given in implementation chapter.
To Aid us in functional development of the system, we have taken the help of Data
Flow Diagrams, which are mentioned in Chapter 3.3

3.3. Architectural Strategies
We have developed the system using the Top-Down approach[6]. In this method, the
entire system is visualized a whole, later each component of the system is split into modules,
which, in the next level are further divided into sub-modules and so on.
•

Matlab and Java programming language have been used to develop the application

•

Making an application platform independent requires the usage of higher-level
languages, which can achieve platform independence, thus Java is being used here.

•

User Interface developed in Java enables a layman to easily understand the depicted
functionality of the application and corresponding mapping is being done to help
making the usage of the application easy

Dept. of CSE, R.V.C.E

Jan-May’2007

18

High Level Design
•

Face Detection and Recognition

Usage of JAMA – a Java Matrix Package, is done to help us in standardizing the
operations being performed, thereby achieving computational efficiency.

3.4. System Architecture
The approach used in our application development is a function-based approach, where
in we classify the system into different functions, which can perform certain operations on
the given input and give us the required output. Thus based on this approach, we classify our
Face Detection and Recognition software into three basic functionalities namely! Pre-Processing
! Face Detection
! Face Recognition
Pre-processing is the stage where we take a color image which is either a .jpg or a .tif or
a .bmp file, perform operations on the image like gray scale conversion[10], histogram
equalization[11], noise reduction[11] etc. to see to it that the final image obtained is free of
color, lightning or scaling constraints, thus helping us to analyze each image equally rather
than giving priority to any single image based on its color, lighting or scaling factors. The
output of this functionality is a pre-processed image, which is independent of the abovementioned considerations
Face Detection is the next stage, where in a pre-processed image is taken as an input
and calculations are performed on that particular image to see whether it contains a
recognizable face or not. If a face is present, then that particular area of face is highlighted
and it is cut from the input image and given to the next functionality for further calculations.
The detection of face in a pre-processed image is done using an algorithm proposed in a
paper [5]. The output of this functionality is a detected face scaled to particular size.
Face Recognition is the final stage of the system, where the Detected face is taken
from the Face Detection phase, and it is compared with the existing faces in the database (in
our context, eigen faces) and if there is a match (within a given threshold[4]) then the output
about the particular face is displayed.

Dept. of CSE, R.V.C.E

Jan-May’2007

19

High Level Design

Face Detection and Recognition

The rationale used in dividing our application into three basic functionalities is simple.
The user of the application can give any form of image (compatible with our application).
The system which is used to recognize this image doesn’t know the contents in the image,
thus we need to treat every image as same, thus to achieve this equality, we go for preprocessing. Also when an image is given, it is not necessary that it should contain a human
face, user might be intelligent enough to give a nature picture or a picture of an animal or a
completely abstract picture, thus we require a detection functionality which detects if the
given input image contains a human face or not, if it contains a human face, then it is going
to crop the input image and give only the human face to the next stage. A recognition system
is required to recognize the input got from the detection phase from the available set of faces
in the database and display the information accordingly.

3.5. System Architecture (DFDs)
Large systems are always decomposed into subsystems that provide some related set of
services. The initial design process of identifying these subsystems and establishing a
framework for sub-system control and communication is called architecture design. The
output of this design process is a description of the software architecture.

3.5.1 DFDs – Data Flow Diagrams
Data-flow models [7] are an intuitive way of showing how data is processed by a
system. At the analysis level, they should be used to model the way in which data is
processed in the existing system. The notations used in these models represents functional
processing, data stores and data movements between functions. Dataflow models are used to
show how data flows through a sequence of processing steps. The data is transformed at each
step before moving on to the next stage. These processing steps or transformations are
program functions when dataflow diagrams are used to document a software design.

Dept. of CSE, R.V.C.E

Jan-May’2007

20

High Level Design

Face Detection and Recognition

Level 0 DFD – The Face Detection and Recognition System
This DFD depicted in Fig 3.1 shows the three most significant functions of our system.
This is the most basic split of functions, which can be done for a Face Detection and
Recognition system. The image input by the user is pre-processed and sent to face detector.
After detecting the face it is sent to face recognition.

Input Image

Jpeg or tiff
images

1

Face
Detection

2

Detected Face

PreProcessing

Pre-processed
Image

Info. about the
Image

Face
Recognition

3

Trained Faces

Database

Fig 3.1 – Level 0 DFD for Face Detection and Recognition System

Dept. of CSE, R.V.C.E

Jan-May’2007

21

High Level Design

Face Detection and Recognition

Level 1 DFD for Node 2 – The Preprocessing of Input Image
This DFD depicted in Fig 3.2 shows the steps present in the preprocessing block of the
Face Detection and Recognition system. The data flow from one functionality to another is
clearly depicted here; also the transformation of the data that takes place is also represented.

Detected Face
2.1
Gray
Scale
Converter

Face Image

2.2
Gray Image

Brightnes
Norm.

Brightness
Normalized
Image

For Face
Recognition /
Training

Noise
Reduced
Image

Noise
Reduction

Histogram
Equalized
Image

2.4

Histogra
m
Equalize.

2.3

Fig 3.2 – Level 1 DFD for Pre-processing

Dept. of CSE, R.V.C.E

Jan-May’2007

22

High Level Design

Face Detection and Recognition

Level 1 DFD for Node 1 – Face Detection
This DFD depicted in Fig 3.3 shows the Functionalities involved in the Face Detection
block of the system. The conversion of the Input Image into an image containing only a face
(if present) is shown here. The input to this stage is a color image in RGB format.

Input Image

Jpeg or tiff Image

1.1

1.2

1.3

RGB
To
HSV

Edge
Map
Extrac

Hue,
Saturat.
Extrac.

Image in
HSV

Edge
Detected
Image

Hue,
Saturation
Values

1.7
Compar
&
Classify

Calc.
Values

Detected Face

Calc.
Ht. wt
Centrod

Detected Skin
Regions

1.6

Connec-tivity
Analysi

Diff. Image

1.5

Comp.
Threshold

1.4

Database

Fig 3.3 – Level 1 DFD for Face Detection

Dept. of CSE, R.V.C.E

Jan-May’2007

23

High Level Design

Face Detection and Recognition

Level 1 DFD for Node 3 – The Face Recognition System
This DFD depicted in Fig 3.4 shows the steps involved in the Face Recognition block
of the system. The final output of this block will be the information about the face that was
given as an input to the Face Detection and Recognition system. Before recognition can be
performed it is necessary to perform training on the set of images in the database.

Detected Face
3.1

3.2

Initializa-tion or
Training

Project
onto
Eigen
Faces

Faces

Eigen Vector

Classify
Face

Info. About Face

Projected
Vectors

Determine

Weights
Weights

3.4

3.3

Database

Fig 3.4 – Level 1 DFD for Face Recognition

Dept. of CSE, R.V.C.E

Jan-May’2007

24

High Level Design

Face Detection and Recognition

Level 2 DFD for Node 3.1 – Training
No Face Detection and Recognition system can be directly used to recognize an image
without training it. This DFD depicted in Fig 3.6 shows how our system undergoes training
with the input image being a detected face image from the given set of training images. The
training is the most time consuming part of face recognition system.

Detected Face
3.1.1
Face Image

3.1.2

Mean
Face
Calc.

Mean Face

Compare
Mean and
Input

Difference

K max Eigen Vectors & Wts

Database

Select k
Eigen
Vectors,
Weights

M Eigen
Faces

3.1.4

PCA
3.1.3

Fig 3.5 – Level 2 DFD for Training of Detected Face

Dept. of CSE, R.V.C.E

Jan-May’2007

25

Detailed Design

Face Detection and Recognition

4.Detailed Design
4.1. Detailed Design
Once the high level design is completed the next stage is to perform detailed design of the software.
While the high level design focuses on the tasks to be performed, the detailed design concentrates on how these
can be performed. It describes the modules in terms of the data structures used and the algorithms, which
explain how the modules are implemented. A major task of detailed design is to spell out, in detail, the
attributes and methods needed by each class.

4.2. Structured Charts
"Structured Design" (STRD[6]) is a method that can be applied both for the preliminary and for the
detailed design of the software. The objective of STRD in the preliminary design, is to structure both the higher
ranking control sequences and the actual processing functions in form of a module hierarchy.

The structure chart is the graphic means of representation for STRD. The basic
elements of a structure chart are modules. In the case of the SW architecture, modules refer
to individual subprograms. The representation differentiates between modules, predefined
modules, data modules, macros, and multiple entry point modules.
By means of structure charts, the calling structure between modules (functions,
subprograms) can be represented. These representations include sequence, selection, and
iteration in connection with module calls. With each call, data and control flows can be listed
separately. If required, the call parameters may be better specified in table-like footnotes. The
structure charts also permit comments to the modules. In order to improve the arrangement of
large diagrams, relations can also be represented by means of connectors. These make a
representation of relations beyond the page margins possible.
Structure charts show module structure and calling relationships. In a multi-threaded
system, each task (thread of execution) is represented as a structure chart. Large structure
charts are leveled into a stack of connected diagrams.

Dept. of CSE, R.V.C.E

Jan–May’2007

26

Detailed Design

Face Detection and Recognition

4.2.1. Structured Chart for Face Detection and Recognition System
This Structured Chart given in Fig 4.1 depicts the structure and calling relationships in
the main module. Each component of this structured chart is broken down into lower level
components.

Main GUI

Input Image
Detected Face

Face Detection

Detected Face

Pre-Processed Image

Pre-processed Image

Recognized Face

Pre-Processing

Face Recognition

Fig 4.1 – Structured Chart for Face Detection and Recognition System

Dept. of CSE, R.V.C.E

Jan–May’2007

27

Detailed Design

Face Detection and Recognition

4.2.2. Structured Chart for Pre-processing
This Structured Chart given in Fig 4.2 depicts the structure and calling relationships
in the Pre-processing module. In this Structured chart, we can clearly see the calling
relationships and the data that flows between each of the modules present in the structured
chart.

Pre-Processing

Detected
Faces

Gray Scale
Image

Normalized Image

Equalized Image

Normalized Image

Gray Scale
Image

Gray Scale Conversion

Equalized Image

Brightness
Normalization

Histogram
Equalization

Noise Reduced
Image

Noise Reduction

Fig 4.2 – Structure Chart for Pre-processing

Dept. of CSE, R.V.C.E

Jan–May’2007

28

Detailed Design

Face Detection and Recognition

4.2.3. Structured Chart for Noise Reduction
This Structured Chart given in Fig 4.3 depicts the structure and calling relationships
in the Noise Reduction module. In this Chart we show the different data dependencies
between the modules present in Noise Reduction. The final output of this is an image in
which the noise levels will be very less.

Noise Reduction

Smoothened Image

Histogram Equalized
Image
Edge Enhanced Image
Edge Enhanced Image

Smoothened Image

High Pass Filter

Median Pass Filter

Noise
Reduced
Image

Low Pass Filter

Fig 4.3 – Structure Chart for Noise Reduction

Dept. of CSE, R.V.C.E

Jan–May’2007

29

Detailed Design

Face Detection and Recognition

4.2.4. Structured Chart for Face Detection
This Structured Chart given in Fig 4.4 depicts the structure and calling relationships
in the Face Detection module. In this Chart, we depict how data flows between the different
modules present in the Face Detection main module and the order in which each sub-module
is called is also clearly depicted.

Face Detection
Input
Image
HSV Image

HSV Comp.

Edge Detected Img

Edge Detected Img
HSV Image

RGB 2 HSV

Detected Skin

Adjusted Img

HSV Comp.

Detected Skin

Adjusted Img

Edge Map

HSVExtrac

Wt. Ht.
Centroid

Thres. Comp

Conn. Ana

Wt. Ht.
Centroid

Wt.Ht.Cent

Detected Face

Classify

Fig 4.4 – Structure Chart for Face Detection

Dept. of CSE, R.V.C.E

Jan–May’2007

30

Detailed Design

Face Detection and Recognition

4.2.5. Structured Chart for Face Recognition
This Structured Chart given in Fig 4.5 depicts the structure and calling relationships
in the Face Recognition module. In this chart, we show how each sub-module is called, the
order in which they are called and what are the input and outputs of each of the sub-modules.
All these information are clearly depicted.

Face Recognition

Calculated Wts.
Pre-processed Face

Initialized Values

Initialized Values

Training

Eigen Faces

Eigen Faces

Calculated Wts.

Project Eigen Faces

Wt. Calculation

Recognized Face

Classify

Fig 4.5 – Structure Chart for Face Recognition

Dept. of CSE, R.V.C.E

Jan–May’2007

31

Detailed Design

Face Detection and Recognition

4.2.6. Structured Chart for Training
This Structured Chart given in Fig 4.6 depicts the structure and calling relationships
in the main module. In this chart, we show how data gets transformed from a plain face
detected image into an eigen face and eigen value which is used in the training of the system.

Training

Detected Face

Mean Face

Mean Face

Mean Face Calc.

Comp. Mean, I/p.

PCA

Select Eigen Vec. &
Wts.

Fig 4.6 – Structured Chart for Training

Dept. of CSE, R.V.C.E

Jan–May’2007

32

Detailed Design

Face Detection and Recognition

4.3. Module 1: Face Detection
Face detection is a computer technology that determines the locations and sizes of
human faces in arbitrary (digital) images. It detects facial features and ignores anything else,
such as buildings, trees and bodies. Face detection can be regarded as a more general case of
face localization; in face localization, the task is to find the locations and sizes of a known
number of faces (usually one). In face detection, one does not have this additional
information.

4.3.1. Introduction
Classification: Module
Face detection means to detect the presence of a face in the image. A given natural
image often contains many more background patterns than face patterns. Indeed, the number
of background patterns may be 1,000 to 100,000 times larger than the number of face
patterns. This means that if one desires a high face-detection rate, combined with a low
number of false detections in an image, one needs a very specific classifier.

4.3.2. Purpose
The input image may or may not contain a human face. The purpose of this module is
to detect the presence or absence of such a face and to mark such a region in the image. All
nonface images must not be detected.

Dept. of CSE, R.V.C.E

Jan–May’2007

33

Detailed Design

Face Detection and Recognition

4.3.3. Functionality
Start
Input Image
RGB to HSV

Converted Image

Edge Map Extraction

Edge Detected Image
HSV Value Extraction
Extracted Value
Compare with Threshold
Difference Image
Connectivity Analysis
Skin Region Detected
Calculate ht wt & centroid
Compare & Classify
Detected Face
Stop
Fig 4.7 – Flow Chart for Face Detection

Dept. of CSE, R.V.C.E

Jan–May’2007

34

Detailed Design

Face Detection and Recognition

Input: An image containing zero or more human faces
Output: If a face exists then the portion of the image containing the face is the output of this
phase else a message is popped up stating that such a face doesn’t exist.

4.3.4. Intercomponent Relationship
Uses: This module uses the following sub modules
Facehistogram
Converttohsv
Region
Goldenratio

Resources: Requires a set human faces for constructing face histogram

4.4. Module 2: FaceHistogram
In order to train the face detection system we need to download images and extract
the skin pixels manually. For each pixel hue and saturation values are extracted and the value
of corresponding bin is incremented by one. After training[4] is complete histogram is
normalized. The skin color falls in a small region in the entire hue saturation scale.

4.4.1 Introduction
Classification: Function
Face histogram[5] means constructing the frequency distribution table for the skin of
the faces. The faces should be of different races and regions so that all kinds of faces are
accounted for.

4.4.2. Purpose
The human skin has a hue and saturation which maps into a particular range . The
purpose of this module is to determine the region into which human skins map into by
constructing the histogram of human faces.

Dept. of CSE, R.V.C.E

Jan–May’2007

35

Detailed Design

Face Detection and Recognition

4.4.3. Functionality
Input: A set of face images.
Output: Histogram of all faces representing skin pixels
The pseudo code for this module is as follows
Input <- Input image
Width <- get width of the image
Height <- get height of the image
hsv <- Converttohsv( Input )
For i <- 1 to Height
For j <- 1 to Width
r <- hsv[i][j][0]
s <- hsv[i][j][1]
r<-(int) (floor(r*100))
s<-(int)(floor( s*100))
colhist[r][s]<-colhist[r][s]+1
End for loop
End for loop
Return colhist
End of pseudo code

4.4.4. Intercomponent Relationship
Interactions: This is a sub-module of face detection module. This module is called before
the main face detection module is run, in order train the software for human faces.

Resources: Requires a set of face images
Uses: This module uses the facility of the following sub-modules:
Converttohsv

Dept. of CSE, R.V.C.E

Jan–May’2007

36

Detailed Design

Face Detection and Recognition

4.5. Module 3: Converttohsv
The HSV[10] (Hue, Saturation, Value) model, also known as HSB[10] (Hue,
Saturation, Brightness), defines a color space in terms of three constituent components:
Hue, the color type (such as red, blue, or yellow) which ranges from 0-360 (but
normalized to 0-100% in some applications)
Saturation, the "vibrancy" of the color which also ranges from 0-100%. Also sometimes
called the "purity”. The lower the saturation of a color, the more "grayness" is present and the
more faded the color will appear, thus useful to define desaturation as the qualitative inverse
of saturation
Value, the brightness of the color which ranges from 0-100%

4.5.1. Introduction
Classification: Function
HSV stands for Hue, Saturation and value. This is another format of storing color
images.

4.5.2. Purpose
Human skin can be easily detected if the image represented in HSV format. Hence the
purpose of this module is to convert RGB format to HSV format. Each pixel in the input
image is transformed into HSV scale.

4.5.3. Functionality
Input: Input image in RGB
Output: Output image in HSV.

Dept. of CSE, R.V.C.E

Jan–May’2007

37

Detailed Design

Face Detection and Recognition

The pseudo code for this module is as follows
Input <- RGB[ ][ ][ ] //A 3-Dimensional array containing the RGB values of the
//image
Height <- Get height of the image
Width <- Get width of the image
For i <- 1 to height
For j <- 1 to width
r <- RGB[i][j][1]
g <- RGB[i][j][2]
b <- RGB[i][j][3]
min_val <- min(r,g,b)
max_val <- max(r,g,b)
v <-max_val
delta <- max-min
If ( max !=0 )
s <- delta /max
Else
hsv[i][j][0]<-0
hsv[i][j][1]<-0
hsv[i][j][2]<-v
continue
end if-else
if ( r == max_val)
h <- ( g – b ) / delta
else if ( g == max_val)
h <- 2 + ( b – r ) / delta
else
h <- 4 + ( r- g ) / delta
h <- h * 60

Dept. of CSE, R.V.C.E

Jan–May’2007

38

Detailed Design

Face Detection and Recognition
if ( h < 0)
h <- h + 360
hsv[i][j][0] <- (float)h / 360
hsv[i][j][1] <- s
hsv [i][j][2] <- v

End for loop
End for loop
Return hsv
End of pseudo code

4.6. Module 4: Calculate_Skin
In order for the face detection module to work properly using the method we have
used it must be able to differentiate between skin and non-skin pixels[5]. This is done using
the hsv scale values as human skin belongs only to a small region of this scale.

4.6.1. Introduction
Classification: Function
Each skin pixel has its Hue and Saturation values in a defined interval. Once the
input is converted into HSV scale each pixel is examined to determine if it belongs to the
defined interval. If so it is classified as skin pixel.

4.6.2. Purpose
The purpose of this module is to classify an image as skin pixels and non-skin pixels
based on the face histogram created for the training set. The skin pixels are given separate
values from non-pixel values so that further modules can differentiate between them.

4.6.3. Functionality
Input: The face histogram previously generated using training images is loaded into
memory. The input image is sent as an input.

Dept. of CSE, R.V.C.E

Jan–May’2007

39

Detailed Design

Face Detection and Recognition

Output: A binary image with skin pixels detected.
The pseudo code for this module is as follows
Colorhist <- load the face histogram into memory from file
Input <- input image
Height <- get height of the image
Width <- get width of the image
For i <- 1 to Height
For j <- 1 to Width
Skin [i][j] <- 0 ; // initialize skin image ,1 if skin pixel
// else non-skin
End for loop
End for loop
For i <- 1 to 100
For j <- 1 to 100
b[i][j] <- colhist[i][j] /max;
End for loop
End for loop
For i <- 1 to Height
For j <- 1 to width
r <- hsv [i][j][0];
s <- hsv [i][j][1];
r <- floor ( r * 100 );
s <- floor ( s * 100 );
if ( b [r ] [s] > 0.1 )
Skin[i][j] <- 1 //Skin Pixel found
End for loop
End for loop
End of pseudo code

Dept. of CSE, R.V.C.E

Jan–May’2007

40

Detailed Design

Face Detection and Recognition

4.6.4. Intercomponent Relationship
Interactions: This is a sub-module of face-detection module
Resources: Face-histogram
Uses: This module uses the facilities of the following modules:
Converttohsv

4.7. Module 5:Region
Regioning is necessary in order to group together skin pixels so that they form a
meaningful region. The regions are formed using either 4-connectivity or 8-connectivity
algorithms[11].

4.7.1 Introduction
Classification: Function
Region is a part of an image, which could potentially be a face. Once regions are
formed they can be checked to see if they represent a face or not. This enables in reducing
false detections[8].

4.7.2. Purpose
The purpose of this module is to group related skin pixels into regions, which could
eventually represent a face.

4.7.3. Functionality
Input: Image with different values for skin and non-skin pixels.
Output: The image classified into different regions.
The pseudo code for this module is as follows
Input <- Skin Image // Image with skin pixels classified.
Height <- Height of Skin Image

Dept. of CSE, R.V.C.E

Jan–May’2007

41

Detailed Design

Face Detection and Recognition

Width <- Width of Skin image
For i<- 1 to Height
For j <- 1 to Width
Reg[i][j] <- 0 //it will eventually contain the regions labeled
//according to 8-connectivity
End for loop
End for loop
Count <-0
For i<- 1 to Height
For j <- 1 to Width
A <- Res[i-1][j-1] // Top-left neighbor
B <- Res[i-1][j] // top neighbor
C <- Res[i-1][j+1] // Top-Right neighbor
D <- Res[i] [j-1] //Left Neighbor
If ( A ==0 && B ==0 && C ==0 && D ==0)
Count++
Res[i][j] <- Count
Else if all belong to reg k
Res[i][j] <- Count
Else
Res[i][j] <- min of the region values
Indicate the dependency of the regions
End for loop
End for loop
// Resolve the dependency in the regions
For i <- Count back to 1
If flag[i]
for j <- 1 to Height
for k <- 1 to Width
if res[j[k] == i
res[j][k] <- flag[i];

Dept. of CSE, R.V.C.E

Jan–May’2007

42

Detailed Design

Face Detection and Recognition
end for loop
end for loop

end for loop
return res
end of pseudo code

4.8. Module 6: Goldenratio
The golden ratio[10], also known as the divine proportion, golden mean, or golden
section, is a number often encountered when taking the ratios of distances in simple
geometric figures such as the pentagon, pentagram, decagon and dodecahedron. It is denoted
, or sometimes . In mathematics and the arts, two quantities are in the golden ratio ( which
is ( 1 + sqrt(5)) / 2, approximately 1.6180339887 ) if the ratio between the sum of those
quantities and the larger one is the same as the ratio between the larger one and the smaller.

4.8.1 Introduction
Classification: Function
Golden ratio refers to the fact that many things in nature follow the golden ratio of
height to width including the human face.

4.8.2. Purpose
After the previous grouping stage many groups of potential faces would be found.
The purpose of this module is to choose among those only the faces using the golden ratio.

4.8.3. Functionality
Input: Images with regions demarcated.
Output: Images with only faces demarcated.
The pseudo code for this module is as follows

Dept. of CSE, R.V.C.E

Jan–May’2007

43

Detailed Design

Face Detection and Recognition

Input <- region labeled image
For i<- 1 to N // N = number of regions detected
Reg [i][] [] <- find coordinates with res[j][k] equal to i
For j <-1 to N //number of pixels in region i
Find Height of the region
Find Width of the region
End for loop
K <- height / width
If k>0
Face_ratio <- k
Else
Face_ratio <- 1 / k
If ( ( Face_ratio > = (1 + sqrt(5))/2 – threshold ) &&
(Face_ratio < =( 1+sqrt(5) )/2 + threshold ) )
Face region detected
End for loop
End of pseudo code

4.9. Module 7: Preprocess
This module of the face recognition system as the term implies is used to preprocess
the input images input into the system. Preprocess[11] basically means to manipulate the
images so that they follow particular specifications, which is necessary for further stages.

4.9.1. Introduction
Classification: Module
Preprocessing means to process or modify the image in order to obtain a constant
image. The prefix ‘pre’ implies that this module is performed before actual face recognition.

Dept. of CSE, R.V.C.E

Jan–May’2007

44

Detailed Design

Face Detection and Recognition

4.9.2. Purpose
The purpose of this module is two fold. To process the image in such a way that the face
recognition module gets a constant input. The second purpose is to improve the clarity of the
image.

4.9.3. Functionality
Start
Detected Face

Gray Scale Conversion

Gray Scale Image

Brightness Normalization

Norm. Image

Histogram Equalize

Equalized Image

Noise Reduction

Noise Reduced Image

Stop
Fig 4.8 – Flow Chart for Pre-processing

Dept. of CSE, R.V.C.E

Jan–May’2007

45

Detailed Design

Face Detection and Recognition

• Input:
Detected image with only face in RGB format

• Output:
The output is grayscale converted and processed image.

4.9.4. Intercomponent Relationship
Uses: This module uses the following sub-modules
Grayscale conversion
Histogramequalisation
Filter
Resize

Interactions: The module interacts with face recognition by supplying its input. It gets its
input from the face detecton unit.

Interface:
Constants: max_size: Maximum size of the input image
Min_size: Minimum size of image
Filter_map: Matrix used for filtering
Exceptions: over_size: When size exceeds max_size
Under_size: When size is less than min_size

4.10. Module 8: Grayscale Conversion
Grayscale[10] conversion module is necessary to convert any color image into
corresponding grayscale equivalent. There are no of methods to do this. We have used a
method, which experimentally gives the best results.

Dept. of CSE, R.V.C.E

Jan–May’2007

46

Detailed Design

Face Detection and Recognition

4.10.1 Introduction
Classification: Function
Gray scale conversion means to convert any image into gray color. Grayscale gives
better performance than color images for face recognition.

4.10.2. Purpose
The user may specify input in different types of color formats[11]. The purpose of
this module is to convert any such image into standard gray format[11]. Converting to gray
scale also results in saving memory as 8 bits can be used to represent gray color rather than
24 bits for color images.

4.10.3. Functionality
Input: Color image in .jpg or .tif format
Output: Gray image
The pseudo code for this module is as follows:
Input <- Input Image
For i <- 1 to N, No of rows
For j<- 1 to N, No of columns
Pixel <- Input [i][j]
Red <- red component of pixel
Green <- green component of pixel
Blue <- blue component of pixel
Gray <- 0.59*red + 0.30*green + 0.19*blue
End for loop
End for loop
End of pseudo code

Dept. of CSE, R.V.C.E

Jan–May’2007

47

Detailed Design

Face Detection and Recognition

4.11. Module 9: Histogram Equalization
One

method

of

enhancing

an

image

is

commonly

called

"histogram

equalization"[10]. With this technique, the intensity histogram of an image is first calculated.
From this an adjustment is calculated so that the resultant image has a cumulative histogram,
which is more nearly linear. The aim is to try to make more effective use of the overall
intensity range available.

4.11.1 Introduction
Classification: Function
It means the input image is modified so that the histogram of the final image has flat
histogram curve. This results in the image having high contrast and hence visually appealing
image.

4.11.2. Purpose
The image input by the user might not have sufficient contrast between light and dark
pixels. The purpose of this module is to modify the image by improving its contrast.

4.11.3. Functionality
Input: Gray scale image
Output: Histogram equalized Gray image
The pseudocode is as follows:
Input <- Input Image
For i <- 1 to N, NO. of rows
For j <- 1 to N, No. of columns
K <- Input Image [i][j]
Hist [k] <- Hist [k] + 1
End for loop
End for loop

Dept. of CSE, R.V.C.E

Jan–May’2007

48

Detailed Design

Face Detection and Recognition

// Calculate sum of the histograms obtained
For i <-1 to G, No. of gray levels
Sum <- Sum + Hist [i]
Sum_of_Hist [i] <- Sum
End for loop
// Transform input image to output image
Area <- Area of Input Image (rows X columns)
Dm <- No. of gray levels in output image
For i <- 1 to N, No. of rows
For j <- 1 to N, No. of columns
K <- Input Image[i][j]
Out_Image[i][j] <- ( Dm / Area ) * Sum_of_Hist[k]
End for loop
End for loop
End of pseudo code

4.12. Module 10: Low Pass Filter
Another processing procedure falling into the enhancement category that often
divulges valuable information of a different nature is spatial filtering[11]. Although less
commonly performed, this technique explores the distribution of pixels of varying brightness
over an image and, especially detects and sharpens boundary discontinuities. Low pass
filters, which suppress high frequencies, are useful in smoothing an image, and may reduce
or eliminate "salt and pepper" noise.

4.12.1 Introduction
Classification: Function
It filters out unnecessary disturbances in the image. It is used to reduce the noise
present in the images.

Dept. of CSE, R.V.C.E

Jan–May’2007

49

Detailed Design

Face Detection and Recognition

4.12.2. Purpose
The purpose of low pass filter is to remove salt and pepper type of noise in the input
image. It is used to reduce the noise present in the images. This is important as it might
reduce the accuracy of face recognition system.

4.12.3. Functionality
Input: Grayscale image
Output: Filtered gray image
Input <- Input Image
Initialize Convolution_mask[3][3]
Initialize Constant_divisor
For i <- 2 to N-1 , No. of pixels
For j <-2 to N-1, No. of pixels
Sum <- 0
For a <- -1 to 1
For b <- -1 to 1
Sum <- Sum + Input[i+a][j+b] *
Convolution_Mask[a+1][b+1]
End for loop
End for loop
Sum <- Sum / Constant_divisor
If ( sum < 0 )
Input[i][j] <- 0
Else if ( sum > 0 )
Input[i][j] <- max_gray_level
Else
Input[i][j] <- sum
End for loop
End for loop
End of pseudo code

Dept. of CSE, R.V.C.E

Jan–May’2007

50

Detailed Design

Face Detection and Recognition

4.13. Module 11: Resize
Resizing[12] is a basic function arising from the fact that images available on Internet
as well as input by the user are of different sizes. This vast difference in sizes results in
difficulty while recognizing faces. Hence the images must be resized to be of standard size.
That is if the images are large they must be minimized and if they are small they must be
enlarged.

4.13.1 Introduction
Classification: Function
Resizes the input image. All the images sent to the face recognition module are of
fixed size as specified by us.

4.13.2. Purpose
The input image may be of various sizes. The purpose of this module is to fix the
sizes of all images to a standard size. Large images are minimized while small ones are
enlarged as required.

4.13.3. Functionality
Input: Grayscale image
Output: Gray image of standard size
The pseudocode is as follows:
Input <- Input Image
Size <- Get Image dimension
If ( Size > Threshold )
Modified_In_Img <- Resize(Input, threshold_x, threshold_y)
End of pseudo code

Dept. of CSE, R.V.C.E

Jan–May’2007

51

Detailed Design

Face Detection and Recognition

4.13.4. Intercomponent Relationship
Interactions: This is a sub-module of preprocess module. The preprocess calls this module
if the input is not of the standard size.

Interface:
Constants: out_row: No of rows in output image
Out_col: No of columns in output image

4.14. Module 12: Face Recognition
A facial recognition system is a computer-driven application for automatically
identifying a person from a digital image. It does that by comparing selected facial features in
the live image and a facial database.
It is typically used for security systems and can be compared to other biometrics such
as fingerprint or eye iris recognition systems.
Popular recognition algorithms include eigenface, fisherface, the Hidden Markov
model, and the neuronal motivated Dynamic Link Matching. A newly emerging trend,
claimed to achieve previously unseen accuracies, is three-dimensional face recognition.
Another emerging trend uses the visual details of the skin, as captured in standard digital or
scanned images. Tests on the FERET database, the widely used industry benchmark, showed
that this approach is substantially more reliable than previous algorithms.

4.14.1. Introduction
Classification: Module
Face recognition means to recognize the face in the detected image. If the face is
already known then a positive response is obtained else a negative response is obtained.

4.14.2. Purpose
This is the main module of our software whose purpose is to recognize the face if it is
already in the database. If the face is not found an appropriate message should be displayed.

Dept. of CSE, R.V.C.E

Jan–May’2007

52

Detailed Design

Face Detection and Recognition

4.14.3. Functionality
Start

Face Detection

Training
Choice
Recognition

Eigen Vectors

Eigen Vectors

Project onto Eigen Faces

Project onto Eigen Faces

Projected Vectors

Projected Vectors

Determine Weights

Determine Weights

Match from Database

Classify Faces

Info. about Face

Info. about Face

Stop

Fig 4.9. Flow Chart for Face Recognition

Dept. of CSE, R.V.C.E

Jan–May’2007

53

Detailed Design

Face Detection and Recognition

Input: A preprocessed image containing only the face.
Output: The name of the person in the image and his related info
4.14.4. Intercomponent Relationship
Uses : This module uses the following sub modules
Training
PCA
Classify

Interacts: Interacts with the pre-process unit, which supplies the pre-processed image to this
unit.

Resources: Database of face images.

4.15. Module 13: Training
Irrespective of the method used for face recognition training[4] is essential so that the
system has learnt how a face looks like. In case of neural network, training involves
modifying the weights of the synaptic connections so that network attains stability. In case of
eigen vectors training involves identifying the weights of the faces in the database which can
later be used during recognition.

4.15.1 Introduction
Classification: Function
Training is a process of using the faces in the databases to generate and store values
of weights, which can be used by classification module.

4.15.2. Purpose
Using the faces in the database the eigen vectors are generated and the weights are
stored in database. The weights are generated using principal component analysis.

Dept. of CSE, R.V.C.E

Jan–May’2007

54

Detailed Design

Face Detection and Recognition

4.15.3. Functionality
Input: A set of human faces.
Output: The set of weight vectors
Input <- Input Image
// converting N X N images into 1 X N^2 vector
For i <- 1 to M, No. of images in the database
In_img[i] <- 0
S <- 0
For j <- 1 to N, N is the image dimension
For k <- 1 to N, N is the image dimension
In_img[j][k] <- pixel value of image
S <- S + 1
End for loop
End for loop
End for loop
// calculate the mean face
For j <1 to N^2 , N is the image dimension
For k <-1 to M, No. of images in database
// for every M images, calculate sum of all N^2 pixels
Temp[j] <- Temp[j] + In_img[k][j]
End for loop
End for loop
// calculate mean
For i <- 1 to N^2
Mean_img[i] <- Temp[i] / M
End for loop
End of pseudo code

Dept. of CSE, R.V.C.E

Jan–May’2007

55

Detailed Design

Face Detection and Recognition

4.16. Module 14: PCA
In statistics, principal components analysis (PCA)[4] is a technique for simplifying
a data set, by reducing multidimensional data sets to lower dimensions for analysis.
Technically speaking, PCA is an orthogonal linear transformation that transforms the data to
a new coordinate system such that the greatest variance by any projection of the data comes
to lie on the first coordinate (called the first principal component), the second greatest
variance on the second coordinate, and so on.

4.16.1 Introduction
Classification: Function
PCA stands for Principal Component Analysis. A mathematical approach to represent
the faces using eigen vectors.

4.16.2. Purpose
The purpose of this module is to generate eigen values and eigen vectors of the input
image. Eigen values can be generated using mathematical definition of eigen values or
vectors. However we have used JAMA package available in java to generate eigen values.

4.16.3. Functionality
Input: A preprocessed image.
Output: Weight vector of the input image
// zero mean input image of dimension M X N^2
Input <- Input Image
A <- transpose ( Zero mean Image )
AT <- Zero mean Image
For i <- 1 to M , No. of images
For j <- 1 to M , No. of images
Covariance[i][j] <- 0

Dept. of CSE, R.V.C.E

Jan–May’2007

56

Detailed Design

Face Detection and Recognition
For k <- 1 to N^2
Covariance[i][j] <- Covariance[i][j] + AT[i][j] * A[k][j]
End of for loop

End of for loop
End of for loop
// the matrix Covariance is of dimension M X M
// calculate M eigen vectors
// Eig matrix is of size M X M , which gives M eigen vectors of M dimension
Eig <- Eigen_vectors( Covariance )
Val <- Eigen_values( Covariance )
Eigen_face <- Eig * A
Weights <- eigen_face * (input –A )’
End of pseudo code

4.17. Module 15: Classification
Classification is the final step in the face detection and recognition system. It is here
that we determine the identity of the person whose image as be given in the input. In case the
person cannot be identified, obviously a message stating that the person cannot be recognized
must be displayed.

4.17.1 Introduction
Classification: Function
Classification means to state that an object belongs to particular class or group.
However in case of the face recognition system classification simply means to identify the
person.

Dept. of CSE, R.V.C.E

Jan–May’2007

57

Detailed Design

Face Detection and Recognition

4.17.2. Purpose
The purpose is to indicate the name of the person. Along with his identity all other
details, which were taken during training phase, are also supplied as output. If the face is not
found in the database then such a message must be displayed.

4.17.3. Functionality
Input: Single facial image
Output: Name of the person
The pseudo code for this module is as follows
Load the values of eigenface , weights , avg_face into memory
Input <- Input image to be recognized
Mean_input <- Input – avg_face
For i <- 1 to M //M number of training images
For j <- 1 to N^2 //N X N is the dimension of the image
For k <- 1 to N^2
Weight [i] <-Weight[i]+(Eigen_face[i][j]*Mean_input[k])
End for loop
End for loop
End for loop
For i <- 1 to M
For j <- 1 to M
wt1 [i][j] <- training_Weight [i][j] - Weight(j);
count <- count+1;
end for loop
End for loop
For i <- 1 to M
Tmp <- 0
For j <- 1 to M
Tmp <- Tmp+wt1 [i][j] *wt1 [i][j]
End for loop

Dept. of CSE, R.V.C.E

Jan–May’2007

58

Detailed Design

Face Detection and Recognition

ws[i] <- tmp;
End for loop
min <- ws[1]
index <- 1;
For i <- 1 to M
If ( ws [i] < min )
min <- ws(i);
index <- i;
End for loop
tmp <- names[index]
Return tmp
End of pseudo code

Dept. of CSE, R.V.C.E

Jan–May’2007

59

Implementation

Face Detection and Recognition

5. Implementation
5.1. Implementation
The implementation phase of any project development is the most important phase as
it yields the final solution, which solves the problem at hand. The implementation phase
involves the actual materialization of the ideas, which are expressed in the analysis document
and developed in the design phase. Implementation should be a perfect mapping of the
design document in a suitable programming language in order to achieve the necessary final
product. Often a product is ruined due to incorrect language chosen for implementation or an
unsuitable method of programming. It is better for the coding phase do be directly linked to
design phase in the sense if the design is in terms of object oriented terms then
implementation should be preferably carried out in a object oriented way. The factors
concerning the programming language and platform chosen are described in the next couple
of sections.

5.2. Programming language
As stated earlier, the programming language chosen should reflect the necessities of
the project to be completed expressed in terms of the analysis and design documents.
Therefore before choosing the language for implementation what features the project needs
are to be decided. The face detection and recognition project needs certain unique features in
a language to be implemented. Some of the features that are required are stated as follows:
! Image processing is an important necessity in the project as preprocessing module
heavily requires processing of input images.
! Matrix manipulations are another important necessity. A language, which provides
quick and easy implementation for matrices are preferred as computationally heavy
matrix manipulations are necessary.
! Considering the present emphasis on graphical user interface, the language must have
tools to create pleasant looking and simple to use user interfaces. Linking the front
end with the backend code should also easy.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

60

Implementation

Face Detection and Recognition

! Other than the above specific requirements few general requirements like that the
language should be simple to learn and code, should provide debugging features etc
must also make a contribution towards deciding the language of implementation.
With these necessities in mind, we had to decide on a programming language to start
implementation. As stated in the design chapter we have decided to use rapid prototyping
to test the feasibility and accuracy of the face detection and recognition system before a
complete deliverable is developed in a high level programming language.

5.2.1. Matlab
Rapid Application Development (RAD[6]) requires using tools and softwares,
which enables in developing some version of the product quickly without having to
completely define the data structures and complete functionality. MATLAB[13] is a
numerical computing environment and programming language. MATLAB allows easy
matrix manipulation, plotting of functions and data, implementation of algorithms, creation
of user interfaces, and interfacing with programs in other languages. There also built in
toolboxes for image manipulation, graphs etc.
With these handy features, RAD was relatively easy using matlab. An
implementation of the face recognition system could be quickly developed to test its
recognition results. Matlab is similar to a scripting language in the sense there is no
declaration of variables, functions etc. However it still supports all the high level features of
other languages like recursion, function definitions etc.

5.2.2. Java
Once the rapid prototype was developed we had to decide upon a language in which
the final deliverable was to be written. The necessary requirements are stated at the
beginning of this section. Java is the programming language chosen for our implementation.
Java is an object-oriented applications programming language developed by Sun
Microsystems in the early 1990s. Java applications are typically compiled to bytecode,
although compilation to native machine code is also possible. At runtime, bytecode is usually

Dept. of CSE, R.V.C.E

Jan-May’ 2007

61

Implementation

Face Detection and Recognition

either interpreted or compiled to native code for execution, although direct hardware
execution of bytecode by a Java processor is also possible. Java is the optimal programming
language for or project because of the following reasons:
! Java has a simple and easy to program syntax. Though it is an object-oriented
language it can be used for functional development of products as well.
! Developing graphical user interfaces s very simple in java. It has a rich set of classes
and methods for creating forms, Buttons, labels and events. As a result a clean and
nice looking user interface can be developed.
! Java is platform independent which is one of its design goals. This results in great
level cross-platform independence and portability.
! Java has simple methods for reading images from files of different formats. This is an
important feature as reading input images is the basic requirement of our project.
Challenges Encountered and their solutions:
There were a no. of challenges faced while implementing the face detection and
recognition system. Some of the problems faced included absence of certain features in the
programming languages, while other problems were due to lack of proper understanding of
the language. Some of these major problems are stated in brief in following section along
with their solutions.
Problem 1: Unable to write image files in java.
While coding we found that we couldn’t directly write and image file in java. That is
java didn’t have features to save an object of type image. We initially have overcome this
problem partially by converting the image data into an array and writing the array into a file.
However the disadvantage of this method is that written image cannot be displayed directly.
Finally the solution to this problem was discovered. Basically ImageIO class of java has a
write method, which can save Buffered Images. So we converted an object of type ‘image’
into an object of type ‘BufferedImage’ and then sent this modified data to write method of
ImageIO.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

62

Implementation

Face Detection and Recognition

Problem 2: Difficulty in writing code to determine eigen values.
It is a basic requirement in our project to determine the eigen values and eigen vectors
of huge square matrix. Going by the standard definition of eigen values, the code to
determine it involves determining the determinant of the matrix, which is a recursive function
taking lots of time. We decided to use the JAMA[9] package. This is open source java
package designed to assist the developers in performing important matrix manipulations
functions including determining eigen values and eigen vectors.
Problem 3: Unable to display images in an auto generated form.
Use of Integrated Development Environment (IDE) for coding results in simplified
front-end creation. The IDE automatically generates code to create the components in the
front end of the software. However a problem encountered was the fact that the auto
generated code is read-only and cannot be manipulated. This created difficulties while
displaying images dynamically in already running forms at the press of a button. In order to
overcome this, the following method was adopted. Initially a panel was created of necessary
size containing only an empty label. The label can contain any imageicon as its display
picture. Hence an ImageIcon object is created using the required image in its constructor.
And then this imageicon is passed into the label at the press of corresponding button.

5.3. Coding Standards
The Code Standards for the Java Programming Language document contains the
standard conventions that we at follow. It covers filenames, file organization, indentation,
comments, declarations, statements, and white space, naming conventions, programming
practices. Why have code conventions? Code conventions are important to programmers for
a number of reasons:
! 80% of the lifetime cost of a piece of software goes to maintenance.
! Hardly any software is maintained for its whole life by the original author.
! Code conventions improve the readability of the software, allowing engineers to
understand new code more quickly and thoroughly.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

63

Implementation

Face Detection and Recognition

Some of the conventions, which are followed by us, are stated as follows:
File Names: The code written follows standard convention for creating filenames as well as
the major requirement that java source code should have suffix .java while java byte code
should have .class as suffix.
File Organization: Each java source file should have single public class or interface. Files
longer than 2000 lines should be avoided. A file typically has the following ordering:
•

Beginning Comments

•

Package and import statements

•

Class and interface definitions

Comments: Java programs can have two kinds of comments: implementation comments and
documentation comments. Implementation comments are those found in C++, which are
delimited by /*...*/, and //. Documentation comments (known as "doc comments") are Javaonly, and are delimited by /** ... */. Doc comments can be extracted to HTML files using the
javadoc tool. Comments should be used to give overviews of code and provide additional
information that is not readily available in the code itself. Comments should contain only
information that is relevant to reading and understanding the program. For example,
information about how the corresponding package is built or in what directory it resides
should not be included as a comment. Comments should not be enclosed in large boxes
drawn with asterisks or other characters. Comments should never include special characters
such as form-feed and backspace.
Declarations: One declaration per line is recommended since it encourages commenting.
Initialize local variables where they're declared. Put declarations only at the beginning of
blocks.
Statements: Each line should contain at most one statement. Compound statements are
statements that contain lists of statements enclosed in braces "{statements}". The enclosed
statements should be indented one more level than the compound statement. The opening
brace should be at the end of the line that begins the compound statement; the closing brace
should begin a line and be indented to the beginning of the compound statement.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

64

Implementation

Face Detection and Recognition

Naming Conventions: Naming conventions make programs more understandable by making
them easier to read. They can also give information about the function of the identifier-for
example, whether it's a constant, package, or class-which can be helpful in understanding the
code. Most of the naming conventions are followed.
Indentation: Proper indentation is necessary to understand which code belongs to which
block of code. The actual tab spacing may vary. Avoid lines longer than 80 characters, since
they're not handled well by many terminals and tools.

5.4. Platform
The face detection and recognition system is designed to work on Windows operating
systems (specifically we have tested on Windows XP and Windows 2000). The reason we
chose to use Windows systems are mainly due to relative simplicity of the operating systems
as well abundant documentation available for windows system. Since there is no necessity to
manipulate system data structures there is no necessity of open source operating system. Also
since we are using java, which is platform independent, it is easy to adopt the project to work
on other operating systems like Linux.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

65

Testing

Face Detection and Recognition

6. Testing
6.1 Testing
Software Testing[6]: is the process used to help identify the correctness,
completeness, security, and quality of developed computer software. Testing is a process of
technical investigation, performed on behalf of stakeholders, that is intended to reveal
quality-related information about the product with respect to the context in which it is
intended to operate. This includes, but is not limited to, the process of executing a program or
application with the intent of finding errors. Quality is not an absolute; it is value to some
person. With that in mind, testing can never completely establish the correctness of arbitrary
computer software; testing furnishes a 'criticism' or comparison that compares the state and
behavior of the product against a specification. An important point is that software testing
should be distinguished from the separate discipline of Software Quality Assurance (SQA),
which encompasses all business process areas, not just testing.
There are many approaches to software testing, but effective testing of complex
products is essentially a process of investigation, not merely a matter of creating and
following routine procedure. One definition of testing is "the process of questioning a
product in order to evaluate it", where the "questions" are operations the tester attempts to
execute with the product, and the product answers with its behavior in reaction to the probing
of the tester. Although most of the intellectual processes of testing are nearly identical to that
of review or inspection, the word testing is connoted to mean the dynamic analysis of the
product—putting the product through its paces. Some of the common quality attributes
include capability, reliability, efficiency, portability, maintainability, compatibility and
usability. A good test is sometimes described as one, which reveals an error; however, more
recent thinking suggests that a good test is one which reveals information of interest to
someone who matters within the project community.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

66

Testing

Face Detection and Recognition

6.2 Unit Testing
In computer programming, unit testing[6] is a procedure used to validate that
individual units of source code are working properly. A unit is the smallest testable part of an
application. In procedural programming a unit may be an individual program, function,
procedure etc, while in object-oriented programming, the smallest unit is always a Class;
which may be a base/super class, abstract class or derived/child class. Units are distinguished
from modules in that modules are typically made up of units.

6.2.1 Face Detection Unit
In this unit, we are going to test how the detection of a given face takes place in the
given input image. This detection depends upon several factors like the background, the
amount of face exposed, and different lighting conditions. Testing of this unit involves
varying the above parameters, and observing the output.
6.2.1.1 Testing Strategy
Purpose: The input image may or may not contain a human face. The purpose of this
module is to detect the presence or absence of such a face and to mark such a region in the
image.
Features to be tested: Features to be tested includes the different features that generally
appear in the day to day scenario, which have been successfully implemented in the current
software product.. The features to be tested for Face Detection Unit are:
! Different Background
! Different Lighting Conditions
! Occlusions like hair, beard, glasses etc.
! Multiple Faces in a single image

Dept. of CSE, R.V.C.E

Jan-May’ 2007

67

Testing

Face Detection and Recognition

Pass / Fail Criteria: If the Face Detection unit, detects the presence of faces in the given
input image, taking into considerations all the features that have been implemented, then we
conclude that the unit under consideration has passed the unit testing.
Assumptions and Dependencies: Our application is being trained by a given set of skins.
Our assumptions are –
! The given person is properly clothed, not exposing much of his torso.
! The background considered should not match with any of the trained skin colors.

6.2.1.2 Test Cases
Sl No. of test case :
Name of test :
Item / Feature being tested :
Remarks :

1
Lighting
Detection under different lighting conditions
Pass

Input Image

Expected Output

Actual Output

Fig 6.1 – Test case 1, Checking for Brightness

Dept. of CSE, R.V.C.E

Jan-May’ 2007

68

Testing

Face Detection and Recognition

Sl No. of test case :
Name of test :
Item / Feature being tested :
Remarks :

2
Occlusion
Occlusions like spectacles, beard etc
Pass

Input Image

Expected Output

Actual Output

Fig 6.2 – Test case 2 , Checking for Occlusions
Sl No. of test case :
Name of test :
Item / Feature being tested :
Remarks :

3
MultipleFaces
Multiple human faces in a single input image.
Pass

Input Image

Expected Output

Actual Output

Fig 6.3 – Test case 3 , Checking for Multiple faces in Input image

Dept. of CSE, R.V.C.E

Jan-May’ 2007

69

Testing
Sl No. of Test Case :
Name of test :
Item/Feature being Tested :
Remarks :
Input Image

Face Detection and Recognition
4
VaryingBackground
Non uniform Background in the input image
Fail
Expected Output

Actual Output

Fig 6.4 - Test Case 4, Checking for Varying Background in the Input image

6.2.2 Pre-processing Unit
This unit of the face recognition system as the term implies is used to preprocess the
input images input into the system. Preprocess basically means to manipulate the images so
that they follow particular specifications, which is necessary for further stages.
6.2.2.1 Testing Strategy
Purpose: The purpose of this module is two fold. To process the image in such a way that
the face recognition module gets a constant input. The second purpose is to improve the
clarity of the image.
Features to be tested: Features to be tested includes the different features that generally
appear in the day-to-day scenario, which have been successfully implemented in the current
software product. The features to be tested for Pre-processing Unit are:
! Poor contrast image
! Image with Noise

Dept. of CSE, R.V.C.E

Jan-May’ 2007

70

Testing
Pass / Fail Criteria:

Face Detection and Recognition
If the Pre-processing unit Pre-processes the images, taking into

considerations all the features that have been implemented, then we conclude that the unit
under consideration has passed the unit testing.
Assumptions and Dependencies: The pre-processing is being done for a facial image, so the
following assumptions are made –
! Image should not be too dark or too bright so that the facial features cannot be
extracted.
! Image is not too distorted.

6.2.2.2 Test Cases
Sl No. of test case :
Name of test :
Item / Feature being tested :
Remarks :

5
Low Contrast
An image with reasonably low contrast
Pass

Input Image

Expected Output

Actual Output

Fig 6.5 – Test case 5 , Checking for Low Contrast Image

Dept. of CSE, R.V.C.E

Jan-May’ 2007

71

Testing

Face Detection and Recognition

Sl No. of test case :
Name of test :
Item / Feature being tested :
Remarks :

6
NoisyImage
Image with Considerable Noise
Pass

Input Image

Expected Output

Actual Output

Fig 6.6 – Test case 6 , Checking for Noisy Image

6.2.3 Face Recognition Unit
Face recognition means to recognize the face in the detected image. If the face is
already known then a positive response is obtained else a negative response is obtained.
6.2.3.1 Testing Strategy
Purpose: This is the main module of our software whose purpose is to recognize the face if it
is already in the database. If the face is not found an appropriate message should be
displayed.
Features to be tested: Features to be tested includes the different features that generally
appear in the day to day scenario, which have been successfully implemented in the current
software product.. The features to be tested for Face Recognition Unit are :
! Varying Expression
! Occlusions like spectacles, beard etc.
! Slight rotation of faces

Dept. of CSE, R.V.C.E

Jan-May’ 2007

72

Testing
Pass / Fail Criteria:

Face Detection and Recognition
If the Face Recognition unit recognizes the images, taking into

considerations all the features that have been implemented, then we conclude that the unit
under consideration has passed the unit testing.
Assumptions and Dependencies: The recognition is being done for a facial image, so the
following assumptions are made –
! Preferably the plane of the face should be perpendicular to the camera lens.
! Inclinations of the face plane are encouraged but to a very small degree.
! Aging factor is not taken into consideration.

6.2.3.2 Test Cases
Sl No. of test case :
Name of test :
Item / Feature being tested :
Remarks :
Input Image

7
ExpressionImage
Image has some facial expression
Pass
Expected Output

Actual Output

Fig 6.7 – Test case 7, Checking for Facial Expression

Dept. of CSE, R.V.C.E

Jan-May’ 2007

73

Testing

Face Detection and Recognition

Sl No. of test case :
Name of test :
Item / Feature being tested :
Remarks :

8
With_or_without_Occlusion
Input image has occlusions
Pass

Input Image

Expected Output

Actual Output

Fig 6.8 – Test case 8, Checking for Occlusions while Face Recognition
Sl No. of test case :
Name of test :
Item / Feature being tested :
Remarks :
Input Image

9
Tilted_image
Input image which is slightly tilted
Pass
Expected Output

Actual Output

Fig 6.9 – Test case 9, Checking for Tilted Face Recognition

Dept. of CSE, R.V.C.E

Jan-May’ 2007

74

Testing
Sl No. of test case :
Name of test :
Item/Feature being tested :
Remarks :
Input Image

Face Detection and Recognition
10
Tilted_image
Input image which is tilted
Fail
Expected Output

Actual Output

Fig 6.10 – Test Case 10, Checking for Tilted Face Recognition

6.3 Integration Testing
Integration testing[6] (sometimes called Integration and Testing, abbreviated I&T) is
the phase of software testing in which individual software modules are combined and tested
as a group. It follows unit testing and precedes system testing.
Integration testing takes as its input modules that have been unit tested, groups them in larger
aggregates, applies tests defined in an integration test plan to those aggregates, and delivers
as its output the integrated system ready for system testing.

6.3.1 Testing Strategy
Purpose: The purpose of the entire system can be split into three categories, face detection,
pre-processing and the face recognition system. The purpose of the face detection system is
to cut the face from the given input face and store it as a detected face image, the purpose of
pre-processing is to get a normalized image whose features are not dependent on brightness,
color contrasts or hue or saturation. Finally the purpose of the face recognition system is to

Dept. of CSE, R.V.C.E

Jan-May’ 2007

75

Testing

Face Detection and Recognition

take an input detected and pre-processed image and to match it with the images in the
existing image database and to give out a suitable output depending on the result of the
match.
Features to be tested: Features to be tested includes the different features that generally
appear in the day-to-day scenario, which have been successfully implemented in the current
software product. The features to be tested while doing integration are:
! Integration between the input form and the Face Detection Unit
! Integration between the Face Detection Unit and Pre-processing Unit
! Integration between the Pre-processing Unit and the Face Recognition Unit.
Pass / Fail Criteria: If the Face Detection and Recognition system, recognizes the images,
taking into considerations all the features that have been implemented, then we conclude that
the unit under consideration has passed the Integration testing.
Assumptions and Dependencies: The following are the dependencies identified in the Face
Detection and Recognition System.
! The Face Recognition unit depends on our face detection unit. The accuracy of
detection determines the accuracy of recognition.
! Although our application is capable of recognizing multiple faces in a given input
image, it is only capable of sending the largest detected face for the recognition
system.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

76

Testing

Face Detection and Recognition

6.3.2 Test Cases
Sl No. of test case :
Name of test :
Item / Feature being tested :
Remarks :

11
Integration
Complete Integration of all the three main modules
Pass

Fig 6.11 – Test case 11, Checking for Integration of all the modules

Dept. of CSE, R.V.C.E

Jan-May’ 2007

77

Testing

Face Detection and Recognition

6.4 Interface Testing
We need to identify each system interface as well as the functionality of the software to
accomplish the system requirements. The logical characteristics of each interface between the
software product and its users need to be specified.

6.4.1 Software Interface
As technology continues to be a part of our daily lives, the need for powerful, more
robust programs continually increases. A well-planned software interface design can make a
powerful and complicated software program appear very simple and intuitive.
Name: Java Matrix Package
Mnemonic: JAMA
Version No. : 1.0.1
Source : http://math.nist.gov/javanumerics/jama/
6.4.1.1 Testing Strategy
Purpose: The purpose of this package is to facilitate the matrix manipulations as every
image is treated as a matrix of pixel values.
Features to be tested: Since the basic purpose of this package is to assist the application
developers to write functions using the inbuilt matrix manipulation functions the features to
be tested, in our application only includes methods of the package like
! Transpose
! Eigen Value Decomposition
Pass / Fail Criteria: If we are able to retrieve the result generated by the function present in
the module and use the result thus obtained in one of the functionality of our system, then we
say that the JAMA is properly incorporated in our system..

Dept. of CSE, R.V.C.E

Jan-May’ 2007

78

Testing

Face Detection and Recognition

6.4.1.2 Test Cases
Sl No. of test case :
Name of test :
Item / Feature being tested :
Remarks :
Input Matrix

12
Eigen_value
Generation of Eigen Values
Pass
Expected Output

Actual Output

Fig 6.12 – Test case 12 , Checking the Generation of Eigen value and vector using JAMA

6.4.2. User Interface
Good user interface design is critical to the success of a system[6]. An interface that
is difficult to use will at best result in a high level of user errors. At worst, users will simply
refuse to use the software system irrespective of its functionality. If information is presented
in a confusing or misleading way, users may misunderstand the meaning of information.

6.4.2.1. Testing Strategy

Dept. of CSE, R.V.C.E

Jan-May’ 2007

79

Testing

Face Detection and Recognition

Purpose: Although text-based interfaces are still widely used, especially in legacy systems,
computer users now expect application systems to have some form of graphical user
interface. So the actual purpose is to provide a simple, easy to use graphical interface.
Features to be tested: Unlike other modules, testing for user interface is different in the
sense many of the testing scenarios are subjective. That is there is no clear-cut definition as
to whether the features stated here are actually satisfied in our project. Some of the necessary
features of a good user-interface design are as follows:
•

User familiarity: The interface should use terms and concepts, which are drawn from
the experience of the people who will use the system.

•

Consistency: The interface should be consistent in that, wherever possible
comparable operations should be activated in the same way.

•

Recoverability: The interface should include mechanisms to allow users to recover
from errors.

•

User guidance: The interface should provide meaningful feedback when errors occur
and provide context-sensitive user help facilities.

Pass / Fail Criteria: As stated earlier there are no specific pass/fail criteria for user interface
testing. If the GUI looks pleasing to the eye and satisfies few of the above features we can
consider that the GUI has passed the testing.

6.4.2.2 Test Cases

Dept. of CSE, R.V.C.E

Jan-May’ 2007

80

Testing
Sl No. of test case :
Name of test :
Item / Feature being tested :
Remarks :

Face Detection and Recognition
13
Familiarity
To test how familiar are the terms used in project
Pass

Our face detection and recognition only uses the terms that are familiar to common
man. Simple terms like recognize, start training, browse are used. A sample user interface
form is as follows:

Fig 6.13 – Test case 13, checking the Familiarity of the terms used in the Project

Sl No. of test case :
Name of test :

Dept. of CSE, R.V.C.E

14
Recover

Jan-May’ 2007

81

Testing
Item / Feature being tested :
Remarks :

Face Detection and Recognition
To provide guidance to user when he commits error and
allow him to recover from such errors
Pass

The application developed by us provides message boxes containing the necessary
information regarding the possible error committed by the user. After that user can return to
that original form where he had committed the mistake to correct his mistake and continue. A
sample of this feature is as shown below:

Fig 6.14 – Test case 14 , Checking for Proper UI guidance when user commits error

6.5. Results
Dept. of CSE, R.V.C.E

Jan-May’ 2007

82

Testing

Face Detection and Recognition

Any product, which has been developed, has to be not only tested for bugs and userinterface but also its performance. This testing is necessary to identify if the product
developed has satisfied the end-users as well as if it has improved performance compared to
its competitive products in the same field.
In case of our face detection and recognition system, the main parameters, which
need to be tested, are of course the accuracy with which the faces are detected and
recognized. Due to lack of time we were able to perform moderate amount of testing and the
results are as follows:
Face Detection
Conditions
Perfect inputs under

Total no

No of faces

No of false

Percentage of

of faces

detected

detections

success

25

21

3

84%

10

7

1

70%

35

28

4

80%

constant lighting conditions
Varying lighting and
background
Total

Table 6.1 Results of Face Detection

Face Recognition

Dept. of CSE, R.V.C.E

Jan-May’ 2007

83

Testing

Face Detection and Recognition

Conditions

Total no

No of faces

No of false

Percentage of

of inputs

recognized

recognitions

success

20

17

1

85%

12

9

2

75%

Tilted faces

8

5

2

61%

Total

40

31

5

78%

Frontal faces with no
expressions/occlusions
Frontal faces with
expressions/occlusions

Table

6.2

Dept. of CSE, R.V.C.E

Results

of

Jan-May’ 2007

Face

Recognition

84

Conclusion

Face Detection and Recognition

7. Conclusion
7.1. Summary
An overview of the design and development of a face recognition system has been
presented in this report. Although some aspects of the system are still under experimental
development, the project has resulted in an overall success, being able to perform reliable
recognition in a constrained environment. The face detection system has recorded high
accuracy.
The design of the face recognition system is based upon eigenfaces and has been
Separated into three major modules – face detection, pre-processing and face recognition.
Face detection was accomplished by first performing a skin detection[5] search of the input
image based on color segmentation. Although skin colors differ from person to person, and
race-to-race, it was found that the color remains distributed over a very small region in the
Hue-Saturation-Value scale. While the problem of recognizing faces under gross variations
remains largely unsolved, a possible solution using eigen face approach has been
demonstrated which works very well under certain input conditions.

7.2. Limitations
It is not possible for us to satisfy every minute detail while developing a project over
a fixed period of time. Added to the fact ‘that perfection is not human’ it is extremely natural
that every project has some limitations in terms of the functionality it supports, inputs
accepted and outputs produced. The major limitations in our face detection and recognition
software are stated as follows:
! The face recognition module works fine only for upright images without significant
lateral rotations that is the person in the image should preferably look directly at the
camera.
! Wide variations in the face expressions lead to decrease in accuracy of face
recognition module.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

85

Conclusion

Face Detection and Recognition

! Face detection might give false positives occasionally when the non-face objects in
the image have the same HSV values as those of human skins.
! As of the moment only a few image formats are supported and not all.

7.3. Further Enhancements
Any development is a continuous process, which does not terminate once an
executable has been generated. Every project has certain limitations due to wide various
reasons. Some of these limitations could be overcome, given sufficient time while others
could be overcome with better technologies. Hence some of the further enhancements that
could be performed on our face detection and recognition system are as follows:
! Ability to recognize faces that is laterally rotated with respect to camera.
! To attach a web cam to the system to develop our project further so that it recognizes
the faces from images directly taken from the web cam.
! To reduce false detections in the face detection module by considering other methods
of image representation (we have considered HSV scale).

Dept. of CSE, R.V.C.E

Jan-May’ 2007

86

References

Face Detection and Recognition

8. References
[1] Face Recognition :A literature Survey
IEEE transactions, Vol 15 No.10 page No 1042-1053 Oct 1993
By R.Chellappa and A.Rosenfeld , University Of Maryland
[2] Real Time Face Recognition
By Carlos Leung, University of Queensland, October 1991
[3] Face Recognition using eigen faces
By Ilker Atalay, University of Istanbul, January 1996
www.ilkeratalay.com/download/eigenfaces_msc_thesis.pdf
[4] Face Recognition using Eigen Faces
By Mathew.A.Turk and Alex.P.Pentland, Massachusetts Institute of Technology
“Journal of Cognitive Neuroscience”, Vol. 3, No. 1, Mar. 1991, page. 71-86.
www.face-rec.org/algorithms/PCA/mturk-CVPR91.pdf
[5]

Human Face Detection in Cluttered Color Images Using Skin Color and Edge
Information by K. Sandeep and A.N. Rajagopalan, Department of Electrical
Engineering , Indian Institute of Technology – Madras
www.ee.iitb.ac.in/~icvgip/PAPERS/166.pdf

[6]

Software Engineering ,Sixth Edition By Ian Sommerville –Pearson Publication

[7]

An Integrated Approach to Software Engineering Third Edition by Pankaj Jalote,
Narosa Publishing House

[8]

Face Detection in Color Images, IEEE transactions on Pattern Analysis and Machine
Intelligence, Vol. 24 No. 5 May 2002, Page No 696

Dept. of CSE, R.V.C.E

Jan–May’2007

87

References

Face Detection and Recognition

By Rein Lien Hsu, Student Member, IEEE, Mohammed Abdel Mottaleb, Student
Member, IEEE and Anil K Jain, Fellow, IEEE.
[9]

http://math.nist.gov/javanumerics/jama/ JAMA-A Java Matrix Package

[10] Digital Image Processing 2nd Edition By Rafael .C .Gonzalez , Richard.E.Woods ,
Prentice Hall Publications
[11] Image Processing in C , Second Edition by Dwayne Phillips , R & D Publications
[12] Digital Image Processing using Matlab by Rafael.C.Gonzalez, Richard.E.Woods,
Eddins – Prentice Hall Publications 2004
[13] www.mathworks.com – For Matlab tutorials
[14] Object Oriented Systems Development By Ali Bahrami – McGraw Hill
[15] www.face-rec.org/algorithms - Official Face Recognition Site
[16] http://groups.google.com/group/face-rec/ - Face Recognition Research Community

Dept. of CSE, R.V.C.E

Jan–May’2007

88

Source Code Listing

Face Detection and Recognition

9. Appendix
Appendix A: Source Code Listing
The face Detection and Recognition software developed by us in fairly large in terms
of lines of code. To be more specific the project runs into around 4000 lines of code
including comments generated code and indentation and around 2500 lines of actual java
code. As it is not viable to display so many lines of code in this document only a small
portion of the source code is displayed here.

Face Detection Module
private void Detection() {
//This module is executed when the Next button is pressed in the GUI...
//performs Detection of the input image....
String preproc="prep"+curFile;
//The input image is read using getImage()...
Toolkit toolkit = Toolkit.getDefaultToolkit();
image = toolkit.getImage(global.curfile);
//MediaTracker is used to halt the execution until the image is properly loaded..
MediaTracker mediaTracker = new MediaTracker(this);
mediaTracker.addImage(image, 0);
try
{
mediaTracker.waitForID(0); //halt executed until image loaded...
}
catch (InterruptedException ie)
{
System.err.println(ie);
System.exit(1);
}
//read the width and height of the input image using getWidth() and getHeight()..
int width=image.getWidth(null);
int height=image.getHeight(null);
//the image has to scale d if it exceeds 500X500 dimension..
//the image is proportionately scaled such that the maximum dimension is 500 pixels
//length..

Dept. of CSE, R.V.C.E

Jan-May’ 2007

89

Source Code Listing

Face Detection and Recognition

int max;
double k=1.0;
if(width>height)
max=width;
else
max=height;
if(max>500)
k=500/(double)max;
//newh and neww holds the height and width of the scaled image...
int neww=(int)(width*k);
int newh=(int)(height*k);
//newh and neww is used from here now for processing...
try
{
//the input image is scaled to newh*neww
utility.scale(global.curfile,preproc,neww,newh);
}
catch(Exception e)
{
java.lang.System.out.println(e.getMessage());
}
//read the scaled image
image=toolkit.getImage(preproc);
col=neww;
row=newh;
//oned stores the pixel values of the scaled image in a 1-dimensional array
int oned[]=new int[col*row];
//three contains the RGB values of the image....
three= new int[row][col][4];
//outp is the output image to be produced that contains the marked face..
outp=new int[row][col][4];
PixelGrabber pg = new PixelGrabber(image,0,0,col,row,oned,0,col);
//pixelgrabber is used to grab the pixel intensities of the image
try
{
pg.grabPixels();
if((pg.getStatus()&ImageObserver.ALLBITS)!= 0)
{
//the 32-bit 1-d pixel intensities are converted int ocorresponding RGB values...
three= utility.convert3(oned,col,row);
outp=utility.convert3(oned,col,row);
}
}
catch(Exception e)
{
System.out.println("Error in convert3d()");

Dept. of CSE, R.V.C.E

Jan-May’ 2007

90

Source Code Listing

Face Detection and Recognition

}
// HSV values of the input image is calculated and stored in hsv[][][]
hsv=utility.RGB2HSV(row,col,three);
int max_ar=200;
int maxy_ar=0;
int select_region=0;
//col_hist contains the face histogram...it contains the frequency of the hue and
saturation values of the skin pixels...
//face histogram is made use of to decide if a pixel in input image is a skin pixel...
int col_hist[][]=new int[100][100];
try
{
//face histogram stored in file dettra.txt is read using dataInputStream into col_hist
InputStream is=new FileInputStream("dettra.txt");
DataInputStream di=new DataInputStream(is);
int val;
for(int i=0;i<100;i++)
{
for(int j=0;j<100;j++)
{
val=di.readInt();
col_hist[i][j]=val;
}
}
}
catch(Exception e)
{
java.lang.System.out.println("file not found");
}
//the maximum value in the face histogram....
int m=utility.max(col_hist);
//Normalize the face histogram so that each of the index gives the ratio of the index
w.r.t to max value...
float hist[][]=new float[100][100];
for(int i=0;i<100;i++)
{
for(int j=0;j<100;j++)
{
hist[i][j]=(float)col_hist[i][j]/m;
}
}

Dept. of CSE, R.V.C.E

Jan-May’ 2007

91

Source Code Listing

Face Detection and Recognition

//skin represents a data structure that stores the skin pixel...
//a skin pixel is represented by 1 in skin[][]..
skin=new int[row][col];
for (int i=0;i<row;i++)
{
for(int j=0;j<col;j++)
{
//retrieve value of hue and saturation of each pixel..
float h=hsv[i][j][0];
float s=hsv[i][j][1];
int x=(int)(java.lang.Math.floor(h*100));
int y=(int)(java.lang.Math.floor(s*100));
if(x==100)
x=0;
if(y==100)
y=0;
//if the value in normalized histogram corresponding to h and s is greater than 0.1
then it is decided to be a skin pixel
//0.1 is calculated as threshold through experimentation..
//it represents that the corresponding hue and sat must appear at least 10% of the
max times in histogram to be decided as skin...
if(hist[x][y]>0.1)
skin[i][j]=1;
}
}
//obtaining the regions from the skin image
//the skin pixels present in skin[][] must be grouped to represent the different regions..
//new_sk is padded with 0'sin the boundary and skin is transferred into it ...for
grouping..
int new_sk[][]=new int[row+2][col+2];
for(int i=0;i<row+2;i++)
{
new_sk[i][0]=0;
new_sk[i][col+1]=0;
}
for(int i=0;i<col+2;i++)
{
new_sk[0][i]=0;
new_sk[row+1][i]=0;
}
for(int i=0;i<row;i++)
{
for(int j=0;j<col;j++)
{

Dept. of CSE, R.V.C.E

Jan-May’ 2007

92

Source Code Listing

Face Detection and Recognition

new_sk[i+1][j+1]=skin[i][j];
}
}
//res[][] represents the region to which each of the pixels belongs to.
//if res[][]=0 it represents that it is a non-skin pixel..
//else it stores a region number
int res[][]=new int[row+2][col+2];
//flag is used to store the region collisions.
int flag[]=new int[30000];
int count=0,a,b,c,d;
for(int i=1;i<row+1;i++)
{
for(int j=1;j<col+1;j++)
{
//For each pixel in the image
if(new_sk[i][j]==1)
{
//if it is a skin pixel
//record the region number of top 3 neighbors and the left neighbor...
//region grouping is done using 8-connectivity
a=res[i-1][j-1];//top-left neighbor
b=res[i-1][j]; //top pixel
c=res[i][j-1]; //left pixel
d=res[i-1][j+1]; //top-right pixel
int temp[]={a,b,c,d};
//sort the region numbers in increasing order
for(int x=0;x<4;x++)
for(int y=x+1;y<4;y++)
if(temp[x]>temp[y])
{
int s=temp[x];
temp[x]=temp[y];
temp[y]=s;
}
a=temp[0];
b=temp[1];
c=temp[2];
d=temp[3];
if(a!=0)
{
//if a is skin-pixel
res[i][j]=a; //current pixel belong to region a..
//if any other neighbor pixel is skin, flag them together with a.

Dept. of CSE, R.V.C.E

Jan-May’ 2007

93

Source Code Listing

Face Detection and Recognition

//it means that that pixel belongs to same region as ‘A’ and has to be altered
//later.
if(a!=b)
flag[b]=a;
if(a!=c)
flag[c]=a;
if(a!=d)
flag[d]=a;
}
if(a==0 && b!=0)
{
//if a is non-skin and b is skin-pixel
res[i][j]=b; //current pixel belongs to region b
//flag other neighboring skin pixels with b
if(b!=c)
flag[c]=b;
if(b!=d)
flag[d]=b;
}
if((a==0) && (b==0) && (c!=0))
{
//if c is skin pixel
res[i][j]=c;
//if d is skin. flag it with c
if(c!=d)
flag[d]=c;
}
if((a==0) &&(b==0) && (c==0) && (d!=0))
res[i][j]=d;
//if none of the neighbors are skin pixels, then the current pixel belongs to a new
//region.
//increment the count of the region count..
//assign current pixel to new region.
if(a==0 && b==0 && c==0 && d==0)
{
++count;
res[i][j]=count;
}
}
}
}

Dept. of CSE, R.V.C.E

Jan-May’ 2007

94

Source Code Listing

Face Detection and Recognition

//the dependency in the region grouping has to be removed using the flag[].
//for each pixel that is flagged with another pixel. convert it to that region.
for (int i=count;i>=1;i--)
{
//for all the regions
if(flag[i]!=0)
{
//if the pixel is flagged to belong to another region
//change each and every pixel in the image belonging to region i to region flag[i].
for(int j=1;j<row+1;j++)
for(int l=1;l<col+1;l++)
if(res[j][l]==i)
res[j][l]=flag[i];
}
}
//res from 1 to row+1 contains the region.....skin contains the skin pixels
//co_ord stores pixel coordinates of each region
int co_ord[][]=new int [300000][2];
int aval,bval,counta,countb;
int face_param[]=new int[4];
int skin_count,total_count,max_count=0;
int sel_reg=0;
int facp[]=new int[4];
for(int i=1;i<=count;i++)
{
//for all the regions in the image.
int cen_row=0;
int cen_col=0;
int wid_reg,hei_reg;
double face_ratio;
index=0;//keeps track of number o
//row===y
//col=x
//for all pixels in the image belonging to region i
for (int j=1;j<row+1;j++)
for(int l=1;l<col+1;l++)
if(res[j][l]==i)
{
co_ord[index][0]=j;
co_ord[index][1]=l;
index++;
//add the x-coordinate to co_ord[index][1]
//add y-coordinate to co_ord[index][0]
//co_ord contains all pixel coordinates of region i
}

Dept. of CSE, R.V.C.E

Jan-May’ 2007

95

Source Code Listing

Face Detection and Recognition

if(index!=0)
{
//if the region contains any pixel..
//find the centroid of the region.
for(int j=0;j<index;j++)
{
//for each pixel in region
//add the x and y coordinates of the pixels in the region separately.
cen_row+=co_ord[j][0];
cen_col+=co_ord[j][1];
}
//divide the sum by index to get the centroid of the region
//centroid= (cen_row,cen_col)
cen_row=cen_row/index;
cen_col=cen_col/index;
aval=0;bval=0;counta=0;countb=0;
int temp_val[]=new int[index];
//TO find the width of the region
for(int j=0;j<index;j++)
{
//remove the value of x-coordinate of centroid from each pixel belonging to
//region i
temp_val[j]=co_ord[j][1]-cen_col;
if(temp_val[j]>0)
{
//add the +ve values
aval+=temp_val[j];
counta+=1;
}
else
{
//add the -ve values
bval+=temp_val[j];
countb+=1;
}
}
if(counta!=0)
aval=aval/counta;
if(countb!=0)
bval=bval/countb;
//the width of the region is equal to twice of the sum of the absolute values of the
//sum..
wid_reg=java.lang.Math.abs(aval)+java.lang.Math.abs(bval);
wid_reg*=2;

Dept. of CSE, R.V.C.E

Jan-May’ 2007

96

Source Code Listing

Face Detection and Recognition

//To find the height of the region
aval=0;bval=0;counta=0;countb=0;
for(int j=0;j<index;j++)
{
temp_val[j]=co_ord[j][0]-cen_row;
if(temp_val[j]>0)
{
aval+=temp_val[j];
counta+=1;
}
else
{
bval+=temp_val[j];
countb+=1;
}
}
if(counta!=0)
aval=aval/counta;
if(countb!=0)
bval=bval/countb;
//the height of the region is equal to twice of the sum of the absolute values of the //
//individual sums..
hei_reg=java.lang.Math.abs(aval)+java.lang.Math.abs(bval);
hei_reg*=2;
//find the face_ratio by dividing height of region by width of the region
if ( wid_reg!=0)
face_ratio=(double)hei_reg/(double)wid_reg;
else
face_ratio=(double)hei_reg;
//face_param gives the coordinates of top-left and bottom-right corner of the
//region.
//top-left coordinate=(cen_row-hei_reg/2,cen_col-wid_reg/2)
//bottom-right coordinate=(cen_row+hei_reg/2,cen_col+wid_reg/2)
face_param[0]=cen_row-hei_reg/2;
face_param[1]=cen_col-wid_reg/2;
face_param[2]=cen_row+hei_reg/2;
face_param[3]=cen_col+wid_reg/2;
for(int j=0;j<4;j++)
{
if (face_param[j]<0)
face_param[j]=0;
if(face_param[j]>=row)
face_param[j]=row-1;

Dept. of CSE, R.V.C.E

Jan-May’ 2007

97

Source Code Listing

Face Detection and Recognition

if(face_param[j]>=col)
face_param[j]=col-1;
}
skin_count=0;
total_count=0;
//to find the number of skin pixels and percentage of skin in a region
for(int j=face_param[0];j<=face_param[2];j++)
for(int l=face_param[1];l<=face_param[3];l++)
{
//for each pixel in region
//if skin pixel increment skin_count
if(new_sk[j][l]==1)
skin_count+=1;
total_count+=1;
}
if(total_count<400)
continue;
//per_of_skin in region=skin_count/total_count
double per_of_skin=(double)skin_count/(double)total_count;
double golden_ratio=(1+(java.lang.Math.sqrt(5.0)))/2;//~= 1.618
if((per_of_skin>0.4)&&(face_ratio>golden_ratio0.7)&&(face_ratio<golden_ratio+0.7))
{
//region is diagnosed to be a face if percentage of skin > 40% and face_ratio falls
//in the range of golden_ratio with threshold adjustment
if(max_count<skin_count)
{
//select the largest region in the image...
max_count=skin_count;
sel_reg=i;
for(int j=0;j<4;j++)
facp[j]=face_param[j];
}
//mark the detected regions in the output image
//draws a black box around the detected region boundary
for(int j=face_param[0];j<=face_param[2];j++)
{
outp[j][face_param[1]][1]=0;
outp[j][face_param[1]+1][1]=0;
outp[j][face_param[1]+1][2]=0;
outp[j][face_param[1]][2]=0;
outp[j][face_param[1]][3]=0;
outp[j][face_param[1]+1][3]=0;

Dept. of CSE, R.V.C.E

Jan-May’ 2007

98

Source Code Listing

Face Detection and Recognition

outp[j][face_param[3]][1]=0;
outp[j][face_param[3]][2]=0;
outp[j][face_param[3]][3]=0;
outp[j][face_param[3]-1][1]=0;
outp[j][face_param[3]-1][2]=0;
outp[j][face_param[3]-1][3]=0;
}
for(int j=face_param[1];j<=face_param[3];j++)
{
outp[face_param[0]] [j] [1]=0;
outp[face_param[0]] [j] [2]=0;
outp[face_param[0]] [j] [3]=0;
outp[face_param[2]] [j] [1]=0;
outp[face_param[2]] [j] [2]=0;
outp[face_param[2]] [j] [3]=0;
outp[face_param[0]+1] [j] [1]=0;
outp[face_param[0]+1] [j] [2]=0;
outp[face_param[0]+1] [j] [3]=0;
outp[face_param[2]-1] [j] [1]=0;
outp[face_param[2]-1] [j] [2]=0;
outp[face_param[2]-1] [j] [3]=0;
}
}
}//end of if region found
}//end of for loop of all regions
//save the detected and marked faces in separate files..
int len=curFile.length();
//the detected face is stored in a file in folder called marked..
//the filename is same that of the input file with "_m" appended to it..
//global.marked_face holds the complete pathname..
global.marked_face="./marked/"+(curFile.substring(0,len-4)+"_m.jpg");
//the output image is converted into a 1-d array
oned=utility.convert1(row,col,outp);
//a image is created using create image()
image=createImage(new MemoryImageSource(col,row,oned,0,col));
BufferedImage bi=utility.toBufferedImage(image);
//the created image is stored using IageIO.write()
try
{
File f=new File(global.marked_face);
ImageIO.write(bi,"jpg",f);

Dept. of CSE, R.V.C.E

Jan-May’ 2007

99

Source Code Listing

Face Detection and Recognition

}
catch(Exception e)
{
java.lang.System.err.println("write error");
}
int sel_flag=0;
if(sel_reg==0)
{
//if no region has been found display necessary message
sel_flag=1;
this.setEnabled(false);
message mes=new message(this,1);
mes.setText("Face does not exist or it is too small");
mes.setLocation(400,300);
mes.setVisible(true);
}
if(sel_flag==0)
{
//select the largest region.
index=0;
for (int j=1;j<row+1;j++)
for(int l=1;l<col+1;l++)
if(res[j][l]==sel_reg)
{
//store the coordinates of the largest regions
co_ord[index][0]=j;
co_ord[index][1]=l;
index++;
}
//calculate the top-left and bottom-right corners of the region
int miny_reg=utility.min_reg(co_ord,index,0);
int minx_reg=utility.min_reg(co_ord,index,1);
int maxy_reg=utility.max_reg(co_ord,index,0);
int maxx_reg=utility.max_reg(co_ord,index,1);
int new_hei=maxy_reg-miny_reg;
int new_wid=maxx_reg-minx_reg;
det_face=new int[new_hei][new_wid][4];
for(int i=0;i<new_hei;i++)
for(int j=0;j<new_wid;j++)
{
//copy the largest detected face into a new image
det_face[i][j][0]=three[i+miny_reg][j+minx_reg][0];
det_face[i][j][1]=three[i+miny_reg][j+minx_reg][1];
det_face[i][j][2]=three[i+miny_reg][j+minx_reg][2];

Dept. of CSE, R.V.C.E

Jan-May’ 2007

100

Source Code Listing

Face Detection and Recognition

det_face[i][j][3]=three[i+miny_reg][j+minx_reg][3];
}
len=curFile.length();
//detected face is stored in a folder called detected..
//global.det_face contains the path name of the detected face image
global.det_face="./detected/"+(curFile.substring(0,len-4)+"_d.jpg");
global.image_height=new_hei;
global.image_width=new_wid;
oned=utility.convert1(new_hei,new_wid,det_face);
//create an image
image=createImage(new MemoryImageSource(new_wid,new_hei,oned,0,new_wid));
bi=utility.toBufferedImage(image);
try
{
//write the image int o the file
File f=new File(global.det_face);
ImageIO.write(bi,"jpg",f);
}
catch(Exception e)
{
java.lang.System.err.println("write error");
}
//propagate to next form
//hide this form and pass the control to recognition form
this.setVisible(false);
reco re=new reco();
re.setVisible(true);
re.setLocation(150,100);
}
}

Dept. of CSE, R.V.C.E

Jan-May’ 2007

101

Source Code Listing

Face Detection and Recognition

Pre Processing Module
Note that this module uses many user-defined modules which are not written in this
document.
private void process() {
//this module is executed when the user clicks on the recognize button in the GUI
width=global.image_width;
height=global.image_height;
//the detected face from the detection system is taken as input for this module..
//read the detected face.
Toolkit toolkit = Toolkit.getDefaultToolkit();
Image image = toolkit.getImage(global.det_face);
//Mediatracker is used to halt the system until image is completely loaded..
MediaTracker mediaTracker = new MediaTracker(this);
mediaTracker.addImage(image, 0);
try
{
mediaTracker.waitForID(0);
}
catch (InterruptedException ie)
{
System.err.println(ie);
System.exit(1);
}
//Get the width and height of the detected face..
width=image.getWidth(null);
height=image.getHeight(null);
//the detected face is standardized to a size 100X150...
//the standardization is necessary for the recognition system.
height=150;
width=100;
//face contains the RGB values of the standardized detected face
face=new int[height][width][4];
int face_od[]=new int[height*width];
//create a 100X150 scaled image of the detected face
Image scaled_im=image.getScaledInstance(width,height,0);
//pixelGrabber is used to grab the values of the pixel intensities of the image into 1-D
//array

Dept. of CSE, R.V.C.E

Jan-May’ 2007

102

Source Code Listing

Face Detection and Recognition

PixelGrabber pg = new PixelGrabber(scaled_im,0,0,width,height,face_od,0,width);
try
{
pg.grabPixels();
if((pg.getStatus()&ImageObserver.ALLBITS)!= 0)
{
//convert the 32-Bit intensity values into 24Bit RGB format
face= utility.convert3(face_od,width,height);
}
}
catch(Exception e)
{
System.out.println("pixel error");
}
proc=new int[height][width];
//Perform Gray Scale conversion
proc=cgrey(face,height,width);
//Histogram Equalization
proc=histequal(proc,height,width);
//Apply low pass filtering
proc=lowfilter(proc,height,width);
//Applying Median Filtering
proc=medianfilter(proc,height,width);
//perform brightness normalization..
int count=0;
for(int i=0;i<height;i++)
for(int j=0;j<width;j++)
{
//convert the 2-D pixel intensities into 3-D array for further processing
// the RGB values of the image are equal to gray scaled filtered intensities..
face[i][j][1]=proc[i][j];
face[i][j][2]=proc[i][j];
face[i][j][3]=proc[i][j];
}
//the gray-scaled image is converted into 1-D array
face_od=utility.convert1(height,width,face);
//save the preprocessed detected face ...
//Create an image from the 1-D pixel values
image=createImage(new MemoryImageSource(width,height,face_od,0,width));
BufferedImage bi=utility.toBufferedImage(image);
int len=global.filename.length();
//the preprocessed detected faces are stored in the input folder .
//filename of the preprocessed detected face= filename+"_pd.jpg"
String str="./input/"+(global.filename.substring(0,len-4)+"_pd.jpg");
global.predet_face=str;

Dept. of CSE, R.V.C.E

Jan-May’ 2007

103

Source Code Listing

Face Detection and Recognition

//Write the image into file
try
{
File f=new File(global.predet_face);
ImageIO.write(bi,"jpg",f);
}
catch(Exception e)
{
java.lang.System.err.println("write error");
}
preproc pr =new preproc();
this.setVisible(false);
pr.setLocation(150,100);
pr.setVisible(true);
}

Dept. of CSE, R.V.C.E

Jan-May’ 2007

104

Source Code Listing

Face Detection and Recognition

Face Recognition Module
private void recognize() {
// this module is executed when the user clicks the recognize button
int no_of_images=0;
int width=100;
int height=150;
int [] avg=new int[width*height];
int n2=width*height;
//read the preprocessed detected face
Toolkit toolkit = Toolkit.getDefaultToolkit();
Image image = toolkit.getImage(global.predet_face);
int face_od[]=new int[width*height];
int face[][][]=new int[height][width][4];
proc=new int[height][width];
//use pixelgrabber to collect the intensities of the pixel of the
//preprocessed gray image
PixelGrabber pg = new PixelGrabber(image,0,0,width,height,face_od,0,width);
try
{
pg.grabPixels();
if((pg.getStatus()&ImageObserver.ALLBITS)!= 0)
{
//convert the 32-Bit intensity values into 24Bit format
//containing the gray level intensities
face= utility.convert3(face_od,width,height);
}
}
catch(Exception e)
{
System.out.println("pixel error");
}
//the gray level intensities are stored in a 2-D array
for(int i=0;i<height;i++)
for(int j=0;j<width;j++)
proc[i][j]=face[i][j][1];
try
{
//read the number of images in the training database
//read the value from the file count.txt
InputStream is = new FileInputStream("count.txt");

Dept. of CSE, R.V.C.E

Jan-May’ 2007

105

Source Code Listing

Face Detection and Recognition

DataInputStream ds=new DataInputStream(is);
no_of_images=ds.readInt();
global.no=no_of_images;
is.close();
//read the average face of the training images into an array
is = new FileInputStream("avg.txt");
ds=new DataInputStream(is);
for(int i=0;i<width*height;i++)
avg[i]=ds.readInt();
is.close();
//read the eigen faces of the training images in the database into
//an array for further processing
eig_fac=new double[no_of_images][n2];
is = new FileInputStream("noreigface.txt");
ds=new DataInputStream(is);
for(int i=0;i<no_of_images;i++)
{
for(int j=0;j<n2;j++)
{
eig_fac[i][j]=ds.readDouble();
}
}
is.close();
//read the weights calculated for each of the images in the database from the file
//weight.txt into an array
weight=new double[no_of_images][no_of_images];
is = new FileInputStream("weight.txt");
ds = new DataInputStream(is);
for(int i=0;i<no_of_images;i++)
{
for(int j=0;j<no_of_images;j++)
{
weight[i][j]=ds.readDouble();
}
}
is.close();
}
catch(Exception e)
{
java.lang.System.err.println("Read error");
}
int [] oned=new int[n2];

Dept. of CSE, R.V.C.E

Jan-May’ 2007

106

Source Code Listing

Face Detection and Recognition

int count=0;
for(int i=0;i<height;i++)
{
for(int j=0;j<width;j++)
{ //convert the 2-D input image pixel intensities into 1-D array
oned[count++]=proc[i][j];
}
}
//subtract the average face of the training database from the input image
//this results zero mean input image
for(int i=0;i<n2;i++)
oned[i]=oned[i]-avg[i];
//the zero-mean input image is multiplied with the eigen faces of the database
//to obtain the weights for the input image
//the weight vector is 1X M in size and represents the value of the input image wrt to
//each eigen face .
double wei[]=new double [no_of_images];
for(int i=0;i<no_of_images;i++)
{
double k=0;
for(int j=0;j<n2;j++)
k+=eig_fac[i][j]*oned[j];
wei[i]=k;
}
double diff_wei[][]=new double[no_of_images][no_of_images];
//It is required to find the Euclidean distance of the input image from each of the
//eigen faces and the eigen face located at the minimum distance from the input
//image within the threshold value is to be shown as recognized face..
//to Find the Euclidean distances
for(int i=0;i<no_of_images;i++)
{
for(int j=0;j<no_of_images;j++)
{
diff_wei[j][i]=weight[j][i]-wei[j];
}
}
double sum_weights[]=new double[no_of_images];
for(int i=0;i<no_of_images;i++)
{
double sum=0;

Dept. of CSE, R.V.C.E

Jan-May’ 2007

107

Source Code Listing

Face Detection and Recognition

for(int j=0;j<no_of_images;j++)
{
sum+=diff_wei[j][i]*diff_wei[j][i];
}
sum_weights[i]=java.lang.Math.sqrt(sum);
}
//the index with the minimum distance is calculated
//A threshold of 5000 is chosen and any image whose min is greater than 5000 is
//regarded as unrecognized..
double min=5000;
int index=-1;
for(int i=0;i<no_of_images;i++)
{
if(min>sum_weights[i])
{
min=sum_weights[i];
index=i;
}
}
//pass the control to next form to display the result...
this.setVisible(false);
display d=new display(index);
d.setLocation(150,100);
d.setVisible(true);
}
private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {
//closes the application..
System.exit(0);
}

Dept. of CSE, R.V.C.E

Jan-May’ 2007

108

Source Code Listing

Face Detection and Recognition

Training Module for Face Recognition
private void trainrec() {
//assuming that images are stored in ./training folder
File directory;
String []listi;
directory=new File("./training/");
//read the files from the training directory
listi=directory.list();
int p=0;
if(listi.length==0)
{//if no images are present in the directory
//display suitable message
message m=new message(this);
this.setEnabled(false);
m.setLocation(400,300);
m.setVisible(true);
}
else
{
//if images present in the directory
for(int i=0;i<listi.length;i++)
{
//check for files that are images
String s=listi[i];
if(s.endsWith("jpg"))
{//store the names of the jpg images in an array
listi[p]=listi[i];
p++;
}
}
int no_of_images=p;
//read the image..
Toolkit toolkit = Toolkit.getDefaultToolkit();
int col=100;
int row=150;
int oned[];
//faces contains the M training images stored in 1 X N^2 manner..
//size of faces M X N^2
faces= new int[no_of_images][150*100];
for(int i=0;i<no_of_images;i++)
{//for each image in the training database
//read the image

Dept. of CSE, R.V.C.E

Jan-May’ 2007

109

Source Code Listing

Face Detection and Recognition

image=toolkit.getImage("./training/"+listi[i]);
oned=new int[col*row];
//grab the pixel intensities of the image into 1-d array
PixelGrabber pg = new PixelGrabber(image,0,0,col,row,oned,0,col);
Try
{
pg.grabPixels();
if((pg.getStatus()&ImageObserver.ALLBITS)!= 0)
{
for(int j=0;j<col*row;j++)
{
//read the gray level intensities of the images into a 1-D array..
int val=(oned[j]& 0x000000FF);
//store the image in the faces[][] array
faces[i][j]=val;
}
}
}
catch(Exception e)
{
System.out.println("mainerror");
}
}
//faces contains the pixel intensities of the M images in the database in 1-Dimensional
//manner...
//average face is calculated for the images in the database..
//each of the pixel values corresponding to the images are added and divided by
//no.of.images..
avg=new int[col*row];
for(int i=0;i<col*row;i++)
{
int val=0;
for(int j=0;j<no_of_images;j++)
{
val+=faces[j][i];
}
float val1= (float)val/no_of_images;
avg[i]=(int)val1;
}
try
{ //save the average face in a file avg.txt

Dept. of CSE, R.V.C.E

Jan-May’ 2007

110

Source Code Listing

Face Detection and Recognition

OutputStream ou=new FileOutputStream("avg.txt");
DataOutputStream dout=new DataOutputStream(ou);
for(int k1=0;k1<col*row;k1++)
{
dout.writeInt(avg[k1]);
}
ou.close();
}
catch(Exception e)
{
java.lang.System.out.println("File write error");
}
//zero mean images are calculated for the training database by subtracting
//each of the images by the average face
diff_faces=new int[no_of_images][row*col];
//diff_faces is of size MX N^2
for(int i=0;i<no_of_images;i++)
{
for(int j=0;j<row*col;j++)
{ //calculate diff_faces
diff_faces[i][j]=faces[i][j]-avg[j];
}
}
//transpose of the diff_faces is calculated and stored for further processing
trans_faces=new int[row*col][no_of_images];
//trans_faces is of size N^2 X M
for(int i=0;i<no_of_images;i++)
{ //for all images
for(int j=0;j<row*col;j++)
{ //for all pixels in the image
// transpose the values...
trans_faces[j][i]=diff_faces[i][j];
}
}
//covariance matrix is constructed to obtain the eigen vectors corresponding to the
//training images
//covariance matrix is of size M X M and is obtained by multiplying
// the diff_faces with its transpose
cov_mat=new int[no_of_images][no_of_images];
for(int i=0;i<no_of_images;i++)
{
for(int j=0;j<no_of_images;j++)
{
int val=0;

Dept. of CSE, R.V.C.E

Jan-May’ 2007

111

Source Code Listing

Face Detection and Recognition

for(int k=0;k<row*col;k++)
val+=diff_faces[i][k]*trans_faces[k][j];
cov_mat[i][j]=val;
}
}
double c[][]=new double[no_of_images][no_of_images];
for(int i=0;i<no_of_images;i++)
for(int j=0;j<no_of_images;j++)
c[i][j]=cov_mat[i][j];
//JAMA package has been made use of for finding the eigen vector of the covariance
//matrix
//JAMA package contains functions that perform matrix manipulations efficiently..
//a Matrix object is created using the covariance matrix as its data
Jama.Matrix cov=new Jama.Matrix (c,no_of_images,no_of_images);
//Eigen vectors for the covariance matrix is calculated
Jama.EigenvalueDecomposition e=new Jama.EigenvalueDecomposition(cov);
//getV() returns the eigen vector of the matrix
Jama.Matrix vec=e.getV();
//getD() returns the eigen values of the matrix
Jama.Matrix val= e.getD();
//getArray() returns the array values of the matrix class
double val1[][]=val.getArray();
double vec1[][]=vec.getArray();
//eigen faces are obtained by multiplying the eigen vector with the zero mean image
double [][]eig_fac=new double[no_of_images][row*col];
eig_fac=utility.multi(vec1,diff_faces,no_of_images,no_of_images,row*col);
//save the eigen faces in the file uneigface.txt
utility.save_im2(eig_fac,row*col,no_of_images,"uneigface.txt");
//normalize the eigen faces..
eig_fac=utility.normalis(eig_fac,no_of_images,row*col);
//the normalised face is saved in a fie "noreigface.txt"
utility.save_im2(eig_fac,row*col,no_of_images,"noreigface.txt");
//weights corresponding to each of the eigen vector is calculated
weight=new double[no_of_images][no_of_images];
//weight matrix is obtained by multiplying the eigen face with each of the transposed
//zero mean image
weight=utility.multi(eig_fac,trans_faces,no_of_images,row*col,no_of_images);
//weight of each image is of size 1X M
//hence the entire weight matrix is of size M X M
//weights of each face is stored in column wise manner
//weights are stored in a file "weight.txt" for further processing
utility.save_im2(weight,no_of_images,no_of_images,"weight.txt");

Dept. of CSE, R.V.C.E

Jan-May’ 2007

112

Source Code Listing

Face Detection and Recognition

try
{
//write the value of the number of images in the database to a file
OutputStream os=new FileOutputStream("count.txt");
DataOutputStream ds=new DataOutputStream(os);
ds.writeInt(no_of_images);
os.close();
}
catch(Exception e1)
{
java.lang.System.out.println("write error");
}
//display a message that the training has been successfully completed...
message m=new message(this,4);
this.setVisible(false);
m.setText("TRAINING COMPLETED");
m.setLocation(400,300);
m.setVisible(true);
}
}

Dept. of CSE, R.V.C.E

Jan-May’ 2007

113

List of Figures

Face Detection and Recognition

Appendix B: List of figures
Sl
No.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26

Page
No.
21
22
23
24
25
27
28
29
30
31
32
34
45
53
68
69
69
70
71
72
73
74
74
75
77
79

Figure
No.
3.1
3.2
3.3
3.4
3.5
4.1
4.2
4.3
4.4
4.5
4.6
4.7
4.8
4.9
6.1
6.2
6.3
6.4
6.5
6.6
6.7
6.8
6.9
6.10
6.11
6.12

27

81

6.13

28

82

6.14

Dept. of CSE, R.V.C.E

Name of the Figure
Level 0 DFD for Face Detection and Recognition System

Level 1 DFD for Pre-processing
Level 1 DFD for Face Detection
Level 1 DFD for Face Recognition
Level 2 DFD for Training of Detected Face
Structured Chart for Face Detection and Recognition System

Structured Chart for Pre-processing
Structured Chart for Noise Reduction
Structured Chart for Face Detection
Structured Chart for Face Recognition
Structured Chart for Training
Flow Chart for Face Detection
Flow Chart for Pre-processing
Flow Chart for Face Recognition
Test case 1 , Checking for Brightness
Test case 2 , Checking for Occlusions
Test case 3 , Checking for Multiple Faces in Input image
Test case 4, Checking for Non-Uniform Background
Test case 5 , Checking for Low Contrast Image
Test case 6 , Checking for Noisy Image
Test case 7 , Checking for Facial Expression
Test case 8 , Checking for Occlusions while Recognition
Test case 9 , Checking for Tilted Face Recognition
Test case 10,Checking for Tilted Face Recognition
Test case 11 ,Checking for Integration of all the modules
Test case 12, Checking for Generation of Eigen value
and vector using JAMA
Test case 13, Checking for Familiarity of terms used in
Project
Test case 14, Checking for proper UI guidance when
user commits error

Jan–May’2007

114

List of Tables

Face Detection and Recognition

Appendix C: List of Tables
SI.
No.
1
2

Page
No.
83
84

Table No.
6.1
6.2

Dept. of CSE, R.V.C.E

Name of the Table
Results of Face Detection
Results of Face Recognition

Jan-May’ 2007

115

