import random
import tkinter as tk
from tkinter import messagebox
from snake import *


def redrawWindow(surface):
    global snack
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface=surface)
    pg.display.update()


def drawGrid(w, r, surface):
    size_Btwn = w // r

    x = 0
    y = 0

    for l in range(rows):
        x += size_Btwn
        y += size_Btwn

        pg.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pg.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def randomSnack(row_s, item):
    positions = item.body
    while True:
        x = random.randrange(row_s)
        y = random.randrange(row_s)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break
    return x, y


def message_Box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global snack
    snack = Cube(randomSnack(rows, snake), color=(0, 255, 0))
    while flag:
        pg.time.delay(50)
        clock.tick(10)
        snake.move()
        if snake.body[0].pos == snack.pos:
            snake.addCube()
            snack = Cube(randomSnack(rows, snake), color=(0, 255, 0))
        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1:])):
                print('score: ', len(snake.body))
                message_Box("you lost !", "play again")
                snake.reset((10, 10))
                break

        redrawWindow(window)


width = 500
rows = 20
window = pg.display.set_mode((width, width))
flag = True
snake = Snake((255, 0, 0), (10, 10))
clock = pg.time.Clock()
snack = Cube(randomSnack(rows, snake), color=(0, 255, 0))

if __name__ == '__main__':
    main()
