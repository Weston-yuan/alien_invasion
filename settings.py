class Settings:
  """存储游戏‘外星人入侵‘中所有设置的类"""
  def __init__(self):
    """初始化游戏的静态设置"""
    #屏幕设置
    self.screen_width = 1200
    self.screen_height = 750
    self.bg_color = (0,170,201)

    #飞船设置
    self.ship_speed = 1.5
    self.ship_limit = 3

    #子弹设置
    self.bullet_speed = 1.5
    self.bullet_width = 300
    self.bullet_height = 15
    self.bullet_color = (255, 255, 255)
    self.bullets_allowed = 20

    #外星人设置
    self.alien_speed = 1.0
    self.fleet_drop_speed = 15
    
    #加快游戏节奏的参数
    self.speedup_scale = 1.1
    #外星人分数的提高参数
    self.score_scale = 1.5


    self.initialize_dynamic_settings()

  def initialize_dynamic_settings(self):
    """初始化游戏的动态设置"""
    self.ship_speed = 1.5
    self.bullet_speed = 3.0
    self.alien_speed = 1.0

    #1表示向右，-1表示向左
    self.fleet_direction = 1

    #计分
    self.alien_points = 50

  def increase_speed(self):
    """提高游戏节奏的设置,和外星人分数"""
    self.ship_speed *= self.speedup_scale
    self.bullet_speed *= self.speedup_scale
    self.alien_speed *= self.speedup_scale

    self.alien_points = int(self.alien_points * self.score_scale)


    