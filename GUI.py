"""
This module is for the GUI for the database and app
"""

# imports
import tkinter as tk
import sqlite3
import database


# GUI creation
root = tk.Tk()
root.title("Drink Database")
root.geometry('400x400')

title_label = tk.Label(root, text="Drink Database", font=("Arial", 20))
title_label.pack(pady=20)

# main loop
root.mainloop()