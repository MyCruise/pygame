import os
import pygame

from JoyGame.Src.Include.abspath import abspath_join
from JoyGame.Src.System.picture import Picture
from JoyGame.Src.System.physics import Physics
from JoyGame.Src.Include.vector import Vector2
from JoyGame.Src.Include.glovar import GLOVAR
from JoyGame.Src.System.timer import Timer


class Character:
    def __init__(self, screen, mass, character: str):
        # initialize class
        self.screen = screen
        self.glovar = GLOVAR()
        self.picture = Picture(screen, self.glovar)
        self.clock = pygame.time.Clock()
        self.physics = Physics(screen.width, screen.height, mass, self.clock)

        # initialize variable
        self.frame = 0
        self.character = character
        self.animation_num = 0
        self.timer = Timer()

        self.characters = os.listdir(self.glovar.MaterialsAction)
        self.animations = os.listdir(abspath_join(self.glovar.MaterialsAction, self.characters[0]))

        # action variable
        self.animation = ""
        self.loop = 0
        self.status = ""
        self.idle = True
        self.animation_flip = False

    def load_animation(self, animation):
        anime = {}
        if self.character in self.characters:
            if animation in self.animations:
                path = abspath_join(self.glovar.MaterialsAction, abspath_join(self.character, animation))
                animation = os.listdir(path)
                self.animation_num = len(animation)
                image = pygame.image.load(abspath_join(path, animation[self.frame])).convert_alpha()
                image = pygame.transform.scale(image, self.glovar.block_character)
                image = pygame.transform.flip(image, self.animation_flip, False)
                return image
            else:
                print(animation + "\tanimation not existed")
        else:
            print(self.character + "\tcharacter not existed")

    def set_position(self, position: Vector2):
        self.physics.Position = position

    def sprites_animation(self, animation):
        if self.animation != animation:
            self.frame = 0
        image = self.load_animation(animation)
        self.animation = animation
        self.physics.updatePosition()
        self.screen.screen.blit(image, self.physics.Position.__tuple__())
        return self.update()

    def update(self):
        self.frame += 1
        if self.frame > self.animation_num - 1:
            self.frame = 0
            return True
        else:
            return False

    def update_sprite(self):
        if not self.physics.Speed.getMagnitude():
            self.idle = True
        else:
            self.idle = False
        if self.idle and self.status == "Idle":
            self.sprites_animation("Idle")
        elif self.idle and self.status != "Idle":
            if self.status == "Slashing":
                self.sprites_animation("Slashing")
            if self.status == "Sliding":
                self.sprites_animation("Idle Blinking")
            elif self.status == "Throwing":
                self.sprites_animation("Throwing")
            elif self.status == "Jump":
                if not self.physics.jump_flag:
                    self.sprites_animation("Jump Loop")
            elif self.status == "Kicking":
                self.sprites_animation("Kicking")
        elif not self.idle:
            if self.status == "Slashing":
                self.sprites_animation("Run Slashing")
            elif self.status == "Throwing":
                self.sprites_animation("Run Throwing")
            elif self.status == "Jump":
                self.sprites_animation("Jump Loop")
            elif self.status == "Sliding":
                self.sprites_animation("Sliding")
            elif self.status == "Kicking":
                self.sprites_animation("Kicking")
            elif self.status == "Running":
                self.sprites_animation("Running")

    def move_idle(self):
        self.status = "Idle"
        if self.physics.Speed != Vector2(0, 0) and self.physics.jumpSpeed:
            self.physics.jumpSpeed = Vector2(0, 0)
            self.physics.Speed = Vector2(0, 0)

    def move_up(self):
        self.status = "Running"
        self.physics.Speed = Vector2(0, -self.physics.maxSpeed)

    def move_down(self):
        self.status = "Running"
        self.physics.Speed = Vector2(0, self.physics.maxSpeed)

    def move_left(self):
        self.status = "Running"
        self.animation_flip = True
        self.physics.Speed = Vector2(-self.physics.maxSpeed, 0)

    def move_right(self):
        self.animation_flip = False
        self.status = "Running"
        self.physics.Speed = Vector2(self.physics.maxSpeed, 0)

    def move_upper_left(self):
        self.animation_flip = True
        self.status = "Running"
        self.physics.Speed = Vector2(-self.physics.maxSpeed, -self.physics.maxSpeed)

    def move_upper_right(self):
        self.animation_flip = False
        self.status = "Running"
        self.physics.Speed = Vector2(self.physics.maxSpeed, -self.physics.maxSpeed)

    def move_lower_left(self):
        self.animation_flip = True
        self.status = "Running"
        self.physics.Speed = Vector2(-self.physics.maxSpeed, self.physics.maxSpeed)

    def move_lower_right(self):
        self.animation_flip = False
        self.status = "Running"
        self.physics.Speed = Vector2(self.physics.maxSpeed, self.physics.maxSpeed)

    def move_jump(self):
        self.status = "Jump"
        self.physics.leap()

    def move_throwing(self):
        self.status = "Throwing"

    def move_slashing(self):
        self.status = "Slashing"

    def move_idle_blinking(self):
        pass

    def move_sliding(self):
        self.status = "Sliding"
