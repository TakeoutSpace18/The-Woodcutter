import pygame 
from Constants import * 
from Objects import *
import random
import sys
class Main():

    def __init__(self, screen):
        self.screen = screen
        self.camera = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.sky = Sky()
        self.tree = Tree()
        self.cross = Cross()
        self.saw = Saw()
        self.example = Math(self)
        self.mark = Mark()
        self.score_block = Score(self)
        
        self.score = 0

        self.example.generate()
        self.buttons = [MusicButton(1003,3), SoundButton(956,3), LangButton(5, 5, self)]
        
        pygame.mixer.music.load('data/sound/forest.ogg')
        pygame.mixer.music.set_volume(FOREST_VOLUME)
        pygame.mixer.music.play(loops=-1)

        self.running = True
        self.main_loop()
        
                                                
    def move_saw(self):
        self.tree.vzhik()
        self.saw.move()


    def handle_events(self):  #Отслеживание событий
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
                sys.exit
                pygame.quit()
            elif e.type == pygame.KEYDOWN:

                if e.key == pygame.K_0 or e.key == pygame.K_KP0:
                    self.example.write_event(0)
                if e.key == pygame.K_1 or e.key == pygame.K_KP1:
                    self.example.write_event(1)
                if e.key == pygame.K_2 or e.key == pygame.K_KP2:
                    self.example.write_event(2)
                if e.key == pygame.K_3 or e.key == pygame.K_KP3:
                    self.example.write_event(3)
                if e.key == pygame.K_4 or e.key == pygame.K_KP4:
                    self.example.write_event(4)
                if e.key == pygame.K_5 or e.key == pygame.K_KP5:
                    self.example.write_event(5)
                if e.key == pygame.K_6 or e.key == pygame.K_KP6:
                    self.example.write_event(6)
                if e.key == pygame.K_7 or e.key == pygame.K_KP7:
                    self.example.write_event(7)
                if e.key == pygame.K_8 or e.key == pygame.K_KP8:
                    self.example.write_event(8)
                if e.key == pygame.K_9 or e.key == pygame.K_KP9:
                    self.example.write_event(9)

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    [i.push(1) for i in self.buttons]
            elif e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    [i.push(0) for i in self.buttons]


    def render(self):  #Обновление экрана
        self.camera.fill(BLACK)

        self.sky.render(self.camera)
        self.tree.render(self.camera)
        self.example.render(self.camera)
        self.camera.blit(ROCK, (700,500))
        self.camera.blit(GRASS, (0,0))
        self.saw.render(self.camera)
        self.cross.render(self.camera)
        self.mark.render(self.camera)
        self.score_block.render(self.camera)
        

        [i.render(self.camera) for i in self.buttons]

        self.screen.blit(self.camera,(0,0))
        pygame.display.update()


    def main_loop(self):  #Основной цикл
        while self.running == True:
            self.example.calc(self)
            self.render()
            self.handle_events()

            
pygame.init()
pygame.display.set_icon(ICON)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

game = Main(screen)
