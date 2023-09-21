from src.RenderMatrix import RenderMatrix
from src.Particle import Particle
from src.Vector2D import Vector2D

from time import sleep
from math import sqrt

import numpy as np
import curses

def main():
    screen = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    rows, cols = screen.getmaxyx()
    matrix = RenderMatrix(Vector2D(cols-1,rows-1),screen)

    bars = 3
    sizeparticles = 5
    nparticles = 140
    particles = []
    
    for bar in range(bars):
        randomvel = 0.1+np.random.randint(100)/100
        particles+=[Particle(
            Vector2D(
                (cols/bars)*bar,
                np.random.randint(rows)
            ),
            matrix,
            size=sizeparticles,
            velocity = Vector2D(randomvel,10*np.random.randint(100)/100)
        ) for _ in range(nparticles)]

    #particles += [Particle(Vector2D(np.random.randint(cols/bars),np.random.randint(rows)),matrix,size=sizeparticles) for _ in range(nparticles)]
    for p in particles:
        p.acceleration = Vector2D(0,0.0)#+(np.random.randint(100)-100)/10000)

    while True:
        screen.clear()
        for p in particles:
            p.update()
            p.pre_render(matrix)

        matrix.display()

        screen.refresh()
        sleep(0.02)

    curses.endwin()

if __name__ == '__main__':
    main()
