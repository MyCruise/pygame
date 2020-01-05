import pygame
from pygame.locals import *
from tetris.Src.Character.actor import Actor


class Game:
    def __init__(self):
        pygame.init()
        self.screen_height = 1280
        self.screen_width = 720
        self.screen = pygame.display.set_mode((self.screen_height, self.screen_width))

        self.player1 = Actor((40, 40), (400, 400), (255, 255, 255), 1, "player", 40, direction="up")

        self.MOVE = pygame.USEREVENT + 1
        pygame.time.set_timer(self.MOVE, 250)

        self.background = pygame.Surface((self.screen_height, self.screen_width))
        self.background.fill((0, 0, 0))
        self.running = True

    def process_event(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                return event.key
            elif event.type == QUIT:
                self.running = False
            elif event.type == self.MOVE:
                self.player1.mv_forward()

    def update(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player1.surf, (self.player1.x, self.player1.y))

        pressed_key = self.process_event()
        self.player_mv(pressed_key)
        pygame.display.flip()

    def player_mv(self, pressed_key):
        if pressed_key == K_w:
            self.player1.to_up()
        elif pressed_key == K_s:
            self.player1.to_down()
        elif pressed_key == K_a:
            self.player1.to_left()
        elif pressed_key == K_d:
            self.player1.to_right()

    def games(self):
        while self.running:
            self.update()

    def run(self):
        self.games()


if __name__ == '__main__':
    game = Game()
    game.run()
