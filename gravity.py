import math

import pygame

from gravity_object import GravityObject

# TODO
# Implement Verlet Intergration

SCREEN_SIZE = pygame.Vector2(1280, 720)
BACKGROUND_COLOR = pygame.Color(0, 0, 0) # black
MAX_FRAMERATE = 60 # (fps)
BASE_TIME_MODIFIER = 10

OBJECT_LIMIT = 100

TRAIL_LENGTH = 100

time_modifier = BASE_TIME_MODIFIER

paused = False

mouse_held = False
mouse_held_pos = pygame.Vector2(0,0)

# Gravitaional constant
G = 6.67430 * (10^-11)

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
delta = 0

# A list containg objects that will need gravity simulating
gravity_objects = []

# Test objects
gravity_objects.append(GravityObject(position=pygame.Vector2(400, SCREEN_SIZE.y/2), radius = 50, fixed=True))
gravity_objects.append(GravityObject(position=pygame.Vector2(600, SCREEN_SIZE.y/2), velocity=pygame.Vector2(0, 15), radius = 5))
#gravity_objects.append(GravityObject(position=pygame.Vector2(SCREEN_SIZE.x/3, SCREEN_SIZE.y/2), velocity=pygame.Vector2(0, 1), radius = 10))
#gravity_objects.append(GravityObject(position=pygame.Vector2(600, 500), velocity=pygame.Vector2(0, 0), radius = 5))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_held = True
            mouse_held_pos = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if event.type == pygame.MOUSEBUTTONUP:
            if(mouse_held):
                mouse_pos_vec = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) 
                mouse_vel_vec = mouse_held_pos - mouse_pos_vec

                gravity_objects.append(GravityObject(position=mouse_pos_vec, velocity=mouse_vel_vec / 10, radius = 5))
                #if len(gravity_objects) > OBJECT_LIMIT:
                #    gravity_objects.pop(0)

            mouse_held = False

    if not paused:
        screen.fill(BACKGROUND_COLOR)
        # Calculating new object values and drawing
        for gravity_object in gravity_objects:
            
            gravity_object.draw(screen)
            g_force = pygame.Vector2(0, 0)

            # Iterating throug other objects and applying gravity
            for other_gravity_object in gravity_objects:
                # Don't calculate for itself
                if gravity_object == other_gravity_object:
                    continue

                rel_pos = gravity_object.position - other_gravity_object.position
                distance = rel_pos.magnitude()
                direction = rel_pos / distance

                g_force += ((G * gravity_object.mass * other_gravity_object.mass) / math.pow(distance, 2.0)) * direction
                
            # Updating position, acceleration and velocity values
            if not gravity_object.update(g_force, delta): gravity_objects.remove(gravity_object)

        if(mouse_held): pygame.draw.aaline(screen, pygame.color.Color(255,255,255), mouse_held_pos, pygame.mouse.get_pos())

        pygame.display.flip()

    delta = clock.tick(MAX_FRAMERATE) / 1000.0 * time_modifier

pygame.quit()
