import pygame


class Actor:
    def __init__(self, size, position, color, id, label, step, image="", direction=""):
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.id = id
        self.direction = direction
        self.label = label
        self.step = step
        self.x = position[0]
        self.y = position[1]
        if image != "":
            self.image = pygame.image.load(image).convert()

    def mv_up(self):
        self.y -= self.step

    def mv_down(self):
        self.y += self.step

    def mv_left(self):
        self.x -= self.step

    def mv_right(self):
        self.x += self.step

    def to_up(self):
        self.direction = "up"

    def to_down(self):
        self.direction = "down"

    def to_left(self):
        self.direction = "left"

    def to_right(self):
        self.direction = "right"

    def mv_forward(self):
        if self.direction is "up":
            self.mv_up()
        if self.direction is "down":
            self.mv_down()
        if self.direction is "left":
            self.mv_left()
        if self.direction is "right":
            self.mv_right()
