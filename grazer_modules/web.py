import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('config.py')))

from bs4 import BeautifulSoup
import requests
import psycopg2
import datetime
import subprocess
from pathlib import Path
from tkinter import messagebox as mb


#  My Modules
from configs import config as cf






CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''

def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text])


def get_html(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE, FINDALL):
    CONN = psycopg2.connect(
        host = cf.hostname,
        dbname = cf.database,
        user = cf.username,
        password = cf.pwd,
        port = cf.port_id)
    CUR = CONN.cursor()
    notify('HYPERGRAZE©', '(web) database connected...')
    res = requests.get(URL)
    src = res.content
    html = BeautifulSoup(src, 'lxml')
    notify('HYPERGRAZE©', 'grazing the web...')

    bytes = 0
    count = 1
    
    downloads_path = str(Path.home() / "Downloads")

    # Finding all instances of HTML_TAG
    if (FINDALL == 'no'):
        results = html.find(f'{HTML_TAG}', f'{ATTR_NAME}')

    # finding one instances of HTML_TAG
    elif (FINDALL != 'no'):
        results = html.find_all(f'{HTML_TAG}', f'{ATTR_NAME}')

    with open(f'{downloads_path}/{FILENAME}.{FILETYPE}', 'w') as text_file:
            text_file.write(str(results))

    # getting bytes for the file
    bytes = os.path.getsize(f'{downloads_path}/{FILENAME}.{FILETYPE}')

    mb.showinfo('Info', f'''file sent to:\n {downloads_path}/{FILENAME}.{FILETYPE}\n
        file size: {bytes} bytes
        ''')
        
    # Insert into database web_data
    INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(results), bytes, datetime.datetime.now())
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    notify('HYPERGRAZE©', 'web_data entered')

    # Insert into database user_data
    INSERT_SCRIPT = 'insert into user_data (url, html_tag, file_type, files, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, count, bytes, datetime.datetime.now() )
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    notify('HYPERGRAZE©', 'user_data entered')

    CONN.commit()
    # ! ALL WAYS CLOSE CONNECTIONS
    CUR.close()
    CONN.close()
    notify('HYPERGRAZE©', '(web) database disconnected')    


