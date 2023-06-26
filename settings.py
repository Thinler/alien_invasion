class Settings:
    """存储所有设置的类"""

    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3
        #子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (20,30,80)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        self.fleet_direction = 1 # 1 move right, -1 move left