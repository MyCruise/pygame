import logging as log


def _init():  # 初始化
    global _global_dict
    if '_global_dict' not in globals():
        _global_dict = {}
        if '_global_dict' in locals() or '_global_dict' in globals():
            return True
        else:
            return False
    else:
        log.error("_global_dict does not exists")


def set_value(key: str, value):
    """ 定义一个全局变量 """
    if key in _global_dict:
        log.warning('%s does not exists' % key)
        return False
    else:
        _global_dict[key] = value
        return True


def get_value(key: str, defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return _global_dict[key]
    except KeyError:
        log.error("%s key does not exist" % key)
        return defValue


def is_alive(key: str):
    if key in locals() or 'var' in globals():
        return True
    else:
        return False
