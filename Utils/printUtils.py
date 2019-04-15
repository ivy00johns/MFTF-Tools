def printResults(listOfItems):
    print ("")
    for item in listOfItems:
        print (item)

def printDuplicates(listOfDuplicates):    
    for duplicate in listOfDuplicates:
        message = '''{name}: {count} \
                  '''.format(name=duplicate[0],count=duplicate[1])
        print (message)

def printSearchResultsBySearchAttribute(searchResults):
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

def printTBD():
    print ("Feature will be ADDED at a later point.")
