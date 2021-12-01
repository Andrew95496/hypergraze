import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('config.py')))

from configs import bcolors as b
# from regex import classname_exist





# classname_exist('https://stackoverflow.com/questions/4383571/importing-files-from-different-folder','class', 'sidekbar')

# classname_exist('https://www.w3schools.com/python/python_ml_data_distribution.asp','src', 'rcow')


# ? https://docs.python.org/3/library/re.html

# ! src/href regex
# \s*=\s*"([^"]+)"


# def classname_exist(URL, ATTR,USER_INPUT):
#     FIND = '="\w{0,1000}-*/*\w{0,1000}"'
#     LINK = '# \s*=\s*"([^"]+)"'
#     #* web parser
#     results = requests.get(URL)
#     src = results.content
#     html = BeautifulSoup(src, 'lxml')

#     #* Regex
#     USER_INPUT = f'{ATTR}="{USER_INPUT}"'
#     USER_REGEX = re.compile(USER_INPUT)
#     METACHAR = USER_REGEX.findall(str(html))
#     if not METACHAR:
#         if (ATTR != 'src') or (ATTR != 'href'):
#             USER_REGEX = re.compile(f'{ATTR}{FIND}')
#             METACHAR = USER_REGEX.findall(str(html)) 
#             print(f'{b.WARNING}ATTRIBUTE NAME NOT FOUND{b.ENDC}')       
#             print(f'{b.BOLD}{b.FAIL}Did you mean? {b.ENDC}{b.ENDC}{b.OKCYAN}{split_reg(METACHAR)}{b.ENDC}')
#             print(ATTR + FIND)
#             return False
#         else:
#             USER_REGEX = re.compile(f'{ATTR}{LINK}')
#             METACHAR = USER_REGEX.findall(str(html)) 
#             print(f'{b.WARNING}ATTRIBUTE NAME NOT FOUND{b.ENDC}')       
#             print(f'{b.BOLD}{b.FAIL}Did you mean? {b.ENDC}{b.ENDC}{b.OKCYAN}{split_reg(METACHAR)}{b.ENDC}')
#             print(ATTR + LINK)
#     return True

from autocorrect import Speller

spell = Speller(lang='en')

print(spell('rcow'))
print(spell('mussa'))
print(spell('survice'))
print(spell('hte'))

# find_all_tables_to_excel('https://en.wikipedia.org/wiki/Baltimore_Ravens', 'table', 'wikitable', '__________1______1', 'xlsx')
# get_html('https://stackoverflow.com/questions/4383571/importing-files-from-different-folder','div', 'mt24', 'configworks', 'csv','yes')
# classname_exist('https://stackoverflow.com/questions/4383571/importing-files-from-different-folder','class', 'sidebnar')
# classname_exist('https://en.vipleague.tv/','href', 'row')