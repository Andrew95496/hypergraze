from requests.api import get
from reg import find_data


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

URL = Entry(root, width=28)
HTML_TAG = Entry(root, width=28)
CLASS_NAME = Entry(root, width=28)
FILENAME = Entry(root, width=28)
FILETYPE = Entry(root, width=28)
FINDALL = Entry(root, width=28)

search = Button(root, text="Search",
command=lambda: find_data(URL.get(), HTML_TAG.get(), CLASS_NAME.get(), FILENAME.get(), FILETYPE.get(), FINDALL.get()))

URL.pack()
HTML_TAG.pack()
CLASS_NAME.pack()
FILENAME.pack()
FILETYPE.pack()
FINDALL.pack()
search.pack()

ttk.Button(text="Quit", command=root.destroy).pack()


root.mainloop()