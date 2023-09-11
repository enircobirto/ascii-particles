from src.RenderMatrix import RenderMatrix
from src.Particle import Particle
from src.Vector2D import Vector2D

from xdo import Xdo

from time import sleep

import numpy.random as rn
import numpy as np
import pywinctl
import keyboard
import curses


def main():
    screen = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    curses.use_env(True)

    rows, cols = screen.getmaxyx()
    window = pywinctl.getActiveWindow()
    matrix = RenderMatrix(Vector2D(300,100),screen,window)
    matrix.display()
    
    particles = [Particle(Vector2D(rn.randint(rows),rn.randint(cols)),matrix.size, size=40) for _ in range(300)]
    for p in particles:
        p.velocity = Vector2D(rn.randint(0,10)/10,rn.randint(0,10)/10)
        p.acceleration = Vector2D(0,0.002)
    
    while True:
        screen.clear()

        for p in particles:
            p.update(matrix.limits)
            p.pre_render(matrix)
        matrix.display()

        sleep(0.01)
        screen.refresh()

    curses.endwin()

if __name__ == '__main__':
    main()
