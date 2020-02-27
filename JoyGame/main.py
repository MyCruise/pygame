import os
import sys
import pygame
from pygame.locals import *
from sys import exit

# Character
from JoyGame.Src.Character.actor import Character

# Include
from JoyGame.Src.Include.glovar import GLOVAR
from JoyGame.Src.Include.color import Color

# System
from JoyGame.Src.System.event import next_event
from JoyGame.Src.System.screen import Screen
from JoyGame.Src.System.music import Music
from JoyGame.Src.System.physics import Physics
from JoyGame.Src.System.shape import Shape
from JoyGame.Src.System.text import Text
from JoyGame.Src.System.shape import Button
from JoyGame.Src.System.timer import Timer

# Script
from JoyGame.Src.Script.initCharacter import initCharacter
from JoyGame.Src.Script.menu import MenuControl

# Controller
from JoyGame.Src.Controller.controller import Controller

# UI
from JoyGame.Src.UI.menu import Menu
from JoyGame.Src.UI.map import Map


class Game:
    def __init__(self):
        pygame.init()
        self.control = Controller()
        self.glovar = GLOVAR()
        self.clock = pygame.time.Clock()

        # initialize class
        self.color = Color()
        self.screen = Screen(self.color.White)
        self.shape = Shape(self.screen.screen)
        self.text = Text(self.screen.screen)
        self.timer = Timer()
        self.mc = MenuControl()
        self.menu = Menu(self.screen, self.text, self.clock, self.glovar, self.mc)
        self.button = Button(self.screen.screen, self.text)
        self.title_en = ""
        for letter in self.glovar.title_en_1.split(" "):
            self.title_en += letter
        self.title_en += " "
        for letter in self.glovar.title_en_2.split(" "):
            self.title_en += letter
        pygame.display.set_caption(self.title_en)
        # display information
        print("platform: \t\t" + sys.platform)
        print("revolution: \t" + str(self.screen.resolution))

        # initialize character
        character = initCharacter()

        # initialize event
        self.MAINLOOP = next_event(pygame.USEREVENT)
        self.CONTROLLER = next_event(self.MAINLOOP)

        # initialize timer
        pygame.time.set_timer(self.MAINLOOP, 16)
        pygame.time.set_timer(self.CONTROLLER, 16)

        # initialize variable
        self.running = True
        self.ticks = 0
        self.layout_name = ""
        self.lock_control = 0
        self.joystick_button_pressed = 0
        self.key_button_pressed = 0

    def process_event(self):
        for event in pygame.event.get():
            # Menu control by keyboard
            if event.type == KEYDOWN:
                self.key_button_pressed = 1
                if event.key == K_ESCAPE:
                    self.running = False
                if event.key == K_w and self.timer.elapse() > 0.1:
                    self.mc.front()
                    self.timer.set_timer()
                elif event.key == K_s and self.timer.elapse() > 0.1:
                    self.mc.rear()
                    self.timer.set_timer()
            if event.type == KEYUP:
                self.key_button_pressed = 0
            # Menu control by mouse
            if event.type == MOUSEBUTTONDOWN:
                pass
            if event.type == MOUSEBUTTONUP:
                pass
            if event.type == MOUSEMOTION:
                pass
                # print(*pygame.mouse.get_pos())

            if event.type == self.CONTROLLER:
                # Menu control by controller
                if self.lock_control and self.mc.layer in [1, 2]:
                    if self.control.LS_down and self.timer.elapse() > 0.15:
                        self.mc.rear()
                        self.timer.set_timer()
                    elif self.control.LS_up and self.timer.elapse() > 0.15:
                        self.mc.front()
                        self.timer.set_timer()

                    if self.control.A and self.timer.elapse() > 0.3:
                        self.mc.enter_menu()
                        self.timer.set_timer()

                    if self.control.B and self.timer.elapse() > 0.3:
                        self.mc.previous()
                        self.timer.set_timer()

                    if self.control.hats_up and self.timer.elapse() > 0.15:
                        self.mc.front()
                        self.timer.set_timer()
                    elif self.control.hats_down and self.timer.elapse() > 0.15:
                        self.mc.rear()
                        self.timer.set_timer()

                # Game control
            if event.type == self.MAINLOOP:
                pass

            # Joystick button pressed
            if event.type == pygame.JOYBUTTONDOWN:
                self.joystick_button_pressed = 1

            # Joystick button released
            elif event.type == pygame.JOYBUTTONUP:
                self.joystick_button_pressed = 0

    def update(self):
        self.process_event()
        self.control.joystick()
        self.clock.tick(self.glovar.targetFPS)
        self.ticks = pygame.time.get_ticks() / 1000
        pygame.display.set_caption("Dungeon Adventure" + self.timer.num2time(self.ticks))

        if self.mc.layer == 1 and self.mc.enter:
            # print(self.mc.index, self.mc.layer, self.mc.enter)
            if self.mc.index == 0:
                self.layout_name = "play"
                self.mc.next()
            elif self.mc.index == 1:
                self.layout_name = "setting"
                self.mc.next()
            elif self.mc.index == 2:
                self.layout_name = "tutorial"
                self.mc.next()
            elif self.mc.index == 3:
                self.running = False

        if self.mc.layer == 2 and self.mc.enter:
            pass
        elif self.mc.layer == 3:
            pass
        elif self.mc.layer == 3 and self.mc.enter:
            pass

    def display(self):
        # Loading interface
        if self.mc.layer == 0:
            self.menu.logo_page()
            if self.timer.elapse() > 12 and (self.joystick_button_pressed or self.key_button_pressed):
                self.mc.layer += 1
                self.lock_control = 1
                self.timer.set_timer()
            if self.timer.elapse() > 12:
                self.screen.breath_color_lock = True
                self.menu.load_page()

        # Homepage interface
        if self.mc.layer == 1:
            self.menu.homepage()

        # Layer 2
        if self.mc.layer == 2:
            if self.layout_name == "play":
                self.menu.play()
            if self.layout_name == "setting":
                self.menu.setting()
            if self.layout_name == "tutorial":
                self.menu.tutorial()

        self.menu.__test__()
        pygame.display.flip()

    def games(self):
        while self.running:
            if self.control.detect_joysticks:
                self.control.joystick()
            self.update()
            self.display()

    def run(self):
        self.games()


if __name__ == '__main__':
    game = Game()
    game.run()
