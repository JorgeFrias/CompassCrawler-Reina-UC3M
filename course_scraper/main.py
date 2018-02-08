# COMPASS project
# Courses Information Crawler for UC3M web page.
# Author: Jorge Frias Galan
# Feb/2018

from scrapy import cmdline
import sys

command = ("scrapy crawl --nolog spider_courses")

if sys.argv[1] == 'a':
    print('Not exporting')
    command = ("scrapy crawl --nolog spider_courses")

if sys.argv[1] == 'b':
    print('CSV export')
    command = ("scrapy crawl --nolog spider_courses -o data.csv -t csv")

cmdline.execute(command.split())
