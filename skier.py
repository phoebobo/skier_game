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
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        '''
        :param image:指的是图片路径
        :param rect:位置
        :param down_speed:是往下的速度
        '''
        self.image = pygame.image.load(skier_images[1])
        self.rect = self.image.get_rect()
        self.rect.top = begin_top  # 雪人初始位置
        self.rect.left = begin_left
        # 移动速度
        self.speed = speed
        #场景生成时间 也就是速度
        self.time_set = 40
    #根据按键事件来移动
    def update(self, pressed_keys):
        # 按键事件
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            if self.rect.left > 0:
                self.image = pygame.image.load(skier_images[2]).convert()
                self.rect.left -= self.speed
        elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            if self.rect.left < my_set.screen_width - self.image.get_width():
                self.image = pygame.image.load(skier_images[4]).convert()
                self.rect.left += self.speed
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            if self.rect.top > 0 :
                self.image = pygame.image.load(skier_images[1]).convert()
                self.rect.top -= self.speed
        elif pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            if self.rect.top < my_set.screen_height - self.image.get_height():
                self.image = pygame.image.load(skier_images[1]).convert()
                self.rect.top += self.speed
        if not pressed_keys:
            self.image = pygame.image.load(skier_images[1]).convert()

    def hit(self):  # 碰撞
        pass
    # def move_down(self):
    #     self.rect.top += self.down_speed
