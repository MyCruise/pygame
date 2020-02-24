import os
import sys
import pygame
from pygame.locals import *
from sys import exit
from JoyGame.Src.Include.glovar import GLOVAR
from JoyGame.Src.System.event import next_event
from JoyGame.Src.System.screen import Screen
from JoyGame.Src.Character.actor import Character
from JoyGame.Src.System.shape import Shape
from JoyGame.Src.System.text import Text
# from JoyGame.Src.UI.UI import UI
from JoyGame.Src.UI.menu import Menu
from JoyGame.Src.System.shape import Button
from JoyGame.Src.Script.initCharacter import initCharacter
from JoyGame.Src.UI.map import Map
from JoyGame.Src.Include.color import Color
from JoyGame.Src.Controller.controller import Controller


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dungeon Adventure")
        self.control = Controller()

        # init class
        self.color = Color()
        self.screen = Screen(self.color.White)
        self.shape = Shape(self.screen.screen)
        self.text = Text(self.screen.screen)
        self.menu = Menu(self.screen, self.text)
        self.button = Button(self.screen.screen, self.text)

        # display information
        print("platform: \t\t" + sys.platform)
        print("revolution: \t" + str(self.screen.halfSize()))

        # init character
        character = initCharacter()

        # init event
        self.MAINLOOP = next_event(pygame.USEREVENT)

        pygame.time.set_timer(self.MAINLOOP, 1)

        # init variable
        self.running = True

    def process_event(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                return event.key
            if event.type == MOUSEMOTION:
                print(*pygame.mouse.get_pos())
            if event.type == QUIT:
                exit()
            if event.type == self.MAINLOOP:
                pass
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            elif event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

    def update(self):
        self.screen.screen.blit(self.screen.background, (0, 0))
        self.menu.__start__()
        self.menu.__test__()

        pygame.display.flip()

    def games(self):
        while self.running:
            self.control.joystick()
            self.update()

    def run(self):
        self.games()


if __name__ == '__main__':
    game = Game()
    game.run()
