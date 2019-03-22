import pygame
#初始化
pygame.init()
pygame.mixer.init()
#游戏窗口大小
window_width = 400
window_height = 600
window = pygame.display.set_mode((window_width,window_height))#窗口大小

pygame.display.set_caption('cool')#窗口名字
# pygame.display.set_icon()
background_image = pygame.image.load('timg.jpg').convert()#背景图
skier_images = ['./skier_crash.png','./skier_down.png','./skier_left1.png','./skier_left2.png',
                './skier_right1.png','./skier_right2.png',]
down_image = pygame.image.load(skier_images[1]).convert()

#音乐
# pygame.mixer.muisc.load('bg_music.mp3')

#雪人初始位置
begin_top = 0
begin_left = window_width/2 - down_image.get_width()/2
#定义一个雪人类
class Skier(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('skier_down.png').convert()
        self.rect = self.image.get_rect()
        self.rect.top = begin_top #雪人初始位置
        self.rect.left = begin_left
        #移动速度
        self.down_speed = 1
    #左右移动
    def move_left(self):
        if self.rect.left > 0:
            self.rect.left -= 1
    def move_right(self):
        if self.rect.left < window_width-self.image.get_width():
            self.rect.left += 1
    #速度增减
    def move_fater(self):
        pass
    def move_lower(self):
        pass

    def move_down(self):
        self.rect.top += self.down_speed

skier = Skier()  #创建滑雪小人
while True:
    #先加载背景图
    window.fill([255,255,255])
    window.blit(background_image,(0,0))

    ret = pygame.event.get()  #事件
    #退出游戏判断
    for obj in ret:
        if obj.type == pygame.QUIT:
            print('关闭窗口')
            exit()
    #获取键盘状态
    pressed_keys = pygame.key.get_pressed()
    if not pressed_keys[pygame.K_UP] and skier.rect.bottom < window_height:
        skier.move_down()
    elif pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        skier.move_left()
        print('按下左键')
    elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        skier.move_right()

    window.blit(skier.image, skier.rect)  # 添加小人画面
    pygame.display.update()  #必须要更新显示的内容

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