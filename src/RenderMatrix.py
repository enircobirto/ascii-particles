from src.Vector2D import Vector2D
from utils.grayscale import grayscale

import numpy as np
import skimage

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

    def display(self):
        self.box = self.window.box
        rows, cols = self.screen.getmaxyx()
        self.max = Vector2D(cols,rows) 
        self.fontsize = Vector2D(round(self.box[2]/self.max.x),round(self.box[3]/self.max.y))
        limitStart = Vector2D(floor(self.box[0]/self.fontsize.x),floor(self.box[1]/self.fontsize.y))
        self.limits = [limitStart,limitStart + self.max]
        for y,col in enumerate(self.grid):
            for x,cell in enumerate(col):
                if cell != 0:
                    try:
                        self.screen.addch(y-limitStart.y,x-limitStart.x,grayscale(cell))
                        #self.screen.addstr(x-limitStart.x,y-limitStart.y,str(Vector2D(x,y)))
                        # self.screen.addstr(x-limitStart.x,y-limitStart.y,str(self.limits))
                    except:
                        pass
                    if cell>0:
                        self.grid[y][x] -= 5
                    else:
                        self.grid[y][x] = 0
                    if cell>255:
                        cell = 255
