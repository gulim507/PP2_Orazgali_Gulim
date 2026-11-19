
import pygame
import os
from datetime import datetime

from tools import draw_pencil, draw_line, draw_shape, flood_fill

pygame.init()

WIDTH = 1000
HEIGHT = 700
TOOLBAR_HEIGHT = 155

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 150, 255)
DARK_BLUE = (50, 100, 200)

font = pygame.font.SysFont("Arial", 16)
text_font = pygame.font.SysFont("Arial", 24)

tools = [
    "Pencil", "Line", "Rectangle", "Circle",
    "Square", "Right Triangle", "Triangle",
    "Rhombus", "Eraser", "Fill",
    "Color Picker", "Text"
]

palette = [
    BLACK,
    (255, 0, 0),
    (0, 150, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (255, 0, 255),
    WHITE
]

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill(WHITE)

current_tool = "Pencil"
current_color = BLACK
thickness = 5

thickness_options = [2, 5, 10]

drawing = False
last_pos = None
start_pos = None
preview_pos = None

# Text settings
text_active = False
text_input = ""
text_position = None

running = True

while running:

    screen.fill(WHITE)

    # Toolbar background
    pygame.draw.rect(
        screen, GRAY,
        (0, 0, WIDTH, TOOLBAR_HEIGHT)
    )

    # Tool buttons
    for i, tool in enumerate(tools):

        x = 10 + (i % 6) * 165
        y = 8 + (i // 6) * 40

        button = pygame.Rect(x, y, 155, 32)

        if current_tool == tool:
            pygame.draw.rect(screen, DARK_BLUE, button)
        else:
            pygame.draw.rect(screen, BLUE, button)

        pygame.draw.rect(screen, BLACK, button, 2)

        label = font.render(tool, True, BLACK)
        screen.blit(label, (x + 5, y + 7))

    # Thickness buttons
    label = font.render("Thickness:", True, BLACK)
    screen.blit(label, (10, 91))

    for i, value in enumerate(thickness_options):

        x = 100 + i * 70
        button = pygame.Rect(x, 88, 60, 27)

        if thickness == value:
            pygame.draw.rect(screen, DARK_BLUE, button)
        else:
            pygame.draw.rect(screen, WHITE, button)

        pygame.draw.rect(screen, BLACK, button, 1)

        label = font.render(str(value) + " px", True, BLACK)
        screen.blit(label, (x + 5, 93))

    # Color palette
    label = font.render("Colors:", True, BLACK)
    screen.blit(label, (10, 125))

    for i, color in enumerate(palette):

        x = 100 + i * 38
        button = pygame.Rect(x, 120, 28, 25)

        pygame.draw.rect(screen, color, button)
        pygame.draw.rect(screen, BLACK, button, 1)

        if current_color == color:
            pygame.draw.rect(screen, DARK_BLUE, button, 3)

    # Current color
    pygame.draw.rect(screen, BLACK, (430, 120, 30, 25), 1)
    pygame.draw.rect(screen, current_color, (432, 122, 26, 21))

    # Canvas
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))

    pygame.draw.rect(
        screen,
        BLACK,
        (0, TOOLBAR_HEIGHT, WIDTH, HEIGHT - TOOLBAR_HEIGHT),
        2
    )

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Keyboard
        if event.type == pygame.KEYDOWN:

            # Save with Ctrl + S
            if (
                event.key == pygame.K_s
                and pygame.key.get_mods() & pygame.KMOD_CTRL
            ):

                os.makedirs("saved_images", exist_ok=True)

                timestamp = datetime.now().strftime(
                    "%Y-%m-%d_%H-%M-%S"
                )

                filename = f"paint_{timestamp}.png"
                filepath = os.path.join("saved_images", filename)

                pygame.image.save(canvas, filepath)

                print("Image saved:", filepath)

            # Text input
            elif text_active:

                if event.key == pygame.K_RETURN:

                    if text_input:
                        text_surface = text_font.render(
                            text_input, True, current_color
                        )

                        canvas.blit(text_surface, text_position)

                    text_active = False
                    text_input = ""
                    text_position = None

                elif event.key == pygame.K_ESCAPE:

                    text_active = False
                    text_input = ""
                    text_position = None

                elif event.key == pygame.K_BACKSPACE:

                    text_input = text_input[:-1]

                elif event.unicode.isprintable():

                    text_input += event.unicode

        # Mouse pressed
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_x, mouse_y = event.pos

                # Toolbar
                if mouse_y < TOOLBAR_HEIGHT:

                    text_active = False
                    text_input = ""

                    # Select tool
                    for i, tool in enumerate(tools):

                        x = 10 + (i % 6) * 165
                        y = 8 + (i // 6) * 40

                        button = pygame.Rect(x, y, 155, 32)

                        if button.collidepoint(mouse_x, mouse_y):
                            current_tool = tool

                    # Select thickness
                    for i, value in enumerate(thickness_options):

                        x = 100 + i * 70
                        button = pygame.Rect(x, 88, 60, 27)

                        if button.collidepoint(mouse_x, mouse_y):
                            thickness = value

                    # Select color
                    for i, color in enumerate(palette):

                        x = 100 + i * 38
                        button = pygame.Rect(x, 120, 28, 25)

                        if button.collidepoint(mouse_x, mouse_y):
                            current_color = color

                # Canvas
                else:

                    canvas_pos = (
                        mouse_x,
                        mouse_y - TOOLBAR_HEIGHT
                    )

                    if current_tool == "Fill":

                        flood_fill(
                            canvas,
                            canvas_pos,
                            current_color
                        )

                    elif current_tool == "Color Picker":

                        current_color = canvas.get_at(canvas_pos)[:3]

                    elif current_tool == "Text":

                        text_active = True
                        text_input = ""
                        text_position = canvas_pos

                    else:

                        text_active = False
                        drawing = True

                        last_pos = canvas_pos
                        start_pos = canvas_pos
                        preview_pos = canvas_pos

                        if current_tool == "Pencil":

                            pygame.draw.circle(
                                canvas,
                                current_color,
                                last_pos,
                                max(1, thickness // 2)
                            )

                        elif current_tool == "Eraser":

                            pygame.draw.circle(
                                canvas,
                                WHITE,
                                last_pos,
                                max(1, thickness * 5 // 2)
                            )

        # Mouse movement
        if event.type == pygame.MOUSEMOTION:

            mouse_x, mouse_y = event.pos

            if drawing and mouse_y >= TOOLBAR_HEIGHT:

                new_pos = (
                    mouse_x,
                    mouse_y - TOOLBAR_HEIGHT
                )

                if current_tool == "Pencil":

                    draw_pencil(
                        canvas,
                        last_pos,
                        new_pos,
                        current_color,
                        thickness
                    )

                    last_pos = new_pos

                elif current_tool == "Eraser":

                    draw_pencil(
                        canvas,
                        last_pos,
                        new_pos,
                        WHITE,
                        thickness * 5
                    )

                    last_pos = new_pos

                else:
                    preview_pos = new_pos

        # Mouse released
        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:

                if drawing and preview_pos is not None:

                    if current_tool == "Line":

                        draw_line(
                            canvas,
                            start_pos,
                            preview_pos,
                            current_color,
                            thickness
                        )

                    elif current_tool in [
                        "Rectangle", "Circle", "Square",
                        "Right Triangle", "Triangle", "Rhombus"
                    ]:

                        draw_shape(
                            canvas,
                            current_tool,
                            start_pos,
                            preview_pos,
                            current_color,
                            thickness
                        )

                drawing = False
                last_pos = None
                start_pos = None
                preview_pos = None

    # Shape preview
    if drawing and preview_pos is not None:

        preview_canvas = canvas.copy()

        if current_tool == "Line":

            draw_line(
                preview_canvas,
                start_pos,
                preview_pos,
                current_color,
                thickness
            )

            screen.blit(preview_canvas, (0, TOOLBAR_HEIGHT))

        elif current_tool in [
            "Rectangle", "Circle", "Square",
            "Right Triangle", "Triangle", "Rhombus"
        ]:

            draw_shape(
                preview_canvas,
                current_tool,
                start_pos,
                preview_pos,
                current_color,
                thickness
            )

            screen.blit(preview_canvas, (0, TOOLBAR_HEIGHT))

    # Text preview
    if text_active and text_input:

        preview_text = text_font.render(
            text_input, True, current_color
        )

        screen.blit(
            preview_text,
            (
                text_position[0],
                text_position[1] + TOOLBAR_HEIGHT
            )
        )

    pygame.display.update()

pygame.quit()
