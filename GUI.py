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



# creating the background images
photo = Image.open('recordStore.jpg')
photo = photo.resize((1024, 664), Image.LANCZOS)
photo = ImageTk.PhotoImage(photo)

# photo2 = Image.open('recordStore2.jpg')
# photo2 = photo2.resize((1024, 664), Image.LANCZOS)



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
textStore = tk.Label(text='\nStore Options:\n\n1. Add New Vinyl\n\n2. See All Vinyls\n\n3. Find Vinyl by Name\n\n4. Find Best Album for Vinyl\n\n5. Delete Vinyl by Name\n\n6. Show Vinyls in Rating Range\n\n7. Show Vinyls in Ascending Order\n',
                 font=('Arial', 18), bg=lightPurple)
textStore.place(x=720/2, y=100)

def removeStore():
    print('store gone')
    textRemove = ''
    textStore.configure(text = textRemove, font=('Arial', 10), bg=darkPurple)

def addStoreBack():
    print('store Back')
    textBack = '\nStore Options:\n\n1. Add New Vinyl\n\n2. See All Vinyls\n\n3. Find Vinyl by Name\n\n4. Find Best Album for Vinyl\n\n5. Delete Vinyl by Name\n\n6. Show Vinyls in Rating Range\n\n7. Show Vinyls in Ascending Order\n'
    textStore.configure(text = textBack, font=('Arial', 18), bg=lightPurple)

settingsMenu = tk.Label(root, text = 'Menu:\n1. Change Background\n2. Change Menu Colour\n3. Change Font', font=('Arial', 12), wraplength = 200, bg=lightPurple)
settingsMenu.place(x=100, y=100)

def settingsMenuDisappear():
    settingsMenu.place_forget()

def settingsMenuAppear():
    settingsMenu.place(x=100, y=100)

# creatating the settings for the GUI
def settingsGUI():
    print('Settings GUI opened')
    settingsMenuAppear()
    global settingsButton 
    
    settings()

def settings():
    global enterOptionButtonS, optionEntryS
    optionEntryS = tk.Entry(root)
    optionEntryS.place(x=100, y=250)
    def lookForOptionS():
        while True:
            user_input = optionEntryS.get()
            if user_input == "1":
                changeBackground()
                print('Change Background')
                return
            elif user_input == "2":
                print('Change Menu Colour')
                return
            elif user_input == "3":
                print('Change Font')
                return
            else:
                print('Invalid input, please try again.')
        
    enterOptionButtonS = tk.Button(root, text = 'Enter Option', command = lookForOptionS)
    enterOptionButtonS.place(x=100, y=280)

settingsButton = tk.Button(root, text = 'Settings', command = settingsGUI)
settingsButton.place(x=50, y=50)

def changeBackground():
    settingsMenuDisappear()
    def background1():
        print('background1')

    def background2():
        print('background2')

    def goBackHomeS1():
        background1Button.place_forget()
        background2Button.place_forget()
        backButton1.place_forget()
        settingsMenuAppear()
        print('back home')

    background1Button = tk.Button(root, text = 'background 1', command = background1)
    background1Button.place(x=100, y=200)

    background2Button = tk.Button(root, text = 'background 2', command = background2)
    background2Button.place(x=100, y=220)

    backButton1 = tk.Button(root, text = 'Go Back', command = goBackHomeS1)
    backButton1.place(x=100, y=250)

    print('changed')



# creating the store option entry
def storeGUI():
    optionEntry = tk.Entry(root)
    optionEntry.place(x=880/2, y=570)
    def lookForOption():
        while True:
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
                removeStore()
                prompt_find_best_album(connection)
                return
            elif user_input == "5":
                removeStore()
                prompt_delete_vinyl(connection)
                return
            elif user_input == "6":
                removeStore()
                prompt_vinyl_rate_range(connection)
                return
            elif user_input == "7":
                removeStore()
                prompt_sort_vinyls_asc(connection)
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



# creating the entry boxes, lables, and buttons for the 4th option
def prompt_find_best_album(connection):
    global vinylNameFindBest, entryButton5
    vinylNameFindBest = tk.Entry(root)
    vinylNameFindBest.place(x=880/2, y=100)

    def findBestAlbum():
        global bestAlbumFound
        nameToFind = vinylNameFindBest.get()
        vinyls = database.get_best_album_for_vinyl(connection, nameToFind)
        bestAlbumFound = tk.Label(root, text = f'The best album for {nameToFind} is {vinyls[0][2]}', font=('Arial', 14), wraplength = 600, bg=lightPurple)
        bestAlbumFound.place(x=500/2, y=100)
        vinylNameFindBest.place_forget()

    
    entryButton5 = tk.Button(root, text = 'Enter Vinyl Name', command = findBestAlbum)
    entryButton5.place(x=880/2, y=400)

    def goBackToHome3():
        bestAlbumFound.place_forget()
        vinylNameFindBest.place_forget()
        entryButton5.place_forget()
        entryButton6.place_forget()
        addStoreBack()

    entryButton6 = tk.Button(root, text = 'Go Back', command = goBackToHome3)
    entryButton6.place(x=880/2, y=500)



# creating the entry boxes, lables, and buttons for the 5th option
def prompt_delete_vinyl(connection):
    global vinylNameDelete, entryButton7, entryButton8
    vinylNameDelete = tk.Entry(root)
    vinylNameDelete.place(x=880/2, y=100)

    def findVinylToDelete():
        global deleteVinyl
        vinylToDelete = vinylNameDelete.get()
        database.delete_vinyl_by_name(connection, vinylToDelete)
        deleteVinyl = tk.Label(root, text = f'{vinylToDelete} has been deleted', font=('Arial', 14), wraplength = 600, bg=lightPurple)
        deleteVinyl.place(x=600/2, y=100)
        entryButton7.place_forget()
        vinylNameDelete.place_forget()
        print('deleted vinyl')

    entryButton7 = tk.Button(root, text = 'Enter Vinyl Name', command = findVinylToDelete)
    entryButton7.place(x=880/2, y=400)

    def goBackToHome4():
        deleteVinyl.place_forget()
        vinylNameDelete.place_forget()
        entryButton7.place_forget()
        entryButton8.place_forget()
        addStoreBack()

    entryButton8 = tk.Button(root, text = 'Go Back', command = goBackToHome4)
    entryButton8.place(x=880/2, y=500)



# creating the entry boxes, lables, and buttons for the 6th option
def prompt_vinyl_rate_range(connection):
    global vinylRatingMin, vinylRatingMax, entryButton9,entryButton10
    vinylRatingMin = tk.Entry(root)
    vinylRatingMin.place(x=880/2, y=100)

    vinylRatingMax = tk.Entry(root)
    vinylRatingMax.place(x=880/2, y=150)

    def showVinylsInRange():
        global vinylsInRange
        low = vinylRatingMin.get()
        high = vinylRatingMax.get()
        vinyls = database.show_vinyl_range(connection, low, high)
        vinylsInRange = tk.Label(root, text = f'{vinyls}', font=('Arial', 14), wraplength = 600, bg=lightPurple)
        vinylsInRange.place(x=500/2, y=100)
        vinylRatingMin.place_forget()
        vinylRatingMax.place_forget()
        entryButton9.place_forget()
        print('vinyls shown in range')

    entryButton9 = tk.Button(root, text = 'Enter Vinyl Rating Range', command =showVinylsInRange)
    entryButton9.place(x=880/2, y=400) 

    def goBackToHome5():
        vinylsInRange.place_forget()
        vinylRatingMin.place_forget()
        vinylRatingMax.place_forget()
        entryButton10.place_forget()
        addStoreBack()

    entryButton10 = tk.Button(root, text = 'Go Back', command = goBackToHome5)
    entryButton10.place(x=880/2, y=500)



# creating the entry boxes, lables, and buttons for the 7th option
def prompt_sort_vinyls_asc(connection):
    global entryButton11, vinylsAsc
    vinyls = database.show_vinyl_asc(connection)
    vinylsAsc = tk.Label(root, text = f'{vinyls}', font=('Arial', 14), wraplength = 600, bg=lightPurple)
    vinylsAsc.place(x=500/2, y=100)
    
    def goBackToHome6():
        vinylsAsc.place_forget()
        entryButton11.place_forget()
        addStoreBack()
    
    entryButton11 = tk.Button(root, text = 'Go Back', command = goBackToHome6)
    entryButton11.place(x=880/2, y=500)



# calling the storeGUI and settings functions
settingsMenuDisappear()
storeGUI()



# creating the main loop for the GUI
root.mainloop()