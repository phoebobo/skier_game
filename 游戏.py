import pygame
import random
from random import randrange
from settings import Settings
from skier import Skier
# pygame.display.set_icon()
# background_image = pygame.image.load('timg.jpg').convert()#背景图

# 画图
# pygame.draw.circle(window,[0,0,0],[50,50],50,0)
my_set = Settings()  # 用的是设置类

# 定义一个场景类
class TreeOrFlag(pygame.sprite.Sprite):
    def __init__(self, treeOrFlag):
        pygame.sprite.Sprite.__init__(self)
        self.treeOrFlag = treeOrFlag
        if treeOrFlag:
            self.image = pygame.image.load('./skier_tree.png')
        else:
            self.image = pygame.image.load('./skier_flag.png')
        self.rect = self.image.get_rect()
        self.rect.top = self.rect.height + my_set.screen_height
        self.rect.centerx = randrange(my_set.screen_width - self.rect.width) + self.rect.width / 2

    def update(self, *args):
        self.rect.top -= 1
        if self.rect.top < -self.rect.height:
            self.kill()

# 初始化
pygame.init()
pygame.mixer.init()
# 游戏窗口初始化
window = pygame.display.set_mode((my_set.screen_width, my_set.screen_height))  # 窗口大小
screen = pygame.display.get_surface()
pygame.display.set_caption(my_set.name)  # 窗口名字

clock = pygame.time.Clock()  #帧率显示,先定义一个时间对象

sprites = pygame.sprite.RenderUpdates()  #创建sprite容器
skier_sprite = pygame.sprite.RenderUpdates()
#添加树或旗子创建自定义事件
AddEnemy = pygame.USEREVENT + 1
pygame.time.set_timer(AddEnemy,40)

# 音乐
# pygame.mixer.muisc.load('bg_music.mp3')

#运行游戏
skier = Skier()  # 创建滑雪小人
skier_sprite.add(skier)

#左上角计算分数
countObj = pygame.font.SysFont('方正兰亭超细黑简体',30)
# countObj.set_bold(True)  #加粗
print(pygame.font.get_fonts())
textObj = countObj.render('得分为：0',True,(255,0,0))
textRectObj = textObj.get_rect()

count_num = 0

while True:
    # 先加载背景图
    window.fill(my_set.bg_color)  # 填充，参数填写的是rgb值
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
    #调用方法更新
    skier.update(pressed_keys)
    #判断事件，生成场景
    for event in pygame.event.get():
        if event.type == AddEnemy:
            rand_num = random.randint(1,10)
            if rand_num %2:
                sprites.add(TreeOrFlag(1))
            else:
                sprites.add(TreeOrFlag(0))

    #判断碰撞
    if pygame.sprite.spritecollide(skier,sprites,False):
        # tree_flag = sprites()
        # if tree_flag.treeOrFlag :
        #     count_num -= 50
        # else:
        #     count_num += 10
        count_num += 10
        textObj == countObj.render('得分为：%d' % count_num, False, (255, 0, 0))
        textRectObj = textObj.get_rect()
        print(count_num)
        pygame.display.flip()
    #场景动画更新
    sprites.update()
    updates = sprites.draw(window)
    pygame.display.update(updates)
    #添加画面以及帧率
    window.blit(skier.image, skier.rect)  # 添加小人画面
    window.blit(textObj, textRectObj)
    clock.tick(100)
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

