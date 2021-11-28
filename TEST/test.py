from bs4 import BeautifulSoup
import requests
import psycopg2



# Inputs
URL = input('Input URL: ')
HTML_TAG = input('Input an HTML Tag: ')
CLASS_NAME = input('Input an classname: ')
FILENAME = input('Input Filename: ')
# FINDALL = input('Find all occurrences?[yes/no]: ')


# connection to database
CONN = psycopg2.connect(
        host = '#########',
        dbname = '####',
        user = '########',
        password = '########',
        port = ####)


# Web scraping
results = requests.get(URL)
src = results.content
html = BeautifulSoup(src, 'lxml')
results = html.find(f'{HTML_TAG}', f'{CLASS_NAME}')

# TODO: make the find_all work

# if FINDALL == 'no':
#     results = html.find(f'{HTML_TAG}', f'{CLASS_NAME}')
# else:
#     results = html.find_all(f'{HTML_TAG}', f'{CLASS_NAME}')


# If results are returned put results into a file
try:
    results = results.get_text()
    print(results)

    # put results to file
    text_file = open(f'/Users/drewskikatana/Regex/TEST/TEST_RESULTS{FILENAME}.numbers', 'w')
    text_file.write(str(results))
    text_file.close()
except AttributeError:
    print('Nothing was found: CHECK YOUR PARAMETERS!')


# Insert into database
CUR = CONN.cursor() 
INSERT_SCRIPT = 'insert into web_scraped_data (URL, file_name, results) values (%s, %s, %s);'
INSERT_VALUES = (URL, FILENAME, results)
CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
CONN.commit()

# ! ALL WAYS CLOSE CONNECTIONS
CUR.close()
CONN.close()



# links = table.findAll('a')
# for link in links:
#     urls.append(link)
