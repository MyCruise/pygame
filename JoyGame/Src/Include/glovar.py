from JoyGame.Src.System.save2json import SAVE2CONFIG
from JoyGame.Src.Include.abspath import abspath


class GLOVAR:
    def __init__(self):
        self.s2c = SAVE2CONFIG()

        # Ignore file
        ignore_name = ['.gitignore', '.DS_Store']
        ignore_suffix = []

        init_config = self.s2c.readFromConfig("init", display=False)
        path_config = self.s2c.readFromConfig("path", display=False)
        title_config = self.s2c.readFromConfig("title", display=False)
        self.layout_button_config = self.s2c.readFromConfig("layout_button", display=False)
        self.control_config = self.s2c.readFromConfig("control", display=False)

        # Initialize config
        self.Mode = init_config["Mode"]
        self.Resolution = init_config["Resolution"]
        self.width = int(self.Resolution.split(",")[0])
        self.height = int(self.Resolution.split(",")[1])
        self.targetFPS = init_config["targetFPS"]

        # Path config
        self.EffectAction = abspath(path_config["Effect-action"])
        self.EffectSounds = abspath(path_config["Effect-sounds"])
        self.Icon = abspath(path_config["Image-icon"])
        self.Materials = abspath(path_config["Materials"])
        self.Music = abspath(path_config["Music"])
        self.Fonts = abspath(path_config["Fonts"])

        # Title config
        self.title_cn_1 = title_config["title_cn_1"]
        self.title_cn_2 = title_config["title_cn_2"]
        self.title_en_1 = title_config["title_en_1"]
        self.title_en_2 = title_config["title_en_2"]

        # Layout config
        self.button_maxNum_1 = len(self.layout_button_config)

        # Control config
        self.deadband1 = self.control_config["deadband1"]
        self.deadband2 = self.control_config["deadband2"]


if __name__ == '__main__':
    glovar = GLOVAR()
    print(glovar.layout_button_config["1"])
