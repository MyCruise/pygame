import logging as log

from JoyGame.Src.Tools.save2json import SAVE2CONFIG
from JoyGame.Src.System.global_variable import _init
from JoyGame.Src.System.global_variable import set_value


def init_glovar():
    # initialize global variable
    if _init():
        if init_variable():
            set_value('init_glovar_flag', True)
            return True
        else:
            set_value('init_glovar_flag', False)
            log.error('initialize global variable failure')
            return False
    else:
        log.error('initialize global dictionary failure')


def get_value_from_config(config: dict):
    for dict in config:
        set_value(dict, config[dict])


def init_variable():
    s2c = SAVE2CONFIG()
    # Ignore file
    set_value('ignore_name', ['.gitignore', '.DS_Store'])
    set_value('ignore_suffix', [])
    # Load config file
    init_config = s2c.readFromConfig("init", display=False)
    path_config = s2c.readFromConfig("path", display=False)
    title_config = s2c.readFromConfig("title", display=False)
    control_config = s2c.readFromConfig("control", display=False)

    # Layout config
    set_value('homepage_menu_config', s2c.readFromConfig("layout_button", display=False))
    set_value('game_pause_menu_config', s2c.readFromConfig("game_pause_menu", display=False))
    set_value('play_menu_config', s2c.readFromConfig("play", display=False))
    set_value('setting_menu_config', s2c.readFromConfig("setting", display=False))
    set_value('tutorial_menu_config', s2c.readFromConfig("tutorial", display=False))

    # Initialize config
    get_value_from_config(init_config)

    # Path config
    get_value_from_config(path_config)

    # Title config
    get_value_from_config(title_config)

    # Control config
    get_value_from_config(control_config)
    return True


if __name__ == '__main__':
    init_glovar()
