import pygame

from gravity_object import GravityObject

SCREEN_SIZE = pygame.Vector2(1280, 720)
BACKGROUND_COLOR = pygame.Color(0, 0, 0) # black
MAX_FRAMERATE = 60 # (fps)

# Need to eyeball this
G = 1

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
delta = 0

# A list containg objects that will need gravity simulating
gravity_objects = []

# Test objects
gravity_objects.append(GravityObject(velocity=pygame.Vector2(1,1), radius = 5))
gravity_objects.append(GravityObject(position=pygame.Vector2(SCREEN_SIZE.x/2, SCREEN_SIZE.y/2), radius = 30, density=10))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    # Calculating new object values and drawing
    for gravity_object in gravity_objects:
        # Updating position and velocity values for now
        gravity_object.update()

        #pygame.draw.circle(screen, gravity_object.color, gravity_object.position, gravity_object.radius)
        gravity_object.draw(screen)

    pygame.display.flip()
    delta = clock.tick(MAX_FRAMERATE) / 1000

pygame.quit()