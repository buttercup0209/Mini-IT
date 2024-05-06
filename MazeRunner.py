import pygame
import sys
pygame.init()
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
CELL-SIZE = 36
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1]
    [2, 0, 0, 0, 0, 1, 0, 3]
    [1, 1, 1, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 1, 1, 0, 1]
    [1, 1, 1, 0, 1, 1, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 1]
    [1, 1, 1, 1, 1, 1, 1, 1]
]
player_pos = [1, 0]
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Maze Runner")
while True;
    screen.fill(WHITE)
    for y in range(len(maze));
        for x in range(len(maze[y]));
            if maze[y][x] == 1;
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE))

for event in pygame.event.get();
    if event.type == pygame.QUIT;
        pygame.quit()
        sys.exit()

pygame.display.flip()

