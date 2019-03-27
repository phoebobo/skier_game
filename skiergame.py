import pygame
import random
from random import randrange
from settings import Settings
from skier import Skier
from treeFlag import TreeFlagClass
# pygame.display.set_icon()
# background_image = pygame.image.load('timg.jpg').convert()#背景图
# 画图
# pygame.draw.circle(window,[0,0,0],[50,50],50,0)
my_set = Settings()  # 用的是设置类  系统外观设置
skier_images = ['./skier_crash.png', './skier_down.png', './skier_left1.png', './skier_left2.png',
                './skier_right1.png', './skier_right2.png', ]   #滑雪者的图

if __name__ == '__main__':
    # 初始化
    pygame.init()
    pygame.mixer.init()
    # 游戏窗口初始化
    window = pygame.display.set_mode((my_set.screen_width, my_set.screen_height))  # 窗口大小
    screen = pygame.display.get_surface()
    pygame.display.set_caption(my_set.name)  # 窗口名字
    clock = pygame.time.Clock()  # 帧率显示,先定义一个时间对象
    treeFlag_sprites = pygame.sprite.RenderUpdates()  # 创建sprite容器  树
    # 添加树或旗子创建自定义事件
    AddEnemy = pygame.USEREVENT + 1
    pygame.time.set_timer(AddEnemy, 20)
    # 音乐
    # pygame.mixer.muisc.load('bg_music.mp3')
    skier = Skier(1)  # 创建滑雪小人
    # 左上角计算分数
    # countObj = pygame.font.SysFont('方正兰亭超细黑简体',30)
    countObj = pygame.font.Font(None, 60)
    # countObj.set_bold(True)  #加粗
    print(pygame.font.get_fonts())
    textObj = countObj.render('SCORE:0', True, (255, 0, 0))
    textRectObj = textObj.get_rect()
    # 这个是计算分数
    count_num = 0
    # 计算碰撞次数，10次场景加一次速度，最多叠加10次
    hit_count = 0
    # 显示当前速度
    speedObj = pygame.font.Font(None, 40)
    speed_text = speedObj.render('SPEED:1', True, (255, 0, 0))
    speedRectObj = speed_text.get_rect()
    speedRectObj.top = 60
    #运行游戏
    while True:
        # 先加载背景图
        clock.tick(60)
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
        #调用方法更新
        skier.update(pressed_keys)
        #判断事件，生成场景
        for event in pygame.event.get():
            if event.type == AddEnemy:
                if random.randint(1,10) %2:
                    treeFlag_sprites.add(TreeFlagClass(1,1))
                else:
                    treeFlag_sprites.add(TreeFlagClass(1,0))
        #判断与树或者旗子碰撞
        if pygame.sprite.spritecollide(skier,treeFlag_sprites,False):
            hit = pygame.sprite.spritecollide(skier, treeFlag_sprites, False)
            if hit[0].type == 'tree':
                count_num -= 100
                hit_count += 1
                hit[0].kill()
                skier.image = pygame.image.load(skier_images[0]).convert()
                pygame.time.delay(1000)
            else:
                count_num += 10
                hit_count += 1
                hit[0].kill()
        #判断累计碰撞次数：
        if hit_count <50 and hit_count > 10:
            hit_num = hit_count//10
            for obj in treeFlag_sprites:
                obj.speed = hit_num
            skier.speed = hit_num
        elif hit_count >= 50:
            for obj in treeFlag_sprites:
                obj.speed = 5
            skier.speed = 5
        #场景动画更新
        treeFlag_sprites.update()
        tree_updates = treeFlag_sprites.draw(window)
        pygame.display.update(tree_updates)
        #添加画面以及帧率
        window.blit(skier.image, skier.rect)  # 添加小人画面
        textObj = countObj.render('SCORE:%d' % count_num, False, (255, 0, 0))  #显示得分内容
        textRectObj = textObj.get_rect()
        window.blit(textObj, textRectObj)  #这是得分
        speed_text = speedObj.render('SPEED:%d'%skier.speed, True, (255, 0, 0))  #显示速度内容
        speedRectObj = speed_text.get_rect()
        speedRectObj.top = 60
        window.blit(speed_text,speedRectObj)  #显示速度
        pygame.display.update()  # 必须要更新显示的内容

