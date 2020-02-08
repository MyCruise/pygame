import os
from JoyGame.Src.Include.glovar import GLOVAR

if __name__ == '__main__':
    glovar = GLOVAR()
    print(os.path.exists(glovar.Icon))
