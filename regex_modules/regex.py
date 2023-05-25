import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('config.py')))
sys.path.append(os.path.dirname(os.path.abspath('regex_modules/spellcheck.py')))
import re
from bs4 import BeautifulSoup
import requests
from tkinter import messagebox as mb

# My modules
from configs import bcolors as b
from regex_modules import spell_check, split_LINK, split_ATTR


def attr_name_exist(URL, ATTR,USER_INPUT):
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
                mb.showerror('ATTRIBUTE NAME NOT FOUND', f'Suggestions:\n{split_LINK(set(METACHAR))}')
                return False
            else:
                USER_REGEX = re.compile(f'\s{ATTR}{FIND}')
                METACHAR = USER_REGEX.findall(str(html)) 
                mb.showerror('ATTRIBUTE NAME NOT FOUND', f'Suggestions:\n{split_ATTR(set(METACHAR))}')
                return False
        return True


# ? https://docs.python.org/3/library/re.html
# ? https://github.com/filyp/autocorrect

