import math

import pygame

from gravity_object import GravityObject

SCREEN_SIZE = pygame.Vector2(1280, 720)
BACKGROUND_COLOR = pygame.Color(0, 0, 0)
MAX_FRAMERATE = 60

G = 50


def main():
    paused = False
    mouse_held = False
    mouse_held_pos = pygame.Vector2(0, 0)

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Gravity")
    clock = pygame.time.Clock()
    running = True
    delta = 0

    gravity_objects = [
        GravityObject(position=pygame.Vector2(400, SCREEN_SIZE.y / 2), radius=50, fixed=False),
        GravityObject(position=pygame.Vector2(600, SCREEN_SIZE.y / 2), velocity=pygame.Vector2(0, 15), radius=5),
    ]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_held = True
                mouse_held_pos = pygame.Vector2(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP:
                if mouse_held:
                    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
                    mouse_vel = mouse_held_pos - mouse_pos
                    gravity_objects.append(
                        GravityObject(position=mouse_pos, velocity=mouse_vel / 10, radius=5)
                    )
                mouse_held = False

        if not paused:
            screen.fill(BACKGROUND_COLOR)

            for obj in gravity_objects[:]:
                obj.draw(screen)
                g_force = pygame.Vector2(0, 0)

                for other in gravity_objects:
                    if obj == other:
                        continue
                    rel_pos = other.position - obj.position
                    distance = rel_pos.magnitude()
                    direction = rel_pos / distance
                    g_force += (G * obj.mass * other.mass / math.pow(distance, 2.0)) * direction

                if not obj.update(g_force, delta):
                    gravity_objects.remove(obj)

            absorbed_ids = set()
            for obj in gravity_objects:
                if obj.id in absorbed_ids:
                    continue
                for other in gravity_objects:
                    if other.id in absorbed_ids or obj.id == other.id:
                        continue
                    distance = (obj.position - other.position).magnitude()
                    if obj.radius >= other.radius:
                        if distance + other.radius <= obj.radius:
                            obj.absorb(other)
                            absorbed_ids.add(other.id)
                    else:
                        if distance + obj.radius <= other.radius:
                            other.absorb(obj)
                            absorbed_ids.add(obj.id)
                            break
            gravity_objects = [o for o in gravity_objects if o.id not in absorbed_ids]

            if mouse_held:
                pygame.draw.aaline(screen, "white", mouse_held_pos, pygame.mouse.get_pos())

            pygame.display.flip()

        delta = clock.tick(MAX_FRAMERATE) / 1000.0

    pygame.quit()


if __name__ == "__main__":
    main()
