from bs4 import BeautifulSoup
from numpy import byte
import requests
import psycopg2
import pandas as pd
import datetime
import os
#  My Modules
from configs import config as cf
from regex import classname_exist



def find_data(URL,HTML_TAG, ATTRIBUTE, ATTR_NAME, FILENAME, FILETYPE, FINDALL ):

    CONN = psycopg2.connect(
                host = cf.hostname,
                dbname = cf.database,
                user = cf.username,
                password = cf.pwd,
                port = cf.port_id)
    CUR = CONN.cursor()
    print('database connected...')


    count = 1
    bytes = 0
    if classname_exist(URL, ATTRIBUTE, ATTR_NAME):
        # connection to database
        print('class found')
        # Web scraping
        res = requests.get(URL)
        src = res.content
        html = BeautifulSoup(src, 'lxml')

        print('grazing the web...')
# !##############################################################################################################
        # * SEARCHING, WRITING, AND DATABASING FILE 
        if FILETYPE == 'html':
            if (FINDALL == 'no'):
                results = html.find(f'{HTML_TAG}', f'{ATTR_NAME}')


            elif (FINDALL != 'no'):
                results = html.find_all(f'{HTML_TAG}', f'{ATTR_NAME}')

            with open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}', 'w') as text_file:
                text_file.write(str(results))

            bytes = os.path.getsize(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}')
            # Insert into database
            INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, bytes, date) values (%s, %s, %s, %s, %s, %s);'
            INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(results), bytes, datetime.datetime.now())
            CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
# !##############################################################################################################
        elif HTML_TAG != 'table':
            if (FINDALL == 'no'):
                results = html.find(f'{HTML_TAG}', f'{ATTR_NAME}')
                results = results.get_text()
            else:
                results = html.find_all(f'{HTML_TAG}', f'{ATTR_NAME}')
                results = results[0]
                results = results.get_text()
            with open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}', 'w') as text_file:
                text_file.write(str(results))
            bytes = os.path.getsize(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}')
            # Insert into database
            INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, bytes, date) values (%s, %s, %s, %s, %s, %s);'
            INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(results), bytes, datetime.datetime.now())
            CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
# !##############################################################################################################
        else:
            # FIND ALL TABLES IN URL AND WRITE TO EXCEL FILE
            if (FINDALL != 'no') and (FILETYPE == 'xlsx'):
                table = html.find_all('table', {'class': f'{ATTR_NAME}'})
                tables = pd.read_html(str(table))
                for table in tables:
                    table = pd.DataFrame(table)
                    table.to_excel( f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}{count}.xlsx' )
                    size = os.path.getsize(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}{count}.xlsx')
                    bytes += size
                    count += 1
                #* Insert into database
                INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, bytes, date) values (%s, %s, %s, %s, %s, %s);'
                INSERT_VALUES = (URL, HTML_TAG, FILETYPE ,str(tables),bytes, datetime.datetime.now())
                CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
            # FIND ALL TABLES IN URL AND WRITE TO ANY FILE
            elif (FINDALL != 'no') and (FILETYPE != 'xlsx'):
                table = html.find_all('table', {'class': f'{ATTR_NAME}'})
                tables = pd.read_html(str(table))
                for table in tables:
                    with open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}{count}.{FILETYPE}', 'w') as text_file:
                        text_file.write(str(table))
                    size = os.path.getsize(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}{count}.{FILETYPE}')
                    bytes += size
                    count += 1
                #* Insert into database
                INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, bytes, date) values (%s, %s, %s, %s, %s, %s);'
                INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(tables), bytes, datetime.datetime.now())
                CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
            # FIND FIRST TABLES IN URL AND WRITE TO ANY FILE
            elif (FINDALL == 'no') and (FILETYPE != 'xlsx'):
                table = html.find('table', {'class': f'{ATTR_NAME}'})
                table = table.get_text()
                with open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}', 'w') as text_file:
                    text_file.write(str(table))
                size = os.path.getsize(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}')
                bytes += size
                #* Insert into database
                INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, bytes, date) values (%s, %s, %s, %s, %s, %s);'
                INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(table), bytes, datetime.datetime.now())
                CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
            # FIND FIRST TABLES IN URL AND WRITE TO EXCEL FILE    
            else:
                table = html.find('table', {'class': f'{ATTR_NAME}'})
                table = pd.read_html(str(table))
                table = pd.DataFrame(table[0])
                table.to_excel( f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.xlsx' )
                bytes = os.path.getsize(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}')
                #* Insert into database
                INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, bytes, date) values (%s, %s, %s, %s, %s, %s);'
                INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(table), bytes, datetime.datetime.now())
                CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    else:
        print('CLASSNAME ERROR: class does not exist')

# !##############################################################################################################
    #* Insert user input into database
    INSERT_SCRIPT = 'insert into user_data (url, html_tag, file_type, files, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, count, bytes, datetime.datetime.now() )
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)


    CONN.commit()

    # ! ALL WAYS CLOSE CONNECTIONS
    CUR.close()
    CONN.close()

    print('user_data entered')
