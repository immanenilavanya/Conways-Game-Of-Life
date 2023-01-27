Kimport pygame
import Grid
import ResetGrid

run = Grid.run
display = Grid.display

def buttons():
     
    global run
    start = pygame.Surface([100, 60])
    start.fill((46, 179, 55))
    display.blit(start, (620, 20))
    mouse_pos = pygame.mouse.get_pos()
    
    if 620 < mouse_pos[0] < 620 + 100 and 20 < mouse_pos[1] < 20 + 60:
        pygame.draw.rect(display, (255, 255, 255), (620, 20, 100, 60), 5)
        if pygame.mouse.get_pressed()[0]:
            run = True
    stop = pygame.Surface([100, 60])
    stop.fill((173, 35, 35))
    display.blit(stop, (620, 100))
    
    if 620 < mouse_pos[0] < 620 + 00 and 100 < mouse_pos[1] < 100 + 60:
        pygame.draw.rect(display, (255, 255, 255), (620, 100, 100, 60), 5)
        if pygame.mouse.get_pressed()[0]:
            run = False
    reset = pygame.Surface([100, 60])
    reset.fill((0, 0, 200))
    display.blit(reset, (620, 180))
    
    if 620 < mouse_pos[0] < 620 + 100 and 180 < mouse_pos[1] < 180 + 60:
        pygame.draw.rect(display, (255, 255, 255), (620, 180, 100, 60), 5)
        if pygame.mouse.get_pressed()[0]:
            run = False
            ResetGrid.resetGrid()

    return display        