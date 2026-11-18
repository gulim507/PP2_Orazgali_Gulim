import pygame
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 25)
small_font = pygame.font.SysFont("Arial", 18)

player = MusicPlayer()
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.previous_track()
            elif event.key == pygame.K_q:
                running = False

    screen.fill((35, 35, 45))

    if player.tracks:
        name = player.tracks[player.current]
        title = font.render(name, True, (255, 255, 255))
        screen.blit(title, (30, 80))

        position = pygame.mixer.music.get_pos() / 1000
        duration = player.duration

        if duration > 0:
            progress = min(position / duration, 1)

            pygame.draw.rect(screen, (100, 100, 100),
                             (50, 180, 500, 15))
            pygame.draw.rect(screen, (0, 200, 120),
                             (50, 180, int(500 * progress), 15))

            time_text = small_font.render(
                f"{int(position)} / {int(duration)} sec",
                True, (255, 255, 255)
            )
            screen.blit(time_text, (50, 210))
    else:
        title = font.render("No music files found", True, (255, 255, 255))
        screen.blit(title, (150, 150))

    controls = small_font.render(
        "P: Play   S: Stop   N: Next   B: Previous   Q: Quit",
        True, (255, 255, 255)
    )
    screen.blit(controls, (30, 330))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
