import pygame
import os
from JoyGame.Src.Include.abspath import abspath_join


class Music:
    def __init__(self, path):
        self.musicList = os.listdir(path)
        self.totalMusic = len(self.musicList)

    def get_music(self):
        for music in self.musicList:
            music = abspath_join("JoyGame/Src/System/", music)
            if os.path.exists(music):
                pygame.mixer_music.load(music)

    def stop(self):
        pass

    def pause(self):
        pass

    def set_volume(self):
        pass

    def unpause(self):
        pass

    def rewind(self):
        pass
