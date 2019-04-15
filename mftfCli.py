from __future__ import print_function, unicode_literals
import os
import xml.dom.minidom
from PyInquirer import prompt, print_json
from examples import custom_style_2
from Utils import findUtils
from Utils import printUtils
from Utils import search
from Utils import xmlCrawlers
from Utils import questions

# File Path Variables
actionGroupFiles = []
dataFiles        = []
metadataFiles    = []
pageFiles        = []
sectionFiles     = []
testFiles        = []

# Custom Question Functions
def askTheQuestionPrintTheAnswers(question):
    whichEntityAttributesAnswers  = prompt(question, style=custom_style_2)
    whatTermAreYouSearchingWithAnswers = prompt(questions.whatTermAreYouSearchingWith)

    fullSearchResults = search.searchActionGroups()
    searchAttributes  = whichEntityAttributesAnswers["attributes"]
    searchTerm        = whatTermAreYouSearchingWithAnswers["search_term"]

    results = search.searchFullSearchResultsByAttributes(fullSearchResults, searchAttributes, searchTerm)
    printUtils.printSearchResultsBySearchAttribute(results)

def printTheNodeCounts(entityList, title):
    entityCount = len(entityList["name"])

    message = '''\n {title} count: {count} \
              '''.format(title=title,count=entityCount)
    print (message)

def findAndPrintDuplicates(entityList):
    listOfDuplicates = findUtils.findDuplicates(entityList)
    printUtils.printDuplicates(listOfDuplicates)

#### Ask the questions ####
#
## Ask the Starter Question ##
whatDoYouWantToDoAnswers = prompt(questions.whatDoYouWantToDo)

# Branching logic based on the answer to the Starter Question.
if (whatDoYouWantToDoAnswers["user_action"] == "search"):
    whatAreYouSearchingForAnswers = prompt(questions.whatAreYouSearchingFor)
    entityType = whatAreYouSearchingForAnswers["searching_for"]

    if (entityType == "action_group"):
        askTheQuestionPrintTheAnswers(questions.whichActionGroupAttributes)
    elif (entityType == "data"):
        askTheQuestionPrintTheAnswers(questions.whichDataEntityAttributes)
    elif (entityType == "metadata"):
        askTheQuestionPrintTheAnswers(questions.whichMetadataAttributes)
    elif (entityType == "page"):
        askTheQuestionPrintTheAnswers(questions.whichPageAttributes)
    elif (entityType == "section"):
        askTheQuestionPrintTheAnswers(questions.whichSectionAttributes)
    elif (entityType == "test"):
        askTheQuestionPrintTheAnswers(questions.whichTestAttributes)
    elif (entityType == "everything"):
        printUtils.printTBD()
        pass

elif (whatDoYouWantToDoAnswers["user_action"] == "list"):
    whatDoYouWantToListAnswers = prompt(questions.whatDoYouWantToList)

    if (whatDoYouWantToListAnswers["list_type"] == "nodes"):
        whichCountsDoYouWantToSeeAnswers = prompt(questions.whichCountsDoYouWantToSee)
        countType = whichCountsDoYouWantToSeeAnswers["count_type"]

        if (countType == "action_group"):
            actionGroupsList = search.searchActionGroups()
            printTheNodeCounts(actionGroupsList, "Action Group")
        elif (countType == "data"):
            datasList = search.searchDatas()
            printTheNodeCounts(datasList, "Data")
        elif (countType == "metadata"):
            metadataEntitiesList = search.searchMetadatas()
            printTheNodeCounts(metadataEntitiesList, "Metadata")
        elif (countType == "page"):
            pagesList = search.searchPages()
            printTheNodeCounts(pagesList, "Page")
        elif (countType == "section"):
            sectionsList = search.searchSections()
            printTheNodeCounts(sectionsList, "Section")
        elif (countType == "test"):
            testsList = search.searchTests()
            printTheNodeCounts(testsList, "Test")
        elif (countType == "everything"):
            actionGroupsCount = len((search.searchActionGroups())["name"])
            datasCount        = len((search.searchDatas())["name"])
            metadatasCount    = len((search.searchMetadatas())["name"])
            pagesCount        = len((search.searchPages())["name"])
            sectionsCount     = len((search.searchSections())["name"])
            testsCount        = len((search.searchTests())["name"])

            message = '''\n Action Group count: {actionGroup} \n Data count:         {datas} \n Metadata count:     {metadatas} \n Page count:         {pages} \n Section count:      {sections} \n Test count:         {tests}\
                      '''.format(actionGroup=actionGroupsCount,
                                 datas=datasCount,
                                 metadatas=metadatasCount,
                                 pages=pagesCount,
                                 sections=sectionsCount,
                                 tests=testsCount)
            print (message)
    elif (whatDoYouWantToListAnswers["list_type"] == "duplicates"):
        whichDuplicatesDoYouWantToSeeAnswers = prompt(questions.whichDuplicatesDoYouWantToSee)
        duplicateType = whichDuplicatesDoYouWantToSeeAnswers["duplicate_type"]

        if (duplicateType == "action_group"):
            actionGroupsList = (search.searchActionGroups())["name"]
            findAndPrintDuplicates(actionGroupsList)
        elif (duplicateType == "data"):
            datasList = (search.searchDatas())["name"]
            findAndPrintDuplicates(datasList)
        elif (duplicateType == "metadata"):
            metadataEntitiesList = (search.searchMetadatas())["name"]
            findAndPrintDuplicates(metadataEntitiesList)
        elif (duplicateType == "page"):
            pagesList = (search.searchPages())["name"]
            findAndPrintDuplicates(pagesList)
        elif (duplicateType == "section"):
            sectionsList = (search.searchSections())["name"]
            findAndPrintDuplicates(sectionsList)
        elif (duplicateType == "test"):
            testsList = (search.searchTests())["name"]
            findAndPrintDuplicates(testsList)
        elif (duplicateType == "everything"):
            printUtils.printTBD()
            pass

    elif (whatDoYouWantToListAnswers["list_type"] == "names"):
        whichListDoYouWantToSeeAnswers = prompt(questions.whichListDoYouWantToSee)
        listByNameType = whichListDoYouWantToSeeAnswers.get("list_name_type")
        
        if (listByNameType == "action_group"):
            actionGroupsList = (search.searchActionGroups())["name"]
            printUtils.printResults(actionGroupsList)
        elif (listByNameType == "data"):
            datasList = (search.searchDatas())["name"]
            printUtils.printResults(datasList)
        elif (listByNameType == "metadata"):
            metadataEntitiesList = (search.searchMetadatas())["name"]
            printUtils.printResults(metadataEntitiesList)
        elif (listByNameType == "page"):
            pagesList = (search.searchPages())["name"]
            printUtils.printResults(pagesList)
        elif (listByNameType == "section"):
            sectionsList = (search.searchSections())["name"]
            printUtils.printResults(sectionsList)
        elif (listByNameType == "test"):
            testsList = (search.searchTests())["name"]
            printUtils.printResults(testsList)
        elif (listByNameType == "everything"):
            printUtils.printTBD()
            pass
