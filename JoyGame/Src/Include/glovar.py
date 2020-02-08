from JoyGame.Src.System.save2json import SAVE2CONFIG
from JoyGame.Src.Include.abspath import abspath


class GLOVAR:
    def __init__(self):
        self.s2c = SAVE2CONFIG()

        # ignore file
        ignore_name = ['.gitignore', '.DS_Store']
        ignore_suffix = []

        init_config = self.s2c.readFromConfig("init")
        path_config = self.s2c.readFromConfig("path")

        # initiate config
        self.Fullscreen = init_config["Fullscreen"]
        self.Resolution = init_config["Resolution"]
        self.width = int(self.Resolution.split(",")[0])
        self.height = int(self.Resolution.split(",")[1])
        self.FPS = init_config["FPS"]

        # path config
        self.EffectAction = path_config["Effect-action"]
        self.EffectSounds = path_config["Effect-sounds"]
        self.Icon = path_config["Image-icon"]
        self.Materials = path_config["Materials"]
        self.Music = path_config["Music"]
