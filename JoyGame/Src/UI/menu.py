from pygame import draw
from JoyGame.Src.Include.color import Color
from JoyGame.Src.System.shape import Shape, Button


class Menu:
    def __init__(self, screen, text, clock):
        self.width = screen.Width
        self.height = screen.Height
        self.screen = screen.screen
        self.color = Color()
        self.clock = clock
        self.text = text
        self.shape = Shape(self.screen)
        self.button = Button(self.screen, text)
        self.text_height = 0

    @staticmethod
    def offset(height, offset):
        return height + offset

    def __start__(self):
        time = 1
        self.text.addText("D u n g e o n", 90, (self.width / 2, 100), self.color.Black, None, 1)
        self.text.addText("A d v e n t u r e", 80, (self.width / 2, 210), self.color.Black, None, 1)

        menu_height = 310
        self.button.button1("Play", 35, self.color.Black, (self.width / 2 - 120, menu_height), (240, 60), 10, 1, 0)

        menu_height = self.offset(menu_height, 85)
        self.button.button1("Setting", 35, self.color.Black, (self.width / 2 - 120, menu_height), (240, 60), 10, 1,
                            0)

        menu_height = self.offset(menu_height, 85)
        self.button.button1("Quit", 35, self.color.Black, (self.width / 2 - 120, menu_height), (240, 60), 10, 1,
                            0)

        # self.shape.round_rect(White, (50, 40), (100, 30), 8, 1)

    def __test__(self):
        self.fps = self.clock.get_fps()
        height = 30
        self.text.addText("fps:\t" + str(round(self.fps, 1)), 20, (self.width - 100, height), self.color.Gray, None, 2)
        # self.text.addText("test", 20, (self.width - 100, height+25), self.color.Black, None, 1)
