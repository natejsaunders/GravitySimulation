import pygame

BACKGROUND_COLOR = pygame.Color(0, 0, 0) # black
MAX_FRAMERATE = 60 # (fps)

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    clock.tick(MAX_FRAMERATE)