import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('config.py')))

from bs4 import BeautifulSoup
from numpy import byte
import requests
import psycopg2
import pandas as pd
import datetime
#  My Modules
from configs import config as cf





CONN = psycopg2.connect(
        host = cf.hostname,
        dbname = cf.database,
        user = cf.username,
        password = cf.pwd,
        port = cf.port_id)
CUR = CONN.cursor()
print('(std) database connected...')


def get_std_data(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE, FINDALL):

    

    res = requests.get(URL)
    src = res.content
    html = BeautifulSoup(src, 'lxml')

    print('grazing the web...')

    count = 1
    bytes = 0
    
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
    print('web_data entered')

    INSERT_SCRIPT = 'insert into user_data (url, html_tag, file_type, files, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, count, bytes, datetime.datetime.now() )
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    print('user_data entered')


    CONN.commit()
    # ! ALL WAYS CLOSE CONNECTIONS
    CUR.close()
    CONN.close()
    print('(std) database disconnected')