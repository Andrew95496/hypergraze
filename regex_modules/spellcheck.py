from autocorrect import Speller
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('config.py')))
from tkinter import messagebox as mb






def spell_check(USER_INPUT):
    spell = Speller(lang='en')
    checked = spell(USER_INPUT)
    if checked != USER_INPUT:
        user_response = mb.askquestion('Question',f'Did you mean: {checked}\n')
        if user_response == 'no':
            return True
        else:
            return False       
    return True

