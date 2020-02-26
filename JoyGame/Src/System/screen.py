import pygame
from JoyGame.Src.Include.glovar import GLOVAR


class Screen:
    def __init__(self, background_color):
        self.glovar = GLOVAR()
        # initialize screen size variable
        self.Width = self.glovar.width
        self.Height = self.glovar.height

        self.resolution = (self.Width, self.Height)
        self.targetFPS = self.glovar.targetFPS

        # Set display mode
        self.screen = pygame.display.set_mode(self.resolution)
        if self.glovar.Mode == "FUllscreen":
            self.screen = pygame.display.set_mode(self.resolution, pygame.FULLSCREEN, 32)
        elif self.glovar.Mode == "Noframe":
            self.screen = pygame.display.set_mode(self.resolution, pygame.NOFRAME, 32)
        elif self.glovar.Mode == "Resizable":
            self.screen = pygame.display.set_mode(self.resolution, pygame.RESIZABLE, 32)
        elif self.glovar.Mode == "Hwsurface":
            self.screen = pygame.display.set_mode(self.resolution, pygame.HWSURFACE, 32)

        # self.background = pygame.Surface(self.screen.get_size())
        self.background = pygame.Surface(self.resolution)
        self.background = self.background.convert()
        self.background.fill(background_color)

    def set_background_color(self, color):
        self.background.fill(color)

    def size(self):
        size = (self.Width, self.Height)
        return size

