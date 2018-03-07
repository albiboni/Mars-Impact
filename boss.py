"""
Mars Impact
Alberto Bonifazi, Paolo Rizzo
02/06/2016
Copyright (C) 2016 Alberto Bonifazi, Paolo Rizzo
albertobonifazi09@gmail.com , paolo.rizzo@outlook.com
"""

import pygame as pg
import random


class Boss:
    def __init__(self, position_x, position_y, level):
        self.level = level
        bossimg = ["boss1", "boss2", "Hoekstra", "VanPassen"]
        if self.level == 1:
            self.image = pg.transform.scale(pg.image.load("images/{}.png".format(bossimg[0])), (70, 70))
            self.health = 60
        if self.level == 2:
            self.image = pg.transform.scale(pg.image.load("images/{}.png".format(bossimg[1])), (70, 70))
            self.health = 150
        if self.level == 3:
            self.image = pg.transform.scale(pg.image.load("images/{}.png".format(bossimg[3])), (100, 150))
            self.health = 200
        if self.level == 4:
            self.image = pg.transform.scale(pg.image.load("images/{}.png".format(bossimg[2])), (100, 150))
            self.health = 250
        self.rect = self.image.get_rect()
        self.rect.center = [position_x, position_y]
        self.position_X = position_x
        self.position_Y = position_y

    def update_position(self):
        if self.position_Y <= (70-20):
            self.position_Y += 1.4 * self.level
            self.rect.center = [self.position_X, self.position_Y]
            self.movement = 'UP'
        elif self.position_Y >= (70 / 2 + 400):
            self.position_Y -= 1.4 * self.level
            self.rect.center = [self.position_X, self.position_Y]
            self.movement = 'DOWN'
        elif self.movement == 'UP':
            self.position_Y += 1.4 * self.level
            self.rect.center = [self.position_X, self.position_Y]
        elif self.movement == 'DOWN':
            self.position_Y -= 1.4 * self.level
            self.rect.center = [self.position_X, self.position_Y]


        # self.get_b()
        # while self.get_b():
        #     self.position_Y += 1.0 * 1
        #     self.rect.center = [self.position_X, self.position_Y]
        #     if a == 5:
        #         b = True
        # while b:
        #     self.position_Y -= 1.0 * 1
        #     self.rect.center = [self.position_X, self.position_Y]
        #     if a == 10:
        #         b = False

    def contains_point(self, point):
        if self.rect[0] + self.rect[2]/2 < point[0] < self.rect[0] + self.rect[2] and self.rect[1] - 25 < point[1] < self.rect[1] + self.rect[3] + 30:
            return True
        return False

        # if #100 < self.position_Y < 500:
        # if a == 0:
        # go down
        # self.position_Y += 1.0 * 1  # int((self.level + 10) % 10)
        # elif a == 1:
        # go up
        # self.position_Y -= 1.0 * 1  # int((self.level + 10) % 10)
        # elif self.position_Y <= 100:
        # go down
        # self.position_Y += 0.5 * 1  # int((self.level + 10) % 10)
        # elif self.position_Y >= 500:
        # go up
        # self.position_Y -= 0.5 * 1  # int((self.level + 10) % 10)