import os
import pygame
from mutagen import File


class MusicPlayer:
    def __init__(self):
        self.folder = "music/sample_tracks"
        self.tracks = []

        for file in os.listdir(self.folder):
            if file.lower().endswith((".mp3", ".wav")):
                self.tracks.append(file)

        self.current = 0
        self.duration = 0

        if self.tracks:
            self.load_track()

    def load_track(self):
        path = os.path.join(self.folder, self.tracks[self.current])
        pygame.mixer.music.load(path)

        audio = File(path)
        self.duration = audio.info.length

    def play(self):
        if self.tracks:
            pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        if self.tracks:
            self.current = (self.current + 1) % len(self.tracks)
            self.load_track()
            self.play()

    def previous_track(self):
        if self.tracks:
            self.current = (self.current - 1) % len(self.tracks)
            self.load_track()
