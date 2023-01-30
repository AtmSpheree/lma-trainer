# -*- coding: utf-8 -*-

import pygame

from main_objects import render_multiline_text, ButtonTextSpriteType3
from random import sample, choice


class OrderGameObject(pygame.sprite.Group):
    def __init__(self, *args):
        super().__init__(*args)

    def set_data(self, font_size: int = 25, font: str = None, field_side: int = 1,
                 gap: int = 0, screen_size: tuple = (100, 100), left: int = None,
                 top: int = None, background_color: pygame.Color = pygame.Color('white')):
        self.background_color = background_color
        self.size = (field_side, field_side)
        self.flag = True
        self.hidden = []
        self.gap = gap
        self.font = font
        self.font_size = font_size
        width, height = 0, 0
        for number in range(1, field_side * field_side + 1):
            test_text = render_multiline_text([str(number)], font_size,
                                              pygame.Color('black'), font)
            if test_text.get_width() > width:
                width = test_text.get_width()
            if test_text.get_height() > height:
                height = test_text.get_height()
        width, height = (max([width, height]), max([width, height]))
        height += gap * 2
        width += gap * 2
        self.cell_size = (width, height)
        if left is not None:
            self.left = left
        else:
            self.left = width * field_side
            self.left = (screen_size[0] - self.left) // 2
        if top is not None:
            self.top = top
        else:
            self.top = height * field_side
            self.top = (screen_size[1] - self.top) // 2

    def set_field(self):
        self.field = [['.' for col in range(self.size[0])] for row in range(self.size[1])]
        values = list(map(str, range(1, self.size[0] * self.size[1] + 1)))
        for row in range(self.size[1]):
            data = sample(values, self.size[0])
            self.field[row] = [(item, False) for item in data]
            for item in data:
                values.remove(item)
        for row in range(len(self.field)):
            for col in range(len(self.field[0])):
                sprite = ButtonTextSpriteType3(self)
                sprite.set_background(pygame.Color(self.background_color))
                sprite.set_border(pygame.Color('black'), 1)
                sprite.set_text(self.field[row][col][0], self.font_size,
                                self.font, pygame.Color(self.field[row][col][1]),
                                self.cell_size)
                x = col * self.cell_size[0] + self.left
                y = row * self.cell_size[1] + self.top
                sprite.set_coords(x, y)
                sprite.set_field_coords(row, col)

    def check_field(self):
        for row in range(len(self.field)):
            for col in range(len(self.field[0])):
                if not self.field[row][col][1]:
                    return False
        return True

    def is_minimal(self, arg):
        data = []
        for row in range(len(self.field)):
            for col in range(len(self.field[0])):
                if int(self.field[row][col][0]) not in self.hidden:
                    data.append(int(self.field[row][col][0]))
        if arg == min(data):
            return True
        return False

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
                            break
                        result = self.field[sprite.row][sprite.col]
                        if not result[1]:
                            if self.is_minimal(int(result[0])):
                                result = (result[0], True)
                                sprite.switch_visibility()
                                self.hidden.append(int(result[0]))
                        self.field[sprite.row][sprite.col] = result
        super().update(*args, **kwargs)