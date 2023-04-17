import pyautogui as pg
import numpy as np
import time

grid = []
while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break

    print('Row' + str(len(grid)) + ' complete')

time.sleep(7)


def possible(x, y, n):
    for i in range(0, 9):
        if grid[i][x] == n and i != y: # checks for number (n) in Rows
            return False

    for i in range(0, 9):
        if grid[y][i] == n and i != x: # checks for number (n) in Columns
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3): # checks for numbers in box
            if grid[Y][X] == n:
                return False

    return True


def Print(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter) % 9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0

                return
    Print(grid)
    input('More?')


solve()
