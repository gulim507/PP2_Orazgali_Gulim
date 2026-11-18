
import pygame
from ball import Ball


pygame.init()


WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")

ball = Ball()


clock = pygame.time.Clock()

running = True

while running:

    # Check events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            ball.move(event.key, WIDTH, HEIGHT)


    screen.fill((255, 255, 255))

    ball.draw(screen)


    pygame.display.flip()

    clock.tick(60)


pygame.quit()
