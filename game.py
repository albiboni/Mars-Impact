"""
Mars Impact
Alberto Bonifazi, Paolo Rizzo
02/06/2016
Copyright (C) 2016 Alberto Bonifazi, Paolo Rizzo
albertobonifazi09@gmail.com , paolo.rizzo@outlook.com
"""

import pygame as pg
from player import *
from fire import *
from enemies import *
from font import *
import time
from boss import *

#Some functions and definitions


class game:
    def __init__(self):
        self.timeLastShot = time.time()*1000
        self.time_last_hit = time.time()*1000
        self.time_last_enemy = time.time()
        pg.mixer.init()
        self.backgroundMusic = pg.mixer.Sound("tracks/space.wav")
        self.backgroundMusic.set_volume(0.4)
        self.backgroundMusic.play(-1)
        self.background = pg.transform.scale(pg.image.load("Images/background.png"), (800, 600))
        self.exit_tot = False
    def draw_shots(self):
        for (index,fire) in enumerate(self.fires):
            self.window.blit(fire.get_image(),(fire.position_x, fire.position_y))
            fire.update_position()
            if  fire.position_x >= self.window_width:
                del self.fires[index]
        for (index,fire) in enumerate(self.enemies_fires):
            self.window.blit(fire.get_image(), (fire.position_x, fire.position_y))
            fire.update_position()
            if fire.position_x < 0:
                del self.enemies_fires[index]
        for(index,fire) in enumerate(self.boss_fires):
            self.window.blit(fire.get_image(), (fire.position_x, fire.position_y))
            fire.update_position()
            if fire.position_x < 0:
                del self.boss_fires[index]

    def draw_enemies(self):
        for (index, enemy) in enumerate(self.enemies):
            self.window.blit(enemy.image, (enemy.position_X, enemy.position_Y))
            enemy.update_position()

    def draw_boss(self):
        self.window.blit(self.boss.image, (self.boss.position_X, self.boss.position_Y))
        self.boss.update_position()

    def show_data(self):
        self.score_string = 'Score: ' + str(self.score)
        self.text.message_to_screen(30, self.score_string,self.text.black(), self.window, 600, 50)
        self.life_string = 'Lives: ' + str(self.ship.life)
        self.text.message_to_screen(30, self.life_string, self.text.black(), self.window, 50, 50)
        self.level_string = 'Level: ' + str(self.get_enemy_level())
        self.text.message_to_screen(30, self.level_string, self.text.black(), self.window, 325, 50)

    def draw_menu(self,window):
        window.fill((0,0,0))
        self.text.message_to_screen(60,'MARS IMPACT',(255,255,255),self.window,100,100)
        self.text.message_to_screen(30, 'by: Alberto Bonifazi and Paolo Rizzo', (255, 255, 255), self.window, 100, 150)
        self.text.message_to_screen(30, 'It is the year 2250. Humans have populated Mars, but two evil engineers', (255, 255, 255), self.window, 30, 200)
        self.text.message_to_screen(30, 'have taken control of the only water supply, and are extorting money and', (255, 255, 255), self.window, 30, 240)
        self.text.message_to_screen(30, 'resources from the people of Mars. You, along with your team of Aerospace', (255, 255, 255), self.window, 30, 280)
        self.text.message_to_screen(30, "students, board VirginGalactic's SpaceShipTwelve to go save the people of", (255, 255, 255), self.window, 30, 320)
        self.text.message_to_screen(30, 'Mars. But beware, the engineers have teamed up with the Kregh,', (255, 255, 255), self.window, 30, 360)
        self.text.message_to_screen(30,'a dangerous alien species!', (255, 255, 255), self.window, 30, 400)
        self.text.message_to_screen(30, 'Press SPACE BAR to play', (255, 255, 255), self.window, 100, 460)
        self.text.message_to_screen(30, 'Use arrows to move, and SPACE BAR to shoot', (255, 255, 255), self.window, 100, 490)
        self.text.message_to_screen(40, 'Good Luck!', (255, 255, 255), self.window, 150, 550)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.playing = True
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
            if event.type == pg.QUIT:
                self.playing = False
                pg.quit()
                exit()

    def draw_losing_menu(self, window):
        window.fill((0, 0, 0))
        self.text.message_to_screen(45, 'YOUR MISSION HAS BEEN COMPROMISED!', (255, 255, 255), self.window, 50, 100)
        self.text.message_to_screen(60, self.score_string, (255, 255, 255), self.window, 100, 240)
        self.text.message_to_screen(60, self.level_string, (255, 255, 255), self.window, 100, 310)
        self.text.message_to_screen(30, "But don't give up quite yet, the people of Mars need your help.", (255, 255, 255), self.window, 50, 440)
        self.text.message_to_screen(30, "Press SPACE BAR to start over, and try to defeat the evil engineers.",(255, 255, 255), self.window, 50, 480)
        self.text.message_to_screen(30, "But beware! The Kregh know where you are, and are already onto you!", (255, 255, 255), self.window, 50, 520)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.playing = True
                    self.score = 150
                    self.ship.life = 5
                elif event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def collision(self):
        t = time.time()*1000
        #collision with enemy
        for (index,enemy) in enumerate(self.enemies):
            if enemy.contains_point([self.ship.position[0],self.ship.position[1]]):
                del self.enemies[index]
                if self.ship.life != 1:
                    self.ship.life -= 1
                elif self.ship.life == 1:
                    self.text.message_to_screen(60, 'You lose! Try again!', ((30, 144, 255)), self.window, 200, 200)
                    self.playing = False

            for (index2,fire) in enumerate(self.fires):
                if enemy.contains_point([fire.position_x,fire.position_y]):
                    if enemy.health !=1:
                        enemy.health -= 1
                    elif enemy.health == 1:
                        del self.enemies[index]
                    del self.fires[index2]
                    if self.get_boss() == None :
                        self.score += 1

        if self.boss is not None:
            for (index,fire) in enumerate(self.fires):
                if self.boss.contains_point([fire.position_x,fire.position_y]):
                    if self.boss.health != 0:
                        self.boss.health -= 1
                        del self.fires[index]
                        break
                    elif self.boss.health == 0:
                        self.boss = None
                        self.score += 1
                        del self.fires[index]
                        break

        for (index,fire) in enumerate(self.enemies_fires):
            if self.ship.contains_point([fire.position_x,fire.position_y]):
                del self.enemies_fires[index]
                if t - self.time_last_hit > 1500:
                    if self.ship.life != 1:
                        self.ship.life -= 1
                        self.time_last_hit = t
                    elif self.ship.life == 1:
                        self.text.message_to_screen(60, 'You lose! Try again!', ((30, 144, 255)), self.window, 200, 200)
                        self.playing = False

        for (index, fire) in enumerate(self.boss_fires):
            if self.ship.contains_point([fire.position_x, fire.position_y]):
                del self.boss_fires[index]
                if self.ship.life != 1:
                    self.ship.life -= 1
                elif self.ship.life == 1:
                    self.text.message_to_screen(60, 'You lose! Try again!', ((30, 144, 255)), self.window, 200, 200)
                    self.playing = False

    def get_enemy_level(self):
        if 0 <= self.score <= 20:
            self.level = 1
            return self.level
        elif 20 < self.score <= 55:
            self.level = 2
            return self.level
        elif self.score > 55:
            self.level = 3
            return self.level

    def get_boss(self):
        if self.score == 20:
            return 1
        if self.score == 55:
            return 2
        if self.score == 150:
            return 3
        if self.score == 151:
            return 4
        else:
            return None

    def game_init(self):
        pg.init()
        self.playing = None
        self.window_width = 800
        self.window_height = 600
        self.window = pg.display.set_mode((self.window_width,self.window_height))
        self.window.fill((255,255,255))
        pg.display.set_caption('Mars Impact')
        self.ship = Player()
        self.score = 0
        self.boss = None
        self.text = Font()
        self.fires = []
        self.enemies = []
        self.enemies_fires = []
        self.boss_fires = []
        self.level_mark = 10
        self.window.blit(self.ship.image,self.ship.get_origin())
        pg.key.set_repeat(1,1)
        self.show_intro = True
        self.time_init = time.time()

    def game_event(self):
        t = time.time()*1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    if self.ship.position[1] - 5 > 0:
                        self.ship.up_position_y()
                elif event.key == pg.K_DOWN:
                    if self.ship.position[1] + 55 < self.window_height:
                        self.ship.down_position_y()
                elif event.key == pg.K_LEFT:
                    if self.ship.position[0] - 5 > 0:
                        self.ship.left_position_x()
                elif event.key == pg.K_RIGHT:
                    if self.ship.position[0] + 55 < self.window_width:
                        self.ship.right_position_x()
                elif event.key == pg.K_ESCAPE:
                    self.playing = False
                elif event.key == pg.K_SPACE and pg.key.get_mods() & pg.KMOD_SHIFT:
                    if t - self.timeLastShot > 100:
                        self.fires.append(fire(self.ship.position[0] + 18, self.ship.position[1]+4, 2, direction=1))
                        self.fires.append(fire(self.ship.position[0] + 18, self.ship.position[1] + 40, 2, direction=1))
                        #1 is direction. -1 to the left (enemies)
                        self.timeLastShot = t
                elif event.key == pg.K_SPACE:
                    if t - self.timeLastShot > 100:
                        self.fires.append(fire(self.ship.position[0] + 25, self.ship.position[1]+23, 1, direction=1))
                        self.timeLastShot = t

    def get_time_delta(self):
        if self.get_enemy_level() == 1:
            return 250
        if self.get_enemy_level() == 2:
            return 150
        if self.get_enemy_level() == 3:
            return 100

    def game_execute(self):
        while not self.exit_tot:
            while self.playing is None:
                self.draw_menu(self.window)
                    #if time.time() - self.time_init > 10:
                     #   self.show_intro = False
                    #self.intro_menu.draw(self.window)
            while self.playing:
                self.window.blit(self.background,(0,0))
                self.show_data()
                self.draw_shots()
                #if random.randint(0, 600) == 7:
                if (time.time()-self.time_last_enemy>2 or int(time.time()*500)%self.get_time_delta() == 0) and self.boss == None:
                    new_enemy = Enemy(self.window_width, random.randint(10, self.window_height-60),self.get_enemy_level())
                    self.enemies.append(new_enemy)
                    self.time_last_enemy = time.time()
                for entry in self.enemies:
                    if random.randint(0,140) == 3 and self.boss == None:
                        self.enemies_fires.append(fire(entry.position_X,entry.position_Y+20,1./self.get_enemy_level(),-1))
                if 5 < self.score < 10:
                    self.text.message_to_screen(40, 'Try special fire: shift+space', self.text.black(), self.window, 350, 550)
                if self.score == 55:
                    self.text.message_to_screen(40, 'You are doing great: +5 live', self.text.black(), self.window, 350, 550)
                if self.score == 150:
                    self.text.message_to_screen(40, 'Almost there: +5 lives', self.text.black(), self.window, 350, 550)
                if 152< self.score < 165:
                    self.text.message_to_screen(40, 'Enjoy unlimited extra enemies!', self.text.black(), self.window, 350, 550)
                if self.boss is not None:
                    if random.randint(0, 60/self.get_boss()) == 7:
                        self.boss_fires.append(fire(self.boss.rect.center[0],self.boss.rect.center[1], 1./self.get_boss(), -1))
                    self.draw_boss()
                elif self.get_boss() != None:
                    if self.get_boss() == 1:
                        self.boss = Boss(700, 20, self.get_boss())
                    if self.get_boss() == 2:
                        self.ship.life += 5
                        self.boss = Boss(700,20,self.get_boss())
                    if self.get_boss() == 3 or self.get_boss() == 4:
                        self.ship.life += 5
                        self.boss = Boss(600,20,self.get_boss())
                self.draw_enemies()
                self.window.blit(self.ship.image, self.ship.position)
                self.collision()
                pg.display.update()
                self.game_event()
            while self.playing == False:
                #time.sleep(1)
                self.draw_losing_menu(self.window)
                pg.display.update()
        pg.quit()
        exit()

