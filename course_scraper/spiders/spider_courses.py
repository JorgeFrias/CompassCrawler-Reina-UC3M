# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from course_scraper.items import CourseScraperItem

class SpiderCoursesSpider(CrawlSpider):
    name = 'spider_courses'
    allowed_domains = [
        'www3.uc3m.es',
        'uc3m.es/ss',
        'uc3m.es/reina',
        'aplicaciones.uc3m.es']

    start_urls = ['https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212562160/1371212987094/Bachelor_s_Degree_in_Computer_Science_and_Engineering#curriculum']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('[data-label="Subject"]',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)
        #self.parse_detail_page(response)
        #yield scrapy.Request(response.url, callback=self.parse_detail_page)

        #def parse_detail_page(self, response):
        year_selector = '//div [@class = "anio"]/text()'
        nameId_selector = '//div [@class = "asignatura"]/text()'
        bachelor_selector = '//div[@class="col-xs-8 col-lg-8 col-xl-8"]/center/text()'
        coordinator_selector = '//div[@class="col-xs-10 col-lg-10 col-xl-10"]/text()'
        departament_selector = '//div[@class="col-xs-12 col-lg-12 col-xl-12"]/text()'
        typeAndCourse_slector = '//div[@class="container-fluid"]/div[@class="row"]/div[1]/text()'
        credits_selector = '//div[@class="container-fluid"]/div[@class="row"]/div[2]/text()'
        semester_selector = '//div[@class="container-fluid"]/div[@class="row"]/div[2]/text()'

        year = response.xpath(year_selector).extract_first()
        name = response.xpath(nameId_selector).extract()[0]
        id = response.xpath(nameId_selector).extract()[1]
        bachelor = response.xpath(bachelor_selector).extract()[1]
        coordinator = response.xpath(coordinator_selector).extract()[1]
        departament = response.xpath(departament_selector).extract()[1]
        type = response.xpath(typeAndCourse_slector).extract()[1]
        credits = response.xpath(credits_selector).extract()[7]
        course = response.xpath(typeAndCourse_slector).extract()[3]
        semester = response.xpath(semester_selector).extract()[-1]
        #semestre Problema, no soy capaz de obtenerlo

        ### VALUES CLEANING ###
        # Year = course
        year = year[8:]

        # id
        id = id[1:-1]

        # course
        if course[-1] == 'º':
            course = course[:-1]
        else:
            print('unexpected course value')

        # semester
        if semester[-1] == 'º':
            semester = semester[:-1]
        else:
            print('unexpected semester value')

        # clean the Credits value
        ectsPos = credits.find('ECTS')
        credits = credits[:ectsPos]
        credits = credits.strip()

        # clean \n
        year = year.replace('\n','')
        name = name.replace('\n','')
        id = id.replace('\n','')
        bachelor = bachelor.replace('\n','')
        coordinator = coordinator.replace('\n','')
        departament = departament.replace('\n','')
        type = type.replace('\n','')
        credits = credits.replace('\n','')
        course = course.replace('\n','')
        semester = semester.replace('\n','')

        # clean \t
        year = year.replace('\t','')
        name = name.replace('\t','')
        id = id.replace('\t','')
        bachelor = bachelor.replace('\t','')
        coordinator = coordinator.replace('\t','')
        departament = departament.replace('\t','')
        type = type.replace('\t','')
        credits = credits.replace('\t','')
        course = course.replace('\t','')
        semester = semester.replace('\t','')

        # clean ' '
        credits = credits.replace(' ','')
        course = course.replace(' ','')
        semester = semester.replace(' ','')
        id = id.replace(' ','')


        item = CourseScraperItem()

        item['year'] = year
        item['name'] = name
        item['id'] = id
        item['bachelor'] = bachelor
        item['coordinator'] = coordinator
        item['departament'] = departament
        item['type'] = type
        item['credits'] = credits
        item['course'] = course
        item['semester'] = semester
        item['url'] = response.url

        yield item
