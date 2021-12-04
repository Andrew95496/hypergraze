# from bs4 import BeautifulSoup
# import requests
# import psycopg2
# import pandas as pd

# #  My Modules
# from configs import config as cf


# # * GONNA BE COME MAIN PROJECT or ADVANCED SETTINGS PAGE

# # TODO: Restructure code

# # Inputs
# URL = input('Input URL: ')
# HTML_TAG = input('Input an HTML Tag: ')
# CLASS_NAME = input('Input an classname: ')
# FILENAME = input('Input Filename: ')
# FILETYPE = input('Input File type: ')
# FINDALL = input('Find all occurrences?[yes/no]: ')


# # connection to database
# CONN = psycopg2.connect(
#         host = cf.hostname,
#         dbname = cf.database,
#         user = cf.username,
#         password = cf.pwd,
#         port = cf.port_id)


# # Web scraping
# res = requests.get(URL)
# src = res.content
# html = BeautifulSoup(src, 'lxml')

# # * SEARCHING FOR TABLES
# if HTML_TAG == 'table':
#     try:
#         # FIND ALL TABLES IN URL AND WRITE TO EXCEL FILE
#         if (FINDALL != 'no') and (FILETYPE == 'xlsx'):
#             table = html.find_all('table', {'class': f'{CLASS_NAME}'})
#             tables = pd.read_html(str(table))
#             count = 1
#             for table in tables:
#                 table = pd.DataFrame(table)
#                 table.to_excel( f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}{count}.xlsx' )
#                 count += 1
#             # Insert into database
#             CUR = CONN.cursor() 
#             INSERT_SCRIPT = 'insert into web_scraped_data (URL, file_name, results) values (%s, %s, %s);'
#             INSERT_VALUES = (URL, FILENAME, str(tables))
#             CUR.execute(INSERT_SCRIPT, INSERT_VALUES)

#         # FIND ALL TABLES IN URL AND WRITE TO ANY FILE
#         elif (FINDALL != 'no') and (FILETYPE != 'xlsx'):
#             table = html.find_all('table', {'class': f'{CLASS_NAME}'})
#             tables = pd.read_html(str(table))
#             count = 1
#             for table in tables:
#                 text_file = open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}{count}.{FILETYPE}', 'w')
#                 text_file.write(str(table))
#                 text_file.close()
#                 count += 1

#             # Insert into database
#             CUR = CONN.cursor() 
#             INSERT_SCRIPT = 'insert into web_scraped_data (URL, file_name, results) values (%s, %s, %s);'
#             INSERT_VALUES = (URL, FILENAME, str(tables))
#             CUR.execute(INSERT_SCRIPT, INSERT_VALUES)

#         # FIND FIRST TABLES IN URL AND WRITE TO ANY FILE
#         elif (FINDALL == 'no') and (FILETYPE != 'xlsx'):
#             table = html.find('table', {'class': f'{CLASS_NAME}'})
#             table = table.get_text()
#             text_file = open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}', 'w')
#             text_file.write(str(table))
#             text_file.close()

#             # Insert into database
#             CUR = CONN.cursor() 
#             INSERT_SCRIPT = 'insert into web_scraped_data (URL, file_name, results) values (%s, %s, %s);'
#             INSERT_VALUES = (URL, FILENAME, str(table))
#             CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
            
#         # FIND FIRST TABLES IN URL AND WRITE TO EXCEL FILE    
#         else:
#             table = html.find('table', {'class': f'{CLASS_NAME}'})
#             table = pd.read_html(str(table))
#             table = pd.DataFrame(table[0])
#             table.to_excel( f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.xlsx' )

#             # Insert into database
#             CUR = CONN.cursor() 
#             INSERT_SCRIPT = 'insert into web_scraped_data (URL, file_name, results) values (%s, %s, %s);'
#             INSERT_VALUES = (URL, FILENAME, str(table))
#             CUR.execute(INSERT_SCRIPT, INSERT_VALUES)

#     except AttributeError:
#         print('Nothing was found: CHECK YOUR PARAMETERS!')



# CONN.commit()

# # ! ALL WAYS CLOSE CONNECTIONS
# CUR.close()
# CONN.close()



# # links = table.findAll('a')
# # for link in links:
# # urls.append(link)

# # # * SEARCHING, WRITING, AND DATABASING FILE 
# # if HTML_TAG != 'table':
# #     try:
# #         if (FINDALL == 'no') and (HTML_TAG != 'table'):
# #             results = html.find(f'{HTML_TAG}', f'{CLASS_NAME}')
# #             results = results.get_text()
# #         else:
# #             results = html.find_all(f'{HTML_TAG}', f'{CLASS_NAME}')

# #         text_file = open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}', 'w')
# #         text_file.write(str(results))
# #         text_file.close()

# #         # Insert into database
# #         CUR = CONN.cursor() 
# #         INSERT_SCRIPT = 'insert into web_scraped_data (URL, file_name, results) values (%s, %s, %s);'
# #         INSERT_VALUES = (URL, FILENAME, str(results))
# #         CUR.execute(INSERT_SCRIPT, INSERT_VALUES)
# #     except Exception:
# #         print(Exception)