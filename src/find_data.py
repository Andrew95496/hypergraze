import sys
import os
from tkinter import messagebox as mb


#  My Modules
sys.path.append(os.path.dirname(os.path.abspath('grazer_modules')))
sys.path.append(os.path.dirname(os.path.abspath('regex_modules')))
from regex_modules import attr_name_exist, notify
from grazer_modules import get_html, get_std_data, find_all_tables_to_excel, find_one_table_to_std, find_all_tables_to_std, find_one_table_to_excel

# DEFAULTS
url = 'https://andrew-leacock.netlify.app/html/contact.html'
tag = 'section'
attr = 'class'
attr_name = 'section'
file_name = 'creator_contacts'
file_type = 'html'
find_all = 'no'


def find_data(URL=url,
            HTML_TAG=tag,
            ATTRIBUTE=attr,
            ATTR_NAME=attr_name,
            FILENAME=file_name,
            FILETYPE=file_type,
            FINDALL=find_all):

    if attr_name_exist(URL, ATTRIBUTE, ATTR_NAME):
        notify('ATTRIBUTE NAME FOUND!')

        # * SEARCHING, WRITING, AND DATABASING FILE
        if FILETYPE == 'html':
            get_html(URL, HTML_TAG, ATTR_NAME, FILENAME, FILETYPE, FINDALL)

        elif HTML_TAG != 'table':
            get_std_data(URL, HTML_TAG, ATTR_NAME, FILENAME, FILETYPE, FINDALL)

        else:
            # FIND ALL TABLES IN URL AND WRITE TO EXCEL FILE
            if (FINDALL != 'no') and (FILETYPE == 'xlsx'):
                find_all_tables_to_excel(
                    URL, HTML_TAG, ATTR_NAME, FILENAME, FILETYPE)

            # FIND ALL TABLES IN URL AND WRITE TO ANY FILE
            elif (FINDALL != 'no') and (FILETYPE != 'xlsx'):
                find_all_tables_to_std(
                    URL, HTML_TAG, ATTR_NAME, FILENAME, FILETYPE)

            # FIND FIRST TABLES IN URL AND WRITE TO ANY FILE
            elif (FINDALL == 'no') and (FILETYPE != 'xlsx'):
                find_one_table_to_std(
                    URL, HTML_TAG, ATTR_NAME, FILENAME, FILETYPE)

            # FIND FIRST TABLES IN URL AND WRITE TO EXCEL FILE
            else:
                find_one_table_to_excel(
                    URL, HTML_TAG, ATTR_NAME, FILENAME, FILETYPE)
    else:
        notify('ATTRIBUTE NAME ERROR: attribute name not found!')

    # * Insert user input into database
