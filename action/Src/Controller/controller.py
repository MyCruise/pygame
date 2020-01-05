import pygame
from pygame.locals import *


class Controller:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen_height = 1280
        self.screen_width = 720
        self.screen = pygame.display.set_mode((self.screen_height, self.screen_width))

    def input(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                print(event.key)
            elif event.type == pygame.JOYAXISMOTION:
                print(event)
            elif event.type == pygame.JOYHATMOTION:
                print(event)
            elif event.type == pygame.JOYBUTTONDOWN:
                print(event)

            elif event.type == QUIT:
                self.running = False

    def xbox(self):
        joystick_count = pygame.joystick.get_count()

        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            name = joystick.get_name()

            axes = joystick.get_numaxes()
            for i in range(axes):
                axis = joystick.get_axis(i)

            buttons = joystick.get_numbuttons()
            for i in range(buttons):
                button = joystick.get_button(i)

            hats = joystick.get_numhats()
            for i in range(hats):
                hat = joystick.get_hat(i)

    def keyboard(self):
        pass

    def mouse(self):
        pass


if __name__ == '__main__':
    control = Controller()
    while control.running:
        control.input()
