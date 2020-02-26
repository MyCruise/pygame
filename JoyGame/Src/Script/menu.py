from JoyGame.Src.Include.glovar import GLOVAR


class MenuControl:
    def __init__(self):
        # Initialize class
        self.glovar = GLOVAR()

        # Initialize variable
        self.layer = 0
        self.enter = 0
        self.index = 0
        self.numButton = self.glovar.button_maxNum_1

    def rear(self):
        self.index += 1
        if self.index >= self.numButton:
            self.index -= self.numButton

    def front(self):
        self.index -= 1
        if self.index < 0:
            self.index += self.numButton

    def next(self):
        self.index = 0
        self.layer += 1
        self.enter = 1

    def previous(self):
        self.index = 0
        self.layer -= 1
        if self.layer < 1:
            self.layer = 1
