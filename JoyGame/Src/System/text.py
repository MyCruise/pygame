import os
import pygame
from JoyGame.Src.Include.color import *
# from JoyGame.Src.Include.glovar import GLOVAR
from JoyGame.Src.System.global_variable import get_value


class Text:
    def __init__(self, screen):
        self.screen = screen
        self.language = os.listdir(get_value('Fonts'))
        self.fonts_chinese_path = os.path.join(get_value('Fonts'), self.language[0])
        self.fonts_alpha_path = os.path.join(get_value('Fonts'), self.language[1])
        self.fonts_chinese = os.listdir(self.fonts_chinese_path)
        self.fonts_alpha = os.listdir(self.fonts_alpha_path)
        self.maxLength_chinese = len(self.fonts_chinese)
        self.maxLength_alpha = len(self.fonts_alpha)

    def addText(self, text: str, label: str, size: int, position: tuple, color: tuple, background_color, index: int):
        # Chinese language
        if label == "cn":
            if index > self.maxLength_chinese:
                index = self.maxLength_chinese
            self.fontObj = pygame.font.Font(os.path.join(self.fonts_chinese_path, self.fonts_chinese[index]), size)
        # English language
        elif label == "en":
            if index > self.maxLength_alpha:
                index = self.maxLength_alpha
            self.fontObj = pygame.font.Font(os.path.join(self.fonts_alpha_path, self.fonts_alpha[index]), size)
        # other language
        else:
            if index > self.maxLength_alpha:
                index = self.maxLength_alpha
            self.fontObj = pygame.font.Font("", size)

        # if self.isChinese(text):
        #     pass
        # elif self.isAlphabet(text):
        #     pass
        # else:
        #     pass

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
