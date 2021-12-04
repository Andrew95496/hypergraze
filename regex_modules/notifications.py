import subprocess
from regex import attr_name_exist

CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''

def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text])



from tkinter import messagebox as mb


attr_name_exist('https://www.bjjheroes.com/bjj-fighters/', 'class', 'rcow')