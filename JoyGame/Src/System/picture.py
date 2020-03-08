import os
import pygame
from JoyGame.Src.Include.glovar import GLOVAR


class Picture:
    def __init__(self, screen, glovar):
        self.glovar = glovar
        self.screen = screen

    def load_image(self, filename, size):
        for parent, dirnames, filenames in os.walk(self.glovar.Materials_Images_icon):
            for files in filenames:
                name, suffix = os.path.splitext(files)
                if name == filename:
                    image = pygame.transform.scale(
                        pygame.image.load(self.glovar.Materials_Images_icon + files).convert_alpha(), size)
                    return image

    def addImage(self, image, point):
        self.screen.blit(image, point)


if __name__ == '__main__':
    glovar = GLOVAR()
    for i in os.listdir(glovar.MaterialsImagesIcon):
        print(os.path.splitext(i))
