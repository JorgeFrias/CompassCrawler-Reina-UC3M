# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SpiderCoursesSpider(CrawlSpider):
    name = 'spider_courses'
    allowed_domains = ['uc3m.es',
                       "https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/"]
    start_urls = ['https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212562160/1371212987094/Bachelor_s_Degree_in_Computer_Science_and_Engineering#curriculum']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('[data-label="Subject"]',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)
