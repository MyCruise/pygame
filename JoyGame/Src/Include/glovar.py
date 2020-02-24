from JoyGame.Src.System.save2json import SAVE2CONFIG
from JoyGame.Src.Include.abspath import abspath


class GLOVAR:
    def __init__(self):
        self.s2c = SAVE2CONFIG()

        # ignore file
        ignore_name = ['.gitignore', '.DS_Store']
        ignore_suffix = []

        init_config = self.s2c.readFromConfig("init")
        self.import_init = 0
        path_config = self.s2c.readFromConfig("path")
        self.import_init = 0

        # initiate config
        self.Fullscreen = init_config["Fullscreen"]
        self.Resolution = init_config["Resolution"]
        self.width = int(self.Resolution.split(",")[0])
        self.height = int(self.Resolution.split(",")[1])
        self.targetFPS = init_config["targetFPS"]

        # path config
        self.EffectAction = abspath(path_config["Effect-action"])
        self.EffectSounds = abspath(path_config["Effect-sounds"])
        self.Icon = abspath(path_config["Image-icon"])
        self.Materials = abspath(path_config["Materials"])
        self.Music = abspath(path_config["Music"])
        self.Fonts = abspath(path_config["Fonts"])
