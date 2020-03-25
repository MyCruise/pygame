import os
import json
from JoyGame.Src.System.toJson import config_wt, config_rd
from JoyGame.Src.Include.abspath import abspath_plus
import random


class SAVE2CONFIG:
    def __init__(self):
        self.max_row = 0
        self.max_column = 0
        self.path = abspath_plus('JoyGame/Src/Config/')
        self.map_index = 0
        self.map_row = 0
        self.map_column = 0
        self.map_dict = {}

    def save2config(self, config_name, dict, display=False):
        config_wt(os.path.join(self.path, config_name + "_config"), dict, display)

    def readFromConfig(self, config_name, display=False):
        config_dict = config_rd(os.path.join(self.path, config_name + "_config"), display)
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
            'Width': 1280,
            'Height': 720,
            "Mode": "noframe",
            "Background_Color": (255, 255, 255),
            "targetFPS": 60,
            "Block_Character": (160, 160),
            "Block_Map": (80, 80)
        }
        self.save2config("init", init_dict)

    def save2path(self):
        # "": "",
        path_dict = {
            "Materials": abspath_plus("JoyGame/Src/Assets/Materials/"),
            "Effect_Sounds": abspath_plus("JoyGame/Src/Assets/Effect/sounds/"),
            "Fonts": abspath_plus("JoyGame/Src/Assets/Fonts/"),
            "Materials_Character": abspath_plus("JoyGame/Src/Assets/Materials/character/"),
            "Materials_Environment": abspath_plus("JoyGame/Src/Assets/Materials/environment/"),
            "Materials_Sounds": abspath_plus("JoyGame/Src/Assets/Materials/sounds/"),
            "Materials_Music": abspath_plus("JoyGame/Src/Assets/Materials/music/"),
            "Materials_Images_Icon": abspath_plus("JoyGame/Src/Assets/Materials/image/icon/")
        }
        self.save2config("path", path_dict)

    def save2layout(self):
        # "": "",
        title_dict = {
            "Title_en_1": "Dungeon",
            "Title_en_2": "Adventure",
            "Title_cn_1": "地牢",
            "Title_cn_2": "冒险"
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
            "Deadband1": 0.2,
            "Deadband2": 0.6
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
        # "": "",
        game_pause_menu_dict = {
            "0": ["Resume", 35, 1],
            "1": ["Setting", 35, 1],
            "2": ["Homepage", 35, 1]
        }

        self.save2config("game_pause_menu", game_pause_menu_dict)

    def save2map_dict(self):
        # "": "",
        self.save2config("map", self.map_dict)

    def save2map(self):
        # "": "",
        for i in range(16):
            for j in range(9):
                self.add_map(self.map_dict, (i, j))
        self.save2config("map", self.map_dict)

    def set_map_size(self, max_column, max_row):
        self.map_column = 0
        self.map_row = 0
        self.max_column = max_column
        self.max_row = max_row

    def next_block(self, block: str):
        if self.map_column > self.max_column - 1:
            self.map_row += 1
            self.map_column = 0
            # print("row")
        if self.map_row < self.max_row:
            # print("column")
            if block != "":
                self.add_map(self.map_dict, (self.map_column, self.map_row), block=block)
            self.map_column += 1
            # print(self.map_column)

    def save2map_2(self):
        self.set_map_size(16, 9)
        # 1
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        # 2
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        # 3
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        # 4
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        # 5
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        # 6
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        # 7
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        # 8
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        # 9
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.next_block("bg")
        self.set_map_size(16, 9)
        # 1
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        # 2
        self.next_block("land_1")
        self.next_block("land_2")
        self.next_block("land_2")
        self.next_block("land_2")
        self.next_block("land_2")
        self.next_block("land_3")
        self.next_block("land_1")
        self.next_block("land_2")
        self.next_block("land_2")
        self.next_block("land_2")
        self.next_block("land_2")
        self.next_block("land_2")
        self.next_block("land_2")
        self.next_block("land_2")
        self.next_block("land_3")
        self.next_block("")
        # 3
        self.next_block("land_15")
        self.next_block("land_6")
        self.next_block("land_6")
        self.next_block("land_6")
        self.next_block("land_6")
        self.next_block("land_16")
        self.next_block("land_15")
        self.next_block("land_6")
        self.next_block("land_18")
        self.next_block("land_18")
        self.next_block("land_18")
        self.next_block("land_18")
        self.next_block("land_18")
        self.next_block("land_10")
        self.next_block("land_11")
        self.next_block("")
        # 4
        self.next_block("land_9")
        self.next_block("land_18")
        self.next_block("land_18")
        self.next_block("land_18")
        self.next_block("land_10")
        self.next_block("land_18")
        self.next_block("land_18")
        self.next_block("land_11")
        self.next_block("land_17")
        self.next_block("land_17")
        self.next_block("land_17")
        self.next_block("land_17")
        self.next_block("land_17")
        self.next_block("land_13")
        self.next_block("land_14")
        self.next_block("")
        # 5
        self.next_block("land_12")
        self.next_block("land_17")
        self.next_block("land_17")
        self.next_block("land_17")
        self.next_block("land_13")
        self.next_block("land_17")
        self.next_block("land_17")
        self.next_block("land_14")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        # 6
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        # 7
        self.next_block("")
        self.next_block("")
        self.next_block("land_1")
        self.next_block("land_2")
        self.next_block("land_2")
        self.next_block("land_2")
        self.next_block("land_3")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        # 8
        self.next_block("")
        self.next_block("land_4")
        self.next_block("land_5")
        self.next_block("land_6")
        self.next_block("land_6")
        self.next_block("land_6")
        self.next_block("land_7")
        self.next_block("land_8")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        # 9
        self.next_block("")
        self.next_block("")
        self.next_block("land_9")
        self.next_block("land_18")
        self.next_block("land_18")
        self.next_block("land_18")
        self.next_block("land_11")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")
        self.next_block("")

        self.save2config("map", self.map_dict)

    def add_map(self, dict, point, block=""):
        if not block:
            block = "land_" + str(random.randint(1, 18))
        dict[str(self.map_index)] = [block, point]
        self.map_index += 1
        return dict

    def readFromMap(self):
        return self.readFromConfig("map")

    def init_config(self):
        self.save2player()
        self.save2path()
        self.save2layout()
        self.save2control()
        self.save2play()
        self.save2setting()
        self.save2tutorial()
        self.save2game_pause_menu()
        self.save2map_2()


if __name__ == '__main__':
    s2c = SAVE2CONFIG()
    s2c.init_config()
