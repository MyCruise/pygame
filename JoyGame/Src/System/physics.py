import pygame
from JoyGame.Src.Include.vector import Vector2
from JoyGame.Src.Include.glovar import GLOVAR
from JoyGame.Src.System.screen import Screen


class Physics:
    def __init__(self, speed, mass, acceleration):
        # init variable
        self.glovar = GLOVAR()
        self.screen = Screen()
        self.height = self.screen.height
        self.width = self.screen.width
        self.speed = speed
        self.mass = mass
        self.gravity = Vector2(0, 0.5)
        self.acceleration = acceleration

        # init timer
        self.clock = pygame.time.Clock()

    def updateSpeed(self):
        test = Vector2.__add__(self.acceleration, self.gravity)
        self.speed = Vector2.__add__(self.speed, test)
        return self.speed

    def updateMomentum(self, anotherMass, anotherSpeed):
        self.speed = anotherMass * anotherSpeed / self.mass

    def count_distance(self, speed):
        time_passed = self.clock.tick()
        time_passed_second = time_passed / 1000.
        return speed * time_passed_second

    def gravity_fall(self, y):
        y += self.count_distance(self.speed.y)
        self.speed = self.updateSpeed()

    def set_rigid_body(self):
        pass


def test():
    pass


if __name__ == '__main__':
    pass
