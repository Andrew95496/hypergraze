# PROJECT GUIDE

***THESE ARE ARE RULES TO FOLLOW WHILE WORKING ON THIS PROJECT***

<!-- ## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar. -->

<!-- ```bash
pip install foobar
``` -->
___

## General Rules

- Date format yyyy-mm-dd
___

## Variable Naming

All Caps Variable:
- USER INPUT
- DATABASE CONNECTIONS ex. (CONN, CUR)
- REGEX VARIABLES

```python
# Inputs
URL = input('Input URL: ')
HTML_TAG = input('Input an HTML Tag: ')
CLASS_NAME = input('Input an classname: ')
FILENAME = input('Input Filename: ')
FILETYPE = input('Input File type: ')
FINDALL = input('Find all occurrences?[yes/no]: ')

# connection to database
CONN = psycopg2.connect(
        host = cf.hostname,
        dbname = cf.database,
        user = cf.username,
        password = cf.pwd,
        port = cf.port_id)

CUR = CONN.cursor() 

# Regex
USER_INPUT = input('What do you want to find: ')
USER_REGEX = re.compile(USER_INPUT)
METACHAR = user_regex.findall(text)
print(METACHAR)
```
___

## CHANGELOG.md

- Log all changes
- follow [keepchangelog](https://keepachangelog.com/en/1.0.0/) for change types
- changes are put in bold italics (***)
- file names are italic (*)


```
- *test.py* ***CHANGED*** to *scrape.py*

```

___

## ToDO.txt

- Date the todos when added
- ø = not started | option + O
- ∆ = workng on | option + J
- √ = done | option + V
- add finished date

```
- [1991-01-16] - Restructure Code ∆
- [1991-02-10] - Add Regex to main.py ø
- [1991-02-14] - ERROR HANDLING for AttributeError in scarpe.py ∆
- [1991-02-20] - Add parser to main.py √ - [1991-02-25]

```

___
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)