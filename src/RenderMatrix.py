from src.Vector2D import Vector2D

class RenderMatrix():
    def __init__(self, size):
        self.size = size
        self.grid = [[0]*size.x]*size.y

    def place(self, particleSize, position):
        self.grid[position.x][position.y] += particleSize

    def print_grid(self):
        print(self.grid)

