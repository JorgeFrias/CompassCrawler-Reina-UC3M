# In the pythonic way, static methods are declared outside a class.
# "Pascal heart crying"
import re

"""
Cleans all new lines
"""
def cleanNewLines(stringToClean):
    stringToClean = stringToClean.replace('\n','')
    return  stringToClean

"""
Cleans all last new lines
"""
def cleanLastNewLine(stringToClean):
    if (stringToClean[-1] == '\n'):
        stringToClean = stringToClean[:-1]
        return cleanLastNewLine(stringToClean)        # Recursive call
    else:
        return  stringToClean

"""
Cleans all tabs in the text
"""
def cleanTabs(stringToClean):
    stringToClean = stringToClean.replace('\t', '')
    return  stringToClean

"""
Cleans all withe spaces
"""
def cleanWitheSpaces(stringToClean):
    stringToClean = stringToClean.replace(' ', '')
    return  stringToClean

"""
Extracts all the numeric value from a given string.
"""
def extractNumericValue(stringToExtract):
    #return int(filter(str.isdigit, stringToExtract))
    l = []
    for t in re.split(';|,|\*|\n|\s|\(|\)' ,stringToExtract):
        try:
            l.append(float(t))
        except ValueError:
            pass

    return l

"""
Cleans all HTML tags in a given text
"""
def cleanHTML(raw_html):
    cleanReg = re.compile('<.*?>')
    cleanText = re.sub(cleanReg, '', raw_html)
    return cleanText

### CLEANING PROCEDURES ###
# Usually used functions to apply over text

"""
Cleans:
- Tabs
- HTML
- Last new lines
"""
def cleanProcedure_Paragraphs(stringToClean):
    stringToClean = cleanTabs(stringToClean)
    stringToClean = cleanHTML(stringToClean)
    stringToClean = cleanLastNewLine(stringToClean)
    return stringToClean

def cleanProcedure_SingleLineText(stringToClean):
    stringToClean = cleanTabs(stringToClean)
    stringToClean = cleanNewLines(stringToClean)
    return stringToClean
