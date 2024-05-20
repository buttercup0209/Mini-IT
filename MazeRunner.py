import pygame

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Runner")

white = (255, 255, 255)
gray = (254, 254, 254)

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