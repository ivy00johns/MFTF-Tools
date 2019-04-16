#!/usr/bin/env python3

from examples import custom_style_2
from PyInquirer import prompt, print_json
from Utils import _print
from Utils import _search
from Utils import _questions
from Utils import _exit

def results(listOfItems):
    print ("")
    for item in listOfItems:
        print (item)

def duplicates(listOfDuplicates):    
    for duplicate in listOfDuplicates:
        message = '''{name}: {count} \
                  '''.format(name=duplicate[0],count=duplicate[1])
        print (message)

def nodeCounts(entityList, title):
    entityCount = len(entityList["name"])

    message = '''\n {title} count: {count} \
              '''.format(title=title,count=entityCount)
    print (message)

def searchResultsBySearchAttribute(searchResults):
    print ("")
    for searchResult in searchResults:
        messageStart = '''===== Start Of - Search Results for attribute "{entityType}" - Total Results: {total} ====== \
                       '''.format(entityType=searchResult, total=len(searchResults[searchResult]))
        print (messageStart)

        for item in searchResults[searchResult]:
            print ("- " + item)

        messageEnd   = '''===== End Of   - Search Results for attribute "{entityType}" - Total Results: {total} ====== \
                     '''.format(entityType=searchResult, total=len(searchResults[searchResult]))
        print (messageEnd)

def askTheQuestionPrintTheAnswers(question, entityType):
    whichEntityAttributesAnswers  = prompt(question, style=custom_style_2)
    whatTermAreYouSearchingWithAnswers = prompt(_questions.whatTermAreYouSearchingWith)
    fullSearchResults = None

    if (entityType == "action_group"):
        fullSearchResults = _search.actionGroups()
    elif (entityType == "data"):
        fullSearchResults = _search.datas()
    elif (entityType == "metadata"):
        fullSearchResults = _search.metadatas()
    elif (entityType == "page"):
        fullSearchResults = _search.pages()
    elif (entityType == "section"):
        fullSearchResults = _search.sections()
    elif (entityType == "test"):
        fullSearchResults = _search.tests()
    elif (entityType == "everything"):
        _print.printTBD()
        _exit.program()

    searchAttributes  = whichEntityAttributesAnswers["attributes"]
    searchTerm        = whatTermAreYouSearchingWithAnswers["search_term"]

    results = _search.searchFullSearchResultsByAttributes(fullSearchResults, searchAttributes, searchTerm)
    _print.searchResultsBySearchAttribute(results)

def printTBD():
    print ("Feature will be ADDED at a later point.")
