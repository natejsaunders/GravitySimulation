import random
import math

import pygame


class GravityObject:

    # Bad practice
    SCREEN_SIZE = pygame.Vector2(1280, 720)

    TRAIL_LIMIT = 1000

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

        # Used for storing a trail to draw
        self.points = [self.position]

    def update(self, force, delta):
        if self.fixed: return True

        self.position = self.position + self.velocity * delta + 0.5 * self.acceleration * delta**2

        prev_acc = self.acceleration
        self.acceleration = force / self.mass# * delta

        # Velocity verlet
        self.velocity = self.velocity + ((prev_acc + self.acceleration) / 2) * delta

        if len(self.points) > GravityObject.TRAIL_LIMIT:
            self.points.pop()
        self.points.insert(0, self.position)

        # Deleted from list if returns false
        #if self.position.x > GravityObject.SCREEN_SIZE.x * 10: return False
        #if self.position.y > GravityObject.SCREEN_SIZE.y * 10: return False

        return True

    def draw(self, screen):
        prev_point = self.position
        for point in self.points:
            pygame.draw.aaline(screen, self.color, point, prev_point)
            prev_point = point

        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def __eq__(self, value: object) -> bool:
        if type(value) != GravityObject:
            return False

        return self.id == value.id