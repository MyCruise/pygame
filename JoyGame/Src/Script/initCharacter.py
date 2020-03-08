import os
from JoyGame.Src.Include.abspath import abspath_join
from JoyGame.Src.Character.character import Character
from JoyGame.Src.Include.vector import Vector2
from JoyGame.Src.Include.glovar import GLOVAR


class InitCharacter:
    def __init__(self, screen):
        # Initialize class
        self.glovar = GLOVAR()

        # initialize variable
        self.characters = os.listdir(self.glovar.MaterialsAction)
        self.animations = os.listdir(abspath_join(self.glovar.MaterialsAction, self.characters[0]))

        # initialize variable
        self.FA_1_pos = Vector2(0, 0)
        self.FA_2_pos = Vector2(0, 0)
        self.FA_3_pos = Vector2(0, 0)
        self.G_0_pos = Vector2(0, 0)
        self.G_1_pos = Vector2(0, 0)
        self.G_2_pos = Vector2(0, 0)
        self.G_3_pos = Vector2(0, 0)
        self.Ogre_pos = Vector2(0, 0)
        self.Orc_pos = Vector2(0, 0)

        # initialize character
        self.Fallen_Angels_1 = Character(screen, 10, self.characters[0])
        self.Fallen_Angels_2 = Character(screen, 10, self.characters[1])
        self.Fallen_Angels_3 = Character(screen, 10, self.characters[2])
        self.Goblin_0 = Character(screen, 10, self.characters[3])
        self.Goblin_1 = Character(screen, 10, self.characters[4])
        self.Goblin_2 = Character(screen, 10, self.characters[5])
        self.Goblin_3 = Character(screen, 10, self.characters[6])
        self.Ogre = Character(screen, 10, self.characters[7])
        self.Orc = Character(screen, 10, self.characters[8])

    def init_player(self):
        self.Fallen_Angels_1.physics.setPosition(self.FA_1_pos)
        self.Fallen_Angels_2.physics.setPosition(self.FA_1_pos)
        self.Fallen_Angels_3.physics.setPosition(self.FA_1_pos)

    def init_enemy(self):
        self.Goblin_0.physics.setPosition(self.G_0_pos)
        self.Goblin_1.physics.setPosition(self.G_1_pos)
        self.Goblin_2.physics.setPosition(self.G_2_pos)
        self.Goblin_3.physics.setPosition(self.G_3_pos)
        self.Ogre.physics.setPosition(self.Ogre_pos)
        self.Orc.physics.setPosition(self.Orc_pos)

    def show_player(self):
        self.Fallen_Angels_1.sprites_animation(self.animations[0])
        self.Fallen_Angels_2.sprites_animation(self.animations[0])
        self.Fallen_Angels_3.sprites_animation(self.animations[0])

    def show_enemy(self):
        self.Goblin_0.sprites_animation(self.animations[0])
        self.Goblin_1.sprites_animation(self.animations[0])
        self.Goblin_2.sprites_animation(self.animations[0])
        self.Goblin_3.sprites_animation(self.animations[0])
        self.Ogre.sprites_animation(self.animations[0])
        self.Orc.sprites_animation(self.animations[0])
