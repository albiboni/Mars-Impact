"""
Mars Impact
Alberto Bonifazi, Paolo Rizzo
02/06/2016
Copyright (C) 2016 Alberto Bonifazi, Paolo Rizzo
albertobonifazi09@gmail.com , paolo.rizzo@outlook.com
"""

from game import *
import pygame as pg

class Player:
    def __init__(self):
        self.life = 5
        self.image = pg.image.load("Images/spaceship.png")
        self.image = pg.transform.scale(self.image,(50,50))
        self.position = [0,300]
        self.rect = self.image.get_rect()
        self.rect.center = [self.position[0], self.position[1]]

    def up_position_y(self):
        self.position[1] -= 4.0
        self.rect.center = [self.position[0], self.position[1]]
    def down_position_y(self):
        self.position[1] += 4.0
        self.rect.center = [self.position[0], self.position[1]]
    def right_position_x(self):
        self.position[0] += 4.0
        self.rect.center = [self.position[0], self.position[1]]
    def left_position_x(self):
        self.position[0] -= 4.0
        self.rect.center = [self.position[0], self.position[1]]

    def hit(self):
        self.life -= 1
    def get_origin(self):
        x = self.position[0]
        y = self.position[1] - 25
        return x, y

    def contains_point(self, point):
        if self.rect[0] < point[0] < self.rect[0] + self.rect[2] and self.rect[1] + 10 < point[1] < self.rect[1] + self.rect[3] + 20:
            return True
        return False

   # def rect(self):
    #    return pg.Rect(self.position_x,self.position[1],50,50)
