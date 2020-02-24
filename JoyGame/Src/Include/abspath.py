import os


def root_abspath(prj_name):
    path = ''
    while os.path.split(os.path.abspath(path))[-1] != prj_name:
        path += '../'
        if os.path.split(os.path.abspath(path))[-1] == '':
            print('project name error')
            path = ''
            break
    return path


def abspath_join(path, dir):
    return path + '/' + dir


def abspath(dst_dir=""):
    return root_abspath('pygame_demo') + dst_dir


if __name__ == '__main__':
    path = os.path.exists(abspath('JoyGame/Src/Config'))
    print(path)
