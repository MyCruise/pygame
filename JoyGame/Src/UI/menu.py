from pygame import draw
from JoyGame.Src.Include.color import Color
from JoyGame.Src.System.shape import Shape, Button
from JoyGame.Src.System.effect import Effect


class Menu:
    def __init__(self, screen, text, clock, glovar, mc):
        self.width = screen.Width
        self.height = screen.Height
        self.screen = screen
        self.color = Color()
        self.effect = Effect(self.screen)
        self.clock = clock
        self.glovar = glovar
        self.text = text
        self.mc = mc
        self.shape = Shape(self.screen.screen)
        self.button = Button(self.screen.screen, text)

        # init variable
        self.text_height = 0
        self.numButton = 0
        self.background_color = self.color.Black

    def offset(self, height, offset):
        self.numButton += 1
        return height + offset

    def layout_2_start__(self, size: tuple, start: int, span: int):
        menu_height = start - span
        self.text.addText("D u n g e o n", 90, (self.width / 2, 100), self.color.Black, None, 1)
        self.text.addText("A d v e n t u r e", 80, (self.width / 2, 210), self.color.Black, None, 1)

        for i in range(self.glovar.button_maxNum_1):
            menu_height = self.offset(menu_height, span)
            i = str(i)
            self.button.round_button(self.glovar.layout_button_config[i][0], self.glovar.layout_button_config[i][1],
                                     self.color.Gray, (self.width / 2 - 120, menu_height), size, 10,
                                     self.glovar.layout_button_config[i][2], 0)

    def layout_choice(self, index: int):
        menu_height = 310
        menu_height = self.offset(menu_height, index * 85)
        self.button.choice_button(self.color.Gray, (self.width / 2 - 120, menu_height), (240, 60), 10, 2, 0)

    def layout_1(self):
        self.screen.screen.blit(self.screen.background, (0, 0))
        if self.background_color != self.color.White:
            self.background_color = self.color.__add__(self.background_color, (1, 1, 1))

        self.screen.set_background_color(self.background_color)

    def layout_2(self):
        self.screen.screen.blit(self.screen.background, (0, 0))
        self.layout_2_start__((240, 60), 310, 85)
        self.layout_choice(self.mc.index)
        self.__test__()

    def layout_3(self):
        pass

    def __test__(self):
        self.fps = self.clock.get_fps()
        height = 30
        self.text.addText("fps:\t" + str(round(self.fps, 1)), 20, (self.width - 60, height), self.color.Gray, None, 2)
        # self.text.addText("test", 20, (self.width - 100, height+25), self.color.Black, None, 1)
