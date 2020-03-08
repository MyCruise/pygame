import os
import pygame
from JoyGame.Src.Include.abspath import abspath_join
from JoyGame.Src.Include.glovar import GLOVAR
from JoyGame.Src.Tools.save2json import SAVE2CONFIG
from JoyGame.Src.System.picture import Picture


class Map:
    def __init__(self, screen):
        self.screen = screen
        self.width = self.screen.width
        self.height = self.screen.height
        self.maxBlockNum_w = 0
        self.maxBlockNum_h = 0

        self.s2c = SAVE2CONFIG()
        self.glovar = GLOVAR()
        self.environment = self.glovar.MaterialsEnvironment
        self.label = 0
        self.start = (0, 0)
        self.loadFlag = True
        self.map_point = []
        self.map_block = []
        self.label_list = os.listdir(self.environment)
        self.block_list = os.listdir(abspath_join(self.environment, self.label_list[self.label]))

    def load_map_block(self, map_block):
        if map_block in self.block_list:
            path = abspath_join(self.environment, self.label_list[self.label])
            block = abspath_join(path, map_block)
            image = pygame.image.load(block).convert_alpha()
            image = pygame.transform.scale(image, self.glovar.block_map)
            return image
        else:
            print(str(map_block))

    def saveMap(self):
        index = 0
        map_dict = {}
        for i in range(len(self.map_block)):
            map_dict[str(index)] = [self.map_block[i], self.map_point[i]]
        self.s2c.save2map(map_dict)

    def loadMap(self):
        if not self.map_block and not self.map_point:
            self.map_dict = self.s2c.readFromMap()
            for i in range(len(self.map_dict)):
                self.map_block.append(self.map_dict[str(i)][0])
                self.map_point.append(self.map_dict[str(i)][1])

    def addMapBlock(self, map_block, point):
        point = tuple(map(lambda i, j: i * j, point, self.glovar.block_map))
        if not self.loadFlag:
            self.map_block.append(map_block)
            self.map_point.append(point)
        self.screen.screen.blit(self.load_map_block(map_block), point)

    def mapping(self, map_point: tuple):
        self.loadMap()
        for i in range(len(self.map_dict)):
            point = tuple(map(lambda i, j: i + j, self.map_point[i], map_point))
            self.addMapBlock(self.map_block[i] + ".png", point)


if __name__ == '__main__':
    glovar = GLOVAR()
