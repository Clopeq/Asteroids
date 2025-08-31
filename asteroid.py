import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.position = pygame.Vector2(x, y)
        self.rotation = 0

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rotation = random.uniform(20, 50)
        new_velocity1 = 1.2 * self.velocity.rotate(rotation)
        new_velocity2 = 1.2 * self.velocity.rotate(-rotation)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = new_velocity1
        asteroid2.velocity = new_velocity2

    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)