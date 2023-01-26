import pygame
import random

size = (750, 600)
display = pygame.display.set_mode(size)

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
                display.blit(cell, (j * 20, i * 20))
    return cell


def layout():

    for i in range(len(grid) + 1):
        pygame.draw.line(display, (51, 51, 51), ((i * 20), 0), (i * 20, 600), 2)
    for j in range(len(grid[0]) + 1):
        pygame.draw.line(display, (51, 51, 51), (0, (j * 20)), (600, j * 20), 2)


cell_layout()
layout()
pygame.desplay.flip()
delay.tick(1)
