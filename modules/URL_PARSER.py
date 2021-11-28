from bs4 import BeautifulSoup
import requests
import psycopg2
from config import config as cf


def get_text():
    try:
        URL = input('Type URL: ')
        results = requests.get(URL)
        src = results.content
        html = BeautifulSoup(src, 'lxml')
        text = html.get_text()
    except Exception as error:
        print(f'{error}')
    CONN = None
    CUR = None

    try:
        CONN = psycopg2.connect(
            host = cf.hostname,
            dbname = cf.database,
            user = cf.username,
            password = cf.pwd,
            port = cf.port_id)
        
        # cursor
        CUR = CONN.cursor()  
        #queries
        INSERT_SCRIPT = 'insert into parsed_urls (URL, text) values ( %s, %s);'
        INSERT_VALUES = (URL, text.strip())

        CUR.execute(INSERT_SCRIPT, INSERT_VALUES)

        
        
        
        
        CONN.commit()
        
    except Exception as error:
        print(error)
    finally:
        # ! ALWAYS CLOSE CONNECTIONS
        if CUR is not None:
            CUR.close()
        if CONN is not None:
            CONN.close()
            
    return text