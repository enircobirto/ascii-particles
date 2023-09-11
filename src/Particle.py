from src.Vector2D import Vector2D

class Particle():
    def __init__(self, position, limits, lifespan = 255, size = 25):
        self.position = position
        self.velocity = Vector2D(0,0)
        self.acceleration = Vector2D(0,0)    
        self.lifespan = lifespan
        self.size = size
        self.limits = limits

    def update(self,limits):
        self.limits = limits
        self.velocity += self.acceleration
        self.position += self.velocity
        friction = 0.6

        if self.position.x >= self.limits[1].x:
            self.velocity.x += (self.position.x-self.limits[1].x)/2
            self.velocity.x = self.velocity.x*-1*friction
            
            self.position.x = self.limits[1].x-1

        if self.position.y >= self.limits[1].y:
            self.velocity.y += (self.position.y-self.limits[1].y)/1.5
            self.velocity.y = self.velocity.y*-1*friction
            
            self.position.y = self.limits[1].y
            self.velocity.x = self.velocity.x*0.9

        if self.position.x <= self.limits[0].x:
            self.velocity.x -= (self.limits[0].x-self.position.x)/2
            self.velocity.x = self.velocity.x*-1*friction

            self.position.x = self.limits[0].x+1

        if self.position.y <= self.limits[0].y:
            self.velocity.y -= (self.limits[0].y-self.position.y)/1.5
            self.velocity.y = self.velocity.y*-1*friction

            self.position.y = self.limits[0].y+1

    def pre_render(self,matrix):
        matrix.place(self.size,self.position.floor())

