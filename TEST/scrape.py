import sys
sys.path.append('/Users/drewskikatana/Regex/config')

from bs4 import BeautifulSoup
import requests
import psycopg2
import pandas as pd

#  My Modules
from config import config as cf


# * GONNA BE COME MAIN PROJECT

# TODO: Restructure code

# Inputs
URL = input('Input URL: ')
HTML_TAG = input('Input an HTML Tag: ')
CLASS_NAME = input('Input an classname: ')
FILENAME = input('Input Filename: ')
FILETYPE = input('Input File type: ')
FINDALL = input('Find all occurrences?[yes/no]: ')


# connection to database
CONN = psycopg2.connect(
        host = cf.hostname,
        dbname = cf.database,
        user = cf.username,
        password = cf.pwd,
        port = cf.port_id)


# Web scraping
results = requests.get(URL)
src = results.content
html = BeautifulSoup(src, 'lxml')
# results = html.find(f'{HTML_TAG}', f'{CLASS_NAME}')


if FINDALL == 'no':
    results = html.find(f'{HTML_TAG}', f'{CLASS_NAME}')
    results = results.get_text()
else:
    results = html.find_all(f'{HTML_TAG}', f'{CLASS_NAME}')
    
# If results are returned put results into a file
try:
    # put results to file
    if HTML_TAG == 'table':
        table = html.find_all('table', {'class': f'{CLASS_NAME}'})
        tables = pd.read_html(str(table))
        count = 1
        for table in tables:
            table = pd.DataFrame(table)
            table.to_excel( f'/Users/drewskikatana/Regex/TEST/TEST_RESULTS/{FILENAME}{count}.{FILETYPE}' )
            count += 1
            
            # Insert into database
            CUR = CONN.cursor() 
            INSERT_SCRIPT = 'insert into web_scraped_data (URL, file_name, results) values (%s, %s, %s);'
            INSERT_VALUES = (URL, FILENAME, str(tables))
            CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
            CONN.commit()
    else:
        text_file = open(f'/Users/drewskikatana/Regex/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}', 'w')
        text_file.write(str(results))
        text_file.close()

        # Insert into database
        CUR = CONN.cursor() 
        INSERT_SCRIPT = 'insert into web_scraped_data (URL, file_name, results) values (%s, %s, %s);'
        INSERT_VALUES = (URL, FILENAME, str(results))
        CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
        CONN.commit()
except AttributeError:
    print('Nothing was found: CHECK YOUR PARAMETERS!')




# ! ALL WAYS CLOSE CONNECTIONS
CUR.close()
CONN.close()



# links = table.findAll('a')
# for link in links:
#     urls.append(link)