from src.RenderMatrix import RenderMatrix
from src.Particle import Particle
from src.Vector2D import Vector2D
from time import sleep

import numpy as np
import numpy.random as rn
import keyboard
import curses

def main():
    screen = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    rows, cols = screen.getmaxyx()
    matrix = RenderMatrix(Vector2D(cols-1,rows-1),screen)
    
    particles = [Particle(Vector2D(rn.randint(rows),rn.randint(cols)),matrix.size, size=25) for _ in range(2)]
    for p in particles:
        p.velocity = Vector2D(rn.randint(0,10)/10,rn.randint(0,10)/10)
        p.acceleration = Vector2D(0,0.002)
    
    while True:
        screen.clear()

        for p in particles:
            p.update()
            p.pre_render(matrix)
        matrix.display()

        sleep(0.01)
        screen.refresh()
        if curses.is_term_resized(rows,cols):
            r,c = screen.getmaxyx()
            resized = Vector2D(c-1,r-1)
            matrix.resize(resized)
            for p in particles:
                p.resize(resized)
            rows,cols = screen.getmaxyx()

    curses.endwin()

if __name__ == '__main__':
    main()
