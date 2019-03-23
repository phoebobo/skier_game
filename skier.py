# 定义一个雪人类
import pygame
from settings import Settings

my_set = Settings()
skier_images = ['./skier_crash.png', './skier_down.png', './skier_left1.png', './skier_left2.png',
                './skier_right1.png', './skier_right2.png', ]
down_image = pygame.image.load(skier_images[1])
# 雪人初始位置
begin_top = 0
begin_left = my_set.screen_width / 2 - down_image.get_width() / 2

class Skier(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(skier_images[1]).convert()
        self.rect = self.image.get_rect()
        self.rect.top = begin_top  # 雪人初始位置
        self.rect.left = begin_left
        # 移动速度
        self.down_speed = 1

    def update(self, pressed_keys):
        # 按键事件
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            if self.rect.left > 0:
                self.image = pygame.image.load(skier_images[2]).convert()
                self.rect.left -= 1

        elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            if self.rect.left < 600 - self.image.get_width():
                self.image = pygame.image.load(skier_images[4]).convert()
                self.rect.left += 1
        else:
            self.image = pygame.image.load(skier_images[1]).convert()

    # 速度增减
    def move_fater(self):
        pass

    def move_lower(self):
        pass

    def hit(self):  # 碰撞
        pass
    # def move_down(self):
    #     self.rect.top += self.down_speed
