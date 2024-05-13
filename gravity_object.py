import random
import math

import pygame


class GravityObject:

    id_counter = 1

    def __init__(self, radius=100, density=1, position=pygame.Vector2(0,0), velocity=pygame.Vector2(0,0), acceleration=pygame.Vector2(0,0), fixed=False):
        self.id = GravityObject.id_counter
        GravityObject.id_counter += 1

        self.radius = radius # Pixels
        self.density = density # kg/pixel

        self.mass = (math.pi * math.pow(self.radius, 2)) * self.density
        
        self.position = position.copy()
        self.velocity = velocity.copy() # pixels/frame
        self.acceleration = acceleration.copy() # pixels/frame^2

        self.fixed = fixed

        self.color = pygame.color.Color(random.randint(100,255),random.randint(100,255),random.randint(100,255))

    def update(self, force, delta):
        if self.fixed: return

        self.acceleration.x += force.x / self.mass * delta
        self.acceleration.y += force.y / self.mass * delta

        self.velocity += self.acceleration * delta
        self.position += self.velocity * delta

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def __eq__(self, value: object) -> bool:
        if type(value) != GravityObject:
            return False

        return self.id == value.id