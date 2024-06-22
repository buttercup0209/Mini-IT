import pygame
import os
from pygame.locals import * 
from pygame import mixer
import random
import sys 

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
        [1, 0, 0, 0, 0, 0, 3, 3, 3, 0, 2, 0, 3, 2, 2, 2, 2, 2, 2, 1],
        [1, 0, 0, 0, 0, 3, 2, 2, 2, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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


if __name__ == "__main__":
    main_game()