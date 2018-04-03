# COMPASS project
# Courses Information Crawler for UC3M web page.
# Author: Jorge Frias Galan
# jofriasg@pa.uc3m.es
# Feb/2018

from scrapy import cmdline
import sys
import os
import subprocess

if (len(sys.argv) > 1):
    if (sys.argv[1] is 'd'):
        page = 'https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212562160/1371212987094/Bachelor_s_Degree_in_Computer_Science_and_Engineering#curriculum'
        command = ('scrapy crawl --nolog spider_courses -a start_url=' + page)
        cmdline.execute(command.split())
else:
    print('Welcome to COMPASS UC3M courses parser.\n'
          'This tool helps you to extract the information from the UC3M website '
          'and export it to COMPASS JSON format.\n')
    print('Homepages of the bachelors you want the information, divided by a new line: \n')

    pagesList = []
    while True:
        line = input()
        if line:
            pagesList.append(line)
        else:
            break

    # For each page run a different crawler instance
    for page in pagesList:
        print('Extracting: ' + page)
        command = ('scrapy crawl --nolog spider_courses -a start_url=' + page)
        ls_output = subprocess.check_output(command.split())

    print('\nInformation extracted')

    cwd = os.getcwd()  # Current working directory
    filesPath = os.path.join(cwd, 'Courses')
    print('Stored at: ' + filesPath)