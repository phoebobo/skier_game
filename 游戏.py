import pygame
import random
from random import randrange
from settings import Settings
from skier import Skier
# pygame.display.set_icon()
# background_image = pygame.image.load('timg.jpg').convert()#背景图

# 画图
# pygame.draw.circle(window,[0,0,0],[50,50],50,0)
my_set = Settings()  # 用的是设置类  系统外观设置
skier_images = ['./skier_crash.png', './skier_down.png', './skier_left1.png', './skier_left2.png',
                './skier_right1.png', './skier_right2.png', ]   #滑雪者的图

# 定义两个场景类，一个为树，一个为旗子
#这个是树类
class TreeClass(pygame.sprite.Sprite):
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./skier_tree.png')
        self.rect = self.image.get_rect()
        self.rect.top = self.rect.height + my_set.screen_height
        self.rect.centerx = randrange(my_set.screen_width - self.rect.width) + self.rect.width / 2
        self.speed = speed

    def update(self, *args):
        self.rect.top -= self.speed
        if self.rect.top < -self.rect.height:
            self.kill()

#这是一个旗子类
class FlagClass(pygame.sprite.Sprite):
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./skier_flag.png')
        self.rect = self.image.get_rect()
        self.rect.top = self.rect.height + my_set.screen_height
        self.rect.centerx = randrange(my_set.screen_width - self.rect.width) + self.rect.width / 2
        self.speed = speed

    def update(self, *args):
        self.rect.top -= self.speed
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

tree_sprites = pygame.sprite.RenderUpdates()  #创建sprite容器  树
flag_sprites = pygame.sprite.RenderUpdates()  #旗子容器
#添加树或旗子创建自定义事件
AddEnemy = pygame.USEREVENT + 1
pygame.time.set_timer(AddEnemy,40)
# 音乐
# pygame.mixer.muisc.load('bg_music.mp3')
skier = Skier(1)  # 创建滑雪小人

#左上角计算分数
# countObj = pygame.font.SysFont('方正兰亭超细黑简体',30)
countObj = pygame.font.Font(None,60)
# countObj.set_bold(True)  #加粗
print(pygame.font.get_fonts())
textObj = countObj.render('SCORE:0',True,(255,0,0))
textRectObj = textObj.get_rect()
#这个是计算分数
count_num = 0
#计算碰撞次数，10次场景加一次速度，最多叠加10次
hit_count = 0
#运行游戏
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
            if random.randint(1,10) %2:
                tree_sprites.add(TreeClass(1))
            else:
                flag_sprites.add(FlagClass(1))
    #判断与树碰撞
    if pygame.sprite.spritecollide(skier,tree_sprites,False):
        count_num -= 10
        hit_count += 1
        hit = pygame.sprite.spritecollide(skier,tree_sprites,False)
        hit[0].kill()
        skier.image = pygame.image.load(skier_images[0]).convert()
        # pygame.time.delay(1000)
        # pygame.display.flip()
    #与旗子碰撞
    if pygame.sprite.spritecollide(skier,flag_sprites,False):
        count_num += 10
        hit_count += 1
        hit = pygame.sprite.spritecollide(skier,flag_sprites,False)
        hit[0].kill()
    #判断累计碰撞次数：
    if hit_count <50 and hit_count > 10:
        hit_num = hit_count//10
        for obj in tree_sprites:
            obj.speed = hit_num
        for obj in flag_sprites:
            obj.speed = hit_num
        skier.speed = hit_num
    elif hit_count > 50:
        for obj in tree_sprites:
            obj.speed = 5
        for obj in flag_sprites:
            obj.speed = 5
        skier.speed = hit_num
    #场景动画更新
    tree_sprites.update()
    tree_updates = tree_sprites.draw(window)
    pygame.display.update(tree_updates)
    flag_sprites.update()
    flag_updates = flag_sprites.draw(window)
    pygame.display.update(flag_updates)
    #添加画面以及帧率
    window.blit(skier.image, skier.rect)  # 添加小人画面
    clock.tick(100)
    textObj = countObj.render('SCORE:%s' % count_num, False, (255, 0, 0))  #显示得分内容
    textRectObj = textObj.get_rect()
    window.blit(textObj, textRectObj)  #这是得分
    pygame.display.update()  # 必须要更新显示的内容

