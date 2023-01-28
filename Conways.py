import pygame 
import random

size = (700, 600)
display = pygame.display.set_mode(size)
pygame.display.set_caption("Conway's Game of Life")

delay = pygame.time.Clock()
done = False

grid = [[random.choice([False, True]) for i in range(30)] for j in range(30)]
run = False


def cell_layout():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[j][i]:
                cell = pygame.Surface((18, 18))
                cell.fill((255, 255, 255))
                display.blit(cell, (j*20, i*20))

def layout():
    for i in range(len(grid) + 1):
        pygame.draw.line(display, (0, 0, 0), ((i * 20), 0), (i * 20, 600), 2)
    for j in range(len(grid[0]) + 1):
        pygame.draw.line(display, (0, 0, 0), (0, (j * 20)), (600, j * 20), 2)
    
def commands():
    life = [list(i) for i in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbor_cells = neighbors(i, j, life)
            if life[i][j] == 0 and neighbor_cells == 3:
                grid[i][j] = 1
            elif life[i][j] == 1 and (neighbor_cells < 2 or neighbor_cells > 3):
                grid[i][j] = 0
                
            else:
                grid[i][j] = life[i][j]
                
def neighbors(x, y, life):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            row = x+i
            column = y+j
            if column > len(life[0]) - 1:
                column = 0
            if row > len(life) - 1:
                row = 0
            count += life[row][column]
    return count - life[x][y]

def buttons():
    global run

    start = pygame.Surface([60, 60])
    start.fill((48, 186, 143))
    display.blit(start, (620, 20))
    mouse_pos = pygame.mouse.get_pos()

    if 620 < mouse_pos[0] < 620+60 and 20 < mouse_pos[1] < 20+60:
        pygame.draw.rect(display, (255, 255, 255), (620, 20, 60, 60), 5)
        if pygame.mouse.get_pressed()[0]:
            run = True

    stop = pygame.Surface([60, 60])
    stop.fill((222, 165, 164))
    display.blit(stop, (620, 100))

    if 620 < mouse_pos[0] < 620 + 60 and 100 < mouse_pos[1] < 60 + 60:
        pygame.draw.rect(display, (255, 255, 255), (620, 100, 60, 60), 5)
        if pygame.mouse.get_pressed()[0]:
            run = False
            
    reset = pygame.Surface([60, 60])
    reset.fill((80, 120, 160))
    display.blit(reset, (620, 180))

    if 620 < mouse_pos[0] < 620 + 60 and 180 < mouse_pos[1] < 180 + 60:
        pygame.draw.rect(display, (255, 255, 255), (620, 180, 60, 60), 5)
        if pygame.mouse.get_pressed()[0]:
            run = False
            resetGrid()
            
def resetGrid():
    global grid
    grid = [[random.choice([0, 1]) for i in range(30)] for j in range(30)]
    
while not done:
    display.fill(0)

    cell_layout()
    if run:
        commands()
    layout()

    buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.mouse.get_pos()

    pygame.display.flip()
    delay.tick(10)
