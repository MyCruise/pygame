import pygame
from pygame.locals import *
from sys import exit
from JoyGame.Src.Character.actor import Character
from JoyGame.Src.Include.vector import Vector2
from JoyGame.Src.System.shape import Shape
from JoyGame.Src.Include.color import *


def nextEvent(event):
    return event + 1


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Demo")
        # init screen
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # init shape
        self.Shape = Shape(self.screen)
        self.testButton = self.Shape.button(White, 4, (10, 10, 200, 200))

        # init character
        self.player1 = Character((40, 40), (400, 400), White, 1, "player", Vector2(0, 0), 10, Vector2(0, 0))
        # init event
        self.MAINLOOP = nextEvent(pygame.USEREVENT)
        self.MOVE = nextEvent(self.MAINLOOP)
        self.GRAVITY = nextEvent(self.MOVE)

        pygame.time.set_timer(self.MAINLOOP, 1)
        pygame.time.set_timer(self.GRAVITY, 1)

        # init background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

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
            elif event.type == self.MAINLOOP:
                pass
            elif event.type == self.GRAVITY and self.player1.position.y != self.screen_height:
                self.player1.mv_fall()

    def update(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player1.surf, (self.player1.position.x, self.player1.position.y))
        self.screen.blit(self.testButton, (self.player1.position.x, self.player1.position.y))
        self.screen.blit(self.background, (0, 0))

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
