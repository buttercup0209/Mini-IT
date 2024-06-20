import pygame
import os 
import random
from pygame.locals import *
from pygame import mixer

pygame.init()

clock = pygame.time.Clock()
FPS = 200

screen_width, screen_height = 1050, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Runner")

white = (255, 255, 255)
gray = (255, 255, 255)

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

hall = pygame.image.load(os.path.join('./Assets/Kash_room__2.png')).convert()
hall = pygame.transform.scale(hall, (room_width, room_height))

door_unlocked_image = pygame.image.load(os.path.join('./Assets/Door.png')).convert_alpha()
door_unlocked_image = pygame.transform.scale(door_unlocked_image, (150, 289))

fixed_door_position = (450, 70)
door_positions = [fixed_door_position] + [(150, 70), (750, 70)]
random.shuffle(door_positions[1:])

interaction_area = pygame.Rect(100, 300, 10, 10)

font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 36)

text_position = (50, 100)

note_image = pygame.image.load(os.path.join('./Assets/Note.png')).convert_alpha()
note_image = pygame.transform.scale(note_image, (400, 600))
note_rect = note_image.get_rect(center=(screen_width // 2, screen_height // 2))

button_rect = pygame.Rect(note_rect.right - 60, note_rect.top + 10, 50, 30)

chainsaw_guy_image = pygame.image.load(os.path.join('./Assets/chainsaw guy.png')).convert_alpha()
chainsaw_guy_image = pygame.transform.scale(chainsaw_guy_image, (400, 400))
chainsaw_guy_rect = chainsaw_guy_image.get_rect(center=(screen_width // 2, screen_height // 2))

restart_btn_image = pygame.image.load(os.path.join('./Assets/restart_btn.png')).convert_alpha()
restart_btn_image = pygame.transform.scale(restart_btn_image, (150, 50))
restart_btn_rect = restart_btn_image.get_rect(center=(screen_width // 2, screen_height // 2 + 220))
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [
            pygame.image.load(os.path.join('./Assets/girl.png')).convert_alpha(),
            pygame.image.load(os.path.join('./Assets/girl_move.png')).convert_alpha()
        ]
        self.images = [pygame.transform.scale(img, (225, 225)) for img in self.images]
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = (wall_thickness, room_height - wall_thickness - self.rect.height)
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

def reset_level():
    global door_positions, random_door, show_chainsaw_guy, show_next_level
    random.shuffle(door_positions[1:])
    random_door = random.choice(door_positions[1:])
    show_chainsaw_guy = False
    show_next_level = False
    player.rect.topleft = (wall_thickness, room_height - wall_thickness - player.rect.height)

def next_level():
    next_level_window = pygame.display.set_mode((screen_width, screen_height))
    next_level_window.fill(white)
    next_level_message = font.render("Welcome to level 2!", True, (0, 0, 0))
    next_level_window.blit(next_level_message, (screen_width // 2 - next_level_message.get_width() // 2, screen_height // 2 - next_level_message.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.quit()
    level_2()

def level_2() :

    pygame.mixer.pre_init(44100, -16, 2, 512)
    mixer.init()
    pygame.init()

    clock = pygame.time.Clock()
    fps = 50

    screen_width = 724
    screen_height = 724

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Level 2')

    font = pygame.font.SysFont('"./Assets/PixelifySans-Regular.ttf"', 70)
    font_score = pygame.font.SysFont('"./Assets/PixelifySans-Regular.ttf"', 30)

    tile_size = 36
    game_over = 0

    black = (0, 0, 0)

    snowball_img = pygame.image.load('./Assets/caneRedSmall.png')
    snowball_img = pygame.transform.scale(snowball_img, (snowball_img.get_width() * 1.5, snowball_img.get_height() * 1.5))  
    bg_img = pygame.image.load('./Assets/ice2.jpg')
    restart_img = pygame.image.load('./Assets/restart_btn.png')

    class Player():
        def __init__(self, x, y):
            self.reset(x, y)
    
        def reset(self, x, y):
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
            self.dead_image = pygame.image.load('./Assets/ghost.png')
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

                if pygame.sprite.spritecollide(self, world.alien_group, False):
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
            self.alien_group = pygame.sprite.Group()  

            tundraCenter_img = pygame.image.load('./Assets/tundraCenter_rounded.png')
            tundra_img = pygame.image.load('./Assets/tundra.png')

            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(tundraCenter_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect, tile)  
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(tundra_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect, tile) 
                        self.tile_list.append(tile)
                    if tile == 3:
                        coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                        self.coin_group.add(coin)  
                    if tile == 4:
                        alien = Enemy(col_count * tile_size, row_count * tile_size + 15)
                        self.alien_group.add(alien)  

                    col_count += 1
                row_count += 1

            score_coin = Coin(tile_size // 2, tile_size // 2)
            self.coin_group.add(score_coin)


        def draw(self):
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])
                pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
            self.coin_group.draw(screen)  
            self.alien_group.draw(screen)

    class Enemy(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('./Assets/alienBlue.png')
            scaled_width = int(tile_size * 1)  
            scaled_height = int(tile_size * 1)  
            self.image = pygame.transform.scale(img, (scaled_width, scaled_height))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y - tile_size // 3  
            self.move_direction = 1
            self.move_counter = 0

        def update(self):
            self.rect.x += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 40:
                self.move_direction *= -1
                self.move_counter *= -1

    class Coin(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('./Assets/coin.png')
            self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    class Door():
        def __init__(self, x, y):
            self.image = pygame.image.load('./Assets/level2.png')
            self.image = pygame.transform.scale(self.image, (tile_size * 2, tile_size * 2.5)) 
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def draw(self):
            screen.blit(self.image, self.rect)

    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.clicked = False

        def draw(self):
            action = False

            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                    action = True
                    self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            screen.blit(self.image, self.rect)

            return action

    def draw_text(text, font, text_col, x, y):
        font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 36)
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def reset_game():
        global game_over, score, world, player
        player.reset(45, screen_height - 130)
        world = World(world_data)
        game_over = 0
        score = 0

    def next_level_screen(): 
        font = pygame.font.Font("./Assets/PixelifySans-Regular.ttf", 36)
        next_level_window = pygame.display.set_mode((screen_width, screen_height))
        next_level_window.fill((255, 255, 255))
        next_level_message = font.render("Wow you passed that level", True, (0, 0, 0))
        next_level_window.blit(next_level_message, (screen_width // 2 - next_level_message.get_width() // 2, screen_height // 2 - next_level_message.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(1000)  
        print('Sucessful')    

    world_data = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 2, 0, 0, 0, 3, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 3, 2, 0, 0, 0, 3, 0, 0, 0, 3, 0, 2, 2, 1],
        [1, 0, 0, 0, 0, 3, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 1],
        [1, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 2, 1],
        [1, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1],
        [1, 0, 0, 0, 2, 2, 2, 0, 0, 4, 0, 0, 0, 4, 0, 0, 1, 1, 1, 1],
        [1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]
    ]

    player = Player(45, screen_height - 130)
    world = World(world_data)
    door = Door(screen_width - tile_size * 3.1, screen_height - tile_size * 17.6)

    restart_button = Button(screen_width // 2 - 65, screen_height // 2, restart_img)

    run = True
    score = 0  

    while run:
        clock.tick(fps)

        screen.blit(bg_img, (0, 0))
        screen.blit(snowball_img, (100, 100))

        world.draw()
        door.draw()

        if game_over == 0:
            world.alien_group.update()

        if pygame.sprite.spritecollide(player, world.coin_group, True):
            score += 1
        draw_text('X '  + str(score), font_score, black, tile_size - 3, 4)

        game_over = player.update(game_over)

        if game_over == -1:
            if restart_button.draw():
                reset_game()

        if player.rect.colliderect(door.rect):
            next_level_screen()
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

showing_note = False
show_chainsaw_guy = False
show_next_level = False

reset_level()

running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if showing_note and button_rect.collidepoint(event.pos):
                    showing_note = False
                elif show_chainsaw_guy and restart_btn_rect.collidepoint(event.pos):
                    reset_level()
                elif player.rect.colliderect(interaction_area):
                    showing_note = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for door_pos in door_positions:
                    door_rect = pygame.Rect(door_pos[0], door_pos[1], 150, 289)
                    if player.rect.colliderect(door_rect):
                        if door_pos == random_door:
                            show_chainsaw_guy = True
                        else:
                            show_next_level = True
                            next_level()

    all_sprites.update()
    
    screen.fill(white)
    pygame.draw.rect(screen, gray, ceiling)
    pygame.draw.rect(screen, gray, floor)
    screen.blit(hall,(0,0))
    
    for wall in walls:
        pygame.draw.rect(screen, gray, wall)
        
    for pos in door_positions:
        screen.blit(door_unlocked_image, pos)

    if player.rect.colliderect(interaction_area) and not showing_note:
        show_message = True
    else:
        show_message = False

    for door_pos in door_positions:
        door_rect = pygame.Rect(door_pos[0], door_pos[1], 150, 289)
        if player.rect.colliderect(door_rect) and not show_chainsaw_guy and not show_next_level:
            message = font.render("Click space to enter", True, (0, 0, 0))
            screen.blit(message, (door_pos[0], door_pos[1] - 30))
    
    if show_message:
        message = font.render("Click note to interact", True, (0, 0, 0))
        screen.blit(message, text_position)

    if showing_note:
        screen.blit(note_image, note_rect)
        pygame.draw.rect(screen, (100, 40, 0), button_rect)
        button_text = font.render("Exit", True, (255, 255, 255))
        screen.blit(button_text, (button_rect.x + 5, button_rect.y + 5))

    if show_chainsaw_guy:
        screen.blit(chainsaw_guy_image, chainsaw_guy_rect)
        screen.blit(restart_btn_image, restart_btn_rect)
    
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()


