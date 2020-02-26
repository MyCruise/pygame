import os
import pymunk

from JoyGame.Src.System.toJson import config_wt, config_rd
from JoyGame.Src.Include.abspath import abspath, abspath_join


class SAVE2CONFIG:
    def __init__(self):
        self.path = abspath('JoyGame/Src/Config/')

    def save2config(self, config_name, dict, display=False):
        sorted(dict.keys())
        config_wt(self.path + config_name + "_config", dict, display)
        config_dict = config_rd(self.path + config_name + "_config")
        if display:
            print(config_dict)

    def readFromConfig(self, config_name, display="False"):
        config_dict = config_rd(self.path + config_name + "_config", display)
        if display:
            print(config_dict)
        return config_dict

    def save2player(self):
        # "": "",
        init_dict = {
            "Resolution": "1280,720",
            "Mode": "Fullscreen",
            "targetFPS": 60
        }

        self.save2config("init", init_dict)

    def save2path(self):
        # "": "",
        path_dict = {
            "Image-icon": "JoyGame/Src/Assets/Image/icon",
            "Music": "JoyGame/Src/Assets/Music",
            "Materials": "JoyGame/Src/Assets/Materials",
            "Effect-action": "JoyGame/Src/Assets/Effect/action",
            "Effect-sounds": "JoyGame/Src/Assets/Effect/sounds",
            "Fonts": "JoyGame/Src/Assets/Fonts"
        }

        self.save2config("path", path_dict)

    def save2layout(self):
        # "": "",
        title_dict = {
            "title_cn_1": "D u n g e o n",
            "title_cn_2": "A d v e n t u r e",
            "title_en_1": "地牢",
            "title_en_2": "冒险"
        }

        layout_button_dict = {
            '0': ["Play", 35, 1],
            '1': ["Setting", 35, 1],
            '2': ["Tutorial", 35, 1],
            '3': ["Quit", 35, 1]
        }

        self.save2config("title", title_dict)
        self.save2config("layout_button", layout_button_dict)

    def save2control(self):
        # "": "",
        control_dict = {
            "deadband1": 0.2,
            "deadband2": 0.6
        }

        self.save2config("control", control_dict)

    def init_config(self):
        s2c.save2player()
        s2c.save2path()
        s2c.save2layout()
        s2c.save2control()


if __name__ == '__main__':
    s2c = SAVE2CONFIG()
    s2c.init_config()
