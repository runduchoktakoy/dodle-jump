import pygame
import os
class Game:
    def __init__(self):
        self.background = pygame.image.load(os.path.join("assets","images","background.png"))