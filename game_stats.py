class GameStats:
    """跟踪游戏统计信息"""

    def __init__(self,ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        #non-active mode when just launched
        self.game_active = False
        # 在任何情况下都不应重置最高得分
        self.high_score = 0
        with open('highscore.txt') as fo:
            self.high_score = int(fo.read())




    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1