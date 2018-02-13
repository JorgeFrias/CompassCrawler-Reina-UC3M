# COMPASS project
# Courses Information Crawler for UC3M web page.
# Author: Jorge Frias Galan
# jofriasg@pa.uc3m.es
# Feb/2018

from course_scraper import items
import json
import os.path
from langdetect import detect


class CourseToJSONC(object):
    '''
    {"metadata":[
    {"key":"dc.title","value":"Test_title","language":"en_US"},
    {"key":"dc.identifier","value":"test_identifier","language":"en_US"},
    {"key":"dc.type","value":"test_type","language":"en_US"},
    {"key":"dc.description","value":"test_description","language":"en_US"},
    {"key":"dc.rights","value":"test_rights","language":"en_US"},
    {"key":"dc.subject","value":"test_subject","language":"en_US"},
    {"key":"dc.date","value":"test_date","language":null},
    {"key":"dc.language.iso","value":"test_language","language":"en_US"},
    {"key":"dc.publisher","value":"test_publisher","language":"en_US"},
    {"key":"dc.relation","value":"test_relation","language":"en_US"},
    {"key":"dc.creator","value":"test_creator","language":null},
    {"key":"compass.learningOpportunitySpecification.url","value":"test_url","language":"en_US"},
    {"key":"compass.learningOpportunitySpecification.credit","value":"test_credit","language":"en_US"},
    {"key":"compass.learningOpportunitySpecification.qualification","value":"test_qualification","language":"en_US"},
    {"key":"compass.learningOpportunitySpecification.prerequisite","value":"test_prerequisite","language":"en_US"},
    {"key":"compass.learningOpportunitySpecification.competence","value":"test_competence","language":"en_US"},
    {"key":"compass.learningOpportunitySpecification.objective","value":"test_objective","language":"en_US"},
    {"key":"compass.learningOpportunitySpecification.level","value":"test_level","language":"en_US"},
    {"key":"compass.learningOpportunitySpecification.assessment","value":"test_assessment","language":"en_US"},
    {"key":"compass.learningOpportunitySpecification.hasPart","value":"test_hasPart","language":"en_US"}
    ]
    }
    '''

    # Dictionaries in compass information model

    def createJSON(self, item: items.CourseScraperItem):
        data = self.genDicts(item)
        cwd = os.getcwd()               # Current working directory
        fileName = str(item['bachelor']) + '_' + str(item['id'])
        fileName = os.path.join(cwd, 'Courses', fileName)
        self.saveJSON(data, fileName)

    def genCompassDict(self, key, value, language):
        dict = {
            "key": key,
            "value": value,
            "language": language
        }

        return dict

    def genDicts(self, item: items.CourseScraperItem):
        data = {}
        data['metadata'] = []

        # Language detection [RFC4646] [ISO 639-1]
        lang = detect(item['name'])

        ### MANDATORY FIELDS --------------------------- ###
        # TITLE
        # A name given to the learning opportunity.
        data['metadata'].append(self.genCompassDict('dc.title', item['name'], lang))

        # DESCRIPTION
        # $$$$ Not defined at UC3M
        # data['metadata'].append(self.genCompassDict('dc.description', item['qualification'], 'en_US'))

        # IDENTIFIER
        # An alternative unambiguous reference to the learning opportunity within a given context.
        # Note: the primary identifier is automatically assigned by the system.
        data['metadata'].append(self.genCompassDict('dc.identifier', item['id'], lang))

        # PUBLISHER
        # An entity responsible for making the description of the learning opportunity available.
        data['metadata'].append(self.genCompassDict('dc.publisher', 'UC3M', lang))

        # CREATOR
        # An entity primarily responsible for creating the learning opportunity.
        data['metadata'].append(self.genCompassDict('dc.creator', item['coordinator'], lang))

        ### OPTIONAL FIELDS --------------------------- ###
        # COMPETENCE
        # A prerequisite competence for accessing learning opportunities.
        data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.competence', item['prerequisite'], lang))

        # TYPE
        # The nature or genre of the learning opportunity.
        # Not the same type as UC3M, those are not considered in COMPASS (Compulsive, basic core...)
        # It's hardwired to Talk/Lecture + Class/Group based, as all courses in the UC3M are (Bolonia)
        data['metadata'].append(self.genCompassDict('dc.type', 'Talk/Lecture', lang))
        data['metadata'].append(self.genCompassDict('dc.type', 'Class/Group based', lang))

        # LEVEL
        # An account of the education level of the learning opportunity.
        # The bachelor information contains the kind of degree
        if ( 'bachelor' in item['bachelor'].lower()):
            data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.level', 'Level::ISCE::Bachelor’s or equivalent level ', lang))
        elif ( 'master' in item['bachelor'].lower()):
            data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.level', 'Level::ISCE::Master’s or equivalent level ', lang))

        # URL
        # A hyperlink to a web resource that provides an alternate representation of the learning opportunity.
        data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.url', item['url'], lang))

        # LANGUAGE
        # A language of the learning opportunity.
        # Hard wired to English
        data['metadata'].append(self.genCompassDict('dc.language.iso', lang, lang))


        # SUBJECT
        # The topic of the learning opportunity.
        # Typically, the subject will be represented using keywords, key phrases, or classification codes.
        # Recommended best practice is to use a controlled vocabulary.
        # $$$$ Not trivial conversion
        # data['metadata'].append(self.genCompassDict('dc.subject', item['name'], 'en_US'))




        # data['metadata'].append(self.genCompassDict('dc.rights', item., 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.date', item['semester'], 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.publisher', 'UC3M', 'en_US'))
        # data.append(self.genCompassDict('dc.relation', item., 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.creator', item['bachelor'], 'en_US'))
        data['metadata'].append(
            self.genCompassDict('compass.learningOpportunitySpecification.credit', item['credits'], 'en_US'))
        data['metadata'].append(
            self.genCompassDict('compass.learningOpportunitySpecification.qualification', item['qualification'], 'en_US'))
        data['metadata'].append(
            self.genCompassDict('compass.learningOpportunitySpecification.prerequisite', item['prerequisite'], 'en_US'))
        data['metadata'].append(
            self.genCompassDict('compass.learningOpportunitySpecification.objective', item['programme'], 'en_US'))
        # data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.level', item., 'en_US'))
        # data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.assessment', item., 'en_US'))
        # data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.hasPart', item., 'en_US'))

        return data

    def saveJSON(self, data, fileName):
        try:
            print('Writing json')
            fileName = fileName + '.json'
            with open(fileName, 'w') as outfile:
                 json.dump(data, outfile, indent=1)
            # outfile = open(fileName, 'w')
            # json.dump(data, outfile)

        except:
            print('Error writing to file')
            pass


