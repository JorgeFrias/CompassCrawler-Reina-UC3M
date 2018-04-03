# CompassCrawler-Reina-UC3M
![python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)
![scrapy 1.5](https://img.shields.io/badge/scrapy-1.5-blue.svg)

## Description
This project is under a bigger one the [COMPASS project](http://www.learning-compass.eu), aimed to represent learning opportunities with integrated learning outcomes/competence information. For universities around the world.  

This little sub-project covers the UC3M learning opportunity specification, providing a tool to extract the courses information from the UC3M courses web pages, and exporting it to [COMPASS information model.](http://www.learning-compass.eu/media-center/intellectual-outputs/)  

Technically is a web crawler with conversion to COMPASS JSON.

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->
## Table of contents
- [CompassCrawler-Reina-UC3M](#compasscrawler-reina-uc3m)
	- [Description](#description)
	- [Installation](#installation)
	- [Usage](#usage)
	- [File format](#file-format)
		- [File name](#file-name)
		- [Fields](#fields)
	- [Contributing](#contributing)
		- [Project structure](#project-structure)
	- [License](#license)

<!-- /TOC -->

## Installation
This project can be launch without install, you just need [Python(3.6)](https://www.python.org) and [Scrapy (1.5).](https://doc.scrapy.org/en/latest/intro/install.html) With both installed you are ready to rock.

## Usage
Go to `CompassCrawler\course_scraper` and run the python script main.py (`python main.py`).
You'll be asked to insert the UC3M bachelors home pages _(note is the bachelor page, not the course page)_, to extract the information from their courses as shown below. Once you finish, insert a double enter and the program will start.  
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
All information will be exported in COMPASS JSON format to the default output folder `course_scraper\Courses`, with one JSON for each extracted course.

## File format
### File name   
The generated file names are the name of the bachelor or master under-slash UC3M course id with JSON extension.
### Fields
The fields from the UC3M system often needs translation, in order to be compatible with COMPASS. As shown below you can check the conversions.

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

Fields not contemplated in the table are not implemented in the current script.

## Contributing
You can modify this project as you want, if you want your changes to be applied to the master branch just make your improvements (well documented, good comments and descriptive variable names) and ask for merge.

### Project structure
To make easier yor life you should [learn a bit of Scrapy](https://doc.scrapy.org/en/latest/intro/tutorial.html) before get you hands dirty. Also this section is intended to help you understand the project and modify the code as you need.  
Scrapy is a popular crawling library allowing easy web information extraction, this is possible just customizing a couple of files `items.py, pipelines.py` and the spiders beneath `spiders` folder in this case `spider_courses.py`.  

* `items.py` defines the items fields, an item is a information instance extracted from a page, in our case represents a course an its information.
* `spider_courses` defines the spider which is going to fetch the information from a given page. It has to locate the information in the HTML structure of the page and store the information into a scrapy item instance. The locating of the information is archieved using [XPath](https://en.wikipedia.org/wiki/XPath) in code defined by selectors. In this case the spider also format (lightly) some of the values because XPath is not precise enough for the current page structure.
* `pipelines.py` defines the processing over the extracted items, in this case it generates the COMPASS JSON using `Utils.CourseToJSON` a custom utility intended to translate the UC3M information to COMPASS model and store it in JSON files to later be added to COMPASS service. The supported fields are collected in the table above beneath the section files. All the conversions are explained in code.

## License
