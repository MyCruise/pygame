import pygame
from pygame.locals import *
from sys import exit
from JoyGame.Src.Character.actor import Character
from JoyGame.Src.Include.vector import Vector2
from JoyGame.Src.System.shape import Shape
from JoyGame.Src.System.screen import Screen
# from JoyGame.Src.UI.UI import
from JoyGame.Src.Script.initCharacter import initCharacter
from JoyGame.Src.Include.color import *


def nextEvent(event):
    return event + 1


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Fatigue")

        # init screen
        self.Screen = Screen()
        print(self.Screen.halfSize())

        # init shape
        self.Shape = Shape(self.Screen.screen)

        # init character
        character = initCharacter()
        self.player1 = Character((40, 40), (60, 0), White, 1, "player", Vector2(0, 0), 10, Vector2(0, 0), image="")

        # init event
        self.MAINLOOP = nextEvent(pygame.USEREVENT)
        self.MOVE = nextEvent(self.MAINLOOP)
        self.GRAVITY = nextEvent(self.MOVE)

        pygame.time.set_timer(self.MAINLOOP, 1)
        pygame.time.set_timer(self.GRAVITY, 1)

        # init background
        self.background = pygame.Surface(self.Screen.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(Black)

        # init variable
        self.running = True

    def process_event(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                return event.key
            elif event.type == QUIT:
                exit()
            elif event.type == self.GRAVITY:
                self.player1.mv_fall()
            elif event.type == self.MAINLOOP:
                pass

    def update(self):
        # print(self.player1.position.x, self.player1.position.y)
        self.Screen.screen.blit(self.background, (0, 0))
        self.Screen.screen.blit(self.player1.surf, (self.player1.position.x, self.player1.position.y))

        pressed_key = self.process_event()

        pygame.display.flip()

    def games(self):
        while self.running:
            self.update()

    def run(self):
        self.games()


if __name__ == '__main__':
    game = Game()
    game.run()
