# MFTF-CLI-Utilities

## Description
1. Prototype of my custom MFTF CLI utilities.
2. PLEASE NOTE: 
    * This is my 1st Python project so I apologize in advance for any horrendous code that you may find.
    * This is a WIP with a lot of improvements planend.

## Dependencies
* Python 3
* Cloned Magento repo (i.e.):
    * [Magento 2 CE](https://github.com/magento/magento2ce.git)
    * [Magento 2 EE](https://github.com/magento/magento2ee)
    * [Magento 2 B2B](https://github.com/magento/magento2b2b)
    * [MSI](https://github.com/magento-engcom/msi)


## Setup
1. Clone the "MFTF-CLI-Utilities" repo:
    ```
    git clone https://github.com/ivy00johns/MFTF-CLI-Utilities.git
    ```

## Running
```
cd [MAGENTO_REPO]
python3 [MFTF_CLI_UTILITIES_DIRECTORY]/mftfCli.py
```

## Known Issues
1. The Search functionality is case-sensitive currently.
2. The Search functions for all "Everything" items are not complete at this time.
3. ~~The Search functions for all "Metadata" items are not complete at this time.~~ (FIXED)

### TODO
1. Add progress bars.
2. Add counters to the "List Duplicate" functions.
3. Add support for CLI flags.
4. Add "keys" to the Question options.
5. Add "element" search functions.
6. Add Unit Tests.
7. Add Progress Bars.