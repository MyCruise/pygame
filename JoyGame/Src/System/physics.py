import pygame
import pymunk
from JoyGame.Src.Include.vector import Vector2
from JoyGame.Src.Include.glovar import GLOVAR


class Physics:
    def __init__(self):
        # init variable
        self.glovar = GLOVAR()
        self.last_Position = Vector2(0, 0)
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
        self.changePosition = False

    def setPosition(self, position: Vector2):
        self.Position = position

    def updataPosition(self):
        return self.Speed

    # time_passed = self.clock.tick()
    # time_passed_second = time_passed / 10.
    def updateAltitude(self):
        return self.jumpSpeed

    def updatePosition(self):
        self.updateAltitude()
        self.altitude = self.altitude.__add__(self.updateAltitude())
        self.position = self.position.__add__(self.updataPosition())
        self.Position = Vector2.__add__(self.altitude, self.position)
        self.changePosition = self.isPosition()
        self.last_Position = self.Position

    def isPosition(self):
        return self.last_Position.__tuple__() != self.Position.__tuple__()

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
