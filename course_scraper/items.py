# -*- coding: utf-8 -*-

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

