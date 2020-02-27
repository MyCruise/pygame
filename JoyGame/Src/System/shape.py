import pygame
from math import radians
from JoyGame.Src.System.text import Text
from JoyGame.Src.Include.color import Color


class Shape:
    def __init__(self, screen):
        self.screen = screen

    def round_rect(self, color: tuple, point: tuple, size: tuple, rad: int, width: int):
        rect = [point[0], point[1], point[0] + size[0], point[1] + size[1]]
        dia = 2 * rad
        if size[0] < dia and size[1] < dia:
            dia = min(size[0], size[1])
            rad = dia / 2
        pygame.draw.arc(self.screen, color, (rect[0], rect[1], dia, dia), radians(90),
                        radians(180), width)
        pygame.draw.line(self.screen, color, (rect[0] + rad, rect[1]), (rect[2] - rad, rect[1]), width)

        pygame.draw.arc(self.screen, color, (rect[2] - dia, rect[1], dia, dia), radians(0),
                        radians(90), width)
        pygame.draw.line(self.screen, color, (rect[2], rect[1] + rad), (rect[2], rect[3] - rad), width)

        pygame.draw.arc(self.screen, color, (rect[2] - dia, rect[3] - dia, dia, dia), radians(270), radians(360), width)
        pygame.draw.line(self.screen, color, (rect[0] + rad, rect[3]), (rect[2] - rad, rect[3]), width)

        pygame.draw.arc(self.screen, color, (rect[0], rect[3] - dia, dia, dia), radians(180), radians(270), width)
        pygame.draw.line(self.screen, color, (rect[0], rect[1] + rad), (rect[0], rect[3] - rad), width)

    def horizontal_line(self, color: tuple, point: tuple, len: int, width: int):
        len = int(len / 2)
        start_pos = (point[0] - len, point[1])
        end_pos = (point[0] + len, point[1])
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)

    def vertical_line(self, color: tuple, point: tuple, len: int, width: int):
        len = int(len / 2)
        start_pos = (point[0], point[1] - len)
        end_pos = (point[0], point[1] + len)
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)

    '''
    矩形
    pygame.draw.rect(self.sur, color, rect, width)
    
    多边形
    pygame.draw.polygon(self.sur, color, pointlist, width)
    
    圆
    pygame.draw.circle(self.sur, pos, radius, color, width)
    
    椭圆
    pygame.draw.ellipse(self.sur, color, rect, width)
    
    部分椭圆
    pygame.draw.arc(self.sur, color, Rect, start_angle, stop_angle, width)
    
    线段
    pygame.draw.line(self.sur, color, start_pos, end_pos, width)
    pygame.draw.aaline(self.sur, color, start_pos, end_pos, width)
    
    线段集合
    pygame.draw.lines(self.sur, color, closed, pointlist, width)
    pygame.draw.aalines(self.sur, color, closed, pointlist, width) 
    '''

    def add_ball(self):
        pass

    def create_line(self):
        pass

    def create_box(self):
        pass


class Button:
    def __init__(self, screen, text):
        self.color = Color()
        self.screen = screen
        self.text = text
        self.shape = Shape(self.screen)

    def round_button(self, text: str, font: int, color: tuple, point: tuple, size: tuple, rad: int, width: int,
                     index: int):
        self.shape.round_rect(color, point, size, rad, width)
        self.text.addText(text, font, (point[0] + size[0] / 2, point[1] + size[1] / 2), self.color.Black,
                          None, index)

    def choice_button(self, color: tuple, point: tuple, size: tuple, rad: int, width: int):
        point = tuple(map(lambda i, j: i + j, point, (int(rad / 2), int(rad / 2))))
        size = tuple(map(lambda i, j: i - j, size, (rad, rad)))
        self.shape.round_rect(color, point, size, rad - 3, width)

    def switch_bar(self, color: tuple, point: tuple, length: int, width: int, total: int, index: int):
        if index < 0:
            index = 0
        elif index > total:
            index = total
        interval = length / (total + 1)
        self.shape.horizontal_line(color, point, length, width)
        # pygame.draw.circle(self.screen, pos, radius, color, width)
