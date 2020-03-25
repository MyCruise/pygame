import os
import pygame
from JoyGame.Src.System.global_variable import get_value


class Sounds:
    def __init__(self):
        pygame.mixer.init()
        self.music_path = get_value('Materials_Music')
        self.index = 0
        self.music_list = os.listdir(self.music_path)
        self.maxNum = len(self.music_list) - 1
        self.music_player = None
        self.pause_flag = False

    def __front__(self):
        self.index += 1
        if self.index > self.maxNum:
            self.index = 0

    def __rear__(self):
        self.index -= 1
        if self.index < 0:
            self.index = self.maxNum

    def __file__(self):
        return os.path.join(self.music_path, self.music_list[self.index])

    def __play__(self):
        if not pygame.mixer.music.get_busy():
            if os.path.exists(self.__file__()):
                pygame.mixer.music.load(self.__file__())
                pygame.mixer.music.play(1, 0)
            else:
                print("error")
        else:
            pass

    def set_index(self, index):
        self.index = index

    def set_volume(self, volume):
        if volume < 0:
            volume = 0
        elif volume > 1:
            volume = 1
        pygame.mixer.music.set_volume(volume)

    def pause(self):
        if not self.pause:
            self.pause_flag = True
            pygame.mixer.music.pause()

    def unpause(self):
        if self.pause:
            self.pause_flag = False
            pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()


if __name__ == '__main__':
    sound = Sounds()
    sound.__play__()
    print(sound.music_list)
