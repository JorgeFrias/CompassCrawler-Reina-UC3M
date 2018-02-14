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
        language = detect(item['qualification'])

        ### MANDATORY FIELDS --------------------------- ###
        # TITLE
        # A name given to the learning opportunity.
        data['metadata'].append(self.genCompassDict('dc.title', item['name'], language))

        # DESCRIPTION
        # Not defined at UC3M, generate from qualification
        data['metadata'].append(self.genCompassDict('dc.description', self.descriptionGenerate(item['qualification']), language))

        # IDENTIFIER
        # An alternative unambiguous reference to the learning opportunity within a given context.
        # Note: the primary identifier is automatically assigned by the system.
        data['metadata'].append(self.genCompassDict('dc.identifier', self.idGenerate('UC3M',item['id'], item['bachelor']), language))

        # PUBLISHER
        # An entity responsible for making the description of the learning opportunity available.
        data['metadata'].append(self.genCompassDict('dc.publisher', 'UC3M', language))

        # CREATOR
        # An entity primarily responsible for creating the learning opportunity.
        data['metadata'].append(self.genCompassDict('dc.creator', item['coordinator'], language))

        ### OPTIONAL FIELDS --------------------------- ###
        # COMPETENCE
        # A prerequisite competence for accessing learning opportunities.
        data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.competence', item['prerequisite'], language))

        # TYPE
        # The nature or genre of the learning opportunity.
        # Not the same type as UC3M, those are not considered in COMPASS (Compulsive, basic core...)
        # It's hardwired to Talk/Lecture + Class/Group based, as all courses in the UC3M are (Bolonia)
        data['metadata'].append(self.genCompassDict('dc.type', 'Talk/Lecture', language))
        data['metadata'].append(self.genCompassDict('dc.type', 'Class/Group based', language))

        # LEVEL
        # An account of the education level of the learning opportunity.
        # The bachelor information contains the kind of degree
        if ( 'bachelor' in item['bachelor'].lower()):
            data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.level', 'Level::ISCE::Bachelor’s or equivalent level ', language))
        elif ( 'master' in item['bachelor'].lower()):
            data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.level', 'Level::ISCE::Master’s or equivalent level ', language))

        # URL
        # A hyperlink to a web resource that provides an alternate representation of the learning opportunity.
        data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.url', item['url'], language))

        # LANGUAGE
        # A language of the learning opportunity.
        # Hard wired to English
        data['metadata'].append(self.genCompassDict('dc.language.iso', language, language))


        # SUBJECT
        # The topic of the learning opportunity.
        # Typically, the subject will be represented using keywords, key phrases, or classification codes.
        # Recommended best practice is to use a controlled vocabulary.
        # $$$$ Not trivial conversion
        # data['metadata'].append(self.genCompassDict('dc.subject', item['name'], 'en_US'))


        # data['metadata'].append(self.genCompassDict('dc.rights', item., 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.date', item['semester'], language))
        data['metadata'].append(self.genCompassDict('dc.publisher', 'UC3M', language))
        # data.append(self.genCompassDict('dc.relation', item., 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.creator', item['bachelor'], language))
        data['metadata'].append(
            self.genCompassDict('compass.learningOpportunitySpecification.credit', item['credits'], language))
        data['metadata'].append(
            self.genCompassDict('compass.learningOpportunitySpecification.qualification', item['qualification'], language))
        data['metadata'].append(
            self.genCompassDict('compass.learningOpportunitySpecification.prerequisite', item['prerequisite'], language))
        data['metadata'].append(
            self.genCompassDict('compass.learningOpportunitySpecification.objective', item['programme'], language))
        # data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.level', item., 'en_US'))
        # data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.assessment', item., 'en_US'))
        # data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.hasPart', item., 'en_US'))

        return data

    def  descriptionGenerate(self, potentialDescription):
        listIndicators = ['1', '-', '0', ]
        if (potentialDescription[0] in listIndicators):
            # It's a list (probably)
            potentialDescription = 'This course covers the following topics: \n' + potentialDescription

        return potentialDescription
    '''
    Generates a ID:
    university-courseID-degreeType_degreeAcronym
    Ex. for UC3M 205 Bachelor in Computer Science : UC3M-205-b_CS
    '''
    def idGenerate(self, university, courseID, degree):
        tempDegree = degree.lower()
        degreeType = ''
        if ('master' in tempDegree):
            # It's a master
            degreeType = 'm'
            tempDegree = tempDegree.replace('master in ', '')
        elif ('bachelor' in tempDegree):
            # It's a bachelor
            degreeType = 'b'
            tempDegree = tempDegree.replace('bachelor in ', '')

        # Now in tempDegree is just the name
        # Acronym generation
        degreeWords = tempDegree.split()
        degreeAcronym = ''
        for word in degreeWords:
            degreeAcronym += word[0]

        id = ''
        id = university + '-' + str(courseID) + '-' + degreeType + '_' + degreeAcronym

        return id

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


