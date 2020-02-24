import pygame
from pygame.locals import *
import os
import platform
from JoyGame.Src.Include.vector import Vector2


class Controller:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()

        # init variable
        self.Menu = 0
        self.Start = 0
        self.LT = 0
        self.RT = 0
        self.LB = 0
        self.RB = 0
        self.A = 0
        self.B = 0
        self.X = 0
        self.Y = 0
        self.hats = [0, 0]
        self.LS = [0, 0]
        self.RS = [0, 0]
        self.LS_D = 0
        self.RS_D = 0

        self.running = True

        self.sysstr = platform.system()

        self.controller = 0
        self.last_controller = 0

        self.keyword = pygame.key.get_pressed()
        self.btn = pygame.mouse.get_pressed()

        # init list
        self.name = []

    def input(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                self.keyword = pygame.key.get_pressed()
            if event.type == MOUSEMOTION:
                print(*pygame.mouse.get_pos())
            self.btn = pygame.mouse.get_pressed()
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            elif event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

            if event.type == pygame.QUIT:
                print("exit")

    def iskeyword(self, key):
        return self.keyword == key

    def joystick(self):
        pygame.joystick.init()
        for event in pygame.event.get():  # User did something.
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            elif event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

        joystick_count = pygame.joystick.get_count()

        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            self.name = joystick.get_name()

            axes = joystick.get_numaxes()
            self.LS = [joystick.get_axis(0), joystick.get_axis(1)]
            self.LT = joystick.get_axis(2)
            self.RS = [joystick.get_axis(3), joystick.get_axis(4)]
            # self.RT = joystick.get_axis(5)

            buttons = joystick.get_numbuttons()

            self.A = joystick.get_button(0)
            self.B = joystick.get_button(1)
            self.X = joystick.get_button(2)
            self.Y = joystick.get_button(3)
            self.Menu = joystick.get_button(4)
            self.Start = joystick.get_button(5)
            self.LB = joystick.get_button(6)
            self.RB = joystick.get_button(7)
            self.RS_D = joystick.get_button(8)
            self.LS_D = joystick.get_button(9)

            hats = joystick.get_numhats()
            self.hats = hats

    def detect_joysticks(self):
        # Windows system platform
        if self.sysstr == "Windows":
            if pygame.joystick.get_count():
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

        # Linux system platform
        elif self.sysstr == "Linux":
            if pygame.joystick.get_count():
                self.controller = 1
            else:
                self.controller = 0

            # if os.path.exists("/dev/input/js0"):
            #     self.controller = 1
            # else:
            #     self.controller = 0

            if self.controller != self.last_controller:
                if self.controller == 1:
                    print("controller connected")
                else:
                    print("controller disconnected")
            else:
                pass
            self.last_controller = self.controller
            return self.controller

        # Other system platform
        else:
            print("Other System tasks")


if __name__ == '__main__':
    control = Controller()
    while control.running:
        # if control.isJoystick():
        control.joystick()
        control.input()
        # print(control.name)
        # print(control.LS)
