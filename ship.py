import pygame

class Ship:

    def __init__(self,ai_game):
        """初始化飞船并设置其位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #对每艘新飞船 放置在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船属性x中存储小数值
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False



    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """illustrate ship on certain place """
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)