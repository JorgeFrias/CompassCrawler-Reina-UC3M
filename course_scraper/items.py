# -*- coding: utf-8 -*-
# COMPASS project
# Courses Information Crawler for UC3M web page.
# Author: Jorge Frias Galan
# Feb/2018

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CourseScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    year = scrapy.Field()
    name = scrapy.Field()
    id = scrapy.Field()
    bachelor = scrapy.Field()
    coordinator = scrapy.Field()
    departament = scrapy.Field()
    type = scrapy.Field()
    credits = scrapy.Field()
    course = scrapy.Field()
    semester = scrapy.Field()
    url = scrapy.Field()
    prerequisite = scrapy.Field()
    qualification = scrapy.Field()
    programme = scrapy.Field()
    assessment = scrapy.Field()
