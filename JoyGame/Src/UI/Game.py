import os

import pygame

from JoyGame.Src.Character.character import Character
from JoyGame.Src.Include.vector import Vector2
from JoyGame.Src.UI.map import Map
from JoyGame.Src.System.global_variable import get_value


class Games:
    def __init__(self, screen):
        self.screen = screen
        self.map = Map(self.screen)

        # Initialize varialbe
        self.characters = os.listdir(get_value('Materials_Character'))
        self.animations = os.listdir(os.path.join(get_value('Materials_Character'), self.characters[0]))

        self.character_index = 0

        # Group
        self.group = pygame.sprite.Group()
        self.group_init = False

        # Initialize character
        self.Fallen_Angels_1 = Character(screen, self.characters[0])
        self.Fallen_Angels_1.set_position(Vector2(30, 30))
        self.Fallen_Angels_2 = Character(screen, self.characters[1])
        self.Fallen_Angels_2.set_position(Vector2(500, 300))
        self.Fallen_Angels_4 = Character(screen, self.characters[4])
        self.Fallen_Angels_4.set_position(Vector2(1000, 400))

    def __next__(self):
        self.character_index += 1
        if self.character_index < len(self.characters):
            self.character_index = 0

    def init_character(self):
        self.map.mapping((0, 0))
        self.group.add(self.Fallen_Angels_1)
        self.group.add(self.Fallen_Angels_2)
        self.group.add(self.Fallen_Angels_4)
        self.group_init = True

    def game_ui(self):
        if not self.group_init:
            self.init_character()
        ticks = pygame.time.get_ticks()
        self.map.update(ticks)
        self.group.update(ticks)
        self.group.draw(self.screen.screen)
