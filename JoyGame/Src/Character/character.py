import os
import pygame

from JoyGame.Src.Include.abspath import abspath_join
from JoyGame.Src.System.physics import Physics
from JoyGame.Src.Include.vector import Vector2
from JoyGame.Src.Include.glovar import GLOVAR
from JoyGame.Src.System.timer import Timer
from JoyGame.Src.Tools.save2json import SAVE2CONFIG


class Character(pygame.sprite.Sprite):
    def __init__(self, target, character: str):
        pygame.sprite.Sprite.__init__(self)
        # initialize class
        self.glovar = GLOVAR()
        self.s2c = SAVE2CONFIG()
        self.physics = Physics()

        # initialize variable
        self.character = character

        # action variable

        self.animation = ""
        self.status = ""
        self.idle = True
        self.animation_flip = False
        self.last_animation_flip = False

        self.max_frame = None

        self.target_surface = target
        self.sprite_dict = {}
        self.image = None
        self.master_image = None
        self.rect = None
        self.topleft = 0, 0
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.loadSpriteSheet("Running")

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.master_image = pygame.transform.flip(self.master_image, self.animation_flip, False)
        self.rect = self.physics.position.x, self.physics.position.y, width, height

        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time):
        self.update_sprite()
        self.physics.updatePosition()
        if current_time > self.last_time + self.glovar.targetFPS:
            if not self.animation_flip:
                if self.last_animation_flip != self.animation_flip:
                    self.frame = self.first_frame
                self.frame += 1
                if self.frame > self.last_frame:
                    self.frame = self.first_frame
            else:
                if self.last_animation_flip != self.animation_flip:
                    self.frame = self.last_frame
                self.frame -= 1
                if self.frame < self.first_frame:
                    self.frame = self.last_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            try:
                self.image = self.master_image.subsurface(rect)
            except:
                pass

            self.old_frame = self.frame

    def loadSpriteSheet(self, animation):
        for parent, dirnames, filenames in os.walk(abspath_join(self.glovar.MaterialsAction, self.character)):
            for filename in filenames:
                name, suffix = os.path.splitext(filename)
                if name == animation:
                    if suffix == ".json":
                        json_path = abspath_join(parent, name)
                        self.sprite_dict = self.s2c.readFromSpritesConfig(json_path)
                        self.max_frame = len(self.sprite_dict["frames"])
                    if suffix == ".png":
                        png_path = abspath_join(parent, name + ".png")
                        if self.animation != animation or self.last_animation_flip != self.animation_flip \
                                or self.physics.changePosition:
                            self.frame_width = self.sprite_dict['frames'][0]['sourceSize']['w']
                            self.frame_height = self.sprite_dict['frames'][0]['sourceSize']['h']
                            if os.path.exists(png_path):
                                self.load(png_path, self.frame_width, self.frame_height, self.max_frame)
        self.animation = animation
        self.last_animation_flip = self.animation_flip

    def set_position(self, position: Vector2):
        self.physics.Position = position

    def update_sprite(self):
        if not self.physics.Speed.getMagnitude():
            self.idle = True
        else:
            self.idle = False
        if self.idle and self.status == "Idle":
            self.loadSpriteSheet("Idle")
        elif self.idle and self.status != "Idle":
            if self.status == "Slashing":
                self.loadSpriteSheet("Slashing")
            elif self.status == "Sliding":
                self.loadSpriteSheet("Idle Blinking")
            elif self.status == "Throwing":
                self.loadSpriteSheet("Throwing")
            elif self.status == "Jump":
                if not self.physics.jump_flag:
                    self.loadSpriteSheet("Jump Loop")
            elif self.status == "Kicking":
                self.loadSpriteSheet("Kicking")
        elif not self.idle:
            if self.status == "Slashing":
                self.loadSpriteSheet("Run Slashing")
            elif self.status == "Throwing":
                self.loadSpriteSheet("Run Throwing")
            elif self.status == "Jump":
                self.loadSpriteSheet("Jump Loop")
            elif self.status == "Sliding":
                self.loadSpriteSheet("Sliding")
            elif self.status == "Kicking":
                self.loadSpriteSheet("Kicking")
            elif self.status == "Running":
                self.loadSpriteSheet("Running")

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

    def move_kicking(self):
        self.status = "Kicking"
