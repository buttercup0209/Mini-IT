import pygame 
import time 
import random 
import tkinter as tk
from tkinter import *
import json 
import os 

DATA_FILENAME = "data.json"

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
    
    invalid_user = Label(root, text= "")
    invalid_user.grid(row=9, column=1)
    
    def clicked() :
        with open(DATA_FILENAME) as json_file:
            data = json.load(json_file)
            for x in data:
                if (x['username'] == UserEntry.get() and x['password'] == PwEntry.get()):
                        root.destroy()
                        menu()
                else :
                    invalid_user.config(text="Your username or password may be incorrect!")
        
    Login = Button(root, text = "Log In", fg = "black", command=clicked)
    Login.grid(row= 5, column=1)
    
    def back() :
        root.destroy()
        home()
        
    back_btn = Button(root, text = "Back", fg = "black", command=back)
    back_btn.grid(row= 5, column=2)
    
    root.mainloop()

def age() :
    root = tk.Tk()
    root.title("Maze Runner | Register")
    root.geometry('350x200')
    root.columnconfigure(0, weight= 1)
    root.columnconfigure(1, weight= 1)
    root.columnconfigure(2, weight= 1)
    
    age = Label(root, text = "Enter Age :")
    age.grid(row=0, column=1)
    age_scale = Scale(root, from_= 0, to=99, orient=HORIZONTAL)
    age_scale.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
    def clicked():
        print("Age :", age_scale.get())
        root.destroy()
        register()
    
    Enter = Button(root, text = "Enter", fg = "black", command=clicked)
    Enter.grid(row= 5, column=1)
    
    def back() :
        root.destroy()
        home()
        
    back_btn = Button(root, text = "Back", fg = "black", command=back)
    back_btn.grid(row= 5, column=2)
        
    root.mainloop()
        
def register() :
    root = tk.Tk()
    root.title("Maze Runner | Register")
    root.geometry('350x200')
    root.columnconfigure(0, weight= 1)
    root.columnconfigure(1, weight= 1)
    root.columnconfigure(2, weight= 1)
    
    Username = Label(root, text = "Create Username")
    Username.grid(row=0, column=1)
    
    UserEntry = Entry(root, width=20, borderwidth= 5)
    UserEntry.grid(row=1, column=1)
    
    Password = Label(root, text = "Create Password")
    Password.grid(row=2, column=1)
    
    PwEntry = Entry(root, width=20, borderwidth= 5)
    PwEntry.grid(row=3, column=1)
    
    invalid_user = Label(root, text= "")
    invalid_user.grid(row=9, column=1)
    
    def clicked() :
        if (UserEntry.get() == "" or UserEntry.get() == " "):
            invalid_user.config(text="Username Invalid!")
        elif (PwEntry.get() == "" or PwEntry.get() == " "):
            invalid_user.config(text="Password Invalid!")
        elif (len(PwEntry.get()) < 10):
            invalid_user.config(text="You need at least 10 characters")
        else:
            exists = False
            
            with open(DATA_FILENAME) as json_file:
                data = json.load(json_file)

                for x in data:
                    if (x['username'] == UserEntry.get()):
                        exists = True
            
            if (exists):
                invalid_user.config(text="Username already exist!")
            else:
                dictionary = {
                    "username": UserEntry.get(),
                    "password": PwEntry.get()
                }

                a = []
                if not os.path.isfile(DATA_FILENAME):
                    a.append(dictionary)
                    with open(DATA_FILENAME, mode='w') as f:
                        f.write(json.dumps(a, indent=2))
                else:
                    with open(DATA_FILENAME) as feedsjson:
                        feeds = json.load(feedsjson)

                    feeds.append(dictionary)
                    with open(DATA_FILENAME, mode='w') as f:
                        f.write(json.dumps(feeds, indent=2))
                
                invalid_user.config(text="Registration Successful")
                root.destroy()
                register_success()
    
    Register = Button(root, text = "Register", fg = "black", command=clicked)
    Register.grid(row= 8, column=1)
    
    def back() :
        root.destroy()
        age()
        
    back_btn = Button(root, text = "Back", fg = "black", command=back)
    back_btn.grid(row= 8, column=2)
    
    root.mainloop()
    
def register_success() :
    root = tk.Tk()
    root.title("Maze Runner | Register Success")
    root.geometry('350x200')
    root.columnconfigure(0, weight= 1)
    root.columnconfigure(1, weight= 1)
    root.columnconfigure(2, weight= 1)

    Successful = Label(root, text = "Registration Successful")
    Successful.grid(row=3, column=1)
    
    Successful = Label(root, text = "Login to continue")
    Successful.grid(row=4, column=1)
    
    def clicked() :
        root.destroy()
        login()
        
    Login = Button(root, text = "Log In", fg = "black", command=clicked)
    Login.grid(row= 6, column=1)
    
    root.mainloop()

def credit() :
    root = tk.Tk()
    root.title("Maze Runner")
    root.geometry('1000x600')
    root.columnconfigure(0, weight= 1)
    root.columnconfigure(1, weight= 1)
    root.columnconfigure(2, weight= 1)

    creators = Label(root, text = "Creators" )
    creators.grid(column=1, row=0)

    creators = Label(root, text = "Girindrashinie\nKashvinna Anne\nMithraa Liora\nTarani Devi" )
    creators.grid(column=1, row=2)

    designers = Label(root, text = "Game Design and Graphics" )
    designers.grid(column=1, row=5)

    designers = Label(root, text = "Kashvinna Anne\nMithraa Liora\nTarani Devi" )
    designers.grid(column=1, row=6)

    programmers = Label(root, text = "Programmers" )
    programmers.grid(column=1, row=9)

    programmers = Label(root, text = "Girindrashinie\nKashvinna Anne\nMithraa Liora\nTarani Devi" )
    programmers.grid(column=1, row=10)

    mns = Label(root, text = "Music and Sound" )
    mns.grid(column=1, row=14)

    girin = Label(root, text = "Girindrashinie" )
    girin.grid(column=1, row=15)

    cd = Label(root, text = "Character Design" )
    cd.grid(column=1, row=16)

    cd = Label(root, text = "Copilot" )
    cd.grid(column=1, row=17)

    lang = Label(root, text = "Programming Language" )
    lang.grid(column=1, row=18)

    py = Label(root, text = "Python (Not the snake)" )
    py.grid(column=1, row=19)

    modules = Label(root, text = "Modules" )
    modules.grid(column=1, row=20)

    modules = Label(root, text = "Tkinter\nPygame" )
    modules.grid(column=1, row=21)

    def back() :
        root.destroy()
        menu()
        
    back_btn = Button(root, text = "Back", fg = "black", command=back)
    back_btn.grid(column=2, row= 23)

def menu() :
    root = tk.Tk()
    root.title("Maze Runner")
    root.geometry('1000x600')
    root.columnconfigure(0, weight= 1)
    root.columnconfigure(1, weight= 1)
    root.columnconfigure(2, weight= 1)

    menu = Label(root, text = "Main Menu" )
    menu.grid(column=0, row=1)

    def clicked() :
        root.destroy()
            
    start = Button(root, text = "Play", fg = "black", command=clicked)
    start.grid(column=0, row=2)

    def clicked() :
        root.destroy()

    settings = Button(root, text = "Settings", fg = "black", command=clicked)
    settings.grid(column=0, row=5)
    
    def clicked() :
        root.destroy()

    option = Button(root, text = "Option", fg = "black", command=clicked)
    option.grid(column=0, row=3)

    def clicked() :
        root.destroy()
        credit()

    credits = Button(root, text = "Credits", fg = "black", command=clicked)
    credits.grid(column=0, row=4)


    def clicked() :
        root.destroy()

    quit = Button(root, text = "Quit", fg = "black", command=clicked)
    quit.grid(column=0, row=6)

    root.mainloop()

def game():
    pygame.init()
    
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze Runner")
    
    white = (255, 255, 255)
    gray = (200, 200, 200)
    
    room_width, room_height = 600, 400
    wall_thickness = 10
    
    walls = [
        pygame.Rect(0, 0, room_width, wall_thickness), 
        pygame.Rect(0, 0, wall_thickness, room_height),  
        pygame.Rect(room_width - wall_thickness, 0, wall_thickness, room_height),  
        pygame.Rect(0, room_height - wall_thickness, room_width, wall_thickness),  
    ]
    
    
    ceiling = pygame.Rect(0, 0, room_width, wall_thickness)
    floor = pygame.Rect(0, room_height - wall_thickness, room_width, wall_thickness)
    
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        
        screen.fill(white)
        pygame.draw.rect(screen, gray, ceiling)
        pygame.draw.rect(screen, gray, floor)
        for wall in walls:
            pygame.draw.rect(screen, gray, wall)
    
        pygame.display.flip()
    
    pygame.quit()
    

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