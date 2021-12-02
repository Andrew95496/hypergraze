import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('config.py')))

from bs4 import BeautifulSoup
import requests
import psycopg2
import pandas as pd
import datetime

#  My Modules
from configs import config as cf









def get_html(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE, FINDALL):
    CONN = psycopg2.connect(
        host = cf.hostname,
        dbname = cf.database,
        user = cf.username,
        password = cf.pwd,
        port = cf.port_id)
    CUR = CONN.cursor()
    print('(web) database connected...')
    res = requests.get(URL)
    src = res.content
    html = BeautifulSoup(src, 'lxml')
    print('grazing the web...')

    bytes = 0
    count = 1
    


    # Finding all instances of HTML_TAG
    if (FINDALL == 'no'):
        results = html.find(f'{HTML_TAG}', f'{ATTR_NAME}')

    # finding one instances of HTML_TAG
    elif (FINDALL != 'no'):
        results = html.find_all(f'{HTML_TAG}', f'{ATTR_NAME}')

    with open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}', 'w') as text_file:
            text_file.write(str(results))

    # getting bytes for the file
    bytes = os.path.getsize(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}')

    # Insert into database web_data
    INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(results), bytes, datetime.datetime.now())
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    print('web_data entered')

    # Insert into database user_data
    INSERT_SCRIPT = 'insert into user_data (url, html_tag, file_type, files, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, count, bytes, datetime.datetime.now() )
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    print('user_data entered')

    CONN.commit()
    # ! ALL WAYS CLOSE CONNECTIONS
    CUR.close()
    CONN.close()
    print('(web) database disconnected')    

