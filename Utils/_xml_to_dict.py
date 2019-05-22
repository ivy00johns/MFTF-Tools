#!/usr/bin/env python3

import xmltodict, json, pprint
from Utils import _xmlCrawlers 

def createDictionary(fileList):
	dicts = []

	for files in fileList:
		with open(files) as fd:
			fileContents = fd.read()
			doc = xmltodict.parse(fileContents)
			dicts.append(doc)

	return dicts

def actionGroups():
	actionGroupFiles = _xmlCrawlers.crawlForActionGroupXmlFiles()
	actionGroupDicts = createDictionary(actionGroupFiles)

	return actionGroupDicts

def datas():
	dataFiles = _xmlCrawlers.crawlForDataXmlFiles()
	dataDicts = createDictionary(dataFiles)

	return dataDicts

def metadatas():
	metadataFiles = _xmlCrawlers.crawlForMetadataXmlFiles()
	metadataDicts = createDictionary(metadataFiles)

	return metadataDicts

def pages():
	pageFiles = _xmlCrawlers.crawlForPageXmlFiles()
	pageDicts = createDictionary(pageFiles)

	return pageDicts

def sections():
	sectionFiles = _xmlCrawlers.crawlForSectionXmlFiles()
	sectionDicts = createDictionary(sectionFiles)

	return sectionDicts

def tests():
	testFiles = _xmlCrawlers.crawlForTestXmlFiles()
	testDicts = createDictionary(testFiles)

	return testDicts

def everything():
	return ''
