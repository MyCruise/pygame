import pygame
from JoyGame.Src.Include.glovar import GLOVAR


class Screen:
    def __init__(self, background_color, resolution=""):
        self.glovar = GLOVAR()
        # init screen size variable
        self.fullscreen = self.glovar.Fullscreen
        self.Width = 0
        self.Height = 0

        if resolution == "":
            self.Width = self.glovar.width
            self.Height = self.glovar.height
        elif resolution == "half":
            self.Width = self.halfSize()
            self.Height = self.halfSize()
        elif resolution == "large":
            self.Width = int(self.glovar.width * 3 / 4)
            self.Height = int(self.glovar.height * 3 / 4)
        elif resolution == "small":
            self.Width = int(self.glovar.width * 1 / 4)
            self.Height = int(self.glovar.height * 1 / 4)

        self.FPS = self.glovar.targetFPS

        self.screen = pygame.display.set_mode(self.halfSize(), self.fullscreen)

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(background_color)

    def set_background_color(self, color):
        self.background.fill(color)

    def size(self):
        size = (self.Width, self.Height)
        return size

    def halfSize(self):
        halfSize = (self.Width, self.Height)
        return halfSize
