#!/usr/bin/env python3

from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from Utils2 import _questions_v2 as _questions

####   Ask the Questions   ####
###############################
## Ask the Starter Question ##
whatDoYouWantToDoAnswer = prompt(_questions.whatDoYouWantToDo)
userAction = whatDoYouWantToDoAnswer["user_action"]

#### Branching logic based on the answer to the Starer Question. ####
if (userAction == "search"):
    whatDoYouWantToSearchInAnswers = prompt(_questions.whatDoYouWantToSearchIn)
    searchIn = whatDoYouWantToSearchInAnswers["search_in"]

    if (searchIn == "top_level"):
        whichTopLevelNodeAreYouSearchingInAnswers = prompt(_questions.whichTopLevelNodeAreYouSearchingIn)
        topLevelNode = whichTopLevelNodeAreYouSearchingInAnswers["top_level_node"]
        
        # 1.) Determine which Top Level node you want to search in.
        # 2.) Determine which node attribute you want to search in.
        # 3.) Determine which Keyword you want to search with.
        # 4.) Determine which Action you want to take take with the results.
        if (topLevelNode == "action_group"):
            whichTopLevelActionGroupNodeAttributeAreYouSearchingInAnswers = prompt(_questions.whichTopLevelActionGroupNodeAttributeAreYouSearchingIn)
            actionGroupAttribute = whichTopLevelActionGroupNodeAttributeAreYouSearchingInAnswers["attributes"]

            if (actionGroupAttribute == "names"):
                print("Action Group Names")
            elif (actionGroupAttribute == "extends"):
                print("Action Group Extends")
            elif (actionGroupAttribute == "eveything"):
                print("Everything")

        elif (topLevelNode == "data"):
            print("Data Entity")
        elif (topLevelNode == "metadata"):
            print("Metadata Entity")
        elif (topLevelNode == "page"):
            print("Page")
        elif (topLevelNode == "section"):
            print("Section")
        elif (topLevelNode == "test"):
            print("Test")
        elif (topLevelNode == "everything"):
            print("Everything")

    elif (searchIn == "sub_level"):
        whichTopLevelNodeAreYouLookingForSubLevelNodesUnderAnswers = prompt(_questions.whichTopLevelNodeAreYouLookingForSubLevelNodesUnder)
        topLevelForSubLevels = whichTopLevelNodeAreYouLookingForSubLevelNodesUnderAnswers["top_level_node_search"]

        # 1.) Determine which Top Level node you want to select Sub Level nodes from.
        # 2.) Determine which node attribute you want to search in.
        # 3.) Determine which Keyword you want to search with.
        # 4.) Determine which Action you want to take take with the results.
        if (topLevelForSubLevels == "action_group"):
            print("Action Group")
        elif (topLevelForSubLevels == "data"):
            print("Data Entity")
        elif (topLevelForSubLevels == "metadata"):
            print("Metadata Entity")
        elif (topLevelForSubLevels == "page"):
            print("Page")
        elif (topLevelForSubLevels == "section"):
            print("Section")
        elif (topLevelForSubLevels == "test"):
            print("Test")
        elif (topLevelForSubLevels == "everything"):
            print("Everything")

elif (userAction == "count"):
    whatDoYouWantToCountAnswers = prompt(_questions.whatDoYouWantToCount)
    whatToCount = whatDoYouWantToCountAnswers["count_type"]

    if (whatToCount == "top_level_total"):
        print("Top Level Nodes - TOTALS")
    elif (whatToCount == "top_level_module"):
        print("Top Level Nodes - PER MODULE TOTALS")
    elif (whatToCount == "module_count"):
        print("Modules")

elif (userAction == "list"):
    whatDoYouWantToListAnswers = prompt(_questions.whatDoYouWantToList)
    listType = whatDoYouWantToListAnswers["list_type"]

    if (listType == "module_top_level_names"):
        print("Top Level Node Names - For ALL Modules")
    elif (listType == "all_top_level_names"):
        print("Top Level Node Names - For a specific Module")
    elif (listType == "duplicate_counts"):
        print("Duplicate Node Names + Counts")
    elif (listType == "suite_names"):
        print("Suite Names")
    elif (listType == "module_names"):
        print("Module Names")
    elif (listType == "node_attributes"):
        print("Attributes for a specific Node")

elif (userAction == "print"):
    whatDoYouWantToPrintOutAnswers = prompt(_questions.whatDoYouWantToPrintOut)
    printOutType = whatDoYouWantToPrintOutAnswers["print_out_type"]

    if (printOutType == "specific_file"):
        print("XML for a specific File")
    elif (printOutType == "specific_node"):
        print("XML for a specific Node")
