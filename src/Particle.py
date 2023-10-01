from src.Vector2D import Vector2D
import math

class Particle():
    def __init__(self, position, limits, lifespan = 255, size = 25):
        self.position = position
        self.velocity = Vector2D(0,0)
        self.acceleration = Vector2D(0,0)    
        self.lifespan = lifespan
        self.size = size
        self.limits = limits

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        minFriction=0.9
        friction = minFriction+(1-minFriction)*math.sqrt(self.size/10)/self.size/10

        if self.position.x > self.limits[1].x-1:
            self.velocity.x = self.velocity.x*-1*friction
            
            self.position.x = self.limits[1].x-1
            self.velocity.y = self.velocity.y*friction

        if self.position.y > self.limits[1].y:
            self.velocity.y = self.velocity.y*-1*friction
            
            self.position.y = self.limits[1].y
            self.velocity.x = self.velocity.x*friction

        if self.position.x < self.limits[0].x+1:
            self.velocity.x = self.velocity.x*-1*friction

            self.position.x = self.limits[0].x+1
            self.velocity.y = self.velocity.y*friction

        if self.position.y < self.limits[0].y+1:
            self.velocity.y = self.velocity.y*-1*friction

            self.position.y = self.limits[0].y+1
            self.velocity.x = self.velocity.x*friction

    def update_resized(self,limits):
        self.limits = limits
        self.velocity += self.acceleration
        self.position += self.velocity
        minFriction=0.9
        friction = minFriction+(1-minFriction)*math.sqrt(self.size/10)/self.size/10

        if self.position.x > self.limits[1].x-1:
            self.velocity.x += (self.position.x-self.limits[1].x)*0.25
            
        if self.position.y > self.limits[1].y:
            self.velocity.y += (self.position.y-self.limits[1].y)*0.25

        if self.position.x < self.limits[0].x+1:
            self.velocity.x -= (self.limits[0].x-self.position.x)*0.25

        if self.position.y < self.limits[0].y+1:
            self.velocity.y -= (self.limits[0].y-self.position.y)*0.25

    def pre_render(self,matrix):
        matrix.place(self.size,self.position.round())

