import pygame
from pygame.sprite import AbstractGroup, Sprite
class Ball(Sprite):
    """🏀类"""
    def __init__(self, ai_game) -> None:
        super().__init__()
        """初始化"""
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        #加载图像获取矩形
        self.image=pygame.image.load('images/basketball.bmp')
        self.rect=self.image.get_rect()
        self.rect.midtop=ai_game.chicken.rect.midtop
        #用小鼠存贮y坐标
        self.y=float(self.rect.centery)

    def update(self):
        """向上移动🏀"""
        self.y-=self.settings.ball_speed
        #更新🏀的位置
        self.rect.centery=self.y
    def blitme(self):
        """绘制🏀"""
        self.screen.blit(self.image,self.rect)

