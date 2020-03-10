import pygame
import os
from JoyGame.Src.Include.abspath import abspath_join
from JoyGame.Src.Include.glovar import GLOVAR


class Music:
    def __init__(self):
        # Initialize class
        self.glovar = GLOVAR()

        # Initialize variable
        self.index = 0
        self.pause = 0
        self.volume = 0
        self.musicLabel = os.listdir(self.glovar.MaterialsSounds)
        self.music = None

    def get_music_path(self, label, music):
        if label in self.musicLabel:
            path = abspath_join(self.glovar.MaterialsSounds, label)
            if music in os.listdir(path):
                return abspath_join(path, music)

    def __play__(self, label, music):
        self.music = pygame.mixer_music.load(self.get_music_path(label, music))

    def set_infinity(self):
        self.music.__play__(-1)

    def add2queue(self, musicFile):
        self.music.queue(musicFile)

    def __next__(self):
        self.index += 1

    def stop(self):
        self.music.stop()

    def pause(self):
        if not self.pause:
            self.pause = 1
            self.music.pause()
        else:
            self.pause = 0
            self.music.unpause()
        return self.pause

    def set_volume(self, volume):
        if 0 <= volume <= 1:
            self.volume = self.music.get_volume()
            self.music.set_volume(volume)

    def up_volume(self):
        self.volume += 1
        self.music.set_volume(self.volume)

    def rewind(self):
        pass
