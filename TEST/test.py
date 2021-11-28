import os
import pandas as pd

file = '/Users/drewskikatana/Regex/TEST/TEST_RESULTS/find_all.csv'
file2 = '/Users/drewskikatana/Regex/TEST/scrape.py'
file3 = '/Users/drewskikatana/Regex/README.md'
data = '/Users/drewskikatana/Regex/TEST/TEST_RESULTS/aaa.xlsx'

size = os.path.getsize(data)


df = pd.read_excel(data)

print(size)