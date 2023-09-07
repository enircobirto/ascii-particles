from src.Vector2D import Vector2D
from utils.grayscale import grayscale

class RenderMatrix():
    def __init__(self, size, screen):
        self.size = size
        self.grid = [[0.0 for _ in range(size.x)] for _ in range(size.y)]
        self.screen = screen

    def place(self, particleSize, position):
        self.grid[position.y][position.x] += particleSize

    def display(self):
        for x,col in enumerate(self.grid):
            for y,cell in enumerate(col):
                if cell != 0:
                    try:
                        self.screen.addstr(x,y,grayscale(cell))
                    except:
                        pass
                    if cell>0:
                        self.grid[x][y] -= 1
                    else:
                        self.grid[x][y] = 0
                    if cell>500:
                        self.grid[x][y] = 500

                        
