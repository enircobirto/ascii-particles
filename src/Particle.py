from src.Vector2D import Vector2D

class Particle():
    def __init__(self, position, matrix, lifespan = 255, size = 25, velocity = Vector2D(0,0)):
        self.position = position
        self.velocity = velocity
        self.acceleration = Vector2D(0,0)    
        self.initspan = lifespan
        self.lifespan = lifespan
        self.initsize = size
        self.size = size
        self.max = matrix.size

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        friction = 0.5
        if self.position.x > self.max.x-1:
            self.position.x = self.max.x-1
            self.velocity.x = self.velocity.x*-1
        
        if self.position.y > self.max.y-1:
            self.position.y = 0+self.velocity.y
        
        if self.position.x < 0:
            self.position.x = 1
            self.velocity.x = self.velocity.x*-1
        
        if self.position.y < 0:
            self.position.y = self.max.y-self.velocity.y

        if self.size > 255:
            self.size = 255

        if self.lifespan < 0:
            self.lifespan = self.initspan
        
        self.size = self.initsize*(self.lifespan/255)

        self.lifespan-=2

    def pre_render(self,matrix):
        matrix.place(self.size,self.position.round())

