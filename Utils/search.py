import xml.dom.minidom
from Utils import xmlCrawlers

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
                filteredResults = [i for i in listOfResults if searchTerm in i]
                finalResults[entity] = filteredResults
    
    return finalResults

def searchActionGroups():
    actionGroupFiles = xmlCrawlers.crawlForActionGroupXmlFiles()
    results = fullSearchResultsByAttributes(actionGroupFiles, "actionGroup", ["name", "extends"]) 
    return results

def searchDatas():
    dataFiles = xmlCrawlers.crawlForDataXmlFiles()
    results = fullSearchResultsByAttributes(dataFiles, "entity", ["name", "extends"])
    return results

def searchMetadatas():
    metadataFiles = xmlCrawlers.crawlForMetadataXmlFiles()
    results = fullSearchResultsByAttributes(metadataFiles, "operation", ["name", "url"])
    return results

def searchPages():
    pageFiles = xmlCrawlers.crawlForPageXmlFiles()
    results = fullSearchResultsByAttributes(pageFiles, "page", ["name", "url", "extends"])
    return results

def searchSections():
    sectionFiles = xmlCrawlers.crawlForSectionXmlFiles()
    results = fullSearchResultsByAttributes(sectionFiles, "section", ["name", "extends"])
    return results

def searchTests():
    testFiles = xmlCrawlers.crawlForTestXmlFiles()
    results = fullSearchResultsByAttributes(testFiles, "test", ["name", "extends"])
    return results

def searchEverything():
    pass
