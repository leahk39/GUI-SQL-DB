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


# lable for the store and store removal
textStore = tk.Label(text="\nStore Options:\n\n1. Add New Vinyl\n\n2. See All Vinyls\n\n3. Find Vinyl by Name\n\n4. Find Best Album for Vinyl\n\n5. Delete Vinyl by Name\n\n6. Show Vinyls in Rating Range\n",
                 font=('Arial', 18), bg=lightPurple)
textStore.place(x=720/2, y=100)

def removeStore():
    print('store gone')
    textNO = " "
    textStore.configure(text = textNO)


# creating the store option entry
optionEntry = tk.Entry(root)
optionEntry.place(x=880/2, y=550)

def storeGUI():
    user_input = optionEntry.get()
    if user_input == "1":
        removeStore()
        # prompt_add_new_vinyl(connection)
        
    elif user_input == "2":
        prompt_see_all_vinyls(connection)
        removeStore()
    elif user_input == "3":
        # prompt_find_vinyl(connection)
        # removeStore()
        return
    elif user_input == "4":
        # prompt_find_best_album(connection)
        # removeStore()
        return
    elif user_input == "5":
        # prompt_delete_vinyl(connection)
        # removeStore()
        return
    elif user_input == "6":
        # prompt_vinyl_rate_range(connection)
        # removeStore()
        return
    else:
        print("Invalid input, please try again.")


# creating entry boxes for the 1st 6 options in the menu
def prompt_add_new_vinyl(connection):
    nameVinyl = tk.Entry(root)
    nameVinyl.place(x=880/2, y=100)

    albumVinyl = tk.Entry(root)
    albumVinyl.place(x=880/2, y=150)

    ratingVinyl = tk.Entry(root)
    ratingVinyl.place(x=880/2, y=200)

    name = nameVinyl.get()
    album = albumVinyl.get()
    rating = int(ratingVinyl.get())

    database.add_vinyl(connection, name, album, rating)


def prompt_see_all_vinyls(connection):
    vinyls = database.get_all_vinyls(connection)
    for vinyl in vinyls:
        print(vinyl)


def prompt_find_vinyl(connection):
    name = nameVinyl.get()
    vinyls = database.get_vinyls_by_name(connection, name)
    for vinyl in vinyls:
        print(vinyl)


def prompt_find_best_album(connection):
    name = nameVinyl.get()
    best_album = database.get_best_album_for_vinyl(connection, name)
    for album in best_album:
        print(album)


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

storeGUI()
# main loop
root.mainloop()