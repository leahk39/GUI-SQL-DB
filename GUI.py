"""
This module is for the GUI for the database and app
"""


# imports
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
import database


# GUI creation
root = tk.Tk()
root.title("Record Store")
root.geometry('1024x664')





# creating the background image
photo = Image.open("recordStore.jpg")
photo = photo.resize((1024, 664), Image.LANCZOS)
photo = ImageTk.PhotoImage(photo)


# creating a label to show the image
label = tk.Label(root, image=photo)
label.pack()


textLable1 = tk.Label(root,text=" ",
                 font=('Arial', 10))
textLable1.place(x=1024/2, y=20)

print('hi')
text1 = "Record Store."
textLable1.configure(text = text1)


# main loop
root.mainloop()