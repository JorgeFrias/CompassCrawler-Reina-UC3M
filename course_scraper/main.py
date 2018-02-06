from scrapy import cmdline
import sys

command = ("scrapy crawl --nolog spider_courses")

if sys.argv[1] == 'a':
    command = ("scrapy crawl --nolog spider_courses")

if sys.argv[1] == 'b':
    command = ("scrapy crawl  spider_courses -o data.csv -t csv")

cmdline.execute(command.split())
