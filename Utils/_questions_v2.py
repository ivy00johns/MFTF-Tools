#!/usr/bin/env python3

from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, print_json, Separator

# LIST OF TOP LEVEL NODES
fullListOfTopLevelNodes = [
    {
        "key": "a",
        "name": "Action Groups - <actionGroup>",
        "value": "action_group"
    },
    {
        "key": "d",
        "name": "Data Entities - <entity>",
        "value": "data"
    },
    {
        "key": "m",
        "name": "Metadata Entities - <operations>",
        "value": "metadata"
    },
    {
        "key": "p",
        "name": "Pages - <page>",
        "value": "page"
    },
    {
        "key": "s",
        "name": "Sections - <section>",
        "value": "section"
    },
    {
        "key": "t",
        "name": "Tests - <test>",
        "value": "test"
    },
    {
        "key": "e",
        "name": "Everything",
        "value": "everything"
    }
]

# STARTER QUESTIONS
whatDoYouWantToDo = {
    "type": "list",
    "name": "user_action",
    "message": "What do you want to do?",
    "choices": [
        {
            "key": "s",
            "name": "Search",
            "value": "search"
        },
        {
            "key": "c",
            "name": "Count",
            "value": "count"
        },
        {
            "key": "l",
            "name": "List",
            "value": "list"
        },
        {
            "key": "p",
            "name": "Print",
            "value": "print"
        }
    ]
}

# SEARCH RELATED QUESTIONS
whatDoYouWantToSearchIn = {
    "type": "list",
    "name": "search_in",
    "message": "What do you want to search in?",
    "choices": [
        {
            "key": "t",
            "name": "Top Level Node Attributes",
            "value": "top_level"
        },
        {
            "key": "s",
            "name": "Sub Level Node Attributes",
            "value": "sub_level"
        }
    ]
}

whatDoYouWantToDoWithTheSearchResults = {
    "type": "list",
    "name": "search_results_action",
    "message": "What do you want to do with the search results?",
    "choices": [
        {
            "key": "l",
            "name": "List the Search Results",
            "value": "list_results"
        },
        {
            "key": "n",
            "name": "Print the Node XML",
            "value": "node_xml"
        },
        {
            "key": "f",
            "name": "Print the File Path",
            "value": "file_path"
        }
    ]
}

whatTermAreYouSearchingWith = {
    "type": "input",
    "name": "search_term",
    "message": "What Term are you searching with?"
}

whichTopLevelNodeAreYouSearchingIn = {
    "type": "list",
    "name": "top_level_node",
    "message": "Which Top-Level node are you searching in?",
    "choices": fullListOfTopLevelNodes
}

whichTopLevelNodeAreYouLookingForSubLevelNodesUnder = {
    "type": "list",
    "name": "top_level_node_search",
    "message": "Which Top-Level node do you want to search for Sub-Level nodes under?",
    "choices": fullListOfTopLevelNodes
}

## START - ACTION GROUP SEARCH ##
whichTopLevelActionGroupNodeAttributeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Top-Level Action Group attribute are you searching in?",
    "name": "attributes",
    "choices": [ 
        Separator("== Action Group attributes =="),
        {
            "key": "n",
            "name": "Name",
            "value": "name"
        },
        {
            "key": "e",
            "name": "Extends",
            "value": "extends"
        },
        {
            "key": "f",
            "name": "File Name",
            "value": "filename"
        },
        {
            "key": "a",
            "name": "Insert After",
            "value": "insert_after"
        },
        {
            "key": "b",
            "name": "Insert Before",
            "value": "insert_before"
        },
        {
            "key": "z",
            "disabled": "Disabled",
            "name": "Everything",
            "value": "everything"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

whichActionGroupSubLevelNodeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Action Group Sub-Node are you searching in?",
    "name": "action_group_subnode",
    "choices": [
        Separator("== Action Group Sub-Nodes =="),
        {
            "key": "a",
            "name": "Annotations",
            "value": "annotations"
        },
        {
            "key": "g",
            "name": "Arguments",
            "value": "arguments"
        },
        {
            "key": "c",
            "name": "Actions",
            "value": "actions"
        },
        {
            "key": "z",
            "disabled": "Disabled",
            "name": "Everything",
            "value": "everything"
        }
    ],
    "validate": lambda answer: "You must choose at least one Sub-Node." \
        if len(answer) == 0 else True
}

whichActionGroupSubNodeAttributeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Action Group sub-node attribute are you searching in?",
    "name": "action_group_subnode_attribute",
    "choices": [
        Separator("== Action Group Sub-Node Attributes ==")
    ]
}
##  END  - ACTION GROUP SEARCH ##

## START - DATA ENTITY SEARCH ##
whichTopLevelDataEntityNodeAttributeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Top-Level Data Entity attribute are you searching in?",
    "name": "attributes",
    "choices": [ 
        Separator("== Data Entity attributes =="),
        {
            "key": "n",
            "name": "Name",
            "value": "name"
        },
        {
            "key": "e",
            "name": "Extends",
            "value": "extends"
        },
        {
            "key": "f",
            "name": "File Name",
            "value": "filename"
        },
        {
            "key": "t",
            "name": "Type",
            "value": "type"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

whichDataEntitySubNodeAttributeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Data Entity Sub-Node are you searching in?",
    "name": "action_group_subnode",
    "choices": [
        Separator("== Data Entity Sub-Nodes =="),
        {
            "key": "a",
            "name": "Array",
            "value": "array"
        },
        {
            "key": "d",
            "name": "Data",
            "value": "data"
        },
        {
            "key": "r",
            "name": "Required Entity",
            "value": "required_entity"
        },
        {
            "key": "v",
            "name": "Var",
            "value": "var"
        },
        {
            "key": "z",
            "disabled": "Disabled",
            "name": "Everything",
            "value": "everything"
        }
    ],
    "validate": lambda answer: "You must choose at least one Sub-Node." \
        if len(answer) == 0 else True
}

whichDataEntitySubNodeAttributeAreYouSearchingIn = {
    # TODO
}
##  END  - DATA ENTITY SEARCH ##

## START - METADATA ENTITY SEARCH ##
whichTopLevelMetadataEntityNodeAttributeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Top-Level Metadata Entity attribute are you searching in?",
    "name": "attributes",
    "choices": [ 
        Separator("== Metadata Entity attributes =="),
        {
            "key": "n",
            "name": "Name",
            "value": "name"
        },
        {
            "key": "e",
            "name": "Extends",
            "value": "extends"
        },
        {
            "key": "p",
            "name": "File Name",
            "value": "filename"
        },
        {
            "key": "a",
            "name": "Authorization",
            "value": "authorization"
        },
        {
            "key": "u",
            "name": "URL",
            "value": "url"
        },
        {
            "key": "m",
            "name": "Method",
            "value": "method"
        },
        {
            "key": "s",
            "name": "Success Regex",
            "value": "success_regex"
        },
        {
            "key": "r",
            "name": "Return Regex",
            "value": "return_regex"
        },
        {
            "key": "d",
            "name": "Data Type",
            "value": "data_type"
        },
        {
            "key": "t",
            "name": "Type",
            "value": "type"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

whichMetadataEntitySubNodeAttributeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Metadata Entity Sub-Node are you searching in?",
    "name": "action_group_subnode",
    "choices": [
        Separator("== Metadata Entity Sub-Nodes =="),
        {
            "key": "a",
            "name": "Array",
            "value": "array"
        },
        {
            "key": "c",
            "name": "Content Type",
            "value": "content_type"
        },
        {
            "key": "f",
            "name": "Field",
            "value": "field"
        },
        {
            "key": "h",
            "name": "Header",
            "value": "header"
        },
        {
            "key": "o",
            "name": "Object",
            "value": "object"
        },
        {
            "key": "p",
            "name": "Param",
            "value": "param"
        },
        {
            "key": "z",
            "disabled": "Disabled",
            "name": "Everything",
            "value": "everything"
        }
    ],
    "validate": lambda answer: "You must choose at least one Sub-Node." \
        if len(answer) == 0 else True
}

whichMetadataEntitySubNodeAttributeAreYouSearchingIn = {
    # TODO
}
##  END  - METADATA ENTITY SEARCH ##

## START - PAGE SEARCH ##
whichTopLevelPageNodeAttributeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Top-Level Page attribute are you searching in?",
    "name": "attributes",
    "choices": [ 
        Separator("== Page attributes =="),
        {
            "key": "n",
            "name": "Name",
            "value": "name"
        },
        {
            "key": "u",
            "name": "URL",
            "value": "url"
        },
        {
            "key": "a",
            "name": "Area",
            "value": "area"
        },
        {
            "key": "m",
            "name": "Module",
            "value": "module"
        },
        {
            "key": "t",
            "name": "File Name",
            "value": "filename"
        },
        {
            "key": "p",
            "name": "Parameterized",
            "value": "parameterized"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

whichPageSubNodeAttributeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Page Sub-Node are you searching in?",
    "name": "action_group_subnode",
    "choices": [
        Separator("== Page Sub-Nodes =="),
        {
            "key": "s",
            "name": "Section",
            "value": "sectiomn"
        }
    ],
    "validate": lambda answer: "You must choose at least one Sub-Node." \
        if len(answer) == 0 else True
}

whichPageSubNodeAttributeAreYouSearchingIn = {
    # TODO
}
##  END  - PAGE SEARCH ##

## START - SECTION SEARCH ##
whichTopLevelSectionNodeAttributeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Top-Level Section attribute are you searching in?",
    "name": "attributes",
    "choices": [ 
        Separator("== Section attributes =="),
        {
            "key": "n",
            "name": "Name",
            "value": "name"
        },
        {
            "key": "f",
            "name": "File Name",
            "value": "filename"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

whichSectionSubNodeAttributeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Section Sub-Node are you searching in?",
    "name": "action_group_subnode",
    "choices": [
        Separator("== Section Sub-Nodes =="),
        {
            "key": "e",
            "name": "Element",
            "value": "element"
        }
    ],
    "validate": lambda answer: "You must choose at least one Sub-Node." \
        if len(answer) == 0 else True
}

whichSectionSubNodeAttributeAreYouSearchingIn = {
    # TODO
}
##  END  - SECTION SEARCH ##

## START - TEST SEARCH ##
whichTopLevelTestNodeAttributeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Top-Level Test attribute are you searching in?",
    "name": "attributes",
    "choices": [ 
        Separator("== Test attributes =="),
        {
            "key": "n",
            "name": "Name",
            "value": "name"
        },
        {
            "key": "f",
            "name": "File Name",
            "value": "filename"
        },
        {
            "key": "e",
            "name": "Extends",
            "value": "extends"
        },
        {
            "key": "a",
            "name": "Insert Before",
            "value": "insert_before"
        },
        {
            "key": "b",
            "name": "Insert After",
            "value": "insert_after"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

whichTestSubNodeAttributeAreYouSearchingIn = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which Test Sub-Node are you searching in?",
    "name": "action_group_subnode",
    "choices": [
        Separator("== Test Sub-Nodes =="),
        {
            "key": "n",
            "name": "Annotations",
            "value": "annotations"
        },
        {
            "key": "g",
            "name": "Action Group",
            "value": "action_group"
        },
        {
            "key": "b",
            "name": "Before",
            "value": "before"
        },
        {
            "key": "a",
            "name": "After",
            "value": "after"
        },
        {
            "key": "z",
            "name": "Test Actions",
            "value": "test_actions"
        }
    ],
    "validate": lambda answer: "You must choose at least one Sub-Node." \
        if len(answer) == 0 else True
}

whichTestSubNodeAttributeAreYouSearchingIn = {
    # TODO
}
##  END  - TEST SEARCH ##

# Count specific questions
whatDoYouWantToCount = {
    "type": "list",
    "name": "count_type",
    "message": "What do you want to count?",
    "choices": [
        {
            "key": "t",
            "name": "Top Level Nodes - TOTALS",
            "value": "top_level_total"
        },
        {
            "key": "m",
            "name": "Top Level Nodes - PER MODULE TOTALS",
            "value": "top_level_module"
        },
        {
            "key": "c",
            "name": "Modules",
            "value": "module_count"
        }
    ]
}

# List specific questions
whatDoYouWantToList = {
    "type": "list",
    "name": "list_type",
    "message": "What do you want to list?",
    "choices": [
        {
            "key": "a",
            "name": "Top Level Node Names - For ALL Modules",
            "value": "module_top_level_names"
        },
        {
            "key": "m",
            "name": "Top Level Node Names - For a specific Module",
            "value": "all_top_level_names"
        },
        {
            "key": "d",
            "name": "Duplicate Node Names + Counts",
            "value": "duplicate_counts"
        },
        {
            "key": "s",
            "name": "Suite Names",
            "value": "suite_names"
        },
        {
            "key": "l",
            "name": "Module Names",
            "value": "module_names"
        },
        {
            "key": "n",
            "name": "Attributes for a specific Node",
            "value": "node_attributes"
        }
    ]
}

# Print specific questions
whatDoYouWantToPrintOut = {
    "type": "list",
    "name": "print_out_type",
    "message": "What do you want to print out?",
    "choices": [
        {
            "key": "f",
            "name": "XML for a specific File",
            "value": "specific_file"
        },
        {
            "key": "n",
            "name": "XML for a specific Node",
            "value": "specific_node"
        }
    ]
}
