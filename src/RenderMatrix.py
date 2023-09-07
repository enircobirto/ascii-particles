from src.Vector2D import Vector2D
from utils.grayscale import grayscale

import numpy as np
import skimage

from time import sleep

class RenderMatrix():
    def __init__(self, size, screen):
        self.size = size
        self.grid = np.array([[0 for _ in range(size.x)] for _ in range(size.y)])
        self.screen = screen

    def place(self, particleSize, position):
        try:
            self.grid[position.y][position.x] += particleSize
        except:
            pass

    def display(self):
        for x,col in enumerate(self.grid):
            for y,cell in enumerate(col):
                if cell != 0:
                    try:
                        self.screen.addch(x,y,grayscale(cell))
                    except:
                        pass
                    if cell>0:
                        self.grid[x][y] -= 1
                    else:
                        self.grid[x][y] = 0

    def resize(self,after):
        self.grid = skimage.transform.resize(self.grid,np.array([after.y,after.x]))
        self.size = Vector2D(after.x,after.y)
