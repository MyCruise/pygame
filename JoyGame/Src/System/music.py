import pygame
import os
from JoyGame.Src.Include.abspath import abspath_join


class Music:
    def __init__(self, glovar):
        # Initialize class
        self.glovar = glovar

        # Initialize variable
        self.index = 0
        self.pause = 0
        self.volume = 0
        self.musicList = os.listdir(self.glovar)
        self.totalMusic = len(self.musicList)
        self.music = pygame.mixer_music.load("")

    def get_music(self):
        musicList = []
        for music in self.musicList:
            music = abspath_join("JoyGame/Src/System/", music)
            if os.path.exists(music):
                musicList.append(music)
            else:
                print("%s is not exists." % music)
        self.musicList = musicList

    def set_infinity(self):
        self.music.play(-1)

    def add2queue(self, musicFile):
        self.music.queue(musicFile)

    def next_music(self):
        self.index += 1
        self.music = pygame.mixer_music.load(self.musicList[self.index])

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
