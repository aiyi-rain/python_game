import pygame
from pygame.sprite import AbstractGroup, Sprite
class Alien(Sprite):
    def __init__(self, ai_game) -> None:
        super().__init__()
        """初始化"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings=ai_game.settings
        #加载图像和矩形
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        #初始外星人位置
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #用小数存贮
        self.x=float(self.rect.x)
    def update(self):
        """外星人移动"""
        self.x+=(self.settings.alien_speed*self.settings.alien_direcat)
        self.rect.x=self.x
    def check_limit(self):
        """检查是否碰到边界"""
        if self.rect.right>=self.screen_rect.right or self.rect.left<=0:
            return True

