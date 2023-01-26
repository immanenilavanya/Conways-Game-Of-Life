import Grid
import Neighbours

global grid
def commands():
    life = [list(i) for i in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbour_cells = Neighbours.neighbours(i, j, life)
            if life[i][j] == 0 and neighbour_cells == 3:
                grid[i][j] = 1
            elif life[i][j] == 1 and (neighbour_cells < 2 or neighbour_cells > 3):
                life[i][j] = 0
            else:
                grid[i][j] = life[i][j]
