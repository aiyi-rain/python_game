import sys
import pygame
from pygame import mixer
import random
from settings import Settings
from chicken import Chicken
from ball import Ball
from alien import Alien
class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self) -> None:
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.sceen_width,self.settings.screen_height))
        pygame.display.set_caption('吃我一球')
        #设置背景色
        self.bg_clor=self.settings.bg_color
        #绘制chicken
        self.chicken=Chicken(self)
        #设置🏀编组
        self.balls=pygame.sprite.Group()
        #设置外星人
        self.aliens=pygame.sprite.Group()
        self._create_alien()
        

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self.chicken.update()
            # self._create_alien()
            self._update_aliens()
            self.balls.update()
            self._update_ball()  
            self._check_kill()  
            self._update_screen()


    def _check_events(self):
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)

                
    def _check_keydown_events(self,event):
         """监听击剑事件"""
         if event.key==pygame.K_RIGHT:
            self.chicken.moving_right=True
         elif event.key==pygame.K_LEFT:
            self.chicken.moving_left=True
         elif event.key==pygame.K_q:
            sys.exit()
         elif event.key==pygame.K_SPACE:
             self._fire_ball()
                
    def _check_keyup_events(self,event):
         """监听击剑结束事件"""
         if event.key==pygame.K_RIGHT:
            self.chicken.moving_right=False
         elif event.key==pygame.K_LEFT:
            self.chicken.moving_left=False
    
    def _fire_ball(self):
        """发射🏀"""
        new_ball=Ball(ai_game=self)
        self.balls.add(new_ball)
        #音效
        pygame.mixer.music.load('sound/shoot.mp3')
        pygame.mixer.music.play();
    
    def _update_ball(self):
        
        """删除超出屏幕的🏀"""
        for ball in self.balls.copy():
            if ball.rect.bottom<=0:
                self.balls.remove(ball)
            # print(len(self.balls)) 查看是否删除成功
        

    def _check_kill(self):
        collions=pygame.sprite.groupcollide(self.balls,self.aliens,True,True)
        
        if len(self.aliens)<=0:
            self.balls.empty()
            self._create_alien()
            #音效
            # pygame.mixer.music.load('sound/kill.mp3')
            # pygame.mixer.music.play()
        
    def _create_alien(self):
        for item in range(random.randint(1,8)):
            alien=Alien(self)
            alien.rect.x=random.randint(100,1100)
            alien.rect.y=random.randint(100,400)
            self.aliens.add(alien)
    
    def _update_aliens(self):
        """外星人动起来"""
        self._check_alien_limit()
        self.aliens.update()

    def _check_alien_limit(self):
        for alien in self.aliens.sprites():
            if alien.check_limit():
                self._change_alien_dir()
                break
    
    def _change_alien_dir(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.alien_down_speed
            self.settings.alien_direcat*=-1
       
    def _update_screen(self,):
         #每次循环时都重新绘制屏幕
        self.screen.fill(self.bg_clor)
        self.chicken.blitme()
        #绘画i🏀组
        for ball in self.balls.sprites():
            ball.blitme()
        #绘制外星人
        self.aliens.draw(self.screen)
        #让最近绘制的屏幕可见
        pygame.display.flip()
if __name__=='__main__':
    #创建游戏实例并运行
    ai=AlienInvasion()
    ai.run_game()