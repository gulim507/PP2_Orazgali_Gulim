
import pygame


class Ball:
    def __init__(self):
        self.x = 300
        self.y = 200
        self.radius = 25
        self.speed = 20

    def move(self, key, screen_width, screen_height):

        if key == pygame.K_UP:
            if self.y - self.radius - self.speed >= 0:
                self.y -= self.speed

        elif key == pygame.K_DOWN:
            if self.y + self.radius + self.speed <= screen_height:
                self.y += self.speed

        elif key == pygame.K_LEFT:
            if self.x - self.radius - self.speed >= 0:
                self.x -= self.speed

        elif key == pygame.K_RIGHT:
            if self.x + self.radius + self.speed <= screen_width:
                self.x += self.speed

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (self.x, self.y),
            self.radius
        )
