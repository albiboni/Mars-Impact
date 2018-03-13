"""
Mars Impact
Alberto Bonifazi, Paolo Rizzo
02/06/2016
Copyright (C) 2016 Alberto Bonifazi, Paolo Rizzo
albertobonifazi09@gmail.com , paolo.rizzo@outlook.com
"""

import pygame as pg
import random

class fire:

    def __init__(self,position_x,position_y,level, direction = 1):
        self.position_x = position_x
        self.position_y = position_y
        self.direction = direction
        self.level = level
        self.damage = 1
        self.image_lev1 = pg.transform.scale(pg.image.load("images/laser.png"), (20, 5))
        self.images_lev2 = []
        self.images_enemy = pg.transform.scale(pg.image.load("images/laserEnemies.png"),(20,5))
        for i in range(1, 6):
            self.images_lev2.append(pg.transform.scale(pg.image.load("images/Lightning{}.png".format(i)), (25, 10)))

    def update_position(self):
        self.position_x += self.direction*4/float(self.level)

    def get_image(self):
        if self.level <= 1:
            if self.direction == -1:
                return self.images_enemy
            else:
                return self.image_lev1
        elif self.level == 2:
            return self.images_lev2[random.randint(0, 4)]


