"""
Mars Impact
Alberto Bonifazi, Paolo Rizzo
02/06/2016
Copyright (C) 2016 Alberto Bonifazi, Paolo Rizzo
albertobonifazi09@gmail.com , paolo.rizzo@outlook.com
"""
import pygame as pg


class Font:
    def _init__(self):
        pass

    def font(self,size):
        return pg.font.SysFont(None, size)

    def message_to_screen(self,size, msg, color, surface,position_x, position_y):
        self.screen_text = self.font(size).render(msg, True, color)
        surface.blit(self.screen_text, [position_x, position_y])

    def black(self):
        return (0,0,0)
