from __future__ import print_function, unicode_literals
import os
import xml.dom.minidom
import collections
from collections import Counter
from glob import glob
from PyInquirer import prompt, print_json

#  File Path Variables
actionGroupFiles = []
dataFiles        = []
metadataFiles    = []
pageFiles        = []
sectionFiles     = []
testFiles        = []

start_dir = os.getcwd()

# Folder GREP patterns
actionGroupPattern = "app/code/Magento/*/Test/Mftf/ActionGroup/*"
dataPattern        = "app/code/Magento/*/Test/Mftf/Data/*"
metadataPattern    = "app/code/Magento/*/Test/Mftf/Metadata/*"
pagePattern        = "app/code/Magento/*/Test/Mftf/Page/*"
sectionPattern     = "app/code/Magento/*/Test/Mftf/Section/*"
testPattern        = "app/code/Magento/*/Test/Mftf/Test/*"

# Crawl the current directory for XML files.
def crawlForActionGroupXmlFiles():
    for dir,_,_ in os.walk(start_dir):
        actionGroupFiles.extend(glob(os.path.join(dir,actionGroupPattern)))

def crawlForDataXmlFiles():
    for dir,_,_ in os.walk(start_dir):
        dataFiles.extend(glob(os.path.join(dir,dataPattern)))

def crawlForMetadataXmlFiles():
    for dir,_,_ in os.walk(start_dir):
        metadataFiles.extend(glob(os.path.join(dir,metadataPattern)))

def crawlForPageXmlFiles():
     for dir,_,_ in os.walk(start_dir):
         pageFiles.extend(glob(os.path.join(dir,pagePattern)))

def crawlForSectionXmlFiles():
    for dir,_,_ in os.walk(start_dir):
        sectionFiles.extend(glob(os.path.join(dir,sectionPattern)))

def crawlForTestXmlFiles():
    for dir,_,_ in os.walk(start_dir):
        testFiles.extend(glob(os.path.join(dir,testPattern)))

def crawlForAllXmlFiles():
    crawlForActionGroupXmlFiles()
    crawlForDataXmlFiles()
    crawlForMetadataXmlFiles()
    crawlForPageXmlFiles()
    crawlForSectionXmlFiles()
    crawlForTestXmlFiles()

# Search Functions
def searchActionGroups():
    crawlForActionGroupXmlFiles()

    actionGroupNames = []
    for actionGroupFile in actionGroupFiles:
        currentActionGroup = xml.dom.minidom.parse(actionGroupFile)
        actionGroupNodes = currentActionGroup.getElementsByTagName("actionGroup")
        for actionGroup in actionGroupNodes:
            name = actionGroup.getAttribute("name")
            actionGroupNames.append(name)

    actionGroupNames.sort(key=str.lower)

    cleanedUpActionGroupList = [str(r) for r in actionGroupNames]
    return cleanedUpActionGroupList

def searchDatas():
    crawlForDataXmlFiles()

    dataKeys = []
    for dataFile in dataFiles:
        currentDataFile = xml.dom.minidom.parse(dataFile)
        dataNodes = currentDataFile.getElementsByTagName("entity")
        for dataNode in dataNodes:
            key = dataNode.getAttribute("name")
            dataKeys.append(key)

    dataKeys.sort(key=str.lower)
    
    cleanedUpDataList = [str(r) for r in dataKeys]
    return cleanedUpDataList

def searchMetadatas():
    crawlForMetadataXmlFiles()

def searchPages():
    crawlForPageXmlFiles()

    pageNames = []
    pageUrls = []
    for pageFile in pageFiles:
        currentPageFile = xml.dom.minidom.parse(pageFile)
        pageNodes = currentPageFile.getElementsByTagName("page")
        for pageNode in pageNodes:
            name = pageNode.getAttribute("name")
            url = pageNode.getAttribute("url")
            pageNames.append(name)
            pageUrls.append(url)

    pageNames.sort(key=str.lower)
    pageUrls.sort(key=str.lower)

    cleanedUpNamesList = [str(r) for r in pageNames]
    cleanedUpUrlsList  = [str(r) for r in pageUrls]
    return [cleanedUpNamesList, cleanedUpUrlsList]

def searchSections():
    crawlForSectionXmlFiles()

    sectionNames = []
    for sectionFile in sectionFiles:
        currentSectionFile = xml.dom.minidom.parse(sectionFile)
        sectionNodes = currentSectionFile.getElementsByTagName("section")
        for sectionNode in sectionNodes:
            name = sectionNode.getAttribute("name")
            sectionNames.append(name)
    
    sectionNames.sort(key=str.lower)

    cleanedUpSectionNamesList = [str(r) for r in sectionNames]
    return cleanedUpSectionNamesList

def searchTests():
    crawlForTestXmlFiles()

    testNames = []
    for testFile in testFiles:
        currentTestFile = xml.dom.minidom.parse(testFile)
        testNodes = currentTestFile.getElementsByTagName("test")
        for testNode in testNodes:
            name = testNode.getAttribute("name")
            testNames.append(name)

    testNames.sort(key=str.lower)

    cleanedUpTestNamesList = [str(r) for r in testNames]
    return cleanedUpTestNamesList

def searchEverything():
    crawlForAllXmlFiles()
    
    everything = []

    everything.append(searchActionGroups())
    everything.append(searchDatas())
    everything.append(searchMetadatas())
    everything.append(searchPages())
    everything.append(searchSections())
    everything.append(searchTests())

    return everything

# Custom Functions
def printResults(listOfItems):
    print ("")
    for item in listOfItems:
        print (item)

def findDuplicates(listOfItems):
    return [item for item, count in collections.Counter(listOfItems).items() if count > 1]

# Questions for the User and what they want to do.
whatDoYouWantToDo = {
    'type': 'list',
    'name': 'user_action',
    'message': 'What do you want to do?',
    'choices': [
        'Search',
        'List'
    ]
}

whatDoYouWantToSearchFor = {
    'type': 'list',
    'name': 'search_for',
    'message': 'What are you searching for?',
    'choices': [
        'Everything',
        'Action Groups',
        'Data Entities',
        'Metadata',
        'Pages',
        'Sections',
        'Tests'
    ]
}

whatDoYouWantToSearchWith = {
    'type': 'input',
    'name': 'search_term',
    'message': 'What term do you want to search for?'
}

whatDoYouWantToList = {
    'type': 'list',
    'name': 'list_type',
    'message': 'What do you want to loist?',
    'choices': [
        'Node Counts',
        'Duplicate Nodes',
        'List of Names'
    ]
}

whatDoYouWantToCount = {
    'type': 'list',
    'name': 'count_type',
    'message': 'What do you want to count?',
    'choices': [
        'Everything',
        'Action Groups',
        'Data Entities',
        'Metadata',
        'Pages',
        'Sections',
        'Tests'
    ]
}

whatDoYouWantToSeeDuplicatesOf = {
    'type': 'list',
    'name': 'duplicate_type',
    'message': 'What do you want to see duplicates of?',
    'choices': [
        'Everything',
        'Action Groups',
        'Data Entities',
        'Metadata',
        'Pages',
        'Sections',
        'Tests'
    ]
}

whatDoYouWantToListByName = {
    'type': 'list',
    'name': 'list_name_type',
    'message': 'What list do you want to see?',
    'choices': [
        'Everything',
        'Action Groups',
        'Data Entities',
        'Metadatas',
        'Pages',
        'Sections',
        'Tests'
    ]
}

# Ask the questions.
whatDoYouWantToDoAnswers         = prompt(whatDoYouWantToDo)
whatDoYouWantToSearchForAnswers  = None
whatDoYouWantToSearchWithAnswers = None

# Deal with the answers.
if (whatDoYouWantToDoAnswers.get("user_action") == "Search"):
    whatDoYouWantToSearchForAnswers  = prompt(whatDoYouWantToSearchFor)
    whatDoYouWantToSearchWithAnswers = prompt(whatDoYouWantToSearchWith)

    searchType = whatDoYouWantToSearchForAnswers.get("search_for")
    searchTerm = whatDoYouWantToSearchWithAnswers.get("search_term")

    results = None

    if (searchType == "Action Groups"):
        full_list_of_action_groups = searchActionGroups()
        results = [i for i in full_list_of_action_groups if searchTerm in i]
        printResults(results)
    elif (searchType == "Data Entities"):
        full_list_of_datas = searchDatas()
        results = [i for i in full_list_of_datas if searchTerm in i]
        printResults(results)
    elif (searchType == "Metadata"):
        pass
    elif (searchType == "Pages"):
        full_lists_of_pages = searchPages()
        results = []
        results.append([i for i in full_lists_of_pages[0] if searchTerm in i])
        results.append([i for i in full_lists_of_pages[1] if searchTerm in i])
        printResults(results)
    elif (searchType == "Sections"):
        full_list_of_sections = searchSections()
        results = [i for i in full_list_of_sections if searchTerm in i]
        printResults(results)
    elif (searchType == "Tests"):
        full_list_of_tests = searchTests()
        results = [i for i in full_list_of_tests if searchTerm in i]
        printResults(results)
    elif (searchType == "Everything"):
        pass
        full_list_of_everything = searchEverything()
        print (full_list_of_everything)
else:
    whatDoYouWantToListAnswers = prompt(whatDoYouWantToList)

    listType = whatDoYouWantToListAnswers.get("list_type")

    if (listType == "Node Counts"):
        whatDoYouWantToCountAnswers = prompt(whatDoYouWantToCount)
        countAnswer = whatDoYouWantToCountAnswers.get("count_type")
        nodeCount = None

        if (countAnswer == "Everything"):
            full_list_of_action_groups  = len(searchActionGroups())
            full_list_of_datas          = len(searchDatas())
            full_lists_of_pages         = len(searchPages()[0])
            full_list_of_sections       = len(searchSections())
            full_list_of_tests          = len(searchTests())
            
            nodeCounts = '''\n Action Group count: {actionGroup} \n Data count:         {datas} \n Page count:         {pages} \n Section count:      {sections} \n Test count:         {tests}\
                         '''.format(actionGroup=full_list_of_action_groups,
                                    datas=full_list_of_datas,
                                    pages=full_lists_of_pages,
                                    sections=full_list_of_sections,
                                    tests=full_list_of_tests)
        elif (countAnswer == "Action Groups"):
            full_list_of_action_groups = len(searchActionGroups())
            nodeCounts = '''\n Action Group count: {actionGroup} \
                         '''.format(actionGroup=full_list_of_action_groups)
        elif (countAnswer == "Data Entities"):
            full_list_of_datas = len(searchDatas())
            nodeCounts = '''\n Data count: {datas} \
                         '''.format(datas=full_list_of_datas)
        elif (countAnswer == "Pages"):
            full_lists_of_pages = len(searchPages()[0])
            nodeCounts = '''\n Page count: {pages} \
                         '''.format(pages=full_lists_of_pages)
        elif (countAnswer == "Sections"):
            full_list_of_sections = len(searchSections())
            nodeCounts = '''\n Section count: {sections} \
                         '''.format(sections=full_list_of_sections)
        elif (countAnswer == "Tests"):
            full_list_of_tests = len(searchTests())
            nodeCounts = '''\n Test count: {tests} \
                         '''.format(tests=full_list_of_tests)

        print (nodeCounts)
    elif (listType == "Duplicate Nodes"):
        whatDoYouWantToSeeDuplicatesOfAnswers = prompt(whatDoYouWantToSeeDuplicatesOf)
        duplicateType = whatDoYouWantToSeeDuplicatesOfAnswers.get("duplicate_type")
        duplicates = None

        if (duplicateType == "Action Groups"):
            duplicates = searchActionGroups()
        elif (duplicateType == "Data Entities"):
            duplicates = searchDatas()
        elif (duplicateType == "Pages"):
            duplicates = searchPages()[0]
        elif (duplicateType == "Sections"):
            duplicates = searchSections()
        elif (duplicateType == "Tests"):
            duplicates = searchTests()

        printResults(findDuplicates(duplicates))
    else:
        whatDoYouWantToListByNameAnswers = prompt(whatDoYouWantToListByName)
        listByNameType = whatDoYouWantToListByNameAnswers.get("list_name_type")
        duplicates = None

        if (listByNameType == "Action Groups"):
            printResults(searchActionGroups())
        elif (listByNameType == "Data Entites"):
            printResults(searchDatas())
        elif (listByNameType == "Pages"):
            printResults(searchPages())
        elif (listByNameType == "Sections"):
            printResults(searchSections())
        elif (listByNameType == "Tests"):
            printResults(searchTests())
