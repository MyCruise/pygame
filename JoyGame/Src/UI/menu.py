from pygame import draw
from JoyGame.Src.Include.color import Color
from JoyGame.Src.System.shape import Shape, Button


class Menu:
    def __init__(self, screen, text):
        self.width = screen.Width
        self.height = screen.Height
        self.screen = screen.screen
        self.color = Color()
        self.text = text
        self.shape = Shape(self.screen)
        self.button = Button(self.screen, text)
        self.text_height = 0

    def __start__(self):
        self.text.addText("D u n g e o n", 90, (self.width/2, 100), self.color.Black, None, 0)
        self.text.addText("A d v e n t u r e", 80, (self.width/2, 210), self.color.Black, None, 0)

        self.button.button1("Play", 30, self.color.Black, (self.width/2, 250), (240, 50), 10, 1, 0)
        self.button.button1("Setting", 30, self.color.Black, (self.width/2, 300), (240, 50), 10, 1, 0)
        self.button.button1("Quit", 30, self.color.Black, (self.width/2, 360), (240, 50), 10, 1, 0)

        # self.shape.round_rect(White, (50, 40), (100, 30), 8, 1)

    def __test__(self):
        self.text.addText("test", 20, (self.width - 100, 40), self.color.Black, None, 1)
        self.text.addText("test", 20, (self.width - 98, 42), self.color.Gray, None, 1)
