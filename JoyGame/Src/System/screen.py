import pygame
from JoyGame.Src.Include.glovar import GLOVAR


class Screen:
    def __init__(self):
        self.glovar = GLOVAR()
        # init screen size variable
        self.fullscreen = self.glovar.Fullscreen
        self.width = self.glovar.width
        self.height = self.glovar.height
        self.halfWidth = int(self.width * 3 / 4)
        self.halfHeight = int(self.height * 3 / 4)

        self.FPS = self.glovar.FPS

        self.screen = pygame.display.set_mode(self.halfSize(), self.fullscreen)

    def size(self):
        size = (self.width, self.height)
        return size

    def halfSize(self):
        halfSize = (self.halfWidth, self.halfHeight)
        return halfSize
