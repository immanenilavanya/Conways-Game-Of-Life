def neighbours(x, y, life):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            row = x + i
            col = y + j
            if col > len(life[0]) - 1:
                col = 0
            if row > len(life) -1:
                row = 0
            count += life[row][col]
    return count - life[x][y]
