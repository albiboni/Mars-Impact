"""
Mars Impact
Alberto Bonifazi, Paolo Rizzo
02/06/2016
Copyright (C) 2016 Alberto Bonifazi, Paolo Rizzo
albertobonifazi09@gmail.com , paolo.rizzo@outlook.com
"""

import pygame as pg
from game import *
import random

class Enemy:
    def __init__(self, position_x, position_y,level):
        self.level = level
        enimg = ["ML1green", "ML1grey", "ML1red", "ML2blue", "ML2green", "ML2red", "ML3blue", "ML3green", "ML3red"]
        if self.level == 1 :
            a = random.randint(0, 2)
            self.image = pg.transform.scale(pg.image.load("images/{}.png".format(enimg[a])), (50, 50))
        if self.level == 2:
            a = random.randint(3, 5)
            self.image = pg.transform.scale(pg.image.load("images/{}.png".format(enimg[a])), (50, 50))
        elif self.level == 3:
            a = random.randint(6, 8)
            self.image = pg.transform.scale(pg.image.load("images/{}.png".format(enimg[a])), (50, 50))
        self.image = pg.transform.rotate((self.image), 90)
        self.rect = self.image.get_rect()
        self.rect.center = [position_x, position_y]
        self.position_X = position_x
        self.position_Y = position_y
        self.health = 1* int((self.level+10)%10)

    def update_position(self):
        self.position_X -= 1.2 * int((self.level+10)%10)
        self.rect.center = [self.position_X, self.position_Y]

    def contains_point(self, point):
        if self.rect[0]+self.rect[2]/2 < point[0] < self.rect[0]+self.rect[2] and self.rect[1] < point[1] < self.rect[1]+self.rect[3] + 20:
            return True
        return False

   # def rect(self):
    #    return pg.Rect(self.position_X, self.position_Y, 50, 50)