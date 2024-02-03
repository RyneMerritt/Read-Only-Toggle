import tkinter as tk
import os
import glob
import stat
import keyboard

Ticker = 0
list_of_files = glob.glob(r'C:\Users\rynej\Documents\dataset examples\*')
latest_file = max(list_of_files, key=os.path.getctime)

r = tk.Tk()
frame = tk.Frame(master=r, width=500, height=300)
frame.pack()

label1 = tk.Label(master=frame, text="Press the key you would like to bind to the read only command!", bg="red")
label1.place(x=0, y=0)

def handle_keypress(event):
    keyBind = event.char
    keyboard.add_hotkey(keyBind, lambda: Change())
    keyboard.wait()

def Change():
    global Ticker
    Ticker += 1
    choice = Ticker % 2
    if choice == 1:
        os.chmod(latest_file, stat.S_IREAD)
    elif choice == 0:
        os.chmod(latest_file, stat.S_IWRITE)




r.mainloop()