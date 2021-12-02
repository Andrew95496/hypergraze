from autocorrect import Speller
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('config.py')))
from configs import bcolors as b






def spell_check(USER_INPUT):
    spell = Speller(lang='en')
    checked = spell(USER_INPUT)
    if checked != USER_INPUT:
        print(f'{b.BOLD}{b.FAIL}Did you mean:\n{b.ENDC}{b.ENDC}{b.OKBLUE}{checked}{b.ENDC}\n')
        user_response = input('yes/no?: ')
        if user_response == 'no':
            return True
        else:
            return False       
    return True