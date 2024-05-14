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

#assets
setting = pygame.image.load("./assets/setting_symbol.png")

#Game variable 
start_game = False

#class button 
class Button() :
    def __init__(self, x, y, image) :
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
    def draw(self) :
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos) :
            if pygame.mouse.get_pressed()[0] == 1 :
                action = True
        
        window.blit(self.image, (self.rect.x, self.rect.y))
        
        return action
    
#buttons
setting_button = Button(900, 10, setting)

run = True
while run : 
    clock.tick(FPS)
    
    setting_button.draw() == True
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
            
    pygame.display.update()
    
pygame.quit() 

