#!/usr/bin/env python3

from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, print_json, Separator

# Lists
fullListOfEntities = [
    {
        "key": "e",
        "name": "Everything",
        "value": "everything"
    },
    {
        "key": "a",
        "name": "Action Groups",
        "value": "action_group"
    },
    {
        "key": "d",
        "name": "Data Entities",
        "value": "data"
    },
    {
        "key": "m",
        "name": "Metadata Entities",
        "value": "metadata"
    },
    {
        "key": "p",
        "name": "Pages",
        "value": "page"
    },
    {
        "key": "s",
        "name": "Sections",
        "value": "section"
    },
    {
        "key": "t",
        "name": "Tests",
        "value": "test"
    }
]

# Starter question
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
            "key": "l",
            "name": "List",
            "value": "list"
        }
    ]
}

# Search related questions
whatAreYouSearchingFor = {
    "type": "list",
    "name": "searching_for",
    "message": "What are you searching for?",
    "choices": fullListOfEntities
}

whatTermAreYouSearchingWith = {
    "type": "input",
    "name": "search_term",
    "message": "What term do you want to search for?"
}

# Search Attribute questions
whichOfAllAttributes = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which attributes are you searching for?",
    "name": "attributes",
    "choices": [ 
        Separator("== All searchable attributes =="),
        {
            "key": "e",
            "disabled": "Disabled",
            "name": "Everything",
            "value": "everything"
        },
        {
            "key": "n",
            "name": "Names",
            "value": "name"
        },
        {
            "key": "e",
            "name": "Extends",
            "value": "extends"
        },
        {
            "key": "u",
            "name": "Urls",
            "value": "url"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

whichActionGroupAttributes = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which attributes are you looking for?",
    "name": "attributes",
    "choices": [ 
        Separator("== Action Group attributes =="),
        {
            "key": "z",
            "disabled": "Disabled",
            "name": "Everything",
            "value": "everything"
        },
        {
            "key": "n",
            "name": "Names",
            "value": "name"
        },
        {
            "key": "e",
            "name": "Extends",
            "value": "extends"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

whichDataEntityAttributes = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which attributes are you looking for?",
    "name": "attributes",
    "choices": [ 
        Separator("== Data Entity attributes =="),
        {
            "key": "z",
            "disabled": "Disabled",
            "name": "Everything",
            "value": "everything"
        },
        {
            "key": "n",
            "name": "Names",
            "value": "name"
        },
        {
            "key": "e",
            "name": "Extends",
            "value": "extends"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

whichMetadataAttributes = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which attributes are you looking for?",
    "name": "attributes",
    "choices": [ 
        Separator("== Metadata attributes =="),
        {
            "key": "z",
            "disabled": "Disabled",
            "name": "Everything",
            "value": "everything"
        },
        {
            "key": "n",
            "name": "Names",
            "value": "name"
        },
        {
            "key": "e",
            "name": "Extends",
            "value": "extends"
        },
        {
            "key": "u",
            "name": "Urls",
            "value": "url"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

whichPageAttributes = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which attributes are you looking for?",
    "name": "attributes",
    "choices": [ 
        Separator("== Page attributes =="),
        {
            "key": "x",
            "disabled": "Disabled",
            "name": "Everything",
            "value": "everything"
        },
        {
            "key": "n",
            "name": "Names",
            "value": "name"
        },
        {
            "key": "e",
            "name": "Extends",
            "value": "extends"
        },
        {
            "key": "u",
            "name": "Urls",
            "value": "url"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

whichSectionAttributes = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which attributes are you looking for?",
    "name": "attributes",
    "choices": [ 
        Separator("== Section attributes =="),
        {
            "key": "z",
            "disabled": "Disabled",
            "name": "Everything",
            "value": "everything"
        },
        {
            "key": "n",
            "name": "Names",
            "value": "name"
        },
        {
            "key": "e",
            "name": "Extends",
            "value": "extends"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

whichTestAttributes = {
    "type": "checkbox",
    "qmark": ">",
    "message": "Which attributes are you looking for?",
    "name": "attributes",
    "choices": [ 
        Separator("= Test attributes ="),
        {
            "key": "z",
            "disabled": "Disabled",
            "name": "Everything",
            "value": "everything"
        },
        {
            "key": "n",
            "name": "Names",
            "value": "name"
        },
        {
            "key": "e",
            "name": "Extends",
            "value": "extends"
        }
    ],
    "validate": lambda answer: "You must choose at least one attribute." \
        if len(answer) == 0 else True
}

# List related questions
whatDoYouWantToList = {
    "type": "list",
    "name": "list_type",
    "message": "What do you want to list?",
    "choices": [
        {
            "key": "n",
            "name": "Node counts",
            "value": "nodes"
        },
        {
            "key": "d",
            "name": "List of Duplicate Nodes",
            "value": "duplicates"
        },
        {
            "key": "l",
            "name": "List of Node Names",
            "value": "names"
        }
    ]
}

whichListDoYouWantToSee = {
    "type": "list",
    "name": "list_name_type",
    "message": "What list do you want to see?",
    "choices": fullListOfEntities
}

# Count related questions
whichCountsDoYouWantToSee = {
    "type": "list",
    "name": "count_type",
    "message": "What do you want to count?",
    "choices": fullListOfEntities
}

# Duplicates related questions
whichDuplicatesDoYouWantToSee = {
    "type": "list",
    "name": "duplicate_type",
    "message": "What do you want to see duplicates of?",
    "choices": fullListOfEntities
}
