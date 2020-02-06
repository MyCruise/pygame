from JoyGame.Src.System.toJson import config_wt, config_rd
from JoyGame.Src.Include.abspath import abspath


def save2config(path, config_name, dict):
    sorted(dict.keys())
    config_wt(path + config_name + "_config", dict)
    config_dict = config_rd(path + config_name + "_config")
    print(config_dict)


def readFromConfig(path, config_name):
    config_dict = config_rd(path + config_name + "_config")
    print(config_dict)


if __name__ == '__main__':
    path = abspath('JoyGame/Src/Config/')
    # "": "",
    init_dict = {"resolution": "640*480",
                 "": ""
                 }
    save2config(path, "test", init_dict)
