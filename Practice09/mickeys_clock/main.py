
import pygame
from clock import MickeyClock

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")

mickey_clock = MickeyClock()

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    mickey_clock.draw(screen)

    pygame.display.flip()

    clock.tick(1)

pygame.quit()
