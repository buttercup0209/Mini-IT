import pygame 
import time 
import random 
import tkinter as tk
from tkinter import *
from tkinter import ttk
import json 
import os 
from pygame.locals import *
from pygame import mixer
from PIL import Image, ImageTk
from tkinter import Label, Entry, Button
from tkinter import Button

DATA_FILENAME = "data.json"

def login(): 
    root = tk.Tk()
    root.title("Maze Runner | Login")

    bg_image = Image.open("Assets/login_bg.jpg")
    bg_image_width, bg_image_height = bg_image.size
    root.geometry(f'{bg_image_width}x{bg_image_height}')
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    canvas = tk.Canvas(root, width=bg_image_width, height=bg_image_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    
    pixel_font = ("Press Start 2P", 12)
    
    username_label = Label(root, text="Username", font=pixel_font, bg='white', fg='black')
    username_entry = Entry(root, width=20, borderwidth=5, font=pixel_font)
    password_label = Label(root, text="Password", font=pixel_font, bg='white', fg='black')
    password_entry = Entry(root, width=20, borderwidth=5, font=pixel_font, show="*")
    invalid_user_label = Label(root, text="", font=pixel_font, fg='red')
    
    def clicked() :
        with open(DATA_FILENAME) as json_file:
            data = json.load(json_file)
            for x in data:
                if (x['username'] == username_entry.get() and x['password'] == password_entry.get()):
                        root.destroy()
                        menu()
                        return
                else :
                    invalid_user_label.config(text="Your username or password may be incorrect!")
    
    def back() :
        root.destroy()
        home()
        
    login_button = Button(root, text="Log In", fg="black", command=clicked, font=pixel_font, bg='white')
    back_button = Button(root, text="Back", fg="black", command=back, font=pixel_font, bg='white')

    # Position the widgets on the canvas
    canvas.create_window(bg_image_width//2, 50, window=username_label)
    canvas.create_window(bg_image_width//2, 90, window=username_entry)
    canvas.create_window(bg_image_width//2, 130, window=password_label)
    canvas.create_window(bg_image_width//2, 170, window=password_entry)
    canvas.create_window(bg_image_width//2, 210, window=invalid_user_label)
    canvas.create_window(bg_image_width//2 - 60, 250, window=back_button)
    canvas.create_window(bg_image_width//2 + 60, 250, window=login_button)
    
    root.mainloop()

def age() :
    root = tk.Tk()
    root.title("Maze Runner | Register")

    bg_image = Image.open("Assets/login_bg.jpg")
    bg_image_width, bg_image_height = bg_image.size
    root.geometry(f'{bg_image_width}x{bg_image_height}')
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    canvas = tk.Canvas(root, width=bg_image_width, height=bg_image_height)
    canvas.pack(fill="both", expand=True)
    
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    
    pixel_font = ("Press Start 2P", 12)
    
    age_label = Label(root, text="Enter Age:", font=pixel_font, bg='white', fg='black')
    age_scale = Scale(root, from_=0, to=99, orient="horizontal", font=pixel_font)
    
    def clicked():
        print("Age:", age_scale.get())
        root.destroy()
        register()
    
    def back() :
        root.destroy()
        home()
        
    enter_button = Button(root, text="Enter", fg="black", command=clicked, font=pixel_font, bg='white')
    back_button = Button(root, text="Back", fg="black", command=back, font=pixel_font, bg='white')

    canvas.create_window(bg_image_width//2, 50, window=age_label)
    canvas.create_window(bg_image_width//2, 90, window=age_scale, width=bg_image_width-50)
    canvas.create_window(bg_image_width//2 - 60, 200, window=back_button)
    canvas.create_window(bg_image_width//2 + 60, 200, window=enter_button)
        
    root.mainloop()
        
def register() :
    root = tk.Tk()
    root.title("Maze Runner | Register")

    bg_image = Image.open("Assets/login_bg.jpg")
    bg_image_width, bg_image_height = bg_image.size
    root.geometry(f'{bg_image_width}x{bg_image_height}')
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    canvas = tk.Canvas(root, width=bg_image_width, height=bg_image_height)
    canvas.pack(fill="both", expand=True)
    
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    
    pixel_font = ("Press Start 2P", 12)
    
    username_label = Label(root, text="Create Username", font=pixel_font, bg='white', fg='black')
    username_entry = Entry(root, width=20, borderwidth=5, font=pixel_font)
    password_label = Label(root, text="Create Password", font=pixel_font, bg='white', fg='black')
    password_entry = Entry(root, width=20, borderwidth=5, font=pixel_font, show="*")
    invalid_user_label = Label(root, text="", font=pixel_font, bg='white')

    def show_message(message, color):
        invalid_user_label.config(text=message, fg=color)
        if message:
            canvas.create_window(bg_image_width//2, 210, window=invalid_user_label)
        else:
            canvas.delete(invalid_user_label)
    
    def clicked() :
        if (username_entry.get() == "" or username_entry.get() == " "):
            show_message("Username Invalid!", 'red')
        elif (password_entry.get() == "" or password_entry.get() == " "):
            show_message("Password Invalid!", 'red')
        elif (len(password_entry.get()) < 10):
            show_message("You need at least 10 characters", 'red')
        else:
            exists = False
            
            if os.path.isfile(DATA_FILENAME):
                with open(DATA_FILENAME) as json_file:
                    data = json.load(json_file)

                    for x in data:
                        if (x['username'] == username_entry.get()):
                            exists = True
            
            if (exists):
                show_message("Username already exists!", 'red')
            else:
                new_user = {
                    "username": username_entry.get(),
                    "password": password_entry.get()
                }

                if not os.path.isfile(DATA_FILENAME):
                    with open(DATA_FILENAME, mode='w') as f:
                        json.dump([new_user], f, indent=2)
                else:
                    with open(DATA_FILENAME) as feedsjson:
                        feeds = json.load(feedsjson)

                    feeds.append(new_user)
                    with open(DATA_FILENAME, mode='w') as f:
                        json.dump(feeds, f, indent=2)
                
                show_message("Registration Successful", 'green')
                root.destroy()
                register_success()

    def back() :
        root.destroy()
        age()
    
    register_button = Button(root, text="Register", fg="black", command=clicked, font=pixel_font, bg='white')
    back_button = Button(root, text="Back", fg="black", command=back, font=pixel_font, bg='white')
        
    canvas.create_window(bg_image_width//2, 50, window=username_label)
    canvas.create_window(bg_image_width//2, 90, window=username_entry)
    canvas.create_window(bg_image_width//2, 130, window=password_label)
    canvas.create_window(bg_image_width//2, 170, window=password_entry)
    canvas.create_window(bg_image_width//2, 210, window=invalid_user_label)
    canvas.create_window(bg_image_width//2 - 60, 250, window=back_button)
    canvas.create_window(bg_image_width//2 + 60, 250, window=register_button)
    
    root.mainloop()
    
def register_success() :
    root = tk.Tk()
    root.title("Maze Runner | Register Success")

    bg_image = Image.open("Assets/login_bg.jpg")
    bg_image_width, bg_image_height = bg_image.size
    root.geometry(f'{bg_image_width}x{bg_image_height}')
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    canvas = tk.Canvas(root, width=bg_image_width, height=bg_image_height)
    canvas.pack(fill="both", expand=True)
    
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    
    pixel_font = ("Press Start 2P", 12)

    success_label1 = Label(root, text="Registration Successful", font=pixel_font, bg='white', fg='green')
    success_label2 = Label(root, text="Login to continue", font=pixel_font, bg='white', fg='black')
    
    def clicked() :
        root.destroy()
        login()
        
    login_button = Button(root, text="Log In", fg="black", command=clicked, font=pixel_font, bg='white')
    
    canvas.create_window(bg_image_width//2, 90, window=success_label1)
    canvas.create_window(bg_image_width//2, 130, window=success_label2)
    canvas.create_window(bg_image_width//2, 170, window=login_button)

    root.mainloop()

def settings():
    root = tk.Tk()
    root.title("Maze Runner | Settings")
    
    bg_image = Image.open("Assets/settings page.png")
    bg_image_width, bg_image_height = bg_image.size
    new_width = 800
    new_height = int(bg_image_height * (new_width / bg_image_width))
    bg_image = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_image_width, bg_image_height = bg_image.size
    
    root.geometry(f'{bg_image_width}x{bg_image_height}')
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    canvas = tk.Canvas(root, width=bg_image_width, height=bg_image_height)
    canvas.pack(fill="both", expand=True)
    
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    
    pixel_font = ("Press Start 2P", 16)
    
    settings_label = Label(root, text="SETTINGS", font=pixel_font, bg='black', fg='white')
    
    def clicked():
        root.destroy()
        # volume func
    
    def back():
        root.destroy()
        menu()
    
    vol_label = Label(root, text="Volume", font=pixel_font, bg='black', fg='white')
    vol_scale = Scale(root, from_=0, to=99, orient="horizontal", font=pixel_font, bg='black', fg='white', troughcolor='grey')
    
    enter_button = Button(root, text="Enter", font=pixel_font, bg='black', fg='white', command=clicked)
    back_button = Button(root, text="Back", font=pixel_font, bg='black', fg='white', command=back)
    
    canvas.create_window(bg_image_width // 2, 150, window=settings_label)
    canvas.create_window(bg_image_width // 2, 250, window=vol_label)
    canvas.create_window(bg_image_width // 2, 300, window=vol_scale)
    canvas.create_window(bg_image_width // 2, 400, window=enter_button)
    canvas.create_window(bg_image_width // 2, 450, window=back_button)
    
    root.mainloop()

def credit() :
    root = tk.Tk()
    root.title("Maze Runner | Credits")

    bg_image = Image.open("Assets/menu_bg.png")
    bg_image_width, bg_image_height = bg_image.size
    new_width = 1000
    new_height = int(bg_image_height * (new_width / bg_image_width)) + 400 
    bg_image = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_image_width, bg_image_height = bg_image.size
    
    root.geometry(f'{bg_image_width}x{bg_image_height}')
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    canvas = tk.Canvas(root, width=bg_image_width, height=bg_image_height)
    canvas.pack(fill="both", expand=True)
    
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    
    pixel_font_large = ("Press Start 2P", 20)
    pixel_font = ("Press Start 2P", 16)
    
    frame = tk.Frame(canvas, bg='black')
    frame_id = canvas.create_window(bg_image_width//2, bg_image_height, window=frame, anchor="n")
    
    credits_text = [
        ("Creators", ["Girindrashinie", "Kashvinna Anne", "Mithraa Liora", "Tarani Devi"]),
        ("Game Design and Graphics", ["Kashvinna Anne", "Mithraa Liora", "Tarani Devi"]),
        ("Programmers", ["Girindrashinie", "Kashvinna Anne", "Mithraa Liora", "Tarani Devi"]),
        ("Music and Sound", ["Girindrashinie"]),
        ("Character Design", ["Copilot"]),
        ("Programming Language", ["Python (Not the snake)"]),
        ("Modules", ["Tkinter", "Pygame"]),
    ]
    
    for section, names in credits_text:
        section_label = Label(frame, text=section, font=pixel_font_large, bg='black', fg='white')
        section_label.pack(pady=(20, 0))
        separator = ttk.Separator(frame, orient='horizontal')
        separator.pack(fill='x', padx=10, pady=(0, 20))
        for name in names:
            name_label = Label(frame, text=name, font=pixel_font, bg='black', fg='white')
            name_label.pack()
    
    def auto_scroll():
        canvas.move(frame_id, 0, -1)
        canvas.update()
        if canvas.bbox(frame_id)[3] > 0:
            canvas.after(10, auto_scroll)
        else:
            root.destroy()
            menu()

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    root.after(1000, auto_scroll)  # Start the auto-scrolling after 1 second
    
    root.mainloop()

def menu() :
    root = tk.Tk()
    root.title("Maze Runner")
    
    bg_image = Image.open("Assets/login page.png")
    bg_image_width, bg_image_height = bg_image.size
    new_width = 800
    new_height = int(bg_image_height * (new_width / bg_image_width)) + 200
    bg_image = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_image_width, bg_image_height = bg_image.size
    
    root.geometry(f'{bg_image_width}x{bg_image_height}')
    
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    canvas = tk.Canvas(root, width=bg_image_width, height=bg_image_height)
    canvas.pack(fill="both", expand=True)
    
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    
    pixel_font = ("Press Start 2P", 16)

    menu_label = Label(root, text="MAZE RUNNER", font=pixel_font, bg='black', fg='white')

    def start_game():
        root.destroy()
        game()

    def open_settings():
        #root.destroy()
        print("x")
    
    def open_options() :
        #root.destroy()
        print("x")

    def show_credits() :
        root.destroy()
        credit()

    def quit_game() :
        root.destroy()

    play_button = Button(root, text="Play", font=pixel_font, bg='black', fg='white', command=start_game)
    option_button = Button(root, text="Option", font=pixel_font, bg='black', fg='white', command=open_options)
    settings_button = Button(root, text="Settings", font=pixel_font, bg='black', fg='white', command=open_settings)
    credits_button = Button(root, text="Credits", font=pixel_font, bg='black', fg='white', command=show_credits)
    quit_button = Button(root, text="Quit", font=pixel_font, bg='black', fg='white', command=quit_game)

    canvas.create_window(bg_image_width//2, 150, window=menu_label)
    canvas.create_window(bg_image_width//2, 250, window=play_button)
    canvas.create_window(bg_image_width//2, 300, window=option_button)
    canvas.create_window(bg_image_width//2, 350, window=settings_button)
    canvas.create_window(bg_image_width//2, 400, window=credits_button)
    canvas.create_window(bg_image_width//2, 450, window=quit_button)

    root.mainloop()

def game():
    import pygame 
    import os

    screen_width, screen_height = 1000, 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze Runner")

    white = (255, 255, 255)
    gray = (200, 200, 200)
    brown = (100,40,0)

    room_width, room_height = 1000, 700
    wall_thickness = 10

    walls = [
        pygame.Rect(0, 0, room_width, wall_thickness), 
        pygame.Rect(0, 0, wall_thickness, room_height),  
        pygame.Rect(room_width - wall_thickness, 0, wall_thickness, room_height),  
        pygame.Rect(0, room_height - wall_thickness, room_width, wall_thickness),  
    ]

    ceiling = pygame.Rect(0, 0, room_width, wall_thickness)
    floor = pygame.Rect(0, room_height - wall_thickness, room_width, wall_thickness)

    #Images
    hall = pygame.image.load("./Assets/Pixel room.png")
    hall = pygame.transform.scale(hall, (room_width, room_height))


    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()

            self.image = pygame.image.load("./Assets/girl2.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = (room_width // 2, room_height//2)

        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
            if keys[pygame.K_UP]:
                self.rect.y -= 5
            if keys[pygame.K_DOWN]:
                self.rect.y += 5

    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.blit(hall, (0,0))
        pygame.draw.rect(screen, brown, ceiling)
        pygame.draw.rect(screen, brown, floor)
        for wall in walls:
            pygame.draw.rect(screen, brown, wall)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
    
def home():
    root = tk.Tk()
    root.title("Maze Runner")
    root.geometry('500x300')
    root.columnconfigure(0, weight= 1)
    root.columnconfigure(1, weight= 1)
    root.columnconfigure(2, weight= 1)

    bg_image = Image.open("Assets/home_bg.jpg")
    bg_image = bg_image.resize((500, 300), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(bg_image)

    # Create a canvas
    canvas = Canvas(root, width=500, height=300)
    canvas.pack(fill='both', expand=True)

    canvas.create_image(0, 0, image=bg_image, anchor='nw')

    pixel_font = ("Courier", 12, "bold")

    Login_Reg = Label(root, text="Get Started", bg="white", font=pixel_font)
    Login_Reg_window = canvas.create_window(250, 50, anchor='center', window=Login_Reg)

    def login_clicked():
        root.destroy()
        login()
        
    Login = Button(root, text="Log In", fg="black", command=login_clicked, font=pixel_font)
    Login_window = canvas.create_window(250, 100, anchor='center', window=Login)
    
    def register_clicked():
        root.destroy()
        age()

    Register = Button(root, text="Register", fg="black", command=register_clicked, font=pixel_font)
    Register_window = canvas.create_window(250, 140, anchor='center', window=Register)

    root.mainloop()

home()