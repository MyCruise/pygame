from JoyGame.Src.System.toJson import config_wt, config_rd
from JoyGame.Src.Include.abspath import abspath


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
            "Music": "JoyGame/Src/Assets/Music/",
            "Materials": "JoyGame/Src/Assets/Materials/",
            "Effect-character": "JoyGame/Src/Assets/Effect/character/",
            "Effect-sounds": "JoyGame/Src/Assets/Effect/sounds/",
            "Fonts": "JoyGame/Src/Assets/Fonts/",
            "Materials-character": "JoyGame/Src/Assets/Materials/character/",
            "Materials-environment": "JoyGame/Src/Assets/Materials/environment/",
            "Materials-sounds": "JoyGame/Src/Assets/Materials/sounds/",
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
            "1": [""],
            "2": [""],
            "3": [""]
        }

        self.save2config("tutorial", tutorial_dict)

    def save2game_pause_menu(self):
        # "": "",
        game_pause_menu_dict = {
            "0": ["Resume", 35, 1],
            "1": ["Setting", 35, 1],
            "2": ["Homepage", 35, 1],
        }

        self.save2config("game_pause_menu", game_pause_menu_dict)

    def save2map(self, map_dict):
        # "": "",
        map_dict = {
            "0": ["land_1", (0, 0)],
            "1": ["land_1", (0, 1)],
            "2": ["land_1", (0, 2)],
            "3": ["land_9", (0, 3)],
            "4": ["land_2", (1, 0)],
            "5": ["land_6", (1, 1)],
            "6": ["land_6", (1, 2)],
            "7": ["land_18", (1, 3)],
            "8": ["land_2", (2, 0)],
            "9": ["land_6", (2, 1)],
            "10": ["land_6", (2, 2)],
            "11": ["land_18", (2, 3)],
            "12": ["land_3", (3, 0)],
            "13": ["land_16", (3, 1)],
            "14": ["land_16", (3, 2)],
            "15": ["land_16", (3, 3)],
            "16": ["land_11", (3, 2)]
        }
        self.save2config("map", map_dict)

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


if __name__ == '__main__':
    s2c = SAVE2CONFIG()
    s2c.init_config()
