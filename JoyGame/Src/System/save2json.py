import os
import pymunk

from JoyGame.Src.System.toJson import config_wt, config_rd
from JoyGame.Src.Include.abspath import abspath


class SAVE2CONFIG:
    def __init__(self):
        self.path = abspath('JoyGame/Src/Config/')

    def save2config(self, config_name, dict, display="False"):
        sorted(dict.keys())
        config_wt(self.path + config_name + "_config", dict)
        config_dict = config_rd(self.path + config_name + "_config")
        if not display:
            print(config_dict)

    def readFromConfig(self, config_name, display="False"):
        config_dict = config_rd(self.path + config_name + "_config")
        if not display:
            print(config_dict)
        return config_dict

    def save2player(self):
        # "": "",
        init_dict = {
            "Resolution": "1280,720",
            "Fullscreen": 0,
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

    def save2text(self):
        path_dict = {
            "": ""
        }


if __name__ == '__main__':
    s2c = SAVE2CONFIG()
    s2c.save2player()
    s2c.save2path()
    s2c.save2text()
