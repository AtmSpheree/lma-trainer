# -*- coding: utf-8 -*-

import pygame

import main_constants
import main_objects
from main_objects import render_multiline_text, ButtonTextSpriteType2
from random import sample, choice


class ColorsGameObject(pygame.sprite.Group):
    def __init__(self, *args):
        super().__init__(*args)

    def set_data(self, colors_data: dict, size: tuple = (1, 1),
                 font_size: int = 25, font: str = None, gap: int = 0,
                 screen_size: tuple = (100, 100), left: int = None, top: int = None,
                 background_color: pygame.Color = pygame.Color('white')):
        width, height = 0, 0
        self.background_color = background_color
        for color in colors_data:
            test_text = render_multiline_text([color], font_size,
                                              colors_data[color], font)
            if test_text.get_width() > width:
                width = test_text.get_width()
            if test_text.get_height() > height:
                height = test_text.get_height()
        self.flag = True
        self.size = size
        self.gap = gap
        self.colors = colors_data
        self.font = font
        self.font_size = font_size
        self.cell_size = (width, height)
        if left is not None:
            self.left = left
        else:
            self.left = size[0] * self.cell_size[0] + (self.gap * (size[0] - 1))
            self.left = (screen_size[0] - self.left) // 2
        if top is not None:
            self.top = top
        else:
            self.top = size[1] * self.cell_size[1] + (self.gap * (size[1] - 1))
            self.top = (screen_size[1] - self.top) // 2

    def set_field(self, correct_values: int = 1):
        self.field = [['.' for col in range(self.size[0])] for row in range(self.size[1])]
        coords = [(row, col) for col in range(self.size[0]) for row in range(self.size[1])]
        temp = []
        for coord in sample(coords, correct_values):
            color = (choice(list(self.colors.keys())))
            temp.append(coord)
            self.field[coord[0]][coord[1]] = (color, self.colors[color], False)
        for item in temp:
            coords.remove(item)
        for coord in coords:
            color_name = choice(list(self.colors.keys()))
            color = choice([hex_code for hex_code in self.colors.values()
                                 if hex_code != self.colors[color_name]])
            self.field[coord[0]][coord[1]] = (color_name, color, False)
        for row in range(len(self.field)):
            for col in range(len(self.field[0])):
                sprite = ButtonTextSpriteType2(self)
                sprite.set_background(pygame.Color(self.background_color))
                sprite.set_text(self.field[row][col][0], self.font_size,
                                self.font, pygame.Color(self.field[row][col][1]),
                                self.cell_size)
                x = col * self.cell_size[0] + self.left
                y = row * self.cell_size[1] + self.top
                if col != 0:
                    x += self.gap * col
                if row != 0:
                    y += self.gap * row
                sprite.set_coords(x, y)
                sprite.set_field_coords(row, col)

    def check_field(self):
        for row in range(len(self.field)):
            for col in range(len(self.field[0])):
                if self.colors[self.field[row][col][0]] == self.field[row][col][1]:
                    if not self.field[row][col][2]:
                        return False
                elif self.colors[self.field[row][col][0]] != self.field[row][col][1]:
                    if self.field[row][col][2]:
                        return False
        return True

    def update(self, *args, **kwargs):
        event = None
        if args:
            event = args[0]
        for sprite in self:
            if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                if event is not None:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.flag:
                            self.flag = False
                            sprite.update(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
                            break
                        result = self.field[sprite.row][sprite.col]
                        if result[2]:
                            result = (result[0], result[1], False)
                        else:
                            result = (result[0], result[1], True)
                        self.field[sprite.row][sprite.col] = result
        super().update(*args, **kwargs)