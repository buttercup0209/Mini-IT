import pygame 
import time 
import random 

pygame.init()

clock = pygame.time.Clock()
FPS = 60 

window_width = 1000
window_height = 600
window_title = pygame.display.set_caption("Maze Runner")
window = pygame.display.set_mode((window_width, window_height))

run = True
while run : 
    clock.tick(FPS)
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
            
    pygame.display.update()
    
pygame.quit() 