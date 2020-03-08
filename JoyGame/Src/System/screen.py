import pygame
from pygame.locals import *
from JoyGame.Src.Include.glovar import GLOVAR
from JoyGame.Src.Include.color import Color


class Screen:
    def __init__(self, background_color):
        self.glovar = GLOVAR()
        self.color = Color()
        # initialize screen size variable
        self.width = self.glovar.width
        self.height = self.glovar.height

        self.resolution = (self.width, self.height)
        self.targetFPS = self.glovar.targetFPS

        self.background_color = self.color.Black
        self.target_background_color = self.glovar.background_color
        self.flip_flag = False

        # initialize variable
        self.sur_alpha = 0

        self.breath_color_lock = False

        # Set display mode
        self.screen = self.display_mode(mode=self.glovar.Mode)

        self.background = pygame.Surface(self.resolution)
        self.background = self.background.convert()
        self.background.fill(background_color)

    def display_mode(self, size: tuple = (), mode: str = ""):
        screen = pygame.display.set_mode(self.resolution, True, 32)
        if size:
            self.resolution = size
        if mode == "fullscreen":
            print("screen size:\tFULLSCREEN")
            screen = pygame.display.set_mode(self.resolution, FULLSCREEN, 32)
        elif mode == "noframe":
            print("screen size:\tNOFRAME")
            screen = pygame.display.set_mode(self.resolution, NOFRAME, 32)
        elif mode == "resizable":
            print("screen size:\tRESIZABLE")
            screen = pygame.display.set_mode(self.resolution, RESIZABLE, 32)
        elif mode == "doublebuf":
            print("screen size:\tDOUBLEBUF")
            screen = pygame.display.set_mode(self.resolution, DOUBLEBUF | FULLSCREEN, 32)
        elif mode == "hwsirface":
            print("screen size:\tHWSIRFACE")
            screen = pygame.display.set_mode(self.resolution, HWSURFACE | FULLSCREEN, 32)
        return screen

    def set_background_color(self, color: tuple):
        self.background.fill(color)

    def set_target_background_color(self, color: tuple):
        self.target_background_color = color

    def reset_background_color(self):
        if self.background_color != self.target_background_color:
            self.set_background_color(self.target_background_color)

    def breath_color(self, color1: tuple, color2: tuple):
        if self.flip_flag:
            self.background_color = self.color.__add__(self.background_color, (1, 1, 1))
        elif not self.flip_flag:
            self.background_color = self.color.__sub__(self.background_color, (1, 1, 1))
        if self.background_color == color1 and not self.breath_color_lock:
            self.flip_flag = False
        elif self.background_color == color2:
            self.flip_flag = True

    def set_screen_alpha(self):
        if self.flip_flag:
            self.screen.set_alpha(self.sur_alpha)
            self.sur_alpha += 1
        elif not self.flip_flag:
            self.screen.set_alpha(self.sur_alpha)
            self.sur_alpha -= 1
        if self.screen.get_alpha() == 255 and not self.breath_color:
            self.flip_flag = False
        elif self.screen.get_alpha() == 0:
            self.flip_flag = True

    def size(self):
        size = (self.width, self.height)
        return size
