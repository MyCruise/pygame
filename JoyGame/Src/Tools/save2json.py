import os
import json
from JoyGame.Src.System.toJson import config_wt, config_rd
from JoyGame.Src.Include.abspath import abspath
import random


class SAVE2CONFIG:
    def __init__(self):
        self.path = abspath('JoyGame/Src/Config/')
        self.map_index = 0

    def save2config(self, config_name, dict, display=False):
        sorted(dict.keys())
        config_wt(self.path + config_name + "_config", dict, display)
        config_dict = config_rd(self.path + config_name + "_config")
        if display:
            print(config_dict)

    def readFromConfig(self, config_name, display=False):
        config_dict = config_rd(self.path + config_name + "_config", display)
        if display:
            print(config_dict)
        return config_dict

    def readFromSpritesConfig(self, filePath, display=False):
        config_dict = config_rd(filePath, display)
        json_dict = json.dumps(config_dict, sort_keys=True, indent=4, separators=(',', ': '))
        if display:
            print(json_dict)
        return config_dict

    def save2player(self):
        # "": "",
        init_dict = {
            "Resolution": [1280, 720],
            "Mode": "noframe",
            "Background_color": (255, 255, 255),
            "targetFPS": 60,
            "Block_character": (160, 160),
            "Block_map": (80, 80)
        }
        self.save2config("init", init_dict)

    def save2path(self):
        # "": "",
        path_dict = {
            "music": "JoyGame/Src/Assets/music/",
            "Materials": "JoyGame/Src/Assets/Materials/",
            "Effect-character": "JoyGame/Src/Assets/Effect/character/",
            "Effect-sounds": "JoyGame/Src/Assets/Effect/sounds/",
            "Fonts": "JoyGame/Src/Assets/Fonts/",
            "Materials-character": "JoyGame/Src/Assets/Materials/character/",
            "Materials-environment": "JoyGame/Src/Assets/Materials/environment/",
            "Materials-sounds": "JoyGame/Src/Assets/Materials/sounds/",
            "Materials-music": "JoyGame/Src/Assets/Materials/music/",
            "Materials-images-icon": "JoyGame/Src/Assets/Materials/image/icon/"
        }
        self.save2config("path", path_dict)

    def save2layout(self):
        # "": "",
        title_dict = {
            "title_en_1": "D u n g e o n",
            "title_en_2": "A d v e n t u r e",
            "title_cn_1": "地牢",
            "title_cn_2": "冒险"
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

    def save2play(self):
        # "": "",
        play_dict = {
            "0": ["New game"],
            "1": ["Continue"],
            "2": ["Load"]
        }

        self.save2config("play", play_dict)

    def save2setting(self):
        # "": "",
        setting_dict = {
            "1": ["resolution", "1280,720"],
            "2": ["brightness", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            "3": ["display_mode", "fullscreen", "halfscreen", "noframe"],
            "4": ["control_device", "mouse & keyboard", "controller"]
        }

        self.save2config("setting", setting_dict)

    def save2tutorial(self):
        # "": "",
        tutorial_dict = {
            "1": ["1"],
            "2": ["2"],
            "3": ["3"]
        }

        self.save2config("tutorial", tutorial_dict)

    def save2game_pause_menu(self):
        # "land_": "land_",
        game_pause_menu_dict = {
            "0": ["Resume", 35, 1],
            "1": ["Setting", 35, 1],
            "2": ["Homepage", 35, 1]
        }

        self.save2config("game_pause_menu", game_pause_menu_dict)

    def save2map_dict(self, map_dict):
        # "land_": "land_",
        self.save2config("map", map_dict)

    def save2map(self):
        # "land_": "land_",
        map_dict = {}
        for i in range(16):
            for j in range(9):
                map_dict = self.add_map(map_dict, (i, j))
        self.save2config("map", map_dict)

    def add_map(self, dict, point, block=""):
        block = "land_" + str(random.randint(1, 18))
        dict[str(self.map_index)] = [block, point]
        self.map_index += 1
        return dict

    def readFromMap(self):
        return self.readFromConfig("map")

    def init_config(self):
        s2c.save2player()
        s2c.save2path()
        s2c.save2layout()
        s2c.save2control()
        s2c.save2play()
        s2c.save2setting()
        s2c.save2tutorial()
        s2c.save2game_pause_menu()
        s2c.save2map()


if __name__ == '__main__':
    s2c = SAVE2CONFIG()
    s2c.init_config()
