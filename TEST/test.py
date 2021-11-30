# import os
# # import pandas as pd

# # file = '/Users/drewskikatana/Regex/TEST/TEST_RESULTS/find_all.csv'
# # file2 = '/Users/drewskikatana/Regex/TEST/scrape.py'
# # file3 = '/Users/drewskikatana/Regex/README.md'
# # data = '/Users/drewskikatana/Regex/TEST/TEST_RESULTS/file.txt'

# # file_sizes = []

# # size = os.path.getsize(data)


# # file_sizes.append(size)

# # df = pd.DataFrame(file_sizes)

# # print(df)

# # x = '''
# #     In this program, we will try to convert a given string
# #     to a list, where spaces or any other special characters,
# #     according to the users choice, are encountered. To do 
# #     this we use the split() method.
# #     '''

# # x = x.split()

# # print(x)

# FILENAME = '______a'
# FILETYPE = 'docx'


# with open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/{FILENAME}.{FILETYPE}', 'w') as text_file:
#     text_file.write(FILENAME)
from bs4 import BeautifulSoup
from numpy import byte
import requests
import psycopg2
import pandas as pd
import datetime
import os

URL = 'https://en.wikipedia.org/wiki/National_Football_League'

res = requests.get(URL)
src = res.content
html = BeautifulSoup(src, 'lxml')
results = html.find( 'table', 'wikitable')
print(results)

with open(f'/Users/drewskikatana/hypergraze/TEST/TEST_RESULTS/nfl___________html.html', 'w') as text_file:
    text_file.write(str(results))
