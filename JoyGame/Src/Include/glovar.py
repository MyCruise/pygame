import os
from JoyGame.Src.Tools.save2json import SAVE2CONFIG
from JoyGame.Src.Include.abspath import abspath, abspath_join


class GLOVAR:
    def __init__(self):
        self.s2c = SAVE2CONFIG()

        # Ignore file
        ignore_name = ['.gitignore', '.DS_Store']
        ignore_suffix = []

        # Load config file
        init_config = self.s2c.readFromConfig("init", display=False)
        path_config = self.s2c.readFromConfig("path", display=False)
        title_config = self.s2c.readFromConfig("title", display=False)
        self.homepage_menu_config = self.s2c.readFromConfig("layout_button", display=False)
        self.control_config = self.s2c.readFromConfig("control", display=False)
        self.game_pause_menu_config = self.s2c.readFromConfig("game_pause_menu", display=False)

        # Layout 2
        self.play_menu_config = self.s2c.readFromConfig("play", display=False)
        self.setting_menu_config = self.s2c.readFromConfig("setting", display=False)
        self.tutorial_menu_config = self.s2c.readFromConfig("tutorial", display=False)

        # Initialize config
        self.Mode = init_config["Mode"]
        self.Resolution = init_config["Resolution"]
        self.width = self.Resolution[0]
        self.height = self.Resolution[1]
        self.targetFPS = init_config["targetFPS"]
        self.background_color = init_config["Background_color"]
        self.block_character = init_config["Block_character"]
        self.block_map = init_config["Block_map"]

        # Path config
        self.EffectSounds = abspath(path_config["Effect-sounds"])
        self.Materials = abspath(path_config["Materials"])
        self.Music = abspath(path_config["music"])
        self.Fonts = abspath(path_config["Fonts"])
        self.MaterialsAction = abspath(path_config["Materials-character"])
        self.MaterialsEnvironment = abspath(path_config["Materials-environment"])
        self.MaterialsSounds = abspath(path_config["Materials-sounds"])
        self.MaterialsImagesIcon = abspath(path_config["Materials-images-icon"])
        self.MaterialsMusic = abspath(path_config["Materials-music"])

        # Title config
        self.title_cn_1 = title_config["title_cn_1"]
        self.title_cn_2 = title_config["title_cn_2"]
        self.title_en_1 = title_config["title_en_1"]
        self.title_en_2 = title_config["title_en_2"]

        # Control config
        self.deadband1 = self.control_config["deadband1"]
        self.deadband2 = self.control_config["deadband2"]


if __name__ == '__main__':
    glovar = GLOVAR()
    s2c = SAVE2CONFIG()
