# COMPASS project
# Courses Information Crawler for UC3M web page.
# Author: Jorge Frias Galan
# Feb/2018

from course_scraper import items
import json


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
        fileName = 'Courses/' + str(item.bachelor) + str(item.id)
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

#        a = self.genCompassDict('dc.title',  item['name'], 'en_US')
#        data['metadata'].append(a)

        data['metadata'].append(self.genCompassDict('dc.title', item['name'], 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.identifier', item['id'], 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.type', item['type'], 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.description', item['qualification'], 'en_US'))
        # data['metadata'].append(self.genCompassDict('dc.rights', item., 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.subject', item['name'], 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.date', item['semester'], 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.language.iso', 'en_US', 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.publisher', 'UC3M', 'en_US'))
        # data.append(self.genCompassDict('dc.relation', item., 'en_US'))
        data['metadata'].append(self.genCompassDict('dc.creator', item['bachelor'], 'en_US'))
        data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.url', item['url'], 'en_US'))
        data['metadata'].append(
            self.genCompassDict('compass.learningOpportunitySpecification.credit', item['credits'], 'en_US'))
        data['metadata'].append(
            self.genCompassDict('compass.learningOpportunitySpecification.qualification', item['qualification'], 'en_US'))
        data['metadata'].append(
            self.genCompassDict('compass.learningOpportunitySpecification.prerequisite', item['prerequisite'], 'en_US'))
        # data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.competence', item., 'en_US'))
        data['metadata'].append(
            self.genCompassDict('compass.learningOpportunitySpecification.objective', item['programme'], 'en_US'))
        # data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.level', item., 'en_US'))
        # data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.assessment', item., 'en_US'))
        # data['metadata'].append(self.genCompassDict('compass.learningOpportunitySpecification.hasPart', item., 'en_US'))

        return data

    def saveJSON(self, data, filName):
        try:
            print('Writing json')
            with open(filName + '.json', 'a') as outfile:
                json.dump(data, outfile)

        except:
            print('Error writing to file')
            pass


