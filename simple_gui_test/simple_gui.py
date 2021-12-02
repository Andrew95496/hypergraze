# from find_data import find_data
from simple_params import find_data


from tkinter import *
from tkinter import ttk


# URL = input('Input URL: ')
# HTML_TAG = input('Input an HTML Tag: ')
# CLASS_NAME = input('Input an classname: ')
# FILENAME = input('Input Filename: ')
# FILETYPE = input('Input File type: ')
# FINDALL = input('Find all occurrences?[yes/no]: ')


root = Tk()
root.title('Hypergraze')
root.state("zoomed")

#* DROPDOWN MENUS
FILETYPE_OPTIONS = [
'csv',
'xlsx',
'xls',
'txt',
'zip',
'eml',
]  

HTML_TAG_OPTIONS = [
'body',
'title',
'main',
'section',
'article',
'h1',
'h2',
'h3',
'h4',
'h5',
'h6',
'p',
'div',
'a',
'ul',
'ol',
'li',
'span'
]


_FILETYPE = StringVar(root)
_FILETYPE.set(FILETYPE_OPTIONS[0]) 

_HTML_TAG = StringVar(root)
_HTML_TAG.set(HTML_TAG_OPTIONS[0]) 



URL = Entry(root, width=28)
HTML_TAG = OptionMenu(root, _HTML_TAG, *HTML_TAG_OPTIONS)
FILENAME = Entry(root, width=28)
FILETYPE = OptionMenu(root, _FILETYPE, *FILETYPE_OPTIONS)
FINDALL = Entry(root, width=28)

search = Button(root, text="Search",
command=lambda: find_data(URL.get(), _HTML_TAG.get(), FILENAME.get(), _FILETYPE.get(), FINDALL.get()))






URL.pack()
HTML_TAG.pack()
FILENAME.pack()
FILETYPE.pack()
FINDALL.pack()
search.pack()

ttk.Button(text="Quit", command=root.destroy).pack()


root.mainloop()