# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from course_scraper.Utils import CourseToJSON


class CourseScraperPipeline(object):
    def process_item(self, item, spider):
        return item


class CoursesScraperPipelineJson(object):

    a = CourseToJSON.CourseToJSONC()

    def process_item(self, item, spider):
        self.a.createJSON(item)
        return item
