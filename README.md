# CompassCrawler-Reina-UC3M
## Run
To run the crawler (web page information extractor) run the main.py on the terminal. Remember first you need to be in the project folder.  
Then you'll be asked to insert the UC3M bachelors home pages, to extract the information from their courses. Once you finish,
insert a double enter and the program will start.  
All information will be exported in COMPASS JSON format to the default folder C:\Users\CURRENT_USER\\...\course_scraper\Courses

~~~~
$ python main.py
Welcome to COMPASS UC3M courses parser.
This tool helps you to extract the information from the UC3M website and export it to COMPASS JSON format.

Homepages of the bachelors you want the information, divided by a new line:

https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212345976/1371212987094/Bachelor_s_Degree_in_Telecommunication_Technologies_Engineering
https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212485394/1371212987094/Bachelor_s_Degree_in_Communication_System_Engineering

Extracting: https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212345976/1371212987094/Bachelor_s_Degree_in_Telecommunication_Technologies_Engineering

Information extracted
Stored at: C:\Users\CURRENT_USER\...\course_scraper\Courses
~~~~

## Fields
The fields from the UC3M system often needs translation, in order to be compatible with COMPASS.

COMPASS Field | UC3M Field           | Notes
--------------|----------------------|---------------------------------------------------------------------------------------------------------------------------
Title         | Course name          |
Description   | Qualification        |
Identifier    |                      | Generates a ID: university-courseID-degreeType_degreeAcronym Ex. for UC3M 205 Bachelor in Computer Science : UC3M-205-b_CS.
Publisher     |                      | Always "UC3M".
Creator       | Coordinator          |
Competence    | Prerequisite         |
Type          |                      | Always "Talk/Lecture" + "Class/Group based" as all courses in UC3M follows same pattern.
Level         | UC3M Bachelor/Master |
URL           | UC3M Reina URL       |
Language      |                      | The text language of qualification.
Credits       | Credits              | Defined as double + "ECTS" _Ex. "6.0 ECTS"_.
assessment    | assessment           |

Fields not contemplated in the table are not implemented in the system.

## Project Dependencies
Package          | Version
-----------------|----------
Python           | 3.6
Automat          | 0.6.0
PyDispatcher     | 2.0.5
Scrapy           | 1.5.0
Twisted          | 17.9.0
asn1crypto       | 0.24.0
attrs            | 17.4.0
certifi          | 2018.1.18
cffi             | 1.11.4
chardet          | 3.0.4
constantly       | 15.1.0
cryptography     | 2.1.4
cssselect        | 1.0.3
hyperlink        | 17.3.1
idna             | 2.6
incremental      | 17.5.0
langdetect       | 1.0.7
lxml             | 4.1.1
parsel           | 1.4.0
pip              | 9.0.1
pyOpenSSL        | 17.5.0
pyasn1           | 0.4.2
pyasn1-modules   | 0.2.1
pycparser        | 2.18
pypiwin32        | 220
queuelib         | 1.4.2
requests         | 2.18.4
service-identity | 17.0.0
setuptools       | 28.8.0
six              | 1.11.0
urllib3          | 1.22
w3lib            | 1.19.0
zope.interface   | 4.4.3
