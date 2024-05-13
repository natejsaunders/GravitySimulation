import math

import pygame

from gravity_object import GravityObject

# TODO
# Implement Verlet Intergration

SCREEN_SIZE = pygame.Vector2(1280, 720)
BACKGROUND_COLOR = pygame.Color(0, 0, 0) # black
MAX_FRAMERATE = 60 # (fps)
BASE_TIME_MODIFIER = 10

time_modifier = BASE_TIME_MODIFIER

paused = False

# Need to eyeball this
G = 6.67430 * (10^-11)

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
delta = 0

# A list containg objects that will need gravity simulating
gravity_objects = []

# Test objects
gravity_objects.append(GravityObject(position=pygame.Vector2(200, SCREEN_SIZE.y/2), velocity=pygame.Vector2(0, 4.6875), radius = 3))
gravity_objects.append(GravityObject(position=pygame.Vector2(400, SCREEN_SIZE.y/2), velocity=pygame.Vector2(0, 0), radius = 10, fixed=True))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused


    if not paused:
        screen.fill(BACKGROUND_COLOR)
        # Calculating new object values and drawing
        for gravity_object in gravity_objects:

            g_force = pygame.Vector2(0, 0)
            c_force = pygame.Vector2(0, 0)

            # Iterating throug other objects and applying gravity
            for other_gravity_object in gravity_objects:
                # Don't calculate for itself
                if gravity_object == other_gravity_object:
                    continue

                rel_pos = gravity_object.position - other_gravity_object.position
                distance = rel_pos.magnitude()
                direction = rel_pos / distance

                g_force_scalar = ((G * gravity_object.mass * other_gravity_object.mass) / math.pow(distance, 2.0))

                c_force_scalar = (gravity_object.mass * gravity_object.velocity.magnitude()) / distance

                # Adding centrifugal force from possible orbit
                c_force.x += c_force_scalar * direction.x
                c_force.y += c_force_scalar * direction.y

                g_force.x += g_force_scalar * -direction.x
                g_force.y += g_force_scalar * -direction.y

                if not gravity_object.fixed: print(g_force_scalar)

                pygame.draw.aaline(screen, pygame.Color(255,255,255), gravity_object.position, gravity_object.position + direction * (-g_force_scalar*100))
                
            # Updating position and velocity values for now
            gravity_object.update(g_force, delta)#)c_force

            #pygame.draw.circle(screen, gravity_object.color, gravity_object.position, gravity_object.radius)
            gravity_object.draw(screen)
            
        pygame.display.flip()

    delta = clock.tick(MAX_FRAMERATE) / 1000.0 * time_modifier

pygame.quit()
