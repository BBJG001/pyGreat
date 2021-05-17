 1import random
 2import sys
 3import time
 4from urllib.request import urlretrieve
 5import os
 6import pygame
 7
 8
 9SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700  # 画面大小
10MY_BIRTH_LEFT, MY_BIRTH_TOP = SCREEN_WIDTH / 2, SCREEN_HEIGHT - 60
11DIRECTION = [U, D, L, R] = [ U ,  D ,  L ,  R ]  # 控制键
12Tank_IMAGE_POSITION = r D:/tank_img
13URL =  https://gitee.com/tyoui/logo/raw/master/img/

 1# 加载图片
 2def load_img(name_img):
 3    save = Tank_IMAGE_POSITION + os.sep + name_img +  .gif
 4    if not os.path.exists(save):
 5        urlretrieve(URL + name_img +  .gif , save)
 6    return pygame.image.load(save)
 7
 8# 加载背景音乐
 9def load_music(name_music):
10    save = Tank_IMAGE_POSITION + os.sep + name_music +  .wav
11    if not os.path.exists(save):
12        urlretrieve(URL + name_music +  .wav , save)
13    pygame.mixer.music.load(save)
14    pygame.mixer.music.play()

1
2* pygame.sprite模块，官方文档上说这个模块是轻量级的，在游戏开发中也未必要使用。
3* sprite翻译为精灵，在游戏动画一般是指一个独立运动的画面元素，在pygame中，
4就可以是一个带有图像（Surface）和大小位置（Rect）的对象。
5* pygame.sprite.Sprite是pygame精灵的基类，一般来说，需要写一个自己的精灵类继承一下它然后加入自己的代码。
6
7class BaseItem(pygame.sprite.Sprite):
8    def __init__(self):
9        super().__init__()


1class Bullet(BaseItem):
 2    # 参数初始化
 3    def __init__(self, tank, window):
 4        super().__init__()
 5        self.direction = tank.direction
 6        self.speed = tank.speed * 3
 7        self.img = load_img( bullet )
 8        self.rect = self.img.get_rect()
 9        self.window = window
10        self.live = True
11        if self.direction == U:
12            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
13            self.rect.top = tank.rect.top - self.rect.height
14        elif self.direction == D:
15            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
16            self.rect.top = tank.rect.top + tank.rect.height
17        elif self.direction == L:
18            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
19            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.height / 2
20        else:
21            self.rect.left = tank.rect.left + tank.rect.width
22            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.height / 2
23
24    # 子弹显示
25    def display_bullet(self):
26        self.window.blit(self.img, self.rect)
27
28    # 通过按键控制子弹移动
29    def bullet_move(self):
30        if self.direction == U:
31            if self.rect.top > 0:
32                self.rect.top -= self.speed
33                return
34        elif self.direction == D:
35            if self.rect.top < SCREEN_HEIGHT:
36                self.rect.top += self.speed
37                return
38        elif self.direction == L:
39            if self.rect.left > 0:
40                self.rect.left -= self.speed
41                return
42        else:
43            if self.rect.left < SCREEN_WIDTH:
44                self.rect.left += self.speed
45                return
46        self.live = False
47
48    # 我方坦克子弹击中对方坦克
49    def hit_enemy_tank(self):
50        for enemy in TankGame.enemy_tank_list:
51            hit = pygame.sprite.collide_rect(self, enemy)
52            if hit:
53                self.live = False
54                if enemy.click_count == 1:
55                    enemy.live = False
56                    return None
57                enemy.click_count -= 1
58                if enemy.click_count == 2:
59                    enemy.load_image = enemy.img32
60                if enemy.click_count == 1:
61                    enemy.load_image = enemy.img31
62                load_music( hit )
63
64    # 对方坦克子弹击中我方坦克
65    def hit_my_tank(self, tank):
66        hit = pygame.sprite.collide_rect(self, tank)
67        if hit:
68            self.live = False
69            tank.live = False
70
71    # 子弹击中围墙
72    def bullet_collide_wall(self):
73        for wall in TankGame.wall_list:
74            result = pygame.sprite.collide_rect(self, wall)
75            if result:
76                self.live = False
77                if wall.count == 1:
78                    wall.live = False
79                else:
80                    load_music( hit )
81
82    # 子弹击中子弹
83    def bullet_collide_bullet(self):
84        for bullet in TankGame.enemy_bullet_list:
85            if pygame.sprite.collide_rect(bullet, self):
86                bullet.live = False
87                self.live = False


 1class Tank(BaseItem):
 2    # 参数初始化
 3    def __init__(self, left, top, window, image, direction, speed):
 4        super().__init__()
 5        self.window = window
 6        self.load_image = image
 7        self.direction = direction
 8        self.img = self.load_image[self.direction]
 9        self.rect = self.img.get_rect()
10        self.rect.left = left
11        self.rect.top = top
12        self.speed = speed
13        self.tank_width = self.rect.width
14        self.tank_height = self.rect.height
15        self.wall_switch = False
16        self.move_stop = True
17        self.live = True
18        self.old_left = 0
19        self.old_top = 0
20
21    # 开火
22    def fire(self):
23        return Bullet(self, self.window)
24
25    # 显示
26    def display(self):
27        self.img = self.load_image[self.direction]
28        self.window.blit(self.img, self.rect)
29
30    def wall_not(self, direction):
31        if direction == U:
32            return self.rect.top > 0
33        elif direction == D:
34            return self.rect.top <= SCREEN_HEIGHT - self.tank_height
35        elif direction == L:
36            return self.rect.left > 0
37        else:
38            return self.rect.left <= SCREEN_WIDTH - self.tank_width
39
40    def wall_yes(self, direction):
41        if direction == U:
42            if self.rect.top < 0:
43                self.rect.top = SCREEN_HEIGHT
44        elif direction == D:
45            self.rect.top %= SCREEN_HEIGHT
46        elif direction == L:
47            if self.rect.left < 0:
48                self.rect.left = SCREEN_WIDTH
49        else:
50            self.rect.left %= SCREEN_WIDTH
51
52    def move(self, direction):
53        self.old_left = self.rect.left
54        self.old_top = self.rect.top
55        if self.wall_switch:
56            self.wall_yes(direction)
57        elif not self.wall_not(direction):
58            return None
59        if direction == U:
60            self.rect.top -= self.speed
61        elif direction == D:
62            self.rect.top += self.speed
63        elif direction == L:
64            self.rect.left -= self.speed
65        else:
66            self.rect.left += self.speed
67
68    def stay(self):
69        self.rect.left = self.old_left
70        self.rect.top = self.old_top
71
72    def tank_collide_wall(self):
73        for wall in TankGame.wall_list:
74            if pygame.sprite.collide_rect(self, wall):
75                self.stay()
76
77    def tank_collide_tank(self):
78        for tank in TankGame.enemy_tank_list:
79            if pygame.sprite.collide_rect(self, tank):
80                self.stay()

 1class MyTank(Tank):
 2    def __init__(self, left, top, window):
 3        self.img = dict(U=load_img( p2tankU ), D=load_img( p2tankD ), L=load_img( p2tankL ), R=load_img( p2tankR ))
 4        self.my_tank_speed = 4
 5        super().__init__(left, top, window, self.img, U, self.my_tank_speed)
 6
 7
 8class EnemyTank(Tank):
 9    def __init__(self, left, top, window):
10        self.img1 = dict(U=load_img( enemy1U ), D=load_img( enemy1D ), L=load_img( enemy1L ), R=load_img( enemy1R ))
11        self.img2 = dict(U=load_img( enemy2U ), D=load_img( enemy2D ), L=load_img( enemy2L ), R=load_img( enemy2R ))
12        self.img3 = dict(U=load_img( enemy3U ), D=load_img( enemy3D ), L=load_img( enemy3L ), R=load_img( enemy3R ))
13        self.img31 = dict(U=load_img( enemy3U_1 ), D=load_img( enemy3D_1 ), L=load_img( enemy3L_1 ),
14                          R=load_img( enemy3R_1 ))
15        self.img32 = dict(U=load_img( enemy3U_2 ), D=load_img( enemy3D_2 ), L=load_img( enemy3L_2 ),
16                          R=load_img( enemy3R_2 ))
17        # 不同的坦克击中的次数不一样
18        image, self.click_count, speed = random.choice([(self.img1, 1, 4), (self.img3, 3, 3), (self.img2, 1, 5)])
19        super().__init__(left, top, window, image, self.random_direction(), speed)
20        self.step = 100
21
22    @staticmethod
23    def random_direction():
24        n = random.randint(0, 3)
25        return DIRECTION[n]
26
27    def random_move(self):
28        if self.step == 0:
29            self.direction = self.random_direction()
30            self.step = random.randint(10, 100)
31        else:
32            self.move(self.direction)
33            self.step -= 1
34
35    def random_fire(self):
36        if random.randint(0, 50) == 1 and len(TankGame.enemy_bullet_list) < 30:
37            enemy_bullet = self.fire()
38            TankGame.enemy_bullet_list.append(enemy_bullet)

 1class Explode(BaseItem):
 2    def __init__(self, tank, window):
 3        super().__init__()
 4        self.img = [load_img( blast0 ), load_img( blast1 ), load_img( blast2 ), load_img( blast3 ), load_img( blast4 ),
 5                    load_img( blast5 ), load_img( blast6 )]
 6        self.rect = tank.rect
 7        self.stop = 0
 8        self.window = window
 9        self.rect.left = tank.rect.left - tank.rect.width / 2
10    def display_explode(self):
11        load_music( blast )
12        while self.stop < len(self.img):
13            self.window.blit(self.img[self.stop], self.rect)
14            self.stop += 1

 1class Wall(BaseItem):
 2    def __init__(self, left, top, window):
 3        super().__init__()
 4        self.count = random.randint(0, 1)
 5        self.img = [load_img( steels ), load_img( walls )][self.count]
 6        self.rect = self.img.get_rect()
 7        self.rect.left = left
 8        self.rect.top = top
 9        self.window = window
10        self.live = True
11
12    def display_wall(self):
13        self.window.blit(self.img, self.rect)

  1class TankGame:
  2    my_bullet_list = list()
  3    enemy_bullet_list = list()
  4    enemy_tank_list = list()
  5    wall_list = list()
  6
  7    def __init__(self):
  8        if not os.path.exists(Tank_IMAGE_POSITION):
  9            os.makedirs(Tank_IMAGE_POSITION)
 10        pygame.init()
 11        pygame.font.init()
 12        self.display = pygame.display
 13        self.window = self.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.RESIZABLE, 32)
 14        self.display.set_caption( 坦克世界 )
 15        self.my_tank = MyTank(MY_BIRTH_LEFT, MY_BIRTH_TOP, self.window)
 16        self.creat_enemy_number = 10
 17        self.my_tank_lift = 3
 18        self.creat_enemy(self.creat_enemy_number)
 19        self.creat_walls()
 20        self.font = pygame.font.SysFont( kai_ti , 18)
 21        self.number = 1
 22
 23    def creat_enemy(self, number):
 24        for _ in range(number):
 25            left = random.randint(0, SCREEN_WIDTH - self.my_tank.tank_width)
 26            enemy_tank = EnemyTank(left, 20, self.window)
 27            TankGame.enemy_tank_list.append(enemy_tank)
 28
 29    def creat_walls(self):
 30        for i in range(SCREEN_WIDTH // 60 + 1):
 31            wall_h = random.randint(100, 500)
 32            w = Wall(60 * i, wall_h, self.window)
 33            TankGame.wall_list.append(w)
 34
 35    @staticmethod
 36    def show_walls():
 37        for w in TankGame.wall_list:
 38            if w.live:
 39                w.display_wall()
 40            else:
 41                TankGame.wall_list.remove(w)
 42
 43    def start_game(self):
 44        load_music( start )
 45        while True:
 46            self.window.fill([0, 0, 0])
 47            self.get_event()
 48            len_enemy = len(TankGame.enemy_tank_list)
 49            self.window.blit(
 50                self.draw_text( 敌方坦克*{0},我方生命值*{1},当前{2}关 .format(len_enemy, self.my_tank_lift, self.number)), (10, 10))
 51            if len_enemy == 0:
 52                self.creat_enemy_number += 10
 53                self.number += 1
 54                self.my_tank_lift += 1
 55                self.creat_enemy(self.creat_enemy_number)
 56                self.wall_list.clear()
 57                self.creat_walls()
 58            self.show_my_tank()
 59            self.show_enemy_tank()
 60            self.show_bullet(TankGame.enemy_bullet_list)
 61            self.show_bullet(TankGame.my_bullet_list)
 62            self.show_walls()
 63            self.display.update()
 64            time.sleep(0.02)
 65
 66    def show_my_tank(self):
 67        if self.my_tank.live:
 68            self.my_tank.display()
 69            self.my_tank.tank_collide_tank()
 70            self.my_tank.tank_collide_wall()
 71        else:
 72            Explode(self.my_tank, self.window).display_explode()
 73            del self.my_tank
 74            if self.my_tank_lift == 0:
 75                self.end_game()
 76            self.my_tank_lift -= 1
 77            load_music( add )
 78            self.my_tank = MyTank(MY_BIRTH_LEFT, MY_BIRTH_TOP, self.window)
 79        if not self.my_tank.move_stop:
 80            self.my_tank.move(self.my_tank.direction)
 81
 82    def show_enemy_tank(self):
 83        for e in TankGame.enemy_tank_list:
 84            e.random_move()
 85            e.tank_collide_wall()
 86            if e.live:
 87                e.display()
 88            else:
 89                TankGame.enemy_tank_list.remove(e)
 90                Explode(e, self.window).display_explode()
 91            e.random_fire()
 92
 93    def show_bullet(self, ls):
 94        for b in ls:
 95            b.bullet_move()
 96            b.bullet_collide_wall()
 97            if ls is TankGame.my_bullet_list:
 98                b.hit_enemy_tank()
 99                b.bullet_collide_bullet()
100            else:
101                b.hit_my_tank(self.my_tank)
102            if b.live:
103                b.display_bullet()
104            else:
105                ls.remove(b)
106
107    def get_event(self):
108        global SCREEN_WIDTH, SCREEN_HEIGHT
109        event_list = pygame.event.get()
110        for event in event_list:
111            if event.type == pygame.VIDEORESIZE:
112                SCREEN_WIDTH, SCREEN_HEIGHT = event.size
113                self.window = self.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.RESIZABLE, 32)
114
115            if event.type == pygame.QUIT:
116                self.end_game()
117            if event.type == pygame.KEYDOWN:
118                if event.key == pygame.K_w:
119                    self.my_tank.direction = U
120                elif event.key == pygame.K_s:
121                    self.my_tank.direction = D
122                elif event.key == pygame.K_a:
123                    self.my_tank.direction = L
124                elif event.key == pygame.K_d:
125                    self.my_tank.direction = R
126                else:
127                    return None
128                self.my_tank.move_stop = False
129            elif event.type == pygame.MOUSEBUTTONDOWN:
130                if len(TankGame.my_bullet_list) < 3:
131                    bullet = self.my_tank.fire()
132                    load_music( fire )
133                    TankGame.my_bullet_list.append(bullet)
134            elif event.type == pygame.KEYUP:
135                self.my_tank.move_stop = True
136
137    def end_game(self):
138        self.display.quit()
139        sys.exit()
140
141    def draw_text(self, content):
142        text_sf = self.font.render(content, True, [255, 0, 0])
143        return text_sf


1if __name__ ==  __main__ :
2    g = TankGame()
3    g.start_game()