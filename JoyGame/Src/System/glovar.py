from JoyGame.Src.System.save2json import readFromConfig
from JoyGame.Src.Include.abspath import abspath

# ignore file
ignore_name = ['.gitignore', '.DS_Store']
ignore_suffix = []

path = abspath('JoyGame/Src/Config')
init_config = readFromConfig(path, "test")

# global variable
# init_config['']
