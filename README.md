# CompassCrawler-Reina-UC3M
## Run
To run the crawler (web page information extractor) run the main.py on the terminal. Remember first you need to be in the project folder.  
Then you'll be asked to insert the UC3M bachelors home pages, to extract the information from their courses. Once you finish, 
insert a double enter and the program will start.  
All information will be exported in COMPASS JSON format to the default folder C:\Users\CURRENT_USER\...\course_scraper\Courses

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
