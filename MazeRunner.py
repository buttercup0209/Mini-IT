import pygame 
import time 
import random 
import tkinter as tk
from tkinter import *

def login(): 
    root = tk.Tk()
    root.title("Maze Runner | Login")
    root.geometry('350x200')
    root.columnconfigure(0, weight= 1)
    root.columnconfigure(1, weight= 1)
    root.columnconfigure(2, weight= 1)

    username = Label(root, text = "Username")
    username.grid(row=0, column=1)
    
    UserEntry = Entry(root, width=20, borderwidth= 5)
    UserEntry.grid(row=1, column=1)
    
    Password = Label(root, text = "Password")
    Password.grid(row=2, column=1)
    
    PwEntry = Entry(root, width=20, borderwidth= 5)
    PwEntry.grid(row=3, column=1)

    def clicked() :
        Login = Button(root, text = "Log In", fg = "black", command=clicked)
        Login.grid(row= 5, column=1)

    def back() :
        root.destroy()
        home()

        back_btn = Button(root, text = "Back", fg = "black", command=back)
        back_btn.grid(row= 5, column=2)

def home():
    root = tk.Tk()
    root.title("Maze Runner")
    root.geometry('350x200')
    root.columnconfigure(0, weight= 1)
    root.columnconfigure(1, weight= 1)
    root.columnconfigure(2, weight= 1)

    Login_Reg = Label(root, text = "Log In/Register" )
    Login_Reg.grid(column=1, row=0)

    def clicked() :
        root.destroy()
        login()
        
    Login = Button(root, text = "Log In", fg = "black", command=clicked)
    Login.grid(column=0, row=2)
    
    def clicked() :
        root.destroy()
        age()

    Register = Button(root, text = "Register", fg = "black", command=clicked)
    Register.grid(column=2, row=2)

    root.mainloop()

home()
