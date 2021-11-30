import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('config.py')))
#  My Modules
from configs import config as cf
from tables import find_all_tables_to_excel, find_all_tables_to_std, find_one_table_to_std, find_one_table_to_excel
from web import get_html
from regex import classname_exist
from standard import get_std_data



def find_data(URL,HTML_TAG, ATTRIBUTE, ATTR_NAME, FILENAME, FILETYPE, FINDALL ):

    # CONN = psycopg2.connect(
    #             host = cf.hostname,
    #             dbname = cf.database,
    #             user = cf.username,
    #             password = cf.pwd,
    #             port = cf.port_id)
    # CUR = CONN.cursor()
    # print('database connected...')

    if classname_exist(URL, ATTRIBUTE, ATTR_NAME):
        print('class found')

        # # Web scraping
        # res = requests.get(URL)
        # src = res.content
        # html = BeautifulSoup(src, 'lxml')

        # print('grazing the web...')
        # * SEARCHING, WRITING, AND DATABASING FILE 
        if FILETYPE == 'html':
            get_html(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE, FINDALL)


        elif HTML_TAG != 'table':
            get_std_data(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE, FINDALL)


        else:
            # FIND ALL TABLES IN URL AND WRITE TO EXCEL FILE
            if (FINDALL != 'no') and (FILETYPE == 'xlsx'):
                find_all_tables_to_excel(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE)


            # FIND ALL TABLES IN URL AND WRITE TO ANY FILE
            elif (FINDALL != 'no') and (FILETYPE != 'xlsx'):
                find_all_tables_to_std(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE)


            # FIND FIRST TABLES IN URL AND WRITE TO ANY FILE
            elif (FINDALL == 'no') and (FILETYPE != 'xlsx'):
                find_one_table_to_std(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE)


            # FIND FIRST TABLES IN URL AND WRITE TO EXCEL FILE
            else:
                find_one_table_to_excel(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE)
    else:
        print('CLASSNAME ERROR: class does not exist')

    #* Insert user input into database
    
