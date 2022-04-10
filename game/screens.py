import pygame
from pygame import *

class Screen():
    def __init__(self, size):
        self.size = size
        #self.surf = Surface(self.size, SRCALPHA)
        self.group = sprite.Group()