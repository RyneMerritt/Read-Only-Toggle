import os
import glob
from tkinter import *
import stat
import keyboard

Ticker = 0
list_of_files = glob.glob(r'C:\Users\rynej\Documents\dataset examples\*')
latest_file = max(list_of_files, key=os.path.getctime)

keyBind = input("What key would you like to set to enable/disable the read-only?")

File = r"C:\Users\rynej\Documents\dataset examples\example.txt"

def Change():
    global Ticker
    Ticker += 1
    choice = Ticker % 2
    if choice == 1:
        print("The file is now read only!")
        os.chmod(latest_file, stat.S_IREAD)
    elif choice == 0:
        print("The file is now NOT read only!")
        os.chmod(latest_file, stat.S_IWRITE)

keyboard.add_hotkey(keyBind, lambda: Change())
keyboard.wait()