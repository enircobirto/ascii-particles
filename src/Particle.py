from src.Vector2D import Vector2D

class Particle():
    def __init__(self, position, lifespan = 255, size = 1):
        self.position = position
        self.velocity = Vector2D(0,0)
        self.acceleration = Vector2D(0,0)    
        self.lifespan = lifespan
        self.size = size

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity

    def pre_render(self,matrix):
        matrix.place(self.size,self.position)

