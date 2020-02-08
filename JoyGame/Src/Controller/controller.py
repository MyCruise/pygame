import pygame
from pygame.locals import *
import os


class Controller:
    def __init__(self):
        pygame.init()

        # init controller
        self.axis_list = []
        self.button_list = []
        self.hat_list = []
        self.running = True
        self.keyword = pygame.key.get_pressed()
        self.btn = pygame.mouse.get_pressed()
        self.controller = 0
        self.last_controller = 0
        self.surf = []

    def input(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                self.keyword = pygame.key.get_pressed()
            if event.type == MOUSEMOTION:
                print(*pygame.mouse.get_pos())
            self.btn = pygame.mouse.get_pressed()

            if event.type == pygame.QUIT:
                print("exit")

    def iskeyword(self, key):
        return self.keyword == key

    def isjoystick(self):
        return

    def joystick(self):
        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            name = joystick.get_name()

            axes = joystick.get_numaxes()
            for i in range(axes):
                axis = joystick.get_axis(i)
                self.axis_list.append(axis)

            buttons = joystick.get_numbuttons()
            for i in range(buttons):
                button = joystick.get_button(i)
                self.button_list.append(button)

            hats = joystick.get_numhats()
            for i in range(hats):
                hat = joystick.get_hat(i)
                self.hat_list.append(hat)

    def controller_detect(self):
        if os.path.exists("/dev/input/js0"):
            self.controller = 1
        else:
            self.controller = 0

        if self.controller != self.last_controller:
            if self.controller == 1:
                print("controller connected")
            else:
                print("controller disconnected")
        else:
            pass
        self.last_controller = self.controller
        return self.controller


if __name__ == '__main__':
    control = Controller()
    while control.running:
        if control.controller_detect():
            control.joystick()
            control.input()
            for axis in control.axis_list:
                print(axis)
            for button in control.button_list:
                print(button)
            for hat in control.hat_list:
                print(hat)
