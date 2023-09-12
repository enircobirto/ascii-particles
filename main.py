from src.RenderMatrix import RenderMatrix
from src.Particle import Particle
from src.Vector2D import Vector2D

from time import sleep

import subprocess
import numpy.random as rn
import re
import numpy as np
import keyboard
import curses

def main():
    screen = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    curses.use_env(True)

    rows, cols = screen.getmaxyx()


    activewindow = str(subprocess.check_output(["hyprctl","activewindow"]))
    windowId = re.findall(r"Window (.*?) ->",activewindow)[0]
    windowSize = re.findall(r"size: (.*?)\\n",activewindow)[0].split(",")
    windowPos = re.findall(r"at: (.*?)\\n",activewindow)[0].split(",")
    box = [int(i) for i in windowPos + windowSize]
    
    matrix = RenderMatrix(Vector2D(300,100),screen,box,windowId)

    matrix.display()
    
    particles = [Particle(Vector2D(rn.randint(rows),rn.randint(cols)),matrix.size, size=10) for _ in range(25)]
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
