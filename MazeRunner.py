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
    pygame.init()

    clock = pygame.time.Clock()
    FPS = 200

    screen_width, screen_height = 1000, 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze Runner")

    white = (255, 255, 255)
    gray = (128, 128, 128)
    brown = (100,40,0)

    room_width, room_height = 1050, 700
    wall_thickness = 10

    walls = [
        pygame.Rect(0, 0, room_width, wall_thickness),
        pygame.Rect(0, 0, wall_thickness, room_height),
        pygame.Rect(room_width - wall_thickness, 0, wall_thickness, room_height),
        pygame.Rect(0, room_height - wall_thickness, room_width, wall_thickness),
    ]

    ceiling = pygame.Rect(0, 0, room_width, wall_thickness)
    floor = pygame.Rect(0, room_height - wall_thickness, room_width, wall_thickness)

    hall = pygame.image.load(os.path.join('Assets', 'Room3.png')).convert()
    hall = pygame.transform.scale(hall, (room_width - 50, room_height))

    # Load and scale the door image
    door_image = pygame.image.load(os.path.join('./Assets/Door.png')).convert_alpha()
    door_image = pygame.transform.scale(door_image, (150, 289))

    # Define door positions
    fixed_door_position = (150, 70)
    door_positions = [fixed_door_position] + [(710, 70)]

    interaction_area = pygame.Rect(680, 120, 200, 150)

    font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 36)

    text_position = (680, 200)


    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            original_image = pygame.image.load(os.path.join('Assets', 'girl.png')).convert_alpha()
            self.image = pygame.transform.scale(original_image, (225, 225))
            self.rect = self.image.get_rect()
            self.rect.center = (screen_width // 2, screen_height - self.rect.height // 2)

        def update(self):
            keys = pygame.key.get_pressed()
            move_distance = 2
            if keys[pygame.K_LEFT]:
                if self.rect.left > wall_thickness:
                    self.rect.x -= move_distance
            if keys[pygame.K_RIGHT]:
                if self.rect.right < room_width - wall_thickness:
                    self.rect.x += move_distance
            if keys[pygame.K_UP]:
                if self.rect.top > wall_thickness and self.rect.top > 200:
                    self.rect.y -= move_distance
            if keys[pygame.K_DOWN]:
                if self.rect.bottom < room_height - wall_thickness:
                    self.rect.y += move_distance

    def door1():

        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        pygame.init()

        clock = pygame.time.Clock()
        fps = 50

        screen_width = 724
        screen_height = 724

        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Level 1')

        font = pygame.font.SysFont('Bauhaus 93', 70)
        font_score = pygame.font.SysFont('Bauhaus 93', 30)

        tile_size = 36

        black = (0, 0, 0)

        clock_img = pygame.image.load('./Assets/clock.png')
        bg_img = pygame.image.load('./Assets/bluebg.jpg')

        pygame.mixer.music.load('./Assets/music.wav')
        pygame.mixer.music.play(-1, 0.0, 5000)

        coin_fx = pygame.mixer.Sound('./Assets/coin.wav')
        coin_fx.set_volume(2.5)
        jump_fx = pygame.mixer.Sound('./Assets/jump.wav')
        jump_fx.set_volume(2.5)

        class Player():
            def __init__(self, x, y):
                self.images_right = []
                self.images_left = []
                self.index = 0
                self.counter = 0
                for num in range(1, 5):
                    img_right = pygame.image.load(f'./Assets/girl_walk{num}.png')
                    img_right = pygame.transform.scale(img_right, (40, 80))
                    img_left = pygame.transform.flip(img_right, True, False)
                    self.images_right.append(img_right)
                    self.images_left.append(img_left)
                self.image = self.images_right[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.vel_y = 0
                self.jumped = False
                self.direction = 0

            def update(self):
                dx = 0
                dy = 0
                walk_cooldown = 5

                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE] and self.jumped == False:
                    self.vel_y = -15
                    self.jumped = True
                if key[pygame.K_SPACE] == False:
                    self.jumped = False
                if key[pygame.K_LEFT]:
                    dx -= 5
                    self.counter += 1
                    self.direction = -1
                if key[pygame.K_RIGHT]:
                    dx += 5
                    self.counter += 1
                    self.direction = 1
                if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                    self.counter = 0
                    self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                if self.counter > walk_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images_right):
                        self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                self.vel_y += 1
                if self.vel_y > 10:
                    self.vel_y = 10
                dy += self.vel_y

                for tile in world.tile_list:
                    if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                        dx = 0
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                            self.vel_y = 0
                        elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel_y = 0

                self.rect.x += dx
                self.rect.y += dy

                screen.blit(self.image, self.rect)

        class World():
            def __init__(self, data):
                self.tile_list = []
                self.coin_group = pygame.sprite.Group()  

                metalc_img = pygame.image.load('./Assets/metalCenter.png')
                metalcs_img = pygame.image.load('./Assets/metalCenterSticker.png')

                row_count = 0
                for row in data:
                    col_count = 0
                    for tile in row:
                        if tile == 1:
                            img = pygame.transform.scale(metalc_img, (tile_size, tile_size))
                            img_rect = img.get_rect()
                            img_rect.x = col_count * tile_size
                            img_rect.y = row_count * tile_size
                            tile = (img, img_rect, tile)  
                            self.tile_list.append(tile)
                        if tile == 2:
                            img = pygame.transform.scale(metalcs_img, (tile_size, tile_size))
                            img_rect = img.get_rect()
                            img_rect.x = col_count * tile_size
                            img_rect.y = row_count * tile_size
                            tile = (img, img_rect, tile) 
                            self.tile_list.append(tile)
                        if tile == 3:
                            coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                            self.coin_group.add(coin) 
                        col_count += 1
                    row_count += 1

                score_coin = Coin(tile_size // 2, tile_size // 2)
                self.coin_group.add(score_coin)  

            def draw(self):
                for tile in self.tile_list:
                    screen.blit(tile[0], tile[1])
                    pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
                self.coin_group.draw(screen)  


        class Coin(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                img = pygame.image.load('./Assets/coin.png')
                self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
                self.rect = self.image.get_rect()
                self.rect.center = (x, y)


        class Door(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                img = pygame.image.load('./Assets/level1.png')  
                self.image = pygame.transform.scale(img, (tile_size * 2.5, tile_size * 3))  
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y


        def draw_text(text, font, text_col, x, y):
            font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 36)
            img = font.render(text, True, text_col)
            screen.blit(img, (x, y))


        def next_level_screen():
            font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 36)
            next_level_window = pygame.display.set_mode((screen_width, screen_height))
            next_level_window.fill((255, 255, 255))
            next_level_message = font.render("Next Level", True, (0, 0, 0))
            next_level_window.blit(next_level_message, (screen_width // 2 - next_level_message.get_width() // 2, screen_height // 2 - next_level_message.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(1000)  

        world_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 1],
            [1, 0, 0, 0, 2, 2, 2, 0, 3, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 1],
            [1, 3, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1],
            [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 2, 3, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 3, 0, 3, 0, 2, 0, 3, 2, 2, 2, 2, 2, 2, 1],
            [1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        player = Player(45, screen_height - 130)
        world = World(world_data)
        door = Door(screen_width - tile_size * 3.3, screen_height - tile_size * 19.1)  

        run = True
        score = 0  

        while run:
            clock.tick(fps)

            screen.blit(bg_img, (0, 0))
            screen.blit(clock_img, (100, 100))

            world.draw()
            screen.blit(door.image, door.rect)  

            if pygame.sprite.spritecollide(player, world.coin_group, True):
                score += 1
                coin_fx.play()
            draw_text('X '  + str(score), font_score, black, tile_size - 3, 4)

            player.update()

            if player.rect.colliderect(door.rect):
                next_level_screen()
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

        pygame.quit()

    def display_initial_text(screen, text, pos, duration):
        collection = [word.split(' ') for word in text.splitlines()]
        font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 60)
        space = font.size(' ')[0]
        x, y = pos
        start_time = pygame.time.get_ticks()

        while True:
            elapsed_time = pygame.time.get_ticks() - start_time
            if elapsed_time > duration:
                break
            
            screen.fill(gray)
            x, y = pos  # Reset position for each frame
            for lines in collection:
                for words in lines:
                    word_surface = font.render(words, True, (0, 0, 0))
                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= screen_width:
                        x = pos[0]
                        y += word_height
                    screen.blit(word_surface, (x, y))
                    x += word_width + space
                x = pos[0]
                y += word_height

            pygame.display.flip()
            clock.tick(FPS)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def main_game():
        screen.fill(gray)
        display_initial_text(screen, "OH NO! \nYou've gotten yourself trapped! \nNow you'll have to find your way out.", (100, 150), 3000)


        player = Player()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)

        running = True
        while running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            all_sprites.update()

            screen.fill(white)
            pygame.draw.rect(screen, gray, ceiling)
            pygame.draw.rect(screen, gray, floor)
            screen.blit(hall, (0, 0))

            for wall in walls:
                pygame.draw.rect(screen, gray, wall)

            door_enter_text_displayed = False

            for pos in door_positions:
                screen.blit(door_image, pos)
                door_rect = door_image.get_rect(topleft=pos)
                if player.rect.colliderect(door_rect):
                    text_surface = font.render("Click space to enter", True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=(door_rect.centerx, door_rect.top - 20))
                    screen.blit(text_surface, text_rect)
                    door_enter_text_displayed = True
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        level = door_positions.index(pos) + 1
                        door1()


            all_sprites.draw(screen)
            pygame.display.flip()

        pygame.quit()

    main_game()

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