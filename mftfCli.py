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
actionGroupPattern1 = "app/code/Magento/*/Test/Mftf/ActionGroup/*"
actionGroupPattern2 = "dev/tests/acceptance/tests/functional/Magento/FunctionalTest/*/ActionGroup/*"

dataPattern1        = "app/code/Magento/*/Test/Mftf/Data/*"
dataPattern2        = "dev/tests/acceptance/tests/functional/Magento/FunctionalTest/*/Data/*"

metadataPattern1    = "app/code/Magento/*/Test/Mftf/Metadata/*"
metadataPattern2    = "dev/tests/acceptance/tests/functional/Magento/FunctionalTest/*/Metadata/*"

pagePattern1        = "app/code/Magento/*/Test/Mftf/Page/*"
pagePattern2        = "dev/tests/acceptance/tests/functional/Magento/FunctionalTest/*/Page/*"

sectionPattern1     = "app/code/Magento/*/Test/Mftf/Section/*"
sectionPattern2     = "dev/tests/acceptance/tests/functional/Magento/FunctionalTest/*/Section/*"

testPattern1        = "app/code/Magento/*/Test/Mftf/Test/*"
testPattern2        = "dev/tests/acceptance/tests/functional/Magento/FunctionalTest/*/Test/*"

# Crawl the current directory for XML files.
def crawlForActionGroupXmlFiles():
    for dir,_,_ in os.walk(start_dir):
        actionGroupFiles.extend(glob(os.path.join(dir,actionGroupPattern1)))
        actionGroupFiles.extend(glob(os.path.join(dir,actionGroupPattern2)))

def crawlForDataXmlFiles():
    for dir,_,_ in os.walk(start_dir):
        dataFiles.extend(glob(os.path.join(dir,dataPattern1)))
        dataFiles.extend(glob(os.path.join(dir,dataPattern2)))

def crawlForMetadataXmlFiles():
    for dir,_,_ in os.walk(start_dir):
        metadataFiles.extend(glob(os.path.join(dir,metadataPattern1)))
        metadataFiles.extend(glob(os.path.join(dir,metadataPattern2)))

def crawlForPageXmlFiles():
     for dir,_,_ in os.walk(start_dir):
         pageFiles.extend(glob(os.path.join(dir,pagePattern1)))
         pageFiles.extend(glob(os.path.join(dir,pagePattern2)))

def crawlForSectionXmlFiles():
    for dir,_,_ in os.walk(start_dir):
        sectionFiles.extend(glob(os.path.join(dir,sectionPattern1)))
        sectionFiles.extend(glob(os.path.join(dir,sectionPattern2)))

def crawlForTestXmlFiles():
    for dir,_,_ in os.walk(start_dir):
        testFiles.extend(glob(os.path.join(dir,testPattern1)))
        testFiles.extend(glob(os.path.join(dir,testPattern2)))

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

    actionGroupNames   = []
    actionGroupExtends = []
    for actionGroupFile in actionGroupFiles:
        currentActionGroup = xml.dom.minidom.parse(actionGroupFile)
        actionGroupNodes = currentActionGroup.getElementsByTagName("actionGroup")
        for actionGroup in actionGroupNodes:
            name    = actionGroup.getAttribute("name")
            extends = actionGroup.getAttribute("extends")
            actionGroupNames.append(name)
            actionGroupExtends.append(extends)

    actionGroupNames.sort(key=str.lower)
    actionGroupExtends.sort(key=str.lower)

    cleanedUpActionGroupNamesList = [str(r) for r in actionGroupNames]
    cleanedUpActionGroupExtendsList = [str(r) for r in actionGroupExtends]

    return [cleanedUpActionGroupNamesList, cleanedUpActionGroupExtendsList]

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

    metadataNames = []
    metadataUrls  = []
    for metadataFile in metadataFiles:
        currentMetadataFile = xml.dom.minidom.parse(metadataFile)
        metadataNodes = currentMetadataFile.getElementsByTagName("operation")
        for metadataNode in metadataNodes:
            name = metadataNode.getAttribute("name")
            url  = metadataNode.getAttribute("url")
            metadataNames.append(name)
            metadataUrls.append(url)

    metadataNames.sort(key=str.lower)
    metadataUrls.sort(key=str.lower)

    cleanedUpNamesList = [str(r) for r in metadataNames]
    cleanedUpUrlsList  = [str(r) for r in metadataUrls]
    return [cleanedUpNamesList, cleanedUpUrlsList]

def searchPages():
    crawlForPageXmlFiles()

    pageNames = []
    pageUrls = []
    for pageFile in pageFiles:
        currentPageFile = xml.dom.minidom.parse(pageFile)
        pageNodes = currentPageFile.getElementsByTagName("page")
        for pageNode in pageNodes:
            name = pageNode.getAttribute("name")
            url  = pageNode.getAttribute("url")
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
    "type": "list",
    "name": "user_action",
    "message": "What do you want to do?",
    "choices": [
        "Search",
        "List"
    ]
}

whatDoYouWantToSearchFor = {
    "type": "list",
    "name": "search_for",
    "message": "What are you searching for?",
    "choices": [
        "Everything",
        "Action Groups",
        "Data Entities",
        "Metadatas",
        "Pages",
        "Sections",
        "Tests"
    ]
}

# Search by Attribute Questions
whatActionGroupAttributeDoYouWantToSearchFor = {
    "type": "list",
    "name": "search_for_attribute",
    "message": "Which Action Group attribute are you searching for?",
    "choices": [
        "Name",
        "Extends"
    ]
}

whatDataEntityAttributeDoYouWantToSearchFor = {
    "type": "list",
    "name": "search_for_attribute",
    "message": "Which Data Entities attribute are you searching for?",
    "choices": [
        "Name",
        "Extends"
    ]
}

whatMetadataAttributeDoYouWantToSearchFor = {
    "type": "list",
    "name": "search_for_attribute",
    "message": "Which Metadata attribute are you searching for?",
    "choices": [
        "Name",
        "Url",
        "Extends"
    ]
}

whatPageAttributeDoYouWantToSearchFor = {
    "type": "list",
    "name": "search_for_attribute",
    "message": "Which Page attribute are you searching for?",
    "choices": [
        "Name",
        "Url",
        "Extends"
    ]
}

whatSectionAttributeDoYouWantToSearchFor = {
    "type": "list",
    "name": "search_for_attribute",
    "message": "Which Section attribute are you searching for?",
    "choices": [
        "Name",
        "Extends"
    ]
}

whatTestAttributeDoYouWantToSearchFor = {
    "type": "list",
    "name": "search_for_attribute",
    "message": "Which Test attribute are you searching for?",
    "choices": [
        "Name",
        "Extends"
    ]
}

whatDoYouWantToSearchWith = {
    "type": "input",
    "name": "search_term",
    "message": "What term do you want to search for?"
}

whatDoYouWantToList = {
    "type": "list",
    "name": "list_type",
    "message": "What do you want to loist?",
    "choices": [
        "Node Counts",
        "Duplicate Nodes",
        "List of Names"
    ]
}

whatDoYouWantToCount = {
    "type": "list",
    "name": "count_type",
    "message": "What do you want to count?",
    "choices": [
        "Everything",
        "Action Groups",
        "Data Entities",
        "Metadatas",
        "Pages",
        "Sections",
        "Tests"
    ]
}

whatDoYouWantToSeeDuplicatesOf = {
    "type": "list",
    "name": "duplicate_type",
    "message": "What do you want to see duplicates of?",
    "choices": [
        "Everything",
        "Action Groups",
        "Data Entities",
        "Metadatas",
        "Pages",
        "Sections",
        "Tests"
    ]
}

whatDoYouWantToListByName = {
    "type": "list",
    "name": "list_name_type",
    "message": "What list do you want to see?",
    "choices": [
        "Everything",
        "Action Groups",
        "Data Entities",
        "Metadatas",
        "Pages",
        "Sections",
        "Tests"
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
        results = [i for i in full_list_of_action_groups[0] if searchTerm in i]
        printResults(results)
    elif (searchType == "Data Entities"):
        full_list_of_datas = searchDatas()
        results = [i for i in full_list_of_datas if searchTerm in i]
        printResults(results)
    elif (searchType == "Metadatas"):
        full_list_of_metadatas = searchMetadatas()
        results = []
        results.append([i for i in full_list_of_metadatas[0] if searchTerm in i])
        results.append([i for i in full_list_of_metadatas[1] if searchTerm in i])
        printResults(results[0])
        printResults(results[1])
    elif (searchType == "Pages"):
        full_lists_of_pages = searchPages()
        results = []
        results.append([i for i in full_lists_of_pages[0] if searchTerm in i])
        results.append([i for i in full_lists_of_pages[1] if searchTerm in i])
        printResults(results[0])
        printResults(results[1])
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
        
else:
    whatDoYouWantToListAnswers = prompt(whatDoYouWantToList)

    listType = whatDoYouWantToListAnswers.get("list_type")

    if (listType == "Node Counts"):
        whatDoYouWantToCountAnswers = prompt(whatDoYouWantToCount)
        countAnswer = whatDoYouWantToCountAnswers.get("count_type")
        nodeCount = None

        if (countAnswer == "Everything"):
            full_list_of_action_groups  = len(searchActionGroups()[0])
            full_list_of_datas          = len(searchDatas())
            full_list_of_metadatas      = len(searchMetadatas()[0])
            full_lists_of_pages         = len(searchPages()[0])
            full_list_of_sections       = len(searchSections())
            full_list_of_tests          = len(searchTests())
            
            nodeCounts = '''\n Action Group count: {actionGroup} \n Data count:         {datas} \n Metadata count:     {metadatas} \n Page count:         {pages} \n Section count:      {sections} \n Test count:         {tests}\
                         '''.format(actionGroup=full_list_of_action_groups,
                                    datas=full_list_of_datas,
                                    metadatas=full_list_of_metadatas,
                                    pages=full_lists_of_pages,
                                    sections=full_list_of_sections,
                                    tests=full_list_of_tests)
        elif (countAnswer == "Action Groups"):
            full_list_of_action_groups = len(searchActionGroups()[0])
            nodeCounts = '''\n Action Group count: {actionGroup} \
                         '''.format(actionGroup=full_list_of_action_groups)
        elif (countAnswer == "Data Entities"):
            full_list_of_datas = len(searchDatas())
            nodeCounts = '''\n Data count: {datas} \
                         '''.format(datas=full_list_of_datas)
        elif (countAnswer == "Metadatas"):
            full_list_of_metadatas = len(searchMetadatas()[0])
            nodeCounts = '''\n Metadata count: {metadatas} \
                         '''.format(metadatas=full_list_of_metadatas)
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
            duplicates = (searchActionGroups()[0])
        elif (duplicateType == "Data Entities"):
            duplicates = searchDatas()
        elif (duplicateType == "Metadatas"):
            duplicates = (searchMetadatas()[0])
        elif (duplicateType == "Pages"):
            duplicates = (searchPages()[0])
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
            printResults(searchActionGroups()[0])
        elif (listByNameType == "Data Entities"):
            printResults(searchDatas())
        elif (listByNameType == "Metadatas"):
            printResults(searchMetadatas()[0])
        elif (listByNameType == "Pages"):
            printResults(searchPages()[0])
        elif (listByNameType == "Sections"):
            printResults(searchSections())
        elif (listByNameType == "Tests"):
            printResults(searchTests())
