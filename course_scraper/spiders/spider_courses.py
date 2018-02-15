# -*- coding: utf-8 -*-
# COMPASS project
# Courses Information Crawler for UC3M web page.
# Author: Jorge Frias Galan
# jofriasg@pa.uc3m.es
# Feb/2018

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from course_scraper.items import CourseScraperItem
from course_scraper.Utils import TextUtil
import datetime

# GLOBAL CONSTANTS
noInfoString = 'NA'         # Used to populate information less fields


'''
Spider to extract information from the UC3M courses.
Last update: feb/2018
'''
class SpiderCoursesSpider(CrawlSpider):
    name = 'spider_courses'

    # Code to set the start URL
    def __init__(self, *args, **kwargs):
        super(SpiderCoursesSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]
        a = 2

    # Limit the domains, just the course specifications allowed
    allowed_domains = [
        'www3.uc3m.es',
        'uc3m.es/ss',
        'uc3m.es/reina',
        'aplicaciones.uc3m.es']

    # No need for define the pages here, will be set by the user
    # Bachelor's main pages:
    # start_urls = [
    #     'https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212562160/1371212987094/Bachelor_s_Degree_in_Computer_Science_and_Engineering#curriculum',
    #     'https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212560793/1371212987094/Bachelor_s_Degree_in_Telematics_Engineering',
    #     'https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212345976/1371212987094/Bachelor_s_Degree_in_Telecommunication_Technologies_Engineering',
    #     'https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212485394/1371212987094/Bachelor_s_Degree_in_Communication_System_Engineering',
    #     'https://www.uc3m.es/ss/Satellite/Grado/en/Detalle/Estudio_C/1371212533644/1371212987094/Bachelor_s_Degree_in_Audiovisual_System_Engineering'
    #               ]

    # For each extracted link in allowed domains (just course information) call parse item
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('[data-label="Subject"]',)),
             callback="parse_item",
             follow=True),)

    '''
    Extracts the information from the course page
    '''
    def parse_item(self, response):
        print('Processing..' + response.url)

        # XPATH to locate desired information
        year_selector = '//div [@class = "anio"]/text()'
        nameId_selector = '//div [@class = "asignatura"]/text()'
        bachelor_selector = '//div[@class="col-xs-8 col-lg-8 col-xl-8"]/center/text()'
        coordinator_selector = '//div[@class="col-xs-10 col-lg-10 col-xl-10"]/text()'
        departament_selector = '//div[@class="col-xs-12 col-lg-12 col-xl-12"]/text()'
        typeAndCourse_slector = '//div[@class="container-fluid"]/div[@class="row"]/div[1]/text()'
        credits_selector = '//div[@class="container-fluid"]/div[@class="row"]/div[2]/text()'
        semester_selector = '//div[@class="container-fluid"]/div[@class="row"]/div[2]/text()'
        furtherInfo_selector = '//div[@class="panel panel-primary apartado"]/div[2]/textarea/text()'         # Used by prerequisite, qualification, programe & assesment
        assessmentExt_selector = '///div[@class="panel panel-primary apartado"]/div[2]/ul/li/text()'

        # Extract the information given by XPATHs
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
        # Assessment is divided, so we have to put it together
        assessment = response.xpath(furtherInfo_selector).extract()[4]
        assessmentExt = 'Calculation of final grade: \n' + \
                        response.xpath(assessmentExt_selector).extract()[0] + '\n' + \
                        response.xpath(assessmentExt_selector).extract()[1]

        # date = datetime.datetime.now().isoformat('%Y-%m-%d %H:%M')

        ### VALUES CLEANING ###
        # Numbers cleaning
        tmpYearList = TextUtil.extractNumericValue(year)
        year = str(int(tmpYearList[0])) + '/' + str(int(tmpYearList[1]))
        id = int(TextUtil.extractNumericValue(id)[0])
        credits = TextUtil.extractNumericValue(credits)[0]

        # Some information is usually missing in course and semester
        try:
            course = int(TextUtil.extractNumericValue(course)[0])
        except:
            print('Course definition error, defined as: \'' + course + '\'')
            course = noInfoString
            pass

        try:
            semester = int(TextUtil.extractNumericValue(semester)[0])
        except:
            print('Semester definition error, defined as: \' ' + semester + '\'')
            semester = noInfoString
            pass

        # Clean \n & \t
        name = TextUtil.cleanProcedure_SingleLineText(name)
        bachelor = TextUtil.cleanProcedure_SingleLineText(bachelor)
        if (bachelor[-1] is ')'):
            # Usually they are defined like Bachelor Name (id), this removes the (id)
            while (bachelor[-1] is not '('):
                bachelor = bachelor[:-1]                                 # Removes until '('
            bachelor = bachelor[:-1]                                     # Removes '('
        bachelor = TextUtil.cleanProcedure_SingleLineText(bachelor)     # Call again to ensure (last withespace)

        coordinator = TextUtil.cleanProcedure_SingleLineText(coordinator)
        departament = TextUtil.cleanProcedure_SingleLineText(departament)
        type = TextUtil.cleanProcedure_SingleLineText(type)
        # Following cleaning is not necessary using extract numeric value
        #year = TextUtil.cleanProcedure_SingleLineText(year)
        #id = TextUtil.cleanProcedure_SingleLineText(id)
        #course = TextUtil.cleanProcedure_SingleLineText(course)
        #semester = TextUtil.cleanProcedure_SingleLineText(semester)
        #credits = TextUtil.cleanProcedure_SingleLineText(credits)

        # Clean paragraphs
        # Some of the paragraphs may be missing
        try:
            prerequisite = TextUtil.cleanProcedure_Paragraphs(prerequisite)
        except:
            prerequisite = noInfoString
            pass

        try:
            qualification = TextUtil.cleanProcedure_Paragraphs(qualification)
        except:
            qualification = noInfoString
            pass

        try:
            programme = TextUtil.cleanProcedure_Paragraphs(programme)
        except:
            programme = noInfoString
            pass

        try:
            assessment = TextUtil.cleanProcedure_Paragraphs(assessment)
        except:
            assessment = noInfoString
            pass

        try:
            assessmentExt = TextUtil.cleanProcedure_Paragraphs(assessmentExt)
        except:
            assessmentExt = noInfoString
            pass

        assessment = assessment + '\n\n' + assessmentExt

        # Information to the Object
        courseObj = CourseScraperItem()

        courseObj['year'] = year
        courseObj['name'] = name
        courseObj['id'] = id
        courseObj['bachelor'] = bachelor
        courseObj['coordinator'] = coordinator
        courseObj['departament'] = departament
        courseObj['type'] = type
        courseObj['credits'] = credits
        courseObj['course'] = course
        courseObj['semester'] = semester
        courseObj['url'] = response.url
        courseObj['prerequisite'] = prerequisite
        courseObj['qualification'] = qualification
        courseObj['programme'] = programme
        courseObj['assessment'] = assessment
        # courseObj['date'] = date

        yield courseObj
