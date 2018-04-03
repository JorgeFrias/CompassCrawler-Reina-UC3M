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
Scrapy           | 1.5.0

