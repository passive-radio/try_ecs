import pygame

def set_text(text: str, size: tuple, color: tuple, font: pygame.font = None):
    font = pygame.font.Font(font, size)
    return font.render(text, True, color)