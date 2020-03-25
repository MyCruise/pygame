import os
import logging as log


def root_abspath(prj_name):
    root_path = os.path.abspath(os.path.basename(__file__))
    while os.path.basename(root_path) != prj_name:
        root_path = os.path.abspath(os.path.join(root_path, os.path.pardir))
        if os.path.basename(root_path) == '':
            log.error('project name error')
            root_path = ''
            break
    return root_path


def abspath_plus(path):
    root = root_abspath('pygame_demo')
    abspath = os.path.abspath(os.path.join(root, path))
    if os.path.exists(abspath):
        return abspath
    else:
        log.error("abspath: %s dose not exist" % abspath)
        return ''


def abs2rel(path: str):
    path = list(path)
    for index in range(len(path)):
        if path[index] == '\\':
            path[index] = '/'
    for index in range(len(path)):
        if path[index] == '\\':
            path[index] = '/'
    return "".join(path)


if __name__ == '__main__':
    print(abspath_plus(""))
