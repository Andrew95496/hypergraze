# from find_data import find_data
from find_data import find_data


from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk



#STYLES
#colors
main_color = '#FAF6F5'
fire_red = '#C90E27'
fire_rose = '#F2556A'


root = Tk()
style = Style(theme='journal')
root.title('Hypergraze')
root.configure(background=f'{main_color}')
root.geometry('400x350')
root.resizable(width=0, height=0)

Logo = Image.open('/Users/drewskikatana/hypergraze/hypergrazesite/STATIC_MEDIA/LOGO_FILES/main-logo-transparent.png')
Logo = Logo.resize((100, 100), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(Logo)
main_logo = Label(image=logo, bg='#FAF6F5')
main_logo.place(x=5, y=250)


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

main_title = Label(root, text="HYPERGRAZE", fg=f'{fire_rose}',bg=f'{main_color}', font=('Ariel', 20))
main_title.pack()

URL_label = Label(root, text='URL', fg=f'{fire_rose}',bg=f'{main_color}')
URL_label.pack()
URL = ttk.Entry(root, width=35)
URL.pack()


HTML_label = Label(root, text='HTML TAG', fg=f'{fire_rose}',bg=f'{main_color}')
HTML_label.place(x=97, y=75)
_HTML_TAG = StringVar(root)
_HTML_TAG.set(HTML_TAG_OPTIONS[0])
HTML_TAG = ttk.OptionMenu(root, _HTML_TAG, *HTML_TAG_OPTIONS)
HTML_TAG.config(width=5)
HTML_TAG.place(x=88, y=90)


ATTR_label = Label(root, text='ATTRIBUTE',  fg=f'{fire_rose}',bg=f'{main_color}')
ATTR_label.place(x=243, y=75)
_ATTR = StringVar(root)
_ATTR.set(ATTR_OPTIONS[0]) 
ATTR = ttk.OptionMenu(root, _ATTR, *ATTR_OPTIONS)
ATTR.config(width=5)
ATTR.place(x=233, y=90)


ATTR_NAME_label = Label(root, text='ATTRIBUTE NAME', fg=f'{fire_rose}',bg=f'{main_color}')
ATTR_NAME_label.place(x=150, y=120)
ATTR_NAME = ttk.Entry(root, width=35)
ATTR_NAME.place(x=88, y=140)


FILENAME_label = Label(root, text='FILENAME & FILETYPE', fg=f'{fire_rose}',bg=f'{main_color}')
FILENAME_label.place(x=138, y=170)
FILENAME = ttk.Entry(root, width=25)
FILENAME.place(x=88, y=190)

_FILETYPE = StringVar(root)
_FILETYPE.set(FILETYPE_OPTIONS[0])
FILETYPE = ttk.OptionMenu(root, _FILETYPE, *FILETYPE_OPTIONS)
FILETYPE.place(x=247, y=190)


FINDALL_label = Label(root, text='FINDALL [yes/no]', fg=f'{fire_rose}',bg=f'{main_color}')
FINDALL_label.place(x=150, y=215)
FINDALL = ttk.Entry(root, width=35)
FINDALL.place(x=88, y=235)

search = ttk.Button(root, text="Graze",
command=lambda: find_data(URL.get(), _HTML_TAG.get(), _ATTR.get(), ATTR_NAME.get(), FILENAME.get(), _FILETYPE.get(), FINDALL.get()))
search.place(x=170, y=270)

ttk.Button(text="Quit", command=root.destroy).place(x=325, y=300)

root.mainloop()