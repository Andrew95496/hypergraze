import re
from bs4 import BeautifulSoup
import requests

def classname_exist(URL, ATTR,USER_INPUT):
    results = requests.get(URL)
    src = results.content
    html = BeautifulSoup(src, 'lxml')

    USER_INPUT = f'{ATTR}="{USER_INPUT}"'
    USER_REGEX = re.compile(USER_INPUT)
    METACHAR = USER_REGEX.findall(str(html))
    if METACHAR:
        return True


# ? https://docs.python.org/3/library/re.html


