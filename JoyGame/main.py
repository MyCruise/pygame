import sys
import pygame
import logging as log

from pygame.locals import *

sys.path.append("..")
# Include
from JoyGame.Src.Include import init_glovar
from JoyGame.Src import Color

# Tools
from JoyGame.Src import SAVE2CONFIG

# Controller
from JoyGame.Src import Controller

# Script
from JoyGame.Src import MenuControl

# System
from JoyGame.Src import next_event
from JoyGame.Src import get_value
from JoyGame.Src import Music
from JoyGame.Src import Picture
from JoyGame.Src import Screen
from JoyGame.Src import Shape
from JoyGame.Src import Sounds
from JoyGame.Src import Text
from JoyGame.Src import Timer

# UI
from JoyGame.Src import Button
from JoyGame.Src import Menu
from JoyGame.Src import Games


class Game:
    def __init__(self):
        s2c = SAVE2CONFIG()
        s2c.init_config()
        pygame.init()
        if not init_glovar():
            log.error('global variable initialize failure')

        # Initialize class
        self.controller = Controller()
        self.clock = pygame.time.Clock()
        self.color = Color()
        self.screen = Screen(self.color.White)
        self.timer = Timer()
        self.text = Text(self.screen.screen)
        self.shape = Shape(self.screen.screen)
        self.picture = Picture(self.screen)
        self.mc = MenuControl(self.controller, self.timer)
        self.games = Games(self.screen)
        self.music = Music()
        self.sounds = Sounds()
        self.menu = Menu(self.screen, self.text, self.clock, self.mc, self.games)
        self.button = Button(self.screen.screen, self.text)

        pygame.display.set_caption(' '.join([get_value('Title_en_1'), get_value('Title_en_2')]))

        # display information
        print("platform: \t\t" + sys.platform)
        print("revolution: \t" + str(self.screen.resolution))

        # initialize event
        self.MAINLOOP = next_event(pygame.USEREVENT)
        self.CONTROLLER = next_event(self.MAINLOOP)

        # initialize timer
        pygame.time.set_timer(self.MAINLOOP, 1)
        pygame.time.set_timer(self.CONTROLLER, 1)

        # initialize variable
        self.running = True
        self.ticks = 0
        self.lock_control = 0
        self.select_control_device = 0

    def process_event(self):
        for event in pygame.event.get():
            # Menu control by keyboard
            if event.type == KEYDOWN:
                self.mc.key_button_pressed = 1
                if event.key == K_ESCAPE:
                    self.running = False
                if event.key == K_w and self.timer.elapse() > 0.1 and self.lock_control:
                    self.mc.front()
                    self.timer.set_timer()
                elif event.key == K_s and self.timer.elapse() > 0.1 and self.lock_control:
                    self.mc.rear()
                    self.timer.set_timer()
                elif event.key == K_r and self.timer.elapse() > 0.1 and self.lock_control:
                    pygame.joystick.quit()
                    pygame.joystick.init()
                elif event.key == K_KP_ENTER and self.timer.elapse() > 0.1 and self.lock_control:
                    self.mc.enter_menu()
                    self.timer.set_timer()
            if event.type == KEYUP:
                self.controller.key_button_pressed = 0

            # Menu control by mouse
            if event.type == MOUSEBUTTONDOWN:
                self.controller.key_button_pressed = 1
            elif event.type == MOUSEBUTTONUP:
                self.controller.key_button_pressed = 0
            if event.type == MOUSEMOTION:
                self.controller.mouse_position = pygame.mouse.get_pos()

            if event.type == self.MAINLOOP:
                pass

            if event.type == self.CONTROLLER:
                # Menu control by controller
                if self.controller.detect_joysticks():
                    if self.lock_control and self.mc.layer in [1]:
                        self.mc.horizontal_control()

                    elif self.lock_control and self.mc.layer in [2]:
                        self.mc.vertical_control()

                # Joystick button pressed
            if event.type == pygame.JOYBUTTONDOWN:
                self.controller.joystick_button_pressed = 1

            # Joystick button released
            elif event.type == pygame.JOYBUTTONUP:
                self.controller.joystick_button_pressed = 0

    def update(self):
        self.process_event()
        if self.controller.detect_joysticks():
            self.controller.joystick()
        if self.controller.controller != self.controller.last_controller:
            pygame.joystick.quit()
            pygame.joystick.init()
        self.clock.tick(get_value('targetFPS'))
        self.ticks = pygame.time.get_ticks() / 1000
        pygame.display.set_caption("Dungeon Adventure" + self.timer.num2time(self.ticks))

        # Layer 1
        if self.mc.layer == 1:
            self.mc.layer_name = "homepage"
        if self.mc.layer == 1 and self.mc.enter:
            if self.mc.index == 0:
                self.mc.layer_name = "play"
                self.mc.next()
            elif self.mc.index == 1:
                self.mc.layer_name = "setting"
                self.mc.next()
            elif self.mc.index == 2:
                self.mc.layer_name = "tutorial"
                self.mc.next()
            elif self.mc.index == 3:
                self.running = False

        # Layer 2
        elif self.mc.layer == 2 and self.mc.enter:
            if self.mc.index == 0:
                self.mc.layer_name = "start"
                self.mc.next()
            elif self.mc.index == 1:
                self.mc.layer_name = "create"
                self.mc.next()
            elif self.mc.index == 2:
                self.mc.layer_name = "load"
                self.mc.next()

        # Layer 3
        elif self.mc.layer == 3 and (
                self.mc.layer_name == "start" or self.mc.layer_name == "create" or self.mc.layer_name == "load"):
            if not self.mc.pause:
                self.mc.game_control(self.games.Fallen_Angels_2)
            else:
                self.mc.game_menu()
                if self.mc.index == 0 and self.mc.enter:
                    self.mc.pause = False
                    self.mc.enter = False
                elif self.mc.index == 1 and self.mc.enter:
                    self.mc.layer = 2
                    self.mc.index = 0
                    self.mc.enter = False
                    self.mc.layer_name = "setting"
                elif self.mc.index == 2 and self.mc.enter:
                    self.mc.layer = 1
                    self.mc.layer_name = "homepage"
                    self.mc.index = 0
                    self.mc.enter = False

    def display(self):
        # Loading music
        if self.mc.layer == 0 and self.timer.elapse() < 10:
            self.sounds.__play__()
        else:
            self.sounds.pause()

        # Loading interface
        if self.mc.layer == 0:
            self.menu.logo_page()
            if self.timer.elapse() > 12 and (
                    self.controller.joystick_button_pressed or self.controller.key_button_pressed):
                self.mc.layer += 1
                self.lock_control = 1
                self.timer.set_timer()

            if self.timer.elapse() > 12:
                self.screen.breath_color_lock = True
                self.menu.press_bar()

        # Homepage interface
        elif self.mc.layer == 1:
            self.menu.homepage()
            self.mc.pause = False

        # Layer 2
        elif self.mc.layer == 2:
            if self.mc.layer_name == "play":
                self.menu.play()

            elif self.mc.layer_name == "setting":
                self.menu.setting()

            elif self.mc.layer_name == "tutorial":
                self.menu.tutorial()

        # Layer 3
        elif self.mc.layer == 3:
            if self.mc.layer_name == "start":
                self.menu.game()
            if self.mc.layer_name == "create":
                self.menu.game()
            if self.mc.layer_name == "load":
                self.menu.game()
        if self.controller.controller != self.controller.last_controller:
            if self.controller.controller:
                pass
        #         image = self.picture.load_image("switchProController.png", (200, 200))
        #         self.picture.addImage(image, (int(self.screen.width / 2) - 100, int(self.screen.height) - 100))

        '''
        Debug
        '''
        # self.menu.test()

        # pygame.display.flip()
        pygame.display.update()

    def main(self):
        while self.running:
            self.update()
            self.display()

    def run(self):
        self.main()


if __name__ == '__main__':
    main = Game()
    main.run()
