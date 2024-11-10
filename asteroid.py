import pygame, random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            x = random.uniform(20,50)
            v1 = self.velocity.rotate(x)
            print(v1)
            v2 = self.velocity.rotate(-x)
            print(v2)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            print(new_asteroid_1)
            new_asteroid_1.velocity = v1 * 1.2
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            print(new_asteroid_2)
            new_asteroid_2.velocity = v2 * 1.2