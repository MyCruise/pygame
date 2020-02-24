import os
import pygame
from JoyGame.Src.Include.abspath import abspath_join
from JoyGame.Src.Include.color import *
from JoyGame.Src.Include.glovar import GLOVAR


class Text:
    def __init__(self, screen):
        self.screen = screen
        self.glovar = GLOVAR()
        self.language = os.listdir(self.glovar.Fonts)
        self.fonts_chinese_path = abspath_join(self.glovar.Fonts, self.language[0])
        self.fonts_alpha_path = abspath_join(self.glovar.Fonts, self.language[1])
        self.fonts_chinese = os.listdir(self.fonts_chinese_path)
        self.fonts_alpha = os.listdir(self.fonts_alpha_path)
        self.maxLength_chinese = len(self.fonts_chinese)
        self.maxLength_alpha = len(self.fonts_alpha)

    def addText(self, text: str, size: int, position: tuple, color: tuple, background_color, index: int):
        if self.isChinese(text):
            if index > self.maxLength_chinese:
                index = self.maxLength_chinese
            self.fontObj = pygame.font.Font(abspath_join(self.fonts_chinese_path, self.fonts_chinese[index]), size)
        elif self.isAlphabet(text):
            if index > self.maxLength_alpha:
                index = self.maxLength_alpha
            self.fontObj = pygame.font.Font(abspath_join(self.fonts_alpha_path, self.fonts_alpha[index]), size)
        else:
            if index > self.maxLength_alpha:
                index = self.maxLength_alpha
            self.fontObj = pygame.font.Font(abspath_join(self.fonts_alpha_path, self.fonts_alpha[index]), size)

        if background_color is None:
            textSurfaceObj = self.fontObj.render(text, True, color)
        else:
            textSurfaceObj = self.fontObj.render(text, True, color, background_color)
        testRectObj = textSurfaceObj.get_rect()
        testRectObj.center = position
        self.screen.blit(textSurfaceObj, testRectObj)
        return text, size, position, color, background_color, index

    def addFontShadow(self, text: str, size: int, position: tuple, color: tuple, background_color, index: int):
        self.addText(text, size, position, color, background_color, index)

    """判断一个unicode是否是汉字"""

    def isChinese(self, uchar):
        if u'\u4e00' <= uchar <= u'\u9fa5':
            return True
        else:
            return False

    """判断一个unicode是否是数字"""

    def isNumber(self, uchar):
        if u'\u0030' <= uchar <= u'\u0039':
            return True
        else:
            return False

    """判断一个unicode是否是英文字母"""

    def isAlphabet(self, uchar):
        if (u'\u0041' <= uchar <= u'\u005a') or (u'\u0061' <= uchar <= u'\u007a'):
            return True
        else:
            return False

    """判断是否是（汉字，数字和英文字符之外的）其他字符"""

    def is_other(self, uchar):
        if not (self.isChinese(uchar) or self.isNumber(uchar) or self.isAlphabet(uchar)):
            return True
        else:
            return False


if __name__ == '__main__':
    glovar = GLOVAR()
    text = Text("screen")
    print(os.path.exists(abspath_join(glovar.Fonts, text.language[0])))
    print(text.fonts_alpha, text.fonts_alpha[0])
    print(abspath_join(text.fonts_alpha_path, text.fonts_alpha[0]))
    print(text.language)
    # print(glovar.Fonts)
    # print(os.listdir(glovar.Fonts))
