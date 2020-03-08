import pygame
import pymunk
from JoyGame.Src.Include.vector import Vector2
from JoyGame.Src.Include.glovar import GLOVAR


class Physics:
    def __init__(self, width, height, mass, clock):
        # init variable
        self.glovar = GLOVAR()
        self.width = width
        self.height = height
        self.mass = mass
        self.Position = Vector2(0, 0)
        self.position = Vector2(0, 0)
        self.altitude = Vector2(0, 0)

        self.jumpSpeed = Vector2(0, 0)
        self.Speed = Vector2(0, 0)

        # initialize variable
        self.jump_flag = 0
        self.maxJumpSpeed = 20
        self.maxSpeed = 10
        self.maxHeight = 40

        # initialize timer
        self.clock = clock

    def setPosition(self, position: Vector2):
        if 0 < position.x < self.width and 0 < position.y < self.height:
            self.Position = position

    def updateMomentum(self, anotherMass: Vector2, anotherSpeed: Vector2):
        self.Speed = anotherMass * anotherSpeed / self.mass

    def updataPosition(self):
        return self.Speed

    # time_passed = self.clock.tick()
    # time_passed_second = time_passed / 10.
    def updateAltitude(self):
        return self.jumpSpeed

    def updatePosition(self):
        self.updateAltitude()
        # print(self.updateAltitude().__self__(), self.updataPosition().__self__())
        self.altitude = self.altitude.__add__(self.updateAltitude())
        self.position = self.position.__add__(self.updataPosition())
        self.Position = Vector2.__add__(self.altitude, self.position)

    def leap(self):
        if not self.jump_flag:
            self.jumpSpeed = Vector2(0, -self.maxJumpSpeed)
        elif self.altitude.getMagnitude() == self.maxHeight:
            self.jump_flag = True
        elif self.altitude.getMagnitude() == Vector2(0, 0):
            self.jump_flag = False
        if self.jump_flag and self.altitude != Vector2(0, 0):
            self.jumpSpeed = Vector2(0, self.maxJumpSpeed)


if __name__ == '__main__':
    pass
