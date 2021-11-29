from bs4 import BeautifulSoup
import requests
import psycopg2
import pandas as pd
import datetime
import os
#  My Modules
from configs import config as cf



def find_data(URL,HTML_TAG, CLASS_NAME, FILENAME, FILETYPE, FINDALL ):
    # connection to database
    CONN = psycopg2.connect(
            host = cf.hostname,
            dbname = cf.database,
            user = cf.username,
            password = cf.pwd,
            port = cf.port_id)

    print('database connected...')
    count = 1
    # Web scraping
    res = requests.get(URL)
    src = res.content
    html = BeautifulSoup(src, 'lxml')

    print('grazing the web...')

    CUR = CONN.cursor() 

    # * SEARCHING, WRITING, AND DATABASING FILE 
    if HTML_TAG != 'table':
        try:
            if (FINDALL == 'no') and (HTML_TAG != 'table'):
                results = html.find(f'{HTML_TAG}', f'{CLASS_NAME}')
                results = results.get_text()
                
            else:
                results = html.find_all(f'{HTML_TAG}', f'{CLASS_NAME}')
                results = results[0]
                results = results.get_text()
                


            text_file = open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}', 'w')
            text_file.write(str(results))
            size = os.path.getsize(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}')
            text_file.close()

            # Insert into database
            INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, date) values (%s, %s, %s, %s, %s);'
            INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(results), datetime.datetime.now())
            CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
        except Exception:
            Exception
    else:

        try:
            # FIND ALL TABLES IN URL AND WRITE TO EXCEL FILE
            if (FINDALL != 'no') and (FILETYPE == 'xlsx'):
                table = html.find_all('table', {'class': f'{CLASS_NAME}'})
                tables = pd.read_html(str(table))
                bytes = 0
                for table in tables:
                    table = pd.DataFrame(table)
                    table.to_excel( f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}{count}.xlsx' )
                    size = os.path.getsize(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}{count}.xlsx')
                    bytes += size
                    count += 1
                # Insert into database
                INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, date) values (%s, %s, %s, %s, %s);'
                INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(tables), datetime.datetime.now())
                CUR.execute(INSERT_SCRIPT, INSERT_VALUES)

            # FIND ALL TABLES IN URL AND WRITE TO ANY FILE
            elif (FINDALL != 'no') and (FILETYPE != 'xlsx'):
                table = html.find_all('table', {'class': f'{CLASS_NAME}'})
                tables = pd.read_html(str(table))
                for table in tables:
                    text_file = open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}{count}.{FILETYPE}', 'w')
                    text_file.write(str(table))
                    text_file.close()
                    count += 1

                # Insert into database
                INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, date) values (%s, %s, %s, %s, %s);'
                INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(tables), datetime.datetime.now())
                CUR.execute(INSERT_SCRIPT, INSERT_VALUES)

            # FIND FIRST TABLES IN URL AND WRITE TO ANY FILE
            elif (FINDALL == 'no') and (FILETYPE != 'xlsx'):
                table = html.find('table', {'class': f'{CLASS_NAME}'})
                table = table.get_text()
                text_file = open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}', 'w')
                text_file.write(str(table))
                text_file.close()

                # Insert into database
                INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, date) values (%s, %s, %s, %s, %s);'
                INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(table), datetime.datetime.now())
                CUR.execute(INSERT_SCRIPT, INSERT_VALUES)

            # FIND FIRST TABLES IN URL AND WRITE TO EXCEL FILE    
            else:
                table = html.find('table', {'class': f'{CLASS_NAME}'})
                table = pd.read_html(str(table))
                table = pd.DataFrame(table[0])
                table.to_excel( f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.xlsx' )

                # Insert into database
                INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, date) values (%s, %s, %s, %s, %s);'
                INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(table), datetime.datetime.now())
                CUR.execute(INSERT_SCRIPT, INSERT_VALUES)

        except AttributeError:
            print('Nothing was found: CHECK YOUR PARAMETERS!')


    #* Insert user input into database
    INSERT_SCRIPT = 'insert into user_data (url, html_tag, file_type, files, size, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, count, size, datetime.datetime.now() )
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)


    CONN.commit()

    # ! ALL WAYS CLOSE CONNECTIONS
    CUR.close()
    CONN.close()

    print('SUCCESS!')
we