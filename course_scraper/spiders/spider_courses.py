# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from course_scraper.items import CourseScraperItem
from course_scraper.Utils import TextUtil

class SpiderCoursesSpider(CrawlSpider):
    name = 'spider_courses'

    # Limit the domains, just the course specifications
    allowed_domains = [
        'www3.uc3m.es',
        'uc3m.es/ss',
        'uc3m.es/reina',
        'aplicaciones.uc3m.es']

    # Bachelor's main pages:
    start_urls = [
        'https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212562160/1371212987094/Bachelor_s_Degree_in_Computer_Science_and_Engineering#curriculum',
        'https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212560793/1371212987094/Bachelor_s_Degree_in_Telematics_Engineering',
        'https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212345976/1371212987094/Bachelor_s_Degree_in_Telecommunication_Technologies_Engineering',
        'https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212485394/1371212987094/Bachelor_s_Degree_in_Communication_System_Engineering',
        'https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212533644/1371212987094/Bachelor_s_Degree_in_Audiovisual_System_Engineering'
                  ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('[data-label="Subject"]',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)
        #self.parse_detail_page(response)
        #yield scrapy.Request(response.url, callback=self.parse_detail_page)

        #def parse_detail_page(self, response):
        # XPATH to extract desired information
        year_selector = '//div [@class = "anio"]/text()'
        nameId_selector = '//div [@class = "asignatura"]/text()'
        bachelor_selector = '//div[@class="col-xs-8 col-lg-8 col-xl-8"]/center/text()'
        coordinator_selector = '//div[@class="col-xs-10 col-lg-10 col-xl-10"]/text()'
        departament_selector = '//div[@class="col-xs-12 col-lg-12 col-xl-12"]/text()'
        typeAndCourse_slector = '//div[@class="container-fluid"]/div[@class="row"]/div[1]/text()'
        credits_selector = '//div[@class="container-fluid"]/div[@class="row"]/div[2]/text()'
        semester_selector = '//div[@class="container-fluid"]/div[@class="row"]/div[2]/text()'
        furtherInfo_selector = '//div[@class="panel panel-primary apartado"]/div[2]/textarea/text()'         # Used by prerequisite, qualification & programe


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
        prerequisite = response.xpath(furtherInfo_selector).extract()[0]
        qualification = response.xpath(furtherInfo_selector).extract()[1]
        programme = response.xpath(furtherInfo_selector).extract()[2]

        #semestre Problema, no soy capaz de obtenerlo

        ### VALUES CLEANING ###

        # Numbers cleaning
        #year = year[8:]                                     # Year
        tmpYearList = TextUtil.extractNumericValue(id)
        year = str(int(tmpYearList[0])) + '/' + str(int(tmpYearList[1]))
        id = int(TextUtil.extractNumericValue(id)[0])       # Id
        course = int(TextUtil.extractNumericValue(course)[0])
        semester = int(TextUtil.extractNumericValue(semester)[0])
        credits = TextUtil.extractNumericValue(credits)[0]

        # Clean \n & \t
        name = TextUtil.cleanProcedure_SingleLineText(name)
        bachelor = TextUtil.cleanProcedure_SingleLineText(bachelor)
        coordinator = TextUtil.cleanProcedure_SingleLineText(coordinator)
        departament = TextUtil.cleanProcedure_SingleLineText(departament)
        type = TextUtil.cleanProcedure_SingleLineText(type)
        #year = TextUtil.cleanProcedure_SingleLineText(year)
        #id = TextUtil.cleanProcedure_SingleLineText(id)
        #course = TextUtil.cleanProcedure_SingleLineText(course)
        #semester = TextUtil.cleanProcedure_SingleLineText(semester)
        #credits = TextUtil.cleanProcedure_SingleLineText(credits)

        # Clean paragraphs
        prerequisite = TextUtil.cleanProcedure_Paragraphs(prerequisite)
        qualification = TextUtil.cleanProcedure_Paragraphs(qualification)
        programme = TextUtil.cleanProcedure_Paragraphs(programme)

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
        item['prerequisite'] = prerequisite
        item['qualification'] = qualification
        item['programme'] = programme

        yield item
