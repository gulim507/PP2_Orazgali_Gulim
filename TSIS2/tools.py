
import pygame
import math


def draw_pencil(screen, start_pos, end_pos, color, thickness):
    pygame.draw.line(screen, color, start_pos, end_pos, thickness)


def draw_line(screen, start_pos, end_pos, color, thickness):
    pygame.draw.line(screen, color, start_pos, end_pos, thickness)


def draw_shape(screen, tool, start_pos, end_pos, color, thickness):

    x1, y1 = start_pos
    x2, y2 = end_pos

    left = min(x1, x2)
    right = max(x1, x2)
    top = min(y1, y2)
    bottom = max(y1, y2)

    width = right - left
    height = bottom - top

    if tool == "Rectangle":
        rect = pygame.Rect(left, top, width, height)
        pygame.draw.rect(screen, color, rect, thickness)

    elif tool == "Circle":
        radius = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        pygame.draw.circle(screen, color, start_pos, radius, thickness)

    elif tool == "Square":
        side = max(width, height)

        if x2 < x1:
            left = x1 - side
        else:
            left = x1

        if y2 < y1:
            top = y1 - side
        else:
            top = y1

        rect = pygame.Rect(left, top, side, side)
        pygame.draw.rect(screen, color, rect, thickness)

    elif tool == "Right Triangle":
        points = [
            (left, top),
            (left, bottom),
            (right, bottom)
        ]
        pygame.draw.polygon(screen, color, points, thickness)

    elif tool == "Triangle":
        points = [
            ((left + right) // 2, top),
            (left, bottom),
            (right, bottom)
        ]
        pygame.draw.polygon(screen, color, points, thickness)

    elif tool == "Rhombus":
        points = [
            ((left + right) // 2, top),
            (right, (top + bottom) // 2),
            ((left + right) // 2, bottom),
            (left, (top + bottom) // 2)
        ]
        pygame.draw.polygon(screen, color, points, thickness)


def flood_fill(surface, start_pos, fill_color):

    width, height = surface.get_size()

    x, y = start_pos

    if x < 0 or x >= width or y < 0 or y >= height:
        return

    target_color = surface.get_at((x, y))

    if target_color == fill_color:
        return

    stack = [(x, y)]

    while stack:

        x, y = stack.pop()

        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        if surface.get_at((x, y)) != target_color:
            continue

        surface.set_at((x, y), fill_color)

        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))
