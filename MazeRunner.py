import pygame
import os
from pygame.locals import *
from pygame import mixer

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
FPS = 200

screen_width, screen_height = 1000, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Runner")

white = (255, 255, 255)
gray = (255, 255, 255)
brown = (100, 40, 0)

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

hall = pygame.image.load(os.path.join('Assets', 'Pixel room.png')).convert()
hall = pygame.transform.scale(hall, (room_width, room_height))

no_box = pygame.image.load(os.path.join('Assets', 'NO BOX.png')).convert()
no_box = pygame.transform.scale(no_box, (room_width, room_height))

cat_image = pygame.image.load(os.path.join('Assets', 'cat.png')).convert_alpha()
cat_image = pygame.transform.scale(cat_image, (150, 150))

key_image = pygame.image.load(os.path.join('Assets', 'Key.png')).convert_alpha()
key_image = pygame.transform.scale(key_image, (50, 50))

door_locked_image = pygame.image.load(os.path.join('Assets', 'Locked_Door.png')).convert_alpha()
door_locked_image = pygame.transform.scale(door_locked_image, (144, 250))

interaction_area_width, interaction_area_height = 130, 150
interaction_area = pygame.Rect(
    screen_width - interaction_area_width - wall_thickness, 
    screen_height - interaction_area_height - wall_thickness, 
    interaction_area_width, 
    interaction_area_height
)

font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 30)
text_position = (
    screen_width // 2 - 150,
    screen_height - 50
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [
            pygame.image.load(os.path.join('Assets', 'girl.png')).convert_alpha(),
            pygame.image.load(os.path.join('Assets', 'girl_move.png')).convert_alpha()
        ]
        self.images = [pygame.transform.scale(img, (225, 225)) for img in self.images]
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = (room_width // 2, room_height//2)
        self.animation_time = 0.2  
        self.current_time = 0

    def update(self):
        keys = pygame.key.get_pressed()
        move_distance = 2
        moving = False
        if keys[pygame.K_LEFT]:
            if self.rect.left > wall_thickness:
                self.rect.x -= move_distance
                moving = True
        if keys[pygame.K_RIGHT]:
            if self.rect.right < room_width - wall_thickness:
                self.rect.x += move_distance
                moving = True
        if keys[pygame.K_UP]:
            if self.rect.top > wall_thickness and self.rect.top > 200:  
                self.rect.y -= move_distance
                moving = True
        if keys[pygame.K_DOWN]:
            if self.rect.bottom < room_height - wall_thickness:
                self.rect.y += move_distance
                moving = True

        if moving:
            self.current_time += clock.get_time() / 1000
            if self.current_time >= self.animation_time:
                self.current_image = (self.current_image + 1) % len(self.images)
                self.image = self.images[self.current_image]
                self.current_time = 0

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

interaction_occurred = False
small_cat_visible = False
key_found = False
door_visible = True
pixel_room_visible = True

door_x = 110
door_y = 430

door_interaction_area = pygame.Rect(door_x - 50, door_y - 50, 150, 130)  

class Button:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def level_3():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    mixer.init()
    pygame.init()

    clock = pygame.time.Clock()
    fps = 50

    screen_width = 724
    screen_height = 724

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Level 3')

    font = pygame.font.SysFont('Bauhaus 93', 70)
    font_score = pygame.font.SysFont('Bauhaus 93', 30)

    tile_size = 36
    game_over = 0

    Black =(0, 0, 0)

    cherry_img = pygame.image.load('cherry.png')
    bg_img = pygame.image.load('choco1.jpg')
    restart_img = pygame.image.load('restart_btn.png')

    pygame.mixer.music.load('music.wav')
    pygame.mixer.music.play(-1, 0.0, 5000)

    coin_fx = pygame.mixer.Sound('coin.wav')
    coin_fx.set_volume(2.5)
    jump_fx = pygame.mixer.Sound('jump.wav')
    jump_fx.set_volume(2.5)

    class Player():
        def __init__(self, x, y):
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num in range(1, 5):
                img_right = pygame.image.load(f'girl_walk{num}.png')
                img_right = pygame.transform.scale(img_right, (40, 80))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
            self.dead_image = pygame.image.load('ghost.png')
            self.image = self.images_right[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.vel_y = 0
            self.jumped = False
            self.direction = 0
            self.in_air = True

        def update(self, game_over):
            if game_over == 0:
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

                if pygame.sprite.spritecollide(self, world.bee_group, False):
                    game_over = -1

                if pygame.sprite.spritecollide(self, world.lava_group, False):
                    game_over = -1

                self.in_air = True
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
                            self.in_air = False

                self.rect.x += dx
                self.rect.y += dy

            elif game_over == -1:
                self.image = self.dead_image
                if self.rect.y > 200:
                    self.rect.y -= 5

            screen.blit(self.image, self.rect)

            return game_over

    class World():
        def __init__(self, data):
            self.tile_list = []
            self.coin_group = pygame.sprite.Group()  
            self.bee_group = pygame.sprite.Group()  
            self.lava_group = pygame.sprite.Group()

            chocoCenter_img = pygame.image.load('chocoCenter_rounded.png')
            choco_img = pygame.image.load('choco.png')

            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(chocoCenter_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect, tile)  
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(choco_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect, tile)  
                        self.tile_list.append(tile)
                    if tile == 3:
                        snail = Enemy(col_count * tile_size, row_count * tile_size + 15)
                        self.bee_group.add(snail)  
                    if tile == 4:
                        coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                        self.coin_group.add(coin)  
                    if tile == 5:
                        lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                        self.lava_group.add(lava)

                    col_count += 1
                row_count += 1

            score_coin = Coin(tile_size // 2, tile_size // 2)
            self.coin_group.add(score_coin)  

        def draw(self):
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])
                pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
            self.coin_group.draw(screen)  
            self.bee_group.draw(screen)  
            self.lava_group.draw(screen)

    class Enemy(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('bee.png')
            scaled_width = int(tile_size * 1)  
            scaled_height = int(tile_size * 1)  
            self.image = pygame.transform.scale(img, (scaled_width, scaled_height))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y - tile_size // 2.5  
            self.move_direction = 1
            self.move_counter = 0

        def update(self):
            self.rect.x += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 40:
                self.move_direction *= -1
                self.move_counter *= -1

    class Lava(pygame.sprite.Sprite):
        def __init__(self, x , y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('lava.png')
            scaled_width = int(tile_size * 1)  
            scaled_height = int(tile_size * 1)  
            self.image = pygame.transform.scale(img, (scaled_width, scaled_height))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y - tile_size // 2.5  

    class Coin(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('coin.png')
            self.image = pygame.transform.scale(img, (tile_size //2, tile_size // 2))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    class Door():
        def __init__(self, x, y):
            self.image = pygame.image.load('level3.png')
            self.image = pygame.transform.scale(self.image, (tile_size * 2, tile_size * 2.5)) 
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def draw(self):
            screen.blit(self.image, self.rect)

        def check_collision(self, player):
            if self.rect.colliderect(player.rect):
                message_window.open()

    class MessageWindow():
        def __init__(self):
            self.opened = False
            self.font = pygame.font.SysFont('Bauhaus 93', 30)
            self.text_surf = self.font.render('You healed the cat!', True, Black)
            self.text_rect = self.text_surf.get_rect(center=(screen_width // 2, screen_height // 3))

            self.image = pygame.image.load('eyepatch_cat.png').convert_alpha()
            self.image_rect = self.image.get_rect()
            self.image_rect.center = (screen_width // 2, screen_height // 2)

        def draw(self, screen):
            pygame.draw.rect(screen, (200, 200, 200), (screen_width // 4, screen_height // 4, screen_width // 2, screen_height // 2))
            screen.blit(self.text_surf, self.text_rect)

            img_x = (screen_width - self.image.get_width()) // 2  
            img_y = self.text_rect.bottom + 20  
            screen.blit(self.image, (img_x, img_y))
            

        def open(self):
            self.opened = True

        def close(self):
            self.opened = False

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    world_data = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 4, 0, 2, 2, 2, 2, 2, 0, 0, 0, 2, 0, 0, 2, 2, 1],
        [1, 0, 0, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0, 1],
        [1, 4, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 4, 1],
        [1, 2, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 2, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 4, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1],
        [1, 0, 0, 0, 4, 0, 0, 2, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 4, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 1],
        [1, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    player = Player(45, screen_height - 130)
    world = World(world_data)

    message_window = MessageWindow()
    door = Door(screen_width - tile_size * 3.1, screen_height - tile_size * 17.5)  

    restart_button = Button(restart_img, 297, 362) 

    run = True
    score = 0  
    show_restart_button = False

    def restart_game():
        nonlocal game_over, score, show_restart_button
        game_over = 0
        player.rect.x = 45
        player.rect.y = screen_height - 130  
        show_restart_button = False

    while run:
        clock.tick(fps)

        screen.blit(bg_img, (0, 0))
        screen.blit(cherry_img, (100, 100))

        world.draw()
        door.draw()

        if game_over == 0:
            world.bee_group.update()
            world.lava_group.update()

        if pygame.sprite.spritecollide(player, world.coin_group, True):
            score += 1
        draw_text('X ' + str(score), font_score, Black, tile_size - 3, 4)

        if game_over == -1:
            show_restart_button = True
            restart_button.draw(screen)

        game_over = player.update(game_over)

        door.check_collision(player)
        if message_window.opened:
            message_window.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_button.is_clicked(mouse_pos):
                        restart_game()

        pygame.display.update()

    pygame.quit()

def interaction_screen():
    global key_found
    large_cat_image = pygame.transform.scale(cat_image, (600, 600))
    cat_x = screen_width // 2 - 300
    cat_y = screen_height // 2 - 300
    cat_rect = pygame.Rect(cat_x, cat_y, 500, 500)
    key_rect = pygame.Rect(cat_x + 210, cat_y + 155, 150, 50)  
    exit_button_rect = pygame.Rect(screen_width - 110, 10, 100, 50)

    interacting = True

    while interacting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    mouse_x, mouse_y = event.pos
                    if key_rect.collidepoint(mouse_x, mouse_y):
                        key_found = True
                        interacting = False
                    elif exit_button_rect.collidepoint(mouse_x, mouse_y):
                        interacting = False 

        screen.blit(no_box, (0, 0))
        screen.blit(large_cat_image, (cat_x, cat_y))
        font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 36)
        text = font.render("Find where the key must be at. ", True, (0, 0, 0))
        screen.blit(text, text_position)
        pygame.draw.rect(screen, (200, 0, 0), exit_button_rect)
        exit_text = font.render("Exit", True, white)
        screen.blit(exit_text, (screen_width - 90, 20))
        pygame.display.flip()
        clock.tick(FPS)

    return True  

def unlock_door():
    new_window = pygame.display.set_mode((800, 600))
    new_window.fill(brown)
    font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 20)
    text = font.render("Complete the maze and collect all coins to heal the cat!", True, (0, 0, 0))
    new_window.blit(text, (100, 250))
    pygame.display.flip()
    pygame.time.wait(4000)
    level_3()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    if interaction_occurred:
        running = interaction_screen()  
        interaction_occurred = False  

    screen.fill(white)
    if small_cat_visible or not pixel_room_visible:
        screen.blit(no_box, (0, 0))
    else:
        pygame.draw.rect(screen, gray, ceiling)
        pygame.draw.rect(screen, gray, floor)
        screen.blit(hall, (0, 0))
        for wall in walls:
            pygame.draw.rect(screen, gray, wall)

    all_sprites.draw(screen)

    screen.blit(door_locked_image, (door_x, door_y))

    if player.rect.colliderect(door_interaction_area):
        if key_found:
            font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 30)
            text = font.render("Click 'Space' to unlock the door.", True, (0, 0, 0))
            screen.blit(text, (door_x + 50, door_y - 60))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                unlock_door()
                running = False  
        else:
            font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 30)
            text = font.render("The door is locked. Find the key.", True, (0, 0, 0))
            screen.blit(text, (door_x - 30, door_y - 20))

    if player.rect.colliderect(interaction_area) and not small_cat_visible and not key_found:
        font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 30)
        text = font.render("Click 'Space' to interact.", True, (0, 0, 0))
        screen.blit(text, text_position)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            small_cat_visible = True
            pixel_room_visible = False

    if small_cat_visible:
        font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 30)
        small_cat_text = font.render("Oh No! It's an injured kitty!", True, (0, 0, 0))
        screen.blit(cat_image, (screen_width - interaction_area_width - 10 - wall_thickness, screen_height - interaction_area_height - wall_thickness))
        screen.blit(small_cat_text, (screen_width - interaction_area_width - 400 - wall_thickness, screen_height - interaction_area_height + 150 - wall_thickness - 50))
        mouse_pos = pygame.mouse.get_pos()
        small_cat_rect = pygame.Rect(screen_width - interaction_area_width - 10 - wall_thickness, screen_height - interaction_area_height - wall_thickness, 150, 150)
        if small_cat_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:  
                interaction_occurred = True
                small_cat_visible = True

    if key_found:
        screen.blit(key_image, (50, 50))  

    pygame.display.flip()

pygame.quit()


