import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('config.py')))
sys.path.append(os.path.dirname(os.path.abspath('regex_modules/spellcheck.py')))
import re
from bs4 import BeautifulSoup
import requests

# My modules
from configs import bcolors as b
from regex_modules import spell_check, split_LINK, split_ATTR






def classname_exist(URL, ATTR,USER_INPUT):
    if spell_check(USER_INPUT):
        FIND = '="\w{0,1000}-*/*\w{0,1000}"'
        LINK = '\s*=\s*"([^"]+)"'
        #* web parser
        results = requests.get(URL)
        src = results.content
        html = BeautifulSoup(src, 'lxml')

        #* Regex
        USER_INPUT = f'{ATTR}="{USER_INPUT}"'
        USER_REGEX = re.compile(USER_INPUT)
        METACHAR = USER_REGEX.findall(str(html))
        if not METACHAR:
            if (ATTR == 'src') or (ATTR == 'href'):
                USER_REGEX = re.compile(f'\s{ATTR}{LINK}')
                METACHAR = USER_REGEX.findall(str(html)) 
                print(f'{b.WARNING}ATTRIBUTE NAME NOT FOUND{b.ENDC}')       
                print(f'{b.BOLD}{b.FAIL}Suggestions:\n{b.ENDC}{b.ENDC}{b.OKCYAN}{split_LINK(set(METACHAR))}{b.ENDC}')
                print(ATTR + LINK)
                return False
            else:
                USER_REGEX = re.compile(f'\s{ATTR}{FIND}')
                METACHAR = USER_REGEX.findall(str(html)) 
                print(f'{b.WARNING}ATTRIBUTE NAME NOT FOUND{b.ENDC}')       
                print(f'{b.BOLD}{b.FAIL}Suggestions:\n{b.ENDC}{b.ENDC}{b.OKCYAN}{split_ATTR(set(METACHAR))}{b.ENDC}')
                print(ATTR + LINK)
                return False
        return True


# ? https://docs.python.org/3/library/re.html
# ? https://github.com/filyp/autocorrect


