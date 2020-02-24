import os
from JoyGame.Src.Include.glovar import GLOVAR


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __set__(self, instance, value):
        pass

    def __right__(self):
        pass

    def __left__(self):
        pass


if __name__ == '__main__':
    glovar = GLOVAR()
    print(os.path.exists(glovar.Icon))
