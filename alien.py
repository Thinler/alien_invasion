import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人"""

    def __init__(self,ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # aliens at left up at first
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # alien's detailed position
        self.x = float(self.rect.x)

