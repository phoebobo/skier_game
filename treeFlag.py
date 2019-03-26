import pygame
import random
from random import randrange
from settings import Settings

my_set = Settings()
# 定义一个场景类
class TreeFlagClass(pygame.sprite.Sprite):

    def __init__(self,speed,treeFlag):  #传入两个参数，初始速度和bool值树或旗子
        pygame.sprite.Sprite.__init__(self)  #父类的初始化方法要调用
        '''
        :param image =图片
        :param type 判断是树还是旗子
        :param speed 速度
        '''
        if treeFlag:
            self.image = pygame.image.load('./skier_tree.png')
            self.type = 'tree'
        else:
            self.image = pygame.image.load('./skier_flag.png')
            self.type = 'flag'
        self.rect = self.image.get_rect()
        self.rect.top = self.rect.height + my_set.screen_height
        self.rect.centerx = randrange(my_set.screen_width - self.rect.width) + self.rect.width / 2
        self.speed = speed

    def update(self, *args):
        self.rect.top -= self.speed
        if self.rect.top < -self.rect.height:
            self.kill()
