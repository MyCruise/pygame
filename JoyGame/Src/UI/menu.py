import pygame
from pygame import draw, Surface
from JoyGame.Src.Include.color import Color
from JoyGame.Src.System.shape import Shape, Button
from JoyGame.Src.System.effect import Effect
from JoyGame.Src.System.picture import Picture
from JoyGame.Src.UI.Game import Games
from JoyGame.Src.Include.glovar import GLOVAR


class Menu:
    def __init__(self, screen, text, clock, mc, games):
        self.width = screen.width
        self.height = screen.height

        # Initialize class
        self.glovar = GLOVAR()
        self.screen = screen
        self.color = Color()
        self.effect = Effect()
        self.clock = clock
        self.text = text
        self.mc = mc
        self.games = games
        self.picture = Picture(self.screen)
        self.shape = Shape(self.screen.screen)
        self.button = Button(self.screen.screen, text)

        # Initialize variable
        self.text_height = 0
        self.numButton = 0
        self.setting_menu_list = []

        self.any_button_color = self.color.White

        self.length = 300
        self.flip_flag = False

    def offset(self, distance, offset):
        self.numButton += 1
        return distance + offset

    def press_anything_to_continue(self):
        if self.flip_flag:
            self.length += 1
            self.any_button_color = self.color.__add__(self.any_button_color, (1, 1, 1))
        elif not self.flip_flag:
            self.length -= 1
            self.any_button_color = self.color.__sub__(self.any_button_color, (1, 1, 1))
        if self.any_button_color == self.color.Black:
            self.flip_flag = True
        elif self.any_button_color == self.color.White:
            self.flip_flag = False
        self.text.addText("Press any button to continue", "en", 20, (self.width / 2, self.height - 100),
                          self.any_button_color, None, 3)
        self.shape.horizontal_line(self.any_button_color,
                                   (self.width / 2, self.height - 70), self.length, 2)

    def layout_homepage(self, size: tuple, start: int, span: int, index: int):
        menu_height = start - span
        self.text.addText(self.glovar.title_en_1, "en", 90, (self.width / 2, 100), self.color.Black, None, 1)
        self.text.addText(self.glovar.title_en_2, "en", 80, (self.width / 2, 210), self.color.Black, None, 1)

        for i in range(len(self.glovar.homepage_menu_config)):
            menu_height = self.offset(menu_height, span)
            i = str(i)
            self.button.round_button(self.glovar.homepage_menu_config[i][0], self.glovar.homepage_menu_config[i][1],
                                     self.color.Gray, (self.width / 2 - 120, menu_height), size, 10,
                                     self.glovar.homepage_menu_config[i][2], 0)
        menu_height = start
        menu_height = self.offset(menu_height, index * span)
        self.button.choice_button(self.color.Gray, (self.width / 2 - 120, menu_height), (240, 60), 10, 2)

    def play_menu_button(self, text: str, color: tuple, point: tuple, size: tuple):
        self.text.addText(text, "en", int(size[0] / 6), (point[0] + int(size[0] / 2), point[1] + 30), color, None, 3)
        self.shape.horizontal_line(color, (point[0] + int(size[0] / 2), point[1] + 60), size[0], 1)
        self.shape.round_rect(color, point, size, int(size[0] / 10), 2)

    def play_menu(self, point: tuple, span: int):
        for i in range(len(self.glovar.play_menu_config)):
            self.play_menu_button(self.glovar.play_menu_config[str(i)][0], self.color.Gray,
                                  (point[0] + i * span, point[1]), (200, 200))
        menu_width = point[1] - span
        menu_width = self.offset(menu_width, self.mc.index * span)
        self.button.choice_button(self.color.Gray, (point[0] + menu_width - 20, point[1] - 20), (240, 240), 20, 2)

    def setting_menu(self, point: tuple, span: int, length: int, index_list: list):
        if len(index_list) == len(self.glovar.setting_menu_config):
            height = point[1] - span
            for i in self.glovar.setting_menu_config:
                try:
                    height = self.offset(height, span)
                    self.button.switch_bar(self.glovar.setting_menu_config[str(i)][0], self.color.Black,
                                           (point[0], height), length, 3, 4,
                                           len(self.glovar.setting_menu_config[str(i)][index_list[int(i) - 1]]),
                                           index_list[int(i) - 1], 2)
                except Exception as error:
                    print(len(self.glovar.setting_menu_config[i][1:]))
                    print(self.glovar.setting_menu_config[i][1:])
                    print(error)
        else:
            print("False")

    def game_pause_menu(self, size: tuple, start: int, span: int, index: int):
        menu_height = start - span
        for i in range(len(self.glovar.game_pause_menu_config)):
            menu_height = self.offset(menu_height, span)
            i = str(i)
            self.button.round_button(self.glovar.game_pause_menu_config[i][0], self.glovar.game_pause_menu_config[i][1],
                                     self.color.Gray, (self.width / 2 - 120, menu_height), size, 10,
                                     self.glovar.game_pause_menu_config[i][2], 0)
        menu_height = start
        menu_height = self.offset(menu_height, index * span)
        self.button.choice_button(self.color.Gray, (self.width / 2 - 120, menu_height), (240, 60), 10, 2)

    '''
    Interface
    '''

    def logo_page(self):
        self.screen.screen.blit(self.screen.background, (0, 0))
        self.screen.breath_color(self.color.White, self.color.Black)
        # self.picture.load_image("Biohazard", (50, 50), (50, 50))
        self.screen.set_background_color(self.screen.background_color)

    def homepage(self):
        self.screen.screen.blit(self.screen.background, (0, 0))
        self.screen.set_background_color(self.color.White)
        self.layout_homepage((240, 60), 310, 85, self.mc.index)

    def press_bar(self):
        self.press_anything_to_continue()

    def play(self):
        self.screen.reset_background_color()
        self.screen.screen.blit(self.screen.background, (0, 0))
        self.play_menu((200, 300), 300)
        self.button.joystick_button("A", (self.width - 100, self.height - 100))
        self.button.joystick_button("B", (self.width - 60, self.height - 140))
        self.button.joystick_button("X", (self.width - 140, self.height - 140))
        self.button.joystick_button("Y", (self.width - 100, self.height - 180))

    def setting(self):
        self.screen.reset_background_color()
        self.screen.screen.blit(self.screen.background, (0, 0))
        self.setting_menu((int(self.width / 2), 100), 30, 200, [0, 0, 0, 0])

    def tutorial(self):
        self.screen.reset_background_color()
        self.screen.screen.blit(self.screen.background, (0, 0))
        self.text.addText("Icon", "en", 40, (int(self.width / 2), 100), self.color.Gray, None, 2)
        self.picture.addImage(self.picture.load_image("Biohazard", (600, 600)), (int(self.width / 2) - 300, 110))

    def game(self):
        self.screen.reset_background_color()
        self.screen.screen.blit(self.screen.background, (0, 0))
        if not self.mc.pause:
            self.games.game_ui()
        else:
            self.game_pause_menu((240, 60), 310, 85, self.mc.index)

    def test(self):
        height = 30
        background_color = self.color.__sub__(self.color.White, self.screen.screen.get_at((self.width - 10, 10)))
        self.text.addText("fps:\t" + str(round(self.clock.get_fps(), 1)), "en", 20, (self.width - 60, height),
                          background_color, None, 2)
        height += 30
        self.text.addText("index,layer,enter", "en", 20,
                          (self.width - 80, height), background_color, None, 2)
        height += 30
        self.text.addText("%d     %d     %d" % (self.mc.index, self.mc.layer, self.mc.enter), "en", 20,
                          (self.width - 100, height), background_color, None, 2)
        height += 30
        self.text.addText(str(self.mc.pause), "en", 20, (self.width - 100, height), background_color, None, 2)
        # self.text.addText("test", 20, (self.width - 100, height+25), self.color.Black, None, 1)
