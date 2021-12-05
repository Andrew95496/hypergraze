import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('config.py')))

from bs4 import BeautifulSoup
from numpy import byte
import requests
import psycopg2
import pandas as pd
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

downloads_path = str(Path.home() / "Downloads")

def find_all_tables_to_excel(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE):
    CONN = psycopg2.connect(
            host = cf.hostname,
            dbname = cf.database,
            user = cf.username,
            password = cf.pwd,
            port = cf.port_id)
    CUR = CONN.cursor()
    notify('HYPERGRAZE©', '(tables) database connected...')
    res = requests.get(URL)
    src = res.content
    html = BeautifulSoup(src, 'lxml')

    bytes = 0
    count = 1

    

    table = html.find_all('table', {'class': f'{ATTR_NAME}'})
    tables = pd.read_html(str(table))
    for table in tables:
        table = pd.DataFrame(table)
        table.to_excel( f'{downloads_path}/{FILENAME}{count}.xlsx')
        size = os.path.getsize(f'{downloads_path}/{FILENAME}{count}.xlsx')
        bytes += size
        count += 1
    
    mb.showinfo('Info', f'''All files sent to:\n {downloads_path}/\n
        file size: {bytes} bytes
        ''')

    #* Insert into database web_data
    INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE ,str(tables),bytes, datetime.datetime.now())
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    notify('HYPERGRAZE©', 'web_data entered')

    #* Insert into database web_data
    INSERT_SCRIPT = 'insert into user_data (url, html_tag, file_type, files, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, count, bytes, datetime.datetime.now() )
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    notify('HYPERGRAZE©', 'user_data entered')

    CONN.commit()
    # ! ALL WAYS CLOSE CONNECTIONS
    CUR.close()
    CONN.close()
    notify('HYPERGRAZE©', '(tables) database disconnected')








def find_all_tables_to_std(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE):
    CONN = psycopg2.connect(
            host = cf.hostname,
            dbname = cf.database,
            user = cf.username,
            password = cf.pwd,
            port = cf.port_id)
    CUR = CONN.cursor()
    notify('HYPERGRAZE©', '(tables) database connected...')

    res = requests.get(URL)
    src = res.content
    html = BeautifulSoup(src, 'lxml')

    bytes = 0
    count = 1

    table = html.find_all('table', {'class': f'{ATTR_NAME}'})
    tables = pd.read_html(str(table))
    for table in tables:
        with open(f'{downloads_path}/{FILENAME}{count}.{FILETYPE}', 'w') as text_file:
            text_file.write(str(table))
        size = os.path.getsize(f'{downloads_path}/{FILENAME}{count}.{FILETYPE}')
        bytes += size
        count += 1

    mb.showinfo('Info', f'''All files sent to:\n {downloads_path}/\n
        file size: {bytes} bytes
        ''')
    #* Insert into database
    INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(tables), bytes, datetime.datetime.now())
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    notify('HYPERGRAZE©', 'web_data entered')

    INSERT_SCRIPT = 'insert into user_data (url, html_tag, file_type, files, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, count, bytes, datetime.datetime.now() )
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    notify('HYPERGRAZE©', 'user_data entered')

    CONN.commit()

    # ! ALL WAYS CLOSE CONNECTIONS
    CUR.close()
    CONN.close()
    notify('HYPERGRAZE©', '(tables) database disconnected')




def find_one_table_to_std(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE):
    CONN = psycopg2.connect(
            host = cf.hostname,
            dbname = cf.database,
            user = cf.username,
            password = cf.pwd,
            port = cf.port_id)
    CUR = CONN.cursor()
    notify('HYPERGRAZE©', '(tables) database connected...')
    res = requests.get(URL)
    src = res.content
    html = BeautifulSoup(src, 'lxml')

    bytes = 0
    count = 1

    table = html.find('table', {'class': f'{ATTR_NAME}'})
    table = table.get_text()
    with open(f'{downloads_path}/{FILENAME}.{FILETYPE}', 'w') as text_file:
        text_file.write(str(table))
    size = os.path.getsize(f'{downloads_path}/{FILENAME}.{FILETYPE}')
    bytes += size

    mb.showinfo('Info', f'''file sent to:\n {downloads_path}/{FILENAME}.{FILETYPE}\n
        file size: {bytes} bytes
        ''')

    #* Insert into database
    INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(table), bytes, datetime.datetime.now())
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    notify('HYPERGRAZE©', 'web_data entered')

    INSERT_SCRIPT = 'insert into user_data (url, html_tag, file_type, files, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, count, bytes, datetime.datetime.now() )
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    notify('HYPERGRAZE©', 'user_data entered')

    CONN.commit()
    # ! ALL WAYS CLOSE CONNECTIONS
    CUR.close()
    CONN.close()
    notify('HYPERGRAZE©', '(tables) database disconnected')




def find_one_table_to_excel(URL,HTML_TAG, ATTR_NAME, FILENAME, FILETYPE):
    CONN = psycopg2.connect(
            host = cf.hostname,
            dbname = cf.database,
            user = cf.username,
            password = cf.pwd,
            port = cf.port_id)
    CUR = CONN.cursor()
    notify('HYPERGRAZE©', '(tables) database connected...')
    res = requests.get(URL)
    src = res.content
    html = BeautifulSoup(src, 'lxml')

    notify('HYPERGRAZE©', 'grazing the web...')

    bytes = 0
    count = 1

    table = html.find('table', {'class': f'{ATTR_NAME}'})
    table = pd.read_html(str(table))
    table = pd.DataFrame(table[0])
    table.to_excel( f'{downloads_path}/{FILENAME}.xlsx' )
    bytes = os.path.getsize(f'{downloads_path}/{FILENAME}.{FILETYPE}')

    mb.showinfo('Info', f'''file sent to:\n {downloads_path}/{FILENAME}.{FILETYPE}\n
        file size: {bytes} bytes
        ''')
    #* Insert into database
    INSERT_SCRIPT = 'insert into web_data (url, html_tag, file_type, results, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, str(table), bytes, datetime.datetime.now())
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    notify('HYPERGRAZE©', 'web_data entered')

    INSERT_SCRIPT = 'insert into user_data (url, html_tag, file_type, files, bytes, date) values (%s, %s, %s, %s, %s, %s);'
    INSERT_VALUES = (URL, HTML_TAG, FILETYPE, count, bytes, datetime.datetime.now() )
    CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
    notify('HYPERGRAZE©', 'user_data entered')


    CONN.commit()
    
    # ! ALL WAYS CLOSE CONNECTIONS
    CUR.close()
    CONN.close()
    notify('HYPERGRAZE©', '(tables) database disconnected')

