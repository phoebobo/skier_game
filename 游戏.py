import pygame
import random
from settings import Settings

# 初始化
pygame.init()
pygame.mixer.init()
# 游戏窗口初始化
my_settings = Settings()  # 用的是设置类
window = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height))  # 窗口大小
pygame.display.set_caption(my_settings.name)  # 窗口名字

# pygame.display.set_icon()
# background_image = pygame.image.load('timg.jpg').convert()#背景图
skier_images = ['./skier_crash.png', './skier_down.png', './skier_left1.png', './skier_left2.png',
                './skier_right1.png', './skier_right2.png', ]
down_image = pygame.image.load(skier_images[1]).convert()
# 画图
# pygame.draw.circle(window,[0,0,0],[50,50],50,0)

# 音乐
# pygame.mixer.muisc.load('bg_music.mp3')

# 雪人初始位置
begin_top = 0
begin_left = my_settings.screen_width / 2 - down_image.get_width() / 2

#定义一个雪人类
class Skier(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(skier_images[1]).convert()
        self.rect = self.image.get_rect()
        self.rect.top = begin_top #雪人初始位置
        self.rect.left = begin_left
        #移动速度
        self.down_speed = 1
    #左右方向
    def move_left(self):
        if self.rect.left > 0:
            self.image = pygame.image.load(skier_images[2]).convert()
            self.rect.left -= 1
    def move_right(self):
        if self.rect.left < my_settings.screen_width-self.image.get_width():
            self.image = pygame.image.load(skier_images[4]).convert()
            self.rect.left += 1
    #速度增减
    def move_fater(self):
        pass
    def move_lower(self):
        pass

    def hit(self):  #碰撞
        pass
    # def move_down(self):
    #     self.rect.top += self.down_speed

#定义一个场景类
class RandomTree(object):
    def __init__(self,tree_flag):
        self.tree_flag = tree_flag



#运行游戏

skier = Skier()  # 创建滑雪小人
while True:
    # 先加载背景图
    window.fill(my_settings.bg_color)  # 填充，参数填写的是rgb值
    # window.blit(background_image,(0,0))

    ret = pygame.event.get()  # 事件
    # 退出游戏判断
    for obj in ret:
        if obj.type == pygame.QUIT:
            print('关闭窗口')
            exit()
    # 获取键盘状态
    pressed_keys = pygame.key.get_pressed()
    # if not pressed_keys[pygame.K_UP] and skier.rect.bottom < my_settings.screen_height:
    # 场景组
    scene = []
    for i in range(0, 10):
        # 总共10个场景，随机旗子或树
        tree_flag = random.randint(1, 10)
        if tree_flag % 2:
            tree_image = pygame.image.load('./skier_tree.png').convert()
            rect_tree = tree_image.get_rect()
            rect_tree.left = my_settings.screen_width / 10 * tree_flag
            rect_tree.top = my_settings.screen_height+my_settings.screen_height / 10 * random.randint(1, 10)
            window.blit(tree_image, rect_tree)
            scene.append(tree_image)
            scene.append(rect_tree)
        else:
            flag_image = pygame.image.load('./skier_flag.png').convert()
            rect_flag = flag_image.get_rect()
            rect_flag.left = my_settings.screen_width / 10 * tree_flag
            rect_flag.top = my_settings.screen_height+my_settings.screen_height / 10 * random.randint(1, 10)
            window.blit(flag_image, rect_flag)
            scene.append(flag_image)
            scene.append(rect_flag)

    #按键方法
    if not pressed_keys[pygame.K_o]:
        for i in range(0,20):
            if i%2:
                rect_scene = scene[i]
                rect_scene.top -= 1
    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        skier.move_left()
        print('按下左键')
    elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        skier.move_right()
    else:
        skier.image = pygame.image.load(skier_images[1]).convert()
    for i in range(0, 20):
        if i % 2:
            rect_scene = scene[i]
            window.blit(scene[i - 1], rect_scene)
    window.blit(skier.image, skier.rect)  # 添加小人画面
    pygame.display.update()  # 必须要更新显示的内容


# 按键
# elif obj.type == pygame.KEYDOWN:
#     # print('按了键盘')
#     # print('此时按下的键是',obj.key)
#     if obj.key == pygame.K_DOWN or obj.key == pygame.K_s:
#         print('此时按了向下的键')
#     elif obj.key == pygame.K_UP or obj.key == pygame.K_w:
#         print('向上')
#     elif obj.key == pygame.K_LEFT or obj.key == pygame.K_a:
#         skier.move_left()
#         print('向左')
#     elif obj.key == pygame.K_RIGHT or obj.key == pygame.K_d:
#         skier.move_right()
#         print('向右')