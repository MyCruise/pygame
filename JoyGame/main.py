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
        pygame.display.set_caption("Dungeon Adventure")
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

        # display information
        print("platform: \t\t" + sys.platform)
        print("revolution: \t" + str(self.screen.resolution))

        # initialize character
        character = initCharacter()

        # initialize event
        self.MAINLOOP = next_event(pygame.USEREVENT)

        # initialize timer
        pygame.time.set_timer(self.MAINLOOP, 16)

        # initialize variable
        self.running = True
        self.ticks = 0
        self.lock_control = 0
        self.joystick_button_press = 0

    def process_event(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                if event.key == K_w and self.timer.elapse() > 0.15:
                    self.mc.front()
                    self.timer.set_timer()
                elif event.key == K_s and self.timer.elapse() > 0.15:
                    self.mc.rear()
                    self.timer.set_timer()
            if event.type == MOUSEMOTION:
                # print(*pygame.mouse.get_pos())
                pass
            if event.type == QUIT:
                exit()

            if event.type == self.MAINLOOP:
                # Menu control
                if self.lock_control and self.mc.layer == 1:
                    if self.control.LS_down and self.timer.elapse() > 0.15:
                        self.mc.rear()
                        self.timer.set_timer()
                    elif self.control.LS_up and self.timer.elapse() > 0.15:
                        self.mc.front()
                        self.timer.set_timer()

                    if self.control.A and self.timer.elapse() > 0.5:
                        self.mc.next()
                        print("a")
                        print(self.mc.layer)
                        self.timer.set_timer()

                    if self.control.B and self.timer.elapse() > 0.5:
                        self.mc.previous()
                        print("b")
                        print(self.mc.layer)
                        self.timer.set_timer()

                    if self.control.hats_up and self.timer.elapse() > 0.15:
                        self.mc.front()
                        self.timer.set_timer()
                    elif self.control.hats_down and self.timer.elapse() > 0.15:
                        self.mc.rear()
                        self.timer.set_timer()

                # Game control

            # Joystick button pressed
            if event.type == pygame.JOYBUTTONDOWN:
                self.joystick_button_press = 1

            # Joystick button released
            elif event.type == pygame.JOYBUTTONUP:
                self.joystick_button_press = 0

    def update(self):
        self.process_event()
        self.control.joystick()
        self.clock.tick(self.glovar.targetFPS)
        self.ticks = pygame.time.get_ticks() / 1000
        pygame.display.set_caption("Dungeon Adventure" + self.timer.num2time(self.ticks))

    def display(self):
        if self.mc.layer == 0:
            self.menu.layout_1()
            if self.timer.elapse() > 6:
                self.mc.previous()
                self.lock_control = 1
        if self.mc.layer == 1:
            self.menu.layout_2()
            if self.mc.enter == 1:
                if self.mc.index == 0:
                    pass
                if self.mc.index == 1:
                    pass
                if self.mc.index == 2:
                    pass
                if self.mc.index == 3:
                    exit()

        pygame.display.flip()

    def games(self):
        while self.running:
            self.control.joystick()
            self.update()
            self.display()

    def run(self):
        self.games()


if __name__ == '__main__':
    game = Game()
    game.run()
