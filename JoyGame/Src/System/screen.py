import pygame
from pygame.locals import *
from JoyGame.Src.Include.glovar import GLOVAR
from JoyGame.Src.Include.color import Color


class Screen:
    def __init__(self, background_color):
        self.glovar = GLOVAR()
        self.color = Color()
        # initialize screen size variable
        self.Width = self.glovar.width
        self.Height = self.glovar.height

        self.resolution = (self.Width, self.Height)
        self.targetFPS = self.glovar.targetFPS

        self.background_color = self.color.Black
        self.flip_flag = False

        self.breath_color_lock = False

        # Set display mode
        self.screen = self.display_mode(mode=self.glovar.Mode)

        self.background = pygame.Surface(self.resolution)
        self.background = self.background.convert()
        self.background.fill(background_color)

    def display_mode(self, size: tuple = "", mode: str = ""):
        screen = pygame.display.set_mode(self.resolution, True, 32)
        if size:
            self.resolution = size
        if mode == "fullscreen":
            print("fullscreen")
            screen = pygame.display.set_mode(self.resolution, FULLSCREEN, 32)
        elif mode == "noframe":
            print("noframe")
            screen = pygame.display.set_mode(self.resolution, NOFRAME, 32)
        elif mode == "resizable":
            print("resizable")
            screen = pygame.display.set_mode(self.resolution, RESIZABLE, 32)
        return screen

    def set_background_color(self, color):
        self.background.fill(color)

    def breath_color(self, color1, color2):
        if self.flip_flag:
            self.background_color = self.color.__add__(self.background_color, (1, 1, 1))
        elif not self.flip_flag:
            self.background_color = self.color.__sub__(self.background_color, (1, 1, 1))
        if self.background_color == color1 and not self.breath_color_lock:
            self.flip_flag = False
        elif self.background_color == color2:
            self.flip_flag = True

    def size(self):
        size = (self.Width, self.Height)
        return size
