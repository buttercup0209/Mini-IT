import pygame
import os

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Runner")

white = (255, 255, 255)
gray = (255, 255, 255)

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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(os.path.join('images', 'Ground (78x58).png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (room_width // 2, room_height//2)

    def update(self):
        keys = pygame.key.get_pressed
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
    
    screen.fill(white)
    pygame.draw.rect(screen, gray, ceiling)
    pygame.draw.rect(screen, gray, floor)
    for wall in walls:
        pygame.draw.rect(screen, gray, wall)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()