import pygame
pygame.mixer.init(buffer=512)

ENG = 0
RUS = 1

FPS = 30

LANG = RUS

MULTIPLICATION_BY_1 = False

WINDOW_TITLE = 'The Woodcutter'

SCREEN_WIDTH = 1050
SCREEN_HEIGHT = 720

MATH_X = 600
MATH_Y = 230

SAW_X = 230
SAW_Y = 565

CROSS_X = 130
CROSS_Y = 230
CROSS_TIME = 30 #Cколько кадров

MARK_X = 580
MARK_Y = 180
MARK_TIME = 25 #Cколько кадров


SEC_1 = 4 #оценка "Отлично"
SEC_2 = 8 #оценка "Хорошо"

SKY_SPEED = 0.4
TREE_SPAWN_SPEED = 55
TREE_CUT_SPEED = 50



#Изображения:
ICON =   pygame.image.load('data/images/icon.png')
GRASS =  pygame.image.load('data/images/grass.png')
SKY =    pygame.image.load('data/images/sky.png')
ROCK =   pygame.image.load('data/images/rock.png')
SAW =    pygame.image.load('data/images/saw.png')
CROSS =  pygame.image.load('data/images/cross.png')
SCORE_IMG = [pygame.image.load('data/images/score_eng.png'), pygame.image.load('data/images/score_rus.png')]

TREE_1 = pygame.image.load("data/images/tree_1.png")
TREE_2 = pygame.image.load("data/images/tree_2.png")
TREE_3 = pygame.image.load("data/images/tree_3.png")
TREE_4 = pygame.image.load("data/images/tree_4.png")
TREE_5 = pygame.image.load("data/images/tree_5.png")
TREE_6 = pygame.image.load("data/images/tree_6.png")
TREE_7 = pygame.image.load("data/images/tree_7.png")
TREE_8 = pygame.image.load("data/images/tree_8.png")

VZHIK_1 = 2
VZHIK_2 = 4
VZHIK_3 = 5
VZHIK_4 = 7
VZHIK_5 = 7
VZHIK_6 = 10
VZHIK_7 = 13
VZHIK_8 = 11

COL_TREES = 8

TREES = {1:TREE_1, 2:TREE_2, 3:TREE_3, 4:TREE_4, 5:TREE_5, 6:TREE_6, 7:TREE_7, 8:TREE_8, "VZHIK_1":VZHIK_1,"VZHIK_2":VZHIK_2,"VZHIK_3":VZHIK_3,"VZHIK_4":VZHIK_4,"VZHIK_5":VZHIK_5,"VZHIK_6":VZHIK_6,"VZHIK_7":VZHIK_7, "VZHIK_8":VZHIK_8}

MARK_1_ENG = pygame.image.load('data/images/excellent_eng.png')
MARK_2_ENG = pygame.image.load('data/images/good_eng.png')
MARK_3_ENG = pygame.image.load('data/images/bad_eng.png')
MARKS_ENG = [0, MARK_1_ENG, MARK_2_ENG, MARK_3_ENG]

MARK_1_RUS = pygame.image.load('data/images/excellent_rus.png')
MARK_2_RUS = pygame.image.load('data/images/good_rus.png')
MARK_3_RUS = pygame.image.load('data/images/bad_rus.png')
MARKS_RUS = [0, MARK_1_RUS, MARK_2_RUS, MARK_3_RUS]

MARKS  = [MARKS_ENG, MARKS_RUS]

S_x = pygame.image.load('data/images/x.png')
S_0 = pygame.image.load('data/images/0.png')
S_1 = pygame.image.load('data/images/1.png')
S_2 = pygame.image.load('data/images/2.png')
S_3 = pygame.image.load('data/images/3.png')
S_4 = pygame.image.load('data/images/4.png')
S_5 = pygame.image.load('data/images/5.png')
S_6 = pygame.image.load('data/images/6.png')
S_7 = pygame.image.load('data/images/7.png')
S_8 = pygame.image.load('data/images/8.png')
S_9 = pygame.image.load('data/images/9.png')

NUMBERS =  [S_0, S_1, S_2, S_3, S_4, S_5, S_6, S_7, S_8, S_9, S_x]

NUM_WIDTH = 120
NUM_HEIGHT = 168

NUM_MIN_WIDTH = 27
NUM_MIN_HEIGHT = 38

BUTTON_STATE_2 = 1.07   #уменьшение (деление) размера кнопки при наведении мыши
BUTTON_STATE_3 = 1.3   #уменьшение (деление) размера кнопки при клике

RUS_BTN = pygame.image.load('data/images/rus_btn.png')
ENG_BTN = pygame.image.load('data/images/eng_btn.png')

MUSIC = pygame.image.load('data/images/music.png')
NO_MUSIC = pygame.image.load('data/images/no_music.png')

SOUND = pygame.image.load('data/images/sound.png')
NO_SOUND = pygame.image.load('data/images/no_sound.png')

#Звук
FOREST_VOLUME = 0.5
SOUND_VOLUME = 0.9

ERR_SND = pygame.mixer.Sound('data/sound/error.ogg')
SAW_1_SND = pygame.mixer.Sound('data/sound/saw_1.ogg')
SAW_2_SND = pygame.mixer.Sound('data/sound/saw_2.ogg')

SOUND_LIST = [ERR_SND, SAW_1_SND, SAW_2_SND]

#Цвета
BLACK = (  0,  0,  0)


#MODE

OFF = 0
ON = 1
STATE = 0
SPAWN = 1
CUT = 2
LEFT = 3
RIGHT = 4