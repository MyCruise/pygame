import os
import pygame

from JoyGame.Src.Include.abspath import abspath_join
from JoyGame.Src.Include.glovar import GLOVAR
from JoyGame.Src.Include.vector import Vector2
from JoyGame.Src.UI.map import Map
from JoyGame.Src.Character.character import Character
from JoyGame.Src.Character.sprite import MySprite


class Games:
    def __init__(self, screen):
        self.screen = screen
        self.map = Map(self.screen)

        # Initialize varialbe
        self.glovar = GLOVAR()
        self.characters = os.listdir(self.glovar.MaterialsAction)
        self.animations = os.listdir(abspath_join(self.glovar.MaterialsAction, self.characters[0]))

        self.character_index = 0

        # Group
        self.group = pygame.sprite.Group()
        self.group_init = False

        # Initialize character
        self.Fallen_Angels_2 = Character(screen, self.characters[self.character_index])
        self.Fallen_Angels_2.set_position(Vector2(30, 30))

    def __next__(self):
        self.character_index += 1
        if self.character_index < len(self.characters):
            self.character_index = 0

    def init_character(self):
        self.map.mapping((0, 0))
        self.group.add(self.Fallen_Angels_2)
        self.group_init = True

    def game_ui(self):
        if not self.group_init:
            self.init_character()
        ticks = pygame.time.get_ticks()
        self.map.update(ticks)
        self.group.update(ticks)
        self.group.draw(self.screen.screen)
