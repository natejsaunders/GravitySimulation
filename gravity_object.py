import random

import pygame


class GravityObject:

    def __init__(this, radius=100, density=1, position=pygame.Vector2(0,0), velocity=pygame.Vector2(0,0), acceleration=pygame.Vector2(0,0)):
        
        this.radius = radius # Pixels
        this.density = density # kg/pixel
        
        this.position = position
        this.velocity = velocity # pixels/frame
        this.acceleration = acceleration # pixels/frame^2

        this.color = pygame.color.Color(random.randint(100,255),random.randint(100,255),random.randint(100,255))

    def update(this):
        this.position.x += this.velocity.x
        this.position.y += this.velocity.y
        this.velocity.x += this.acceleration.x
        this.velocity.y += this.acceleration.y

    def draw(this, screen):
        print(this.position)
        pygame.draw.circle(screen, this.color, this.position, this.radius)