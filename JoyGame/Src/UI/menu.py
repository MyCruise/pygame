from pygame import draw, Surface
from JoyGame.Src.Include.color import Color
from JoyGame.Src.System.shape import Shape, Button
from JoyGame.Src.System.effect import Effect


class Menu:
    def __init__(self, screen, text, clock, glovar, mc):
        self.width = screen.Width
        self.height = screen.Height
        self.screen = screen
        self.color = Color()
        self.effect = Effect()
        self.clock = clock
        self.glovar = glovar
        self.text = text
        self.mc = mc
        self.shape = Shape(self.screen.screen)
        self.button = Button(self.screen.screen, text)

        # init variable
        self.text_height = 0
        self.numButton = 0

        self.any_button_color = self.color.White

        self.length = 300
        self.flip_flag_1 = False

    def offset(self, height, offset):
        self.numButton += 1
        return height + offset

    def layout_homepage(self, size: tuple, start: int, span: int):
        menu_height = start - span
        self.text.addText(self.glovar.title_en_1, 90, (self.width / 2, 100), self.color.Black, None, 1)
        self.text.addText(self.glovar.title_en_2, 80, (self.width / 2, 210), self.color.Black, None, 1)

        for i in range(self.glovar.button_maxNum_1):
            menu_height = self.offset(menu_height, span)
            i = str(i)
            self.button.round_button(self.glovar.layout_button_config[i][0], self.glovar.layout_button_config[i][1],
                                     self.color.Gray, (self.width / 2 - 120, menu_height), size, 10,
                                     self.glovar.layout_button_config[i][2], 0)

    def press_anything_to_continue(self):
        if self.flip_flag_1:
            self.length += 1
            self.any_button_color = self.color.__add__(self.any_button_color, (1, 1, 1))
        elif not self.flip_flag_1:
            self.length -= 1
            self.any_button_color = self.color.__sub__(self.any_button_color, (1, 1, 1))
        if self.any_button_color == self.color.Black:
            self.flip_flag_1 = True
        elif self.any_button_color == self.color.White:
            self.flip_flag_1 = False
        self.text.addText("Press any button to continue", 20, (self.width / 2, self.height - 100),
                          self.any_button_color, None, 3)
        self.shape.horizontal_line(self.any_button_color,
                                   (self.width / 2, self.height - 70), self.length, 2)

    def layout_homepage_choice(self, index: int):
        menu_height = 310
        menu_height = self.offset(menu_height, index * 85)
        self.button.choice_button(self.color.Gray, (self.width / 2 - 120, menu_height), (240, 60), 10, 2, 0)

    def logo_page(self):
        self.screen.screen.blit(self.screen.background, (0, 0))
        self.screen.breath_color(self.color.White, self.color.Black)
        self.screen.set_background_color(self.screen.background_color)

    def homepage(self):
        self.screen.screen.blit(self.screen.background, (0, 0))
        self.layout_homepage((240, 60), 310, 85)
        self.layout_homepage_choice(self.mc.index)

    def load_page(self):
        self.press_anything_to_continue()

    def play(self):
        self.screen.screen.blit(self.screen.background, (0, 0))

    def setting(self):
        self.screen.screen.blit(self.screen.background, (0, 0))

    def tutorial(self):
        self.screen.screen.blit(self.screen.background, (0, 0))

    def __test__(self):
        self.fps = self.clock.get_fps()
        height = 30
        background_color = self.color.__sub__(self.color.White, self.screen.screen.get_at((self.width - 10, 10)))
        self.text.addText("fps:\t" + str(round(self.fps, 1)), 20, (self.width - 60, height),
                          background_color, None, 2)
        height += 30
        self.text.addText("%d %d %d" % (self.mc.index, self.mc.layer, self.mc.enter), 20, (self.width - 60, height),
                          background_color, None, 2)
        # self.text.addText("test", 20, (self.width - 100, height+25), self.color.Black, None, 1)
