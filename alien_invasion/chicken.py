import pygame
class Chicken:
    """管理chicken的类"""
    def __init__(self,ai_game) -> None:
        """初始化"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings=ai_game.settings
        #加载图像并获取其外接矩形
        self.image=pygame.image.load('images/chicken.bmp')
        self.rect=self.image.get_rect()
        #放置底部
        self.rect.midbottom=self.screen_rect.midbottom
        #属性x中存贮小数
        self.x=float(self.rect.centerx)
        #移动标志
        self.moving_right=False
        self.moving_left=False
    def update(self):
        """根据移动标志调整位置"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.chicken_speed
            # self.rect.centerx+=1
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.chicken_speed
            # self.rect.centerx-=1
        self.rect.centerx=self.x
    def blitme(self):
        #在指定位置绘制chicken
        self.screen.blit(self.image,self.rect)
