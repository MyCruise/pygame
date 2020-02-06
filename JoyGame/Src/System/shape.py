import pygame
from JoyGame.Src.Include.vector import Vector2


class Shape:
    def __init__(self, surface):
        self.sur = surface

    '''
    矩形
    pygame.draw.rect(self.sur, color, width)
    
    多边形
    pygame.draw.polygon(self.sur, color, width)
    
    圆
    pygame.draw.circle(self.sur, pos, radius, color, width)
    
    椭圆
    pygame.draw.ellipse(self.sur, color, Rect, width)
    
    部分椭圆
    pygame.draw.arc(self.sur, color, Rect, start_angle, stop_angle, width)
    
    线段
    pygame.draw.line(self.sur, color, start_pos, end_pos, width)
    pygame.draw.aaline(self.sur, color, start_pos, end_pos, width)
    
    线段集合
    pygame.draw.lines(self.sur, color, closed, pointlist, width)
    pygame.draw.aalines(self.sur, color, closed, pointlist, width)
    '''

    def button(self, color, rad, rect, width=0):
        dia = rad * 2

        pygame.draw.arc(self.sur, color, (rect[0], rect[1], rect[0] + dia, rect[1] + dia), 270, 360, width)
        pygame.draw.line(self.sur, color, (rect[0]+rad, rect[1]), (rect[2]-rad, rect[1]), width)

        pygame.draw.arc(self.sur, color, (rect[2] - dia, rect[1], rect[2], rect[1] + dia), 0, 90, width)
        pygame.draw.line(self.sur, color, (rect[2], rect[1]+rad), (rect[2], rect[3]-rad), width)

        pygame.draw.arc(self.sur, color, (rect[2] - dia, rect[1] - dia, rect[2], rect[1]), 90, 180, width)
        pygame.draw.line(self.sur, color, (rect[0] + rad, rect[3]), (rect[2] - rad, rect[3]), width)

        pygame.draw.arc(self.sur, color, (rect[0], rect[3] - dia, rect[0] + dia, rect[3]), 180, 270, width)
        pygame.draw.line(self.sur, color, (rect[0], rect[1] + rad), (rect[0], rect[3] - rad), width)
