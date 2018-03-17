import pygame
import random
from Constants import *
from time import sleep
class Sky():
    def __init__(self):
        self.image1 = SKY
        self.image2 = SKY

        self.x1 = 0
        self.x2 = 5000

        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()

    def render(self, screen):

        if self.x2 > SCREEN_WIDTH:
            if self.rect1.right <= SCREEN_WIDTH:
                self.x2 = SCREEN_WIDTH - SKY_SPEED * 2
        
        if self.rect1.right <= 0:
            self.x1 = 5000

        if self.rect2.right <= 0:
            self.x2 = 5000

        if self.x1 > SCREEN_WIDTH:
            if self.rect2.right <= SCREEN_WIDTH:
                self.x1 = SCREEN_WIDTH - SKY_SPEED * 2

        self.rect1.left = self.x1
        self.rect2.left = self.x2


        screen.blit(self.image1, (self.rect1.x, self.rect1.y))
        screen.blit(self.image2, (self.rect2.x, self.rect2.y))

        self.x1 = self.x1 - SKY_SPEED
        self.x2 = self.x2 - SKY_SPEED

class Tree():
    def __init__(self):
        self.mode = STATE
        self.tree = 1
        self.x = 0
        self.y = 130
        self.vzhiks = 0

    def spawn(self,tree):
        self.tree = tree
        self.x = SCREEN_WIDTH
        self.y = 130
        self.mode = SPAWN

    def cut(self):
        self.vzhiks = 0
        self.mode = CUT

    def vzhik(self):
        self.vzhiks = self.vzhiks + 1

    def render(self,screen):

        if self.vzhiks == TREES['VZHIK_' + str(self.tree)]:
            self.cut()

        if self.mode == SPAWN and self.x > 10:
            self.x = self.x - TREE_SPAWN_SPEED

        if self.mode == CUT and self.y < SCREEN_HEIGHT:
            self.y = self.y + TREE_CUT_SPEED

        if self.y > SCREEN_HEIGHT - 200:
            self.spawn(random.randint(1,COL_TREES))

        screen.blit(TREES[self.tree], (self.x,self.y))

class Saw():
    def __init__(self):
        self.mode = STATE 
        self.pos = LEFT

        self.x = SAW_X
        self.y = SAW_Y

    def render(self,screen):
        if self.mode == LEFT and self.x > SAW_X and self.y > SAW_Y:
            self.x = self.x - 10
            self.y = self.y - 5
        if self.mode == RIGHT and self.x < SAW_X + 30 and self.y < SAW_Y + 30:
            self.x = self.x + 10
            self.y = self.y + 5

        screen.blit(SAW,(self.x,self.y))

    def move(self):
        if self.pos == LEFT:
            SOUND_LIST[1].play()
            self.mode = RIGHT
            self.pos = RIGHT
            
        else:
            SOUND_LIST[2].play()
            self.mode = LEFT
            self.pos = LEFT

class Math():
    def __init__(self, game):
        self.example = pygame.Surface((NUM_WIDTH*3, NUM_HEIGHT), pygame.SRCALPHA, 32).convert_alpha()
        self.a = None
        self.b = None
        self.result = None
        self.timer = pygame.time.Clock()
        self.game = game
        self.first_run = True
        if MULTIPLICATION_BY_1 == True:
            self.c = 1
        else:
            self.c = 2

    def generate(self):
        self.timer.tick()

        time = self.timer.get_time() // 1000

        if not self.first_run:

            if time <= SEC_1:
                self.game.mark.show(1)
                self.game.score += 5
            if (time <= SEC_2) and (time > SEC_1):
                self.game.mark.show(2)
                self.game.score += 3
            if time > SEC_2:
                self.game.mark.show(3)
                self.game.score += 1
            
            self.timer.tick()
        self.first_run = False
        self.example = pygame.Surface((NUM_WIDTH*3, NUM_HEIGHT), pygame.SRCALPHA, 32).convert_alpha()
        self.clear()

        a = random.randint(self.c, 9)
        self.example.blit(NUMBERS[a], (0,0))
        temp = a

        self.example.blit(NUMBERS[10], (NUM_WIDTH, 0))

        a = random.randint(self.c, 9)
        self.example.blit(NUMBERS[a], (NUM_WIDTH*2,0))

        self.result = temp * a

    def render(self, screen):
        screen.blit(self.example, (MATH_X,MATH_Y))

    def write_event(self,num):
        if self.a != None:
            self.b = num

        if self.a == None:
            self.a = num

    def clear(self):
        self.a = None
        self.b = None

    def calc(self, game):
        if len(str(self.result)) == 1:  # Если ответ однозначный
          
            if self.a != self.result and self.a != None:
                self.clear()
                game.cross.show()
            if self.a == self.result:
                game.move_saw()
                self.generate()
                self.clear()




        if len(str(self.result)) == 2:  # Если ответ двухзначный
            tmp = None
            if self.b != None:
                tmp = str(self.a) + str(self.b)
                tmp = int(tmp)
                
            if tmp != self.result and tmp != None:
                self.clear()
                game.cross.show()



            if tmp == self.result:
                game.move_saw()
                self.generate()
                self.clear()

class Cross():
    def __init__(self):
        self.allow_show = False
        self.count = 0

    def show(self):
        SOUND_LIST[0].play()
        self.allow_show = True
        self.count = 0

    def render(self, screen):
        if self.allow_show:
            screen.blit(CROSS, (CROSS_X, CROSS_Y))
            self.count = self.count + 1

        if self.count > CROSS_TIME:
            self.allow_show = False

class Mark():
    def __init__(self):
        self.allow_show = False
        self.count = 0
        self.img = None
        self.lang = LANG

    def show(self, msg):
        self.allow_show = True
        self.count = 0
        self.img = MARKS[self.lang][msg]

    def render(self, screen):
        if self.allow_show:
            screen.blit(self.img, (MARK_X, MARK_Y))
            self.count = self.count + 1

        if self.count > MARK_TIME:
            self.allow_show = False

class Button():
    def __init__(self, x, y, img1, img2):
        self.off_img = self.prepare_img(img1)
        self.on_img = self.prepare_img(img2)
        
        self.img_pack = self.off_img

        self.rect = img1.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.mode = ON
        self.pressed = False
        self.img = self.img_pack[0]

    def prepare_img(self, img):
        size = img.get_size()

        list_img = list()
        list_img.append(img)


        img2 = pygame.Surface(size,pygame.SRCALPHA, 32).convert_alpha()

        width = int(size[0] / BUTTON_STATE_2)
        height = int(size[1] / BUTTON_STATE_2)

        temp = pygame.transform.scale(img, (width, height))
        
        x = (size[0] - width) / 2
        y = (size[1] - height) / 2

        img2.blit(temp, (x,y))
        list_img.append(img2)


        img3 = pygame.Surface(img.get_size() ,pygame.SRCALPHA, 32).convert_alpha()

        width = int(size[0] / BUTTON_STATE_3)
        height = int(size[1] / BUTTON_STATE_3)

        temp = pygame.transform.scale(img, (width, height))

        x = (size[0] - width) / 2
        y = (size[1] - height) / 2

        img3.blit(temp, (x,y))
        list_img.append(img3)

        return list_img
    
    def render(self, screen):
        if self.mode == OFF: self.img_pack = self.off_img
        if self.mode == ON: self.img_pack = self.on_img

        pos = pygame.mouse.get_pos()
        if pos[0] > self.rect.left and pos[0] < self.rect.right and pos[1] > self.rect.top and pos[1] < self.rect.bottom and self.pressed == 0:
            self.img = self.img_pack[1]

        elif not self.pressed : self.img = self.img_pack[0]

        elif self.pressed: self.img = self.img_pack[2]

        screen.blit(self.img, (self.rect.x, self.rect.y))

    def push(self, p):
        pos = pygame.mouse.get_pos()
        if pos[0] > self.rect.left and pos[0] < self.rect.right and pos[1] > self.rect.top and pos[1] < self.rect.bottom:
            if p == 1: self.pressed = True
            else:
                self.pressed = False
                if self.mode == OFF:
                    self.mode = ON
                    self.action(ON)
                else: 
                    self.mode = OFF 
                    self.action(OFF)

    def action(self, mode):
        pass

class Score():
    def __init__(self, game):
        self.game = game
        self.space = 4
        self.border_space = 5
        self.lang = LANG

    def render(self, screen):
        num = Draw_Number(self.game.score)
        word = SCORE_IMG[self.lang]
        surf = pygame.Surface((word.get_size()[0] + self.space + num.get_size()[0],num.get_size()[1]),pygame.SRCALPHA, 32).convert_alpha()
        surf.blit(word, (0,0))
        surf.blit(num, (word.get_size()[0] + self.space, 0))

        x = SCREEN_WIDTH - surf.get_size()[0] - self.border_space 
        y = SCREEN_HEIGHT - surf.get_size()[1] - self.border_space
        screen.blit(surf, (x, y))

class MusicButton(Button):
    def __init__(self, x, y):
        Button.__init__(self,x,y,NO_MUSIC,MUSIC)

    def action(self, mode):
        if mode == ON:
            pygame.mixer.music.set_volume(FOREST_VOLUME)
        else:
            pygame.mixer.music.set_volume(0)

class SoundButton(Button):
    def __init__(self, x, y):
        Button.__init__(self,x,y,NO_SOUND,SOUND)

    def action(self, mode):
        if mode == ON:
            [i.set_volume(SOUND_VOLUME) for i in SOUND_LIST]
        else:
            [i.set_volume(0) for i in SOUND_LIST]

class LangButton(Button):
    def __init__(self, x, y, game):
        Button.__init__(self,x,y,ENG_BTN,RUS_BTN)
        self.game = game
    def action(self, mode):
        if mode == ON:
            self.game.score_block.lang = self.game.mark.lang = RUS
        else:
            self.game.score_block.lang = self.game.mark.lang = ENG

def Draw_Number(N):


    space = 2
    nums = list()


    if N == 0:
        return pygame.transform.scale(NUMBERS[0], (NUM_MIN_WIDTH,NUM_MIN_HEIGHT))
    else:

        while N > 0:
            nums.append(N % 10)
            N //= 10

        
        surf_width = len(nums)*NUM_MIN_WIDTH + (len(nums)*space - space)
        surf = pygame.Surface((surf_width,NUM_MIN_HEIGHT),pygame.SRCALPHA, 32).convert_alpha()
        nums.reverse()
        x = 0
        for a in nums:
            img = pygame.transform.scale(NUMBERS[a],(NUM_MIN_WIDTH,NUM_MIN_HEIGHT))
            surf.blit(img,(x,0))
            x += (NUM_MIN_WIDTH + space)

        return surf        