import os

import pygame
from JoyGame.Src.Include.vector import Vector2
from JoyGame.Src.System.physics import Physics


class Character:
    def __init__(self, size, position, color, id, label, speed, mass, acceleration, image=""):
        self.size = size
        self.position = Vector2(position[0], position[1])
        self.color = color
        self.physics = Physics(speed, mass, acceleration)
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.id = id
        self.speed = self.physics.speed
        self.mass = self.physics.mass
        self.gravity = self.physics.gravity
        self.acceleration = self.physics.acceleration
        self.label = label
        if image != "":
            self.image = pygame.image.load(image).convert()

    def set_size(self, size):
        self.size = size

    def set_position(self, position):
        self.position = position

    def set_color(self, color):
        self.color = color

    def set_id(self, id):
        self.id = id

    def set_label(self, label):
        self.label = label

    def set_speed(self, speed):
        self.speed = speed

    def set_mass(self, m):
        self.mass = m

    def set_acceleration(self, a):
        self.acceleration = a

    def set_image(self, image):
        if os.path.exists(image):
            self.image = image

    def set_direction(self):
        pass

    def mv_fall(self):
        self.position.y += self.physics.count_distance(self.speed.y)
        self.speed = self.physics.updateSpeed()
