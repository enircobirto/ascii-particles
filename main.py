from src.RenderMatrix import RenderMatrix
from src.Particle import Particle
from src.Vector2D import Vector2D

from time import sleep

import numpy.random as rn
import pywinctl
import curses


def main():
    screen = curses.initscr()
    try:
        curses.curs_set(0)
    except:
        pass
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.use_default_colors()
    curses.use_env(True)

    rows, cols = screen.getmaxyx()
    window = pywinctl.getActiveWindow()
    matrix = RenderMatrix(Vector2D(300,100),screen,window)
    limits = matrix.get_limits()
    
    particles = [Particle(Vector2D(rn.randint(cols)+limits[0].x,rn.randint(rows)+limits[0].y),matrix.size, size=rn.randint(20)+10) for _ in range(4)]
    for p in particles:
        p.velocity = Vector2D(rn.randint(0,10)/10,rn.randint(0,10)/10)
        p.acceleration = Vector2D(0,0.006)
    
    while True:
        screen.clear()

        for p in particles:
            p.update(matrix.get_limits())
            p.pre_render(matrix)

        matrix.display()

        for p in particles:
            matrix.particle_head(p.size,p.position.round())
        sleep(0.01)
        screen.refresh()

    curses.endwin()

if __name__ == '__main__':
    main()
