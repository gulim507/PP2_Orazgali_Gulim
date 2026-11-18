
import pygame
import math
from datetime import datetime


class MickeyClock:

    def __init__(self):
        self.center = (300, 300)

    def draw_hand(self, screen, angle, length, color):

        # Convert angle into radians
        radians = math.radians(angle - 90)

        # Calculate hand endpoint
        end_x = self.center[0] + length * math.cos(radians)
        end_y = self.center[1] + length * math.sin(radians)

        # Draw hand
        pygame.draw.line(
            screen,
            color,
            self.center,
            (int(end_x), int(end_y)),
            10
        )

        # Draw a white circle at the hand end
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(end_x), int(end_y)),
            12
        )

        pygame.draw.circle(
            screen,
            color,
            (int(end_x), int(end_y)),
            12,
            3
        )

    def draw(self, screen):

        screen.fill((245, 245, 245))

        # Draw clock face
        pygame.draw.circle(screen, (255, 255, 255), self.center, 220)
        pygame.draw.circle(screen, (0, 0, 0), self.center, 220, 4)

        # Draw 60 clock marks
        for i in range(60):
            angle = math.radians(i * 6 - 90)

            x1 = self.center[0] + 200 * math.cos(angle)
            y1 = self.center[1] + 200 * math.sin(angle)

            x2 = self.center[0] + 210 * math.cos(angle)
            y2 = self.center[1] + 210 * math.sin(angle)

            pygame.draw.line(
                screen, (0, 0, 0),
                (int(x1), int(y1)),
                (int(x2), int(y2)), 2
            )

        # Get current time
        now = datetime.now()

        minutes = now.minute
        seconds = now.second

        # Calculate angles
        minute_angle = minutes * 6 + seconds * 0.1
        second_angle = seconds * 6

        # Draw right hand for minutes
        self.draw_hand(
            screen, minute_angle, 130, (0, 100, 255)
        )

        # Draw left hand for seconds
        self.draw_hand(
            screen, second_angle, 180, (255, 0, 0)
        )

        # Draw center
        pygame.draw.circle(screen, (0, 0, 0), self.center, 10)

        # Display time
        font = pygame.font.SysFont("Arial", 36)

        time_text = font.render(
            f"{minutes:02d}:{seconds:02d}",
            True, (0, 0, 0)
        )

        screen.blit(time_text, (245, 530))
