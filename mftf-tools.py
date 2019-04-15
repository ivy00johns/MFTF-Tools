#!/usr/bin/env python3

from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from Utils import _exit
from Utils import _find
from Utils import _print
from Utils import _search
from Utils import _questions

# File Path Variables
actionGroupFiles = []
dataFiles        = []
metadataFiles    = []
pageFiles        = []
sectionFiles     = []
testFiles        = []

####   Ask the Questions   ####
###############################
## Ask the Starter Question ##
whatDoYouWantToDoAnswers = prompt(_questions.whatDoYouWantToDo)

# Branching logic based on the answer to the Starter Question.
if (whatDoYouWantToDoAnswers["user_action"] == "search"):
    whatAreYouSearchingForAnswers = prompt(_questions.whatAreYouSearchingFor)
    entityType = whatAreYouSearchingForAnswers["searching_for"]

    if (entityType == "action_group"):
        _print.askTheQuestionPrintTheAnswers(_questions.whichActionGroupAttributes)
    elif (entityType == "data"):
        _print.askTheQuestionPrintTheAnswers(_questions.whichDataEntityAttributes)
    elif (entityType == "metadata"):
        _print.askTheQuestionPrintTheAnswers(_questions.whichMetadataAttributes)
    elif (entityType == "page"):
        _print.askTheQuestionPrintTheAnswers(_questions.whichPageAttributes)
    elif (entityType == "section"):
        _print.askTheQuestionPrintTheAnswers(_questions.whichSectionAttributes)
    elif (entityType == "test"):
        _print.askTheQuestionPrintTheAnswers(_questions.whichTestAttributes)
    elif (entityType == "everything"):
        _print.printTBD()
        _exit.program()

elif (whatDoYouWantToDoAnswers["user_action"] == "list"):
    whatDoYouWantToListAnswers = prompt(_questions.whatDoYouWantToList)

    if (whatDoYouWantToListAnswers["list_type"] == "nodes"):
        whichCountsDoYouWantToSeeAnswers = prompt(_questions.whichCountsDoYouWantToSee)
        countType = whichCountsDoYouWantToSeeAnswers["count_type"]

        if (countType == "action_group"):
            actionGroupsList = _search.actionGroups()
            _print.nodeCounts(actionGroupsList, "Action Group")
        elif (countType == "data"):
            datasList = _search.datas()
            _print.nodeCounts(datasList, "Data")
        elif (countType == "metadata"):
            metadataEntitiesList = _search.metadatas()
            _print.nodeCounts(metadataEntitiesList, "Metadata")
        elif (countType == "page"):
            pagesList = _search.pages()
            _print.nodeCounts(pagesList, "Page")
        elif (countType == "section"):
            sectionsList = _search.sections()
            _print.nodeCounts(sectionsList, "Section")
        elif (countType == "test"):
            testsList = _search.tests()
            _print.nodeCounts(testsList, "Test")
        elif (countType == "everything"):
            actionGroupsCount = len((_search.actionGroups())["name"])
            datasCount        = len((_search.datas())["name"])
            metadatasCount    = len((_search.metadatas())["name"])
            pagesCount        = len((_search.pages())["name"])
            sectionsCount     = len((_search.sections())["name"])
            testsCount        = len((_search.tests())["name"])

            message = '''\n Action Group count: {actionGroup} \n Data count:         {datas} \n Metadata count:     {metadatas} \n Page count:         {pages} \n Section count:      {sections} \n Test count:         {tests}\
                      '''.format(actionGroup=actionGroupsCount,
                                 datas=datasCount,
                                 metadatas=metadatasCount,
                                 pages=pagesCount,
                                 sections=sectionsCount,
                                 tests=testsCount)
            print (message)
    elif (whatDoYouWantToListAnswers["list_type"] == "duplicates"):
        whichDuplicatesDoYouWantToSeeAnswers = prompt(_questions.whichDuplicatesDoYouWantToSee)
        duplicateType = whichDuplicatesDoYouWantToSeeAnswers["duplicate_type"]

        if (duplicateType == "action_group"):
            actionGroupsList = (_search.actionGroups())["name"]
            duplicatesList = _find.duplicates(actionGroupsList)
            _print.duplicates(duplicatesList)
        elif (duplicateType == "data"):
            datasList = (_search.datas())["name"]
            duplicatesList = _find.duplicates(datasList)
            _print.duplicates(duplicatesList)
        elif (duplicateType == "metadata"):
            metadataEntitiesList = (_search.metadatas())["name"]
            duplicatesList = _find.duplicates(metadataEntitiesList)
            _print.duplicates(duplicatesList)
        elif (duplicateType == "page"):
            pagesList = (_search.pages())["name"]
            duplicatesList = _find.duplicates(pagesList)
            _print.duplicates(duplicatesList)
        elif (duplicateType == "section"):
            sectionsList = (_search.sections())["name"]
            duplicatesList = _find.duplicates(sectionsList)
            _print.duplicates(duplicatesList)
        elif (duplicateType == "test"):
            testsList = (_search.tests())["name"]
            duplicatesList = _find.duplicates(testsList)
            _print.duplicates(duplicatesList)
        elif (duplicateType == "everything"):
            _print.printTBD()
            _exit.program()

    elif (whatDoYouWantToListAnswers["list_type"] == "names"):
        whichListDoYouWantToSeeAnswers = prompt(_questions.whichListDoYouWantToSee)
        listByNameType = whichListDoYouWantToSeeAnswers.get("list_name_type")
        
        if (listByNameType == "action_group"):
            actionGroupsList = (_search.actionGroups())["name"]
            _print.results(actionGroupsList)
        elif (listByNameType == "data"):
            datasList = (_search.datas())["name"]
            _print.results(datasList)
        elif (listByNameType == "metadata"):
            metadataEntitiesList = (_search.metadatas())["name"]
            _print.results(metadataEntitiesList)
        elif (listByNameType == "page"):
            pagesList = (_search.pages())["name"]
            _print.results(pagesList)
        elif (listByNameType == "section"):
            sectionsList = (_search.sections())["name"]
            _print.results(sectionsList)
        elif (listByNameType == "test"):
            testsList = (_search.tests())["name"]
            _print.results(testsList)
        elif (listByNameType == "everything"):
            _print.printTBD()
            _exit.program()
