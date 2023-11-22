from src.Vector2D import Vector2D
from utils.grayscale import grayscale

import numpy as np
import skimage
import curses

from time import sleep
import pywinctl
from math import floor
from subprocess import check_output

class RenderMatrix():
    def __init__(self, size, screen, window):
        self.size = size
        self.grid = np.array([[0 for _ in range(size.x)] for _ in range(size.y)])
        self.screen = screen
        self.window = window

    def place(self, particleSize, position):
        try:
            self.grid[position.y][position.x] += particleSize
        except:
            pass

    def particle_head(self,particleSize,position):
        try:
            limits = self.get_limits()
            self.screen.addstr(position.y-limits[0].y-1,position.x-limits[0].x,grayscale(particleSize),curses.A_BOLD)
        except:
            pass

    def display(self):
        c = 450
        curses.init_color(curses.COLOR_GREEN, c,c,c)
        curses.init_pair(1, curses.COLOR_GREEN,-1)
        limits = self.get_limits()
        for y,col in enumerate(self.grid):
            for x,cell in enumerate(col):
                if cell != 0:
                    if cell > 300:
                        self.grid[y][x] = 300
                    try:
                        self.screen.addch(y-limits[0].y-1,x-limits[0].x,grayscale(cell),curses.color_pair(1))
                        #self.screen.addstr(x-limits[0].x,y-limits[0].y,str(Vector2D(x,y)))
                        # self.screen.addstr(x-limits[0].x,y-limits[0].y,str(self.limits))
                    except:
                        pass
                    if cell>0:
                        self.grid[y][x] -= 1

    def get_limits(self):
        box = self.window.box
        rows, cols = self.screen.getmaxyx()
        self.max = Vector2D(cols,rows) 
        self.fontsize = Vector2D(round(box[2]/self.max.x),round(box[3]/self.max.y))
        limitStart = Vector2D(floor(box[0]/self.fontsize.x),floor(box[1]/self.fontsize.y))
        limits = [limitStart,limitStart + self.max]
        return limits
