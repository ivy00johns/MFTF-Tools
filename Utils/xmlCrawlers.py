import importlib
import os
from glob import glob

# File Path Variables
actionGroupFiles = []
dataFiles        = []
metadataFiles    = []
pageFiles        = []
sectionFiles     = []
testFiles        = []

# Start at the Current Working Directory (CWD)
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
def crawlForFilesWithProvidedPattern(crawlPattern):
    files = []
    for dir,_,_ in os.walk(start_dir):
        files.extend(glob(os.path.join(dir,crawlPattern)))
    return files

def crawlForActionGroupXmlFiles():
    actionGroupFiles = []
    actionGroupFiles.extend(crawlForFilesWithProvidedPattern(actionGroupPattern1))
    actionGroupFiles.extend(crawlForFilesWithProvidedPattern(actionGroupPattern2))
    return actionGroupFiles

def crawlForDataXmlFiles():
    dataFiles = []
    dataFiles.extend(crawlForFilesWithProvidedPattern(dataPattern1))
    dataFiles.extend(crawlForFilesWithProvidedPattern(dataPattern2))
    return dataFiles

def crawlForMetadataXmlFiles():
    metadataFiles    = []
    metadataFiles.extend(crawlForFilesWithProvidedPattern(metadataPattern1))
    metadataFiles.extend(crawlForFilesWithProvidedPattern(metadataPattern2))
    return metadataFiles

def crawlForPageXmlFiles():
    pageFiles = []
    pageFiles.extend(crawlForFilesWithProvidedPattern(pagePattern1))
    pageFiles.extend(crawlForFilesWithProvidedPattern(pagePattern2))
    return pageFiles

def crawlForSectionXmlFiles():
    sectionFiles = []
    sectionFiles.extend(crawlForFilesWithProvidedPattern(sectionPattern1))
    sectionFiles.extend(crawlForFilesWithProvidedPattern(sectionPattern2))
    return sectionFiles

def crawlForTestXmlFiles():
    testFiles = []
    testFiles.extend(crawlForFilesWithProvidedPattern(testPattern1))
    testFiles.extend(crawlForFilesWithProvidedPattern(testPattern2))
    return testFiles

def crawlForAllXmlFiles():
    # crawlForActionGroupXmlFiles()
    # crawlForDataXmlFiles()
    # crawlForMetadataXmlFiles()
    # crawlForPageXmlFiles()
    # crawlForSectionXmlFiles()
    # crawlForTestXmlFiles()
    pass