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
root.title('Record Store')
root.geometry('1024x664')



# colours
lightPurple = '#CFACEB'
darkPurple = '#2f2d45'



# creating the background image
photo = Image.open('recordStore.jpg')
photo = photo.resize((1024, 664), Image.LANCZOS)
photo = ImageTk.PhotoImage(photo)



# creating a label to show the image
label = tk.Label(root, image=photo)
label.pack()



# lable for the title
textLable1 = tk.Label(root,text=' ',
                 font=('Arial', 25, 'bold'), fg='black', bg= lightPurple)
textLable1.place(x=880/2, y=20)

print('hi')
text1 = 'Record Store'
textLable1.configure(text = text1)



# lable for the store and store removal
textStore = tk.Label(text='\nStore Options:\n\n1. Add New Vinyl\n\n2. See All Vinyls\n\n3. Find Vinyl by Name\n\n4. Find Best Album for Vinyl\n\n5. Delete Vinyl by Name\n\n6. Show Vinyls in Rating Range\n',
                 font=('Arial', 18), bg=lightPurple)
textStore.place(x=720/2, y=100)

def removeStore():
    print('store gone')
    textRemove = ''
    textStore.configure(text = textRemove, font=('Arial', 10), bg=darkPurple)

def addStoreBack():
    print('store Back')
    textBack = '\nStore Options:\n\n1. Add New Vinyl\n\n2. See All Vinyls\n\n3. Find Vinyl by Name\n\n4. Find Best Album for Vinyl\n\n5. Delete Vinyl by Name\n\n6. Show Vinyls in Rating Range\n'
    textStore.configure(text = textBack, font=('Arial', 18), bg=lightPurple)
    


# creating the store option entry
def storeGUI():
    optionEntry = tk.Entry(root)
    optionEntry.place(x=880/2, y=550)
    def lookForOption():
        user_input = optionEntry.get()
        if user_input == "1":
            removeStore()
            prompt_add_new_vinyl(connection)
            return
        elif user_input == "2":
            removeStore()
            prompt_see_all_vinyls(connection)
            return
        elif user_input == "3":
            removeStore()
            prompt_find_vinyl(connection)
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
            print('Invalid input, please try again.')


    entryButton = tk.Button(root, text = 'Enter Option', command = lookForOption)
    entryButton.place(x=880/2, y=600)



# creating entry boxes for the 1st 6 options in the menu
def prompt_add_new_vinyl(connection):
    global nameVinyl, albumVinyl, ratingVinyl, entryButton1
    nameVinyl = tk.Entry(root)
    nameVinyl.place(x=880/2, y=100)

    albumVinyl = tk.Entry(root)
    albumVinyl.place(x=880/2, y=150)

    ratingVinyl = tk.Entry(root)
    ratingVinyl.place(x=880/2, y=200)

    def addToDatabase1():
        name = nameVinyl.get()
        album = albumVinyl.get()
        rating = int(ratingVinyl.get())

        database.add_vinyl(connection, name, album, rating)
        print('added successfully')
        addStoreBack()
        nameVinyl.place_forget()
        albumVinyl.place_forget()
        ratingVinyl.place_forget()
        entryButton1.place_forget()

    entryButton1 = tk.Button(root, text = 'Enter Names', command = addToDatabase1)
    entryButton1.place(x=880/2, y=400)



# creating lables, buttons aswell as the commands for the 2nd option in the store
def prompt_see_all_vinyls(connection):
    vinyls = database.get_all_vinyls(connection)
    vinylsAll = tk.Label(root, text = f'{vinyls}', font=('Arial', 14), wraplength = 600, bg=lightPurple)
    vinylsAll.place(x=500/2, y=100)
    print('vinyls shown')

    def goBackToHome():
        vinylsAll.place_forget()
        entryButton2.place_forget()
        addStoreBack()
    
    entryButton2 = tk.Button(root, text = 'Go Back', command = goBackToHome)
    entryButton2.place(x=880/2, y=500)



# creating the entry boxes, lables, buttons awswell as the commands for the 3rd option in the store
def prompt_find_vinyl(connection):
    global vinylNameFind, entryButton3
    vinylNameFind = tk.Entry(root)
    vinylNameFind.place(x=880/2, y=100)

    def findVinyl():
        global vinylFound
        nameToFind = vinylNameFind.get()
        vinyls = database.get_vinyls_by_name(connection, nameToFind)
        vinylFound = tk.Label(root, text = f'{vinyls}', font=('Arial', 14), wraplength = 600, bg=lightPurple)
        vinylFound.place(x=500/2, y=100)
        vinylNameFind.place_forget()

    
    entryButton3 = tk.Button(root, text = 'Enter Vinyl Name', command = findVinyl)
    entryButton3.place(x=880/2, y=400)

    def goBackToHome2():
        vinylFound.place_forget()
        vinylNameFind.place_forget()
        entryButton3.place_forget()
        entryButton4.place_forget()
        addStoreBack()

    entryButton4 = tk.Button(root, text = 'Go Back', command = goBackToHome2)
    entryButton4.place(x=880/2, y=500)




# calling the storeGUI function
storeGUI()



# creating the main loop for the GUI
root.mainloop()