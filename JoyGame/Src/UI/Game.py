import os
import pygame

from JoyGame.Src.Include.abspath import abspath_join
from JoyGame.Src.Include.glovar import GLOVAR
from JoyGame.Src.Include.vector import Vector2
from JoyGame.Src.UI.map import Map
from JoyGame.Src.Character.character import Character


class Games:
    def __init__(self, screen):
        self.screen = screen
        self.map = Map(self.screen)

        # Initialize varialbe
        self.glovar = GLOVAR()
        self.characters = os.listdir(self.glovar.MaterialsAction)
        self.animations = os.listdir(abspath_join(self.glovar.MaterialsAction, self.characters[0]))

        self.character_index = 1

        # Initialize character
        self.Fallen_Angels_2 = Character(self.screen, 10, self.characters[self.character_index])
        self.Fallen_Angels_2.set_position(Vector2(30, 30))

    def __next__(self):
        self.character_index += 1
        if self.character_index < len(self.characters):
            self.character_index = 0

    def game_ui(self):
        self.map.mapping((0, 0))
        self.Fallen_Angels_2.update_sprite()

    def main_logic(self):
        pass

    def map(self):
        pass
