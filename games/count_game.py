# -*- coding: utf-8 -*-

import pygame
from os import path
from random import randint
from main_objects import (render_multiline_text, TextInputSprite, ImageSprite)


class CountGameObject(pygame.sprite.Group):
    def __init__(self, *args):
        super().__init__(*args)

    def set_text_params(self, font: str = None, font_size: int = 15,
                        color: pygame.Color = pygame.Color('black')):
        self.font = font
        self.font_size = font_size
        self.color = color

    def set_data(self, image_path: str, variables: list, operations: list,
                 result_operation: str, coords: list, condition: str = '',
                 nums_range: tuple = (1, 10), left: int = 0, top: int = 0):
        self.image_path = image_path
        self.operations = operations
        self.coords = coords
        self.nums_range = nums_range
        self.left, self.top = left, top
        self.variables = variables
        self.result_operation = result_operation
        self.condition = condition
        self.result = 0
        self.render()

    def render(self):
        self.empty()
        # Creating Text Input Sprite Field
        self.text_input = TextInputSprite(self)
        self.text_input.set_condition('isdigit')
        self.text_input.set_text_length(10)
        self.text_input.set_data(self.font, self.font_size, self.color)
        self.text_input.set_line_data(5, pygame.Color('black'), 0.6)
        self.text_input.render(line=True)
        x, y = tuple(list(map(int, self.coords[-1])))
        x += self.left
        y += self.top
        self.text_input.set_coords((x, y))
        self.text_input.render(line=True)

        sprite = ImageSprite(self)
        sprite.set_image(path.join('data/games_data', self.image_path))
        sprite.rect.x = self.left
        sprite.rect.y = self.top
        while True:
            group = pygame.sprite.Group()
            f1 = False
            values = dict()
            for item in self.variables:
                values[item] = randint(*self.nums_range)
            for index in range(len(self.operations)):
                sprite = ImageSprite(group)
                value = eval(self.operations[index], values)
                if self.condition:
                    f2 = eval(self.condition, values)
                else:
                    f2 = True
                if value <= 0 or not f2:
                    f1 = True
                    break
                row = str(value)
                sprite.set_pygame_surface(render_multiline_text([row], self.font_size,
                                                                self.color, self.font))
                sprite.rect.x = self.left + int(self.coords[index][0])
                sprite.rect.y = self.top + int(self.coords[index][1])
            self.result = eval(self.result_operation, values)
            if f1:
                continue
            break
        for sprite in group:
            self.add(sprite)

    def check_result(self):
        if not self.text_input.get_text():
            return False
        if int(self.text_input.get_text()) == self.result:
            return True
        return False