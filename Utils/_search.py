#!/usr/bin/env python3

import xml.dom.minidom
from Utils import _xmlCrawlers

def fullSearchResultsByAttributes(filesList, mainNode, entities):
    entityContents = {}

    for entity in entities:
        contents = []
        for fileList in filesList:
            currentNode = xml.dom.minidom.parse(fileList)
            entityNodes = currentNode.getElementsByTagName(mainNode)
            for entityNode in entityNodes:
                attribute = entityNode.getAttribute(entity)
                contents.append(attribute)

        # Sort the list.
        contents.sort(key=str.lower)

        # Remove unicode "u" from the list.
        cleanedUpList = [str(r) for r in contents]

        # Remove "" from the list.
        cleanedUpList = [x for x in cleanedUpList if x]

        entityContents[entity] = cleanedUpList
    return entityContents

def searchFullSearchResultsByAttributes(fullSearchResults, entities, searchTerm):
    finalResults = {}

    for entity in entities:
        for fullSearchResult in fullSearchResults:
            if (entity == fullSearchResult):
                listOfResults = fullSearchResults[entity]
                filteredResults = [i for i in listOfResults if searchTerm.lower() in i.lower()]
                finalResults[entity] = filteredResults
    
    return finalResults

def actionGroups():
    actionGroupFiles = _xmlCrawlers.crawlForActionGroupXmlFiles()
    results = fullSearchResultsByAttributes(actionGroupFiles, "actionGroup", ["name", "extends"]) 
    return results

def datas():
    dataFiles = _xmlCrawlers.crawlForDataXmlFiles()
    results = fullSearchResultsByAttributes(dataFiles, "entity", ["name", "extends"])
    return results

def metadatas():
    metadataFiles = _xmlCrawlers.crawlForMetadataXmlFiles()
    results = fullSearchResultsByAttributes(metadataFiles, "operation", ["name", "url"])
    return results

def pages():
    pageFiles = _xmlCrawlers.crawlForPageXmlFiles()
    results = fullSearchResultsByAttributes(pageFiles, "page", ["name", "url", "extends"])
    return results

def sections():
    sectionFiles = _xmlCrawlers.crawlForSectionXmlFiles()
    results = fullSearchResultsByAttributes(sectionFiles, "section", ["name", "extends"])
    return results

def tests():
    testFiles = _xmlCrawlers.crawlForTestXmlFiles()
    results = fullSearchResultsByAttributes(testFiles, "test", ["name", "extends"])
    return results

def everything():
    pass

def fullXmlSearchResults(filesList, mainNode):
    xmlEntityNodes = {}

    for fileName in filesList:
        currentNode = xml.dom.minidom.parse(fileName)
        entityNodes = currentNode.getElementsByTagName(mainNode)
        for entityNode in entityNodes:
            xmlEntityNodes[fileName] = entityNode.toprettyxml()
    
    return xmlEntityNodes

def fullActionGroupsXml():
    actionGroupFiles = _xmlCrawlers.crawlForActionGroupXmlFiles()
    results = fullXmlSearchResults(actionGroupFiles, "actionGroup")
    return results