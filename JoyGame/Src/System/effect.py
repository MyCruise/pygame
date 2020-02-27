import pygame
import math
from matplotlib import pyplot as plt


class Effect:
    def __init__(self):
        self.speed = 0
        self.acceleration = 0
        self.distance_lock = 0
        self.distance = 0
        self.last_distance = 0
        self.a = 0
        self.t = 0
        self.now_t = 0

        self.s_list = []
        self.a_list = []

    def update_speed(self):
        self.speed += self.acceleration

    def update_acceleration(self, ):
        print(type(self.acceleration), type(self.a))
        self.acceleration += self.a

    def count_last_distance(self):
        if self.last_distance < self.speed:
            print(self.last_distance, "error")
        else:
            print(self.last_distance)
        self.last_distance -= self.speed

    def nonlinear(self, distance):
        if not self.distance:
            self.last_distance = distance
            self.a = distance * t * 2
            self.distance_lock = 1
        self.count_last_distance()
        self.update_speed()
        self.update_acceleration()
        if self.last_distance == 0:
            self.speed = 0
        return self.speed, self.last_distance

    def load(self, time):
        pass


if __name__ == '__main__':
    effect = Effect()
    t = []
    distance = []
    distance_1 = []
    speed = []
    time = 20

    for i in range(time):
        s, d = effect.nonlinear(10000)
        t.append(i)
        speed.append(s)
        if i < 10:
            distance_1.append(d)
        distance.append(d)

    plt.plot(t, distance)
    plt.plot(t[:len(distance_1)], distance_1)
    plt.plot(t, speed)
    plt.plot(t[:len(distance_1)], speed[:len(distance_1)])
    plt.show()
