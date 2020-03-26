import os
import pygame
import logging as log
from JoyGame.Src.System.global_variable import get_value


class Picture:
    def __init__(self, screen):
        self.screen = screen

    def load_image(self, filename, size):
        for parent, dirnames, filenames in os.walk(get_value('Materials_Images_Icon')):
            for files in filenames:
                if filename == files:
                    image = pygame.transform.scale(
                        pygame.image.load(os.path.join(get_value('Materials_Images_Icon'), files)).convert_alpha(),
                        size)
                    return image
        log.error("%s does not exists" % filename)

    def addImage(self, image, point):
        self.screen.screen.blit(image, point)
