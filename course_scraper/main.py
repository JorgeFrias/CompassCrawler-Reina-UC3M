# COMPASS project
# Courses Information Crawler for UC3M web page.
# Author: Jorge Frias Galan
# jofriasg@pa.uc3m.es
# Feb/2018

from scrapy import cmdline
import sys
import os
import subprocess

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

for page in pagesList:
    print('Extracting: ' + page)
    command = ('scrapy crawl --nolog spider_courses -a start_url=' + page)
    ls_output = subprocess.check_output(command.split())

print('\nInformation extracted')

cwd = os.getcwd()  # Current working directory
filesPath = os.path.join(cwd, 'Courses')
print('Stored at: ' + filesPath)