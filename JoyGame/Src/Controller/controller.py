import os
import platform

import pygame

from JoyGame.Src.System.global_variable import get_value


class Controller:
    def __init__(self):
        # Initialize joystick
        pygame.init()
        pygame.joystick.init()

        # initialize variable
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
        self.hats_up = 0
        self.hats_down = 0
        self.hats_right = 0
        self.hats_left = 0
        self.LS_up = 0
        self.LS_down = 0
        self.LS_left = 0
        self.LS_right = 0
        self.RS_up = 0
        self.RS_down = 0
        self.RS_left = 0
        self.RS_right = 0
        self.hats = [0, 0]
        self.LS = [0, 0]
        self.RS = [0, 0]
        self.LS_D = 0
        self.RS_D = 0

        self.running = True

        self.sysstr = platform.system()

        self.controller = False
        self.last_controller = False

        self.mouse_position = ()

        self.deadband1 = get_value('Deadband1')
        self.deadband2 = get_value('Deadband2')

        self.keyword = pygame.key.get_pressed()
        self.btn = pygame.mouse.get_pressed()
        self.joystick_button_pressed = 0
        self.key_button_pressed = 0

        # initialize list
        self.name = []

    def isKeyword(self, key):
        return key

    def joystick(self):
        pygame.joystick.init()

        joystick_count = pygame.joystick.get_count()

        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            # self.name = joystick.get_name()

            # axes = joystick.get_numaxes()
            # self.LS = [joystick.get_axis(0), joystick.get_axis(1)]
            # self.RS = [joystick.get_axis(3), joystick.get_axis(4)]

            # Deadband1
            if joystick.get_axis(0) < -self.deadband1:
                self.LS_left = 1
            elif joystick.get_axis(0) > self.deadband1:
                self.LS_right = 1
            else:
                self.LS_left = 0
                self.LS_right = 0

            if joystick.get_axis(1) < -self.deadband1:
                self.LS_up = 1
            elif joystick.get_axis(1) > self.deadband1:
                self.LS_down = 1
            else:
                self.LS_up = 0
                self.LS_down = 0

            if joystick.get_axis(3) < -self.deadband1:
                self.RS_left = 1
            elif joystick.get_axis(3) > self.deadband1:
                self.RS_right = 1
            else:
                self.RS_left = 0
                self.RS_right = 0

            if joystick.get_axis(4) < self.deadband1:
                self.RS_up = 1
            elif joystick.get_axis(4) > -self.deadband1:
                self.RS_down = 1
            else:
                self.RS_up = 0
                self.RS_down = 0

            # Deadband2
            if joystick.get_axis(0) < -self.deadband2:
                self.LS_left = 1
            elif joystick.get_axis(0) > self.deadband2:
                self.LS_right = 1
            if joystick.get_axis(1) < -self.deadband2:
                self.LS_up = 1
            elif joystick.get_axis(1) > self.deadband2:
                self.LS_down = 1

            if joystick.get_axis(3) < -self.deadband2:
                self.RS_left = 2
            elif joystick.get_axis(3) > self.deadband2:
                self.RS_right = 2
            if joystick.get_axis(4) < self.deadband2:
                self.RS_up = 2
            elif joystick.get_axis(4) > -self.deadband2:
                self.RS_down = 2

            self.LT = joystick.get_axis(2)
            # self.RT = joystick.get_axis(5)

            # buttons = joystick.get_numbuttons()

            self.A = joystick.get_button(0)
            self.B = joystick.get_button(1)
            self.X = joystick.get_button(2)
            self.Y = joystick.get_button(3)
            self.LB = joystick.get_button(4)
            self.RB = joystick.get_button(5)
            self.Menu = joystick.get_button(6)
            self.Start = joystick.get_button(7)
            self.RS_D = joystick.get_button(8)
            self.LS_D = joystick.get_button(9)

            hats = joystick.get_numhats() - 1
            self.hat = joystick.get_hat(hats)
            self.hats_up = int(self.hat[1] == 1)
            self.hats_right = int(self.hat[0] == -1)
            self.hats_down = int(self.hat[1] == -1)
            self.hats_left = int(self.hat[0] == 1)

    def detect_joysticks(self):
        # Windows system platform
        if self.sysstr == "Windows":
            self.controller = True

        # Linux system platform
        elif self.sysstr == "Linux":
            if os.path.exists("/dev/input/js0"):
                self.controller = True
            else:
                self.controller = False

            if self.controller != self.last_controller:
                pygame.joystick.quit()
                pygame.joystick.init()
                if self.controller:
                    print("controller connected")
                else:
                    print("controller disconnected")
            else:
                pass
            self.last_controller = self.controller

        # Other system platform
        else:
            print("Other System tasks")
        return self.controller


if __name__ == '__main__':
    control = Controller()
    while control.running:
        # if control.isJoystick():
        control.joystick()
        print(control.hats_down)
