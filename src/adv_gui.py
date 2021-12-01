# from find_data import find_data
from __TEST import find_data


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
'sql',
'eml',
'html',
'css',
'py',
'js',
'c',
'cpp',
'swift',
'tex'
] 

HTML_TAG_OPTIONS = [
'html',
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
'table',
'th',
'tr',
'td',
'span',
'rel',
'name',
'content',
] 

ATTR_OPTIONS = [
'id',
'class',
'src',
'href',
'alt',
'lang',
'style',
'title',
] 





_FILETYPE = StringVar(root)
_FILETYPE.set(FILETYPE_OPTIONS[0]) 

_HTML_TAG = StringVar(root)
_HTML_TAG.set(HTML_TAG_OPTIONS[0]) 

_ATTR = StringVar(root)
_ATTR.set(ATTR_OPTIONS[0]) 






URL = Entry(root, width=28)
HTML_TAG = OptionMenu(root, _HTML_TAG, *HTML_TAG_OPTIONS)
ATTR = OptionMenu(root, _ATTR, *ATTR_OPTIONS)
CLASS_NAME = Entry(root, width=28)
FILENAME = Entry(root, width=28)
FILETYPE = OptionMenu(root, _FILETYPE, *FILETYPE_OPTIONS)
FINDALL = Entry(root, width=28)

search = Button(root, text="Search",
command=lambda: find_data(URL.get(), _HTML_TAG.get(), _ATTR.get(),CLASS_NAME.get(), FILENAME.get(), _FILETYPE.get(), FINDALL.get()))






URL.pack()
HTML_TAG.pack()
ATTR.pack()
CLASS_NAME.pack()
FILENAME.pack()
FILETYPE.pack()
FINDALL.pack()
search.pack()

ttk.Button(text="Quit", command=root.destroy).pack()


root.mainloop()