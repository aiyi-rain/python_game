class Settings:
    """设置类"""
    def __init__(self) -> None:
        """初始化游戏设置"""
        #屏幕设置
        self.sceen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        #chicken设置
        self.chicken_speed=1.5
        #🏀设置
        self.ball_speed=0.5
        #外星人设置
        self.alien_speed=0.5
        self.alien_down_speed=10
        #为1向右移动为-1向左移动
        self.alien_direcat=1
