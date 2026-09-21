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


# connecting to the database 
connection = database.connect()
database.create_tables(connection)


# GUI creation
root = tk.Tk()
root.title("Record Store")
root.geometry('1024x664')


# colours
lightPurple = "#CFACEB"


# creating the background image
photo = Image.open("recordStore.jpg")
photo = photo.resize((1024, 664), Image.LANCZOS)
photo = ImageTk.PhotoImage(photo)


# creating a label to show the image
label = tk.Label(root, image=photo)
label.pack()


# lable for the title
textLable1 = tk.Label(root,text=" ",
                 font=('Arial', 25, 'bold'), fg='black', bg= lightPurple)
textLable1.place(x=880/2, y=20)

print('hi')
text1 = "Record Store"
textLable1.configure(text = text1)


# creating the menu option entry
optionEntry = tk.Entry(root)
optionEntry.place(x=880/2, y=550)

def menuGUI():
    user_input = optionEntry.get()
    if user_input == "1":
        prompt_add_new_vinyl(connection)
    elif user_input == "2":
        prompt_see_all_vinyls(connection)
    elif user_input == "3":
        prompt_find_vinyl(connection)
    elif user_input == "4":
        prompt_find_best_album(connection)
    elif user_input == "5":
        prompt_delete_vinyl(connection)
    elif user_input == "6":
        prompt_vinyl_rate_range(connection)
    else:
        print("Invalid input, please try again.")


# creating entry boxes for the 1st 6 options in the menu
nameVinyl = tk.Entry(root)
nameVinyl.place(x=880/2, y=100)

albumVinyl = tk.Entry(root)
albumVinyl.place(x=880/2, y=150)

ratingVinyl = tk.Entry(root)
ratingVinyl.place(x=880/2, y=200)

def prompt_add_new_vinyl(connection):
    name = nameVinyl.get()
    album = albumVinyl.get()
    rating = int(ratingVinyl.get())

    database.add_vinyl(connection, name, album, rating)



# seeAllVinyls = tk.Entry(root)
# seeAllVinyls.place(x=880/2, y=150)

# findVinyl = tk.Entry(root)
# findVinyl.place(x=880/2, y=200)

# findBestAlbumVinyl = tk.Entry(root)
# findBestAlbumVinyl.place(x=880/2, y=250)

# deleteVinyl = tk.Entry(root)
# deleteVinyl.place(x=880/2, y=300)

# rateRangeVinyl = tk.Entry(root)
# rateRangeVinyl.place(x=880/2, y=350)


# creating the 


# main loop
root.mainloop()