import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __int__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand = random.uniform(20, 50)
        veca = self.velocity.rotate(rand)
        vecb = self.velocity.rotate((0 - rand))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a = Asteroid(self.position.x, self.position.y, new_radius)
        a.velocity = veca * 1.2
        b = Asteroid(self.position.x, self.position.y, new_radius)
        b.velocity = vecb * 1.2