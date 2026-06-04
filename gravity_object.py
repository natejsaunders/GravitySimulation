import random
import math

import pygame


class GravityObject:
    TRAIL_LIMIT = 2000
    id_counter = 1

    def __init__(self, radius=100, density=1, position=pygame.Vector2(0, 0),
                 velocity=pygame.Vector2(0, 0), acceleration=pygame.Vector2(0, 0),
                 fixed=False, screen_size=pygame.Vector2(1280, 720)):
        self.id = GravityObject.id_counter
        GravityObject.id_counter += 1

        self.radius = radius
        self.density = density
        self.mass = math.pi * self.radius ** 2 * self.density

        self.position = position.copy()
        self.velocity = velocity.copy()
        self.acceleration = acceleration.copy()

        self.fixed = fixed
        self.screen_size = screen_size

        self.color = pygame.color.Color(
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255),
        )

        self.points = [self.position]

    def update(self, force, delta):
        if self.fixed:
            return True

        self.position = self.position + self.velocity * delta + 0.5 * self.acceleration * delta ** 2

        prev_acc = self.acceleration
        self.acceleration = force / self.mass

        self.velocity = self.velocity + (prev_acc + self.acceleration) / 2 * delta

        if len(self.points) > GravityObject.TRAIL_LIMIT:
            self.points.pop()
        self.points.insert(0, self.position)

        limit = self.screen_size * 10
        if abs(self.position.x) > limit.x or abs(self.position.y) > limit.y:
            return False

        return True

    def draw(self, screen):
        prev_point = self.position
        for point in self.points:
            pygame.draw.aaline(screen, self.color, point, prev_point)
            prev_point = point

        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, GravityObject):
            return False
        return self.id == value.id
