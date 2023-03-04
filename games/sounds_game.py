# -*- coding: utf-8 -*-

import pygame
from os import path
import main_constants
from main_objects import (render_multiline_text, ButtonTextSpriteType4, SoundButtonSpriteType,
                          ButtonTextSpriteType1)


class SoundsGameObject(pygame.sprite.Group):
    def __init__(self, *args):
        super().__init__(*args)
        self.set_btn_colors()
        self.now_pressed = ButtonTextSpriteType4()
        self.now_pressed.set_text(text='')
        self.is_correct_choice = False
        self.is_sounds_data_empty = False
        self.current_status_bar_position = 0

    def is_correct(self):
        return self.is_correct_choice

    def set_btn_colors(self, btn_color: pygame.Color = pygame.Color('grey'),
                       hover_color: pygame.Color = pygame.Color('grey'),
                       changed_color: pygame.Color = pygame.Color('grey')):
        self.btn_color = btn_color
        self.hover_background = hover_color
        self.changed_background = changed_color

    def set_data(self, sounds_list_data: list,
                 font_size: int = 25, font: str = None, gap: int = 0,
                 screen_size: tuple = (100, 100), color: pygame.Color = pygame.Color('black'),
                 background_color: pygame.Color = pygame.Color('white'), vars_left: int = None,
                 vars_top: int = None, sound_btn_left: int = None, sound_btn_top: int = None):
        width, height = 0, 0
        self.background_color = background_color
        self.text_color = color
        data = []
        for i in [item['variants'] for item in sounds_list_data]:
            data += i
        for text in data:
            test_text = render_multiline_text([text], font_size,
                                              self.text_color, font)
            if test_text.get_width() > width:
                width = test_text.get_width()
            if test_text.get_height() > height:
                height = test_text.get_height()
        width += 50
        height += 10
        self.gap = gap
        self.sounds_data = sounds_list_data
        self.font = font
        self.font_size = font_size
        self.btn_size = (width, height)
        self.vars_left = vars_left
        self.vars_top = vars_top
        self.sound_btn_left = sound_btn_left
        self.sound_btn_top = sound_btn_top
        self.screen_size = screen_size

    def set_new_field(self):
        pygame.mixer.music.stop()
        if not self.sounds_data:
            self.is_sounds_data_empty = True
            return
        self.current_status_bar_position += 1
        self.variants = len(self.sounds_data[0]['variants'])
        self.active_data = self.sounds_data.pop(0)
        self.empty()

        if self.vars_left is not None:
            self.vars_left = self.vars_left
        else:
            self.vars_left = self.variants * self.btn_size[0] + (self.gap * (self.variants - 1))
            self.vars_left = self.screen_size[0] - self.gap * (self.variants - 1)
            self.vars_left = (self.vars_left - self.btn_size[0] * self.variants) // 2
        if self.vars_top is not None:
            self.vars_top = self.vars_top
        else:
            self.vars_top = (self.screen_size[1] - self.btn_size[1]) // 2

        for index in range(len(self.active_data['variants'])):
            sprite = ButtonTextSpriteType4(self)
            sprite.set_colors(self.background_color, self.btn_color,
                              self.hover_background, self.changed_background)
            sprite.set_text(self.active_data['variants'][index], self.font_size, self.font,
                            self.text_color, self.btn_size, 50, 4)
            sprite.render_btn(self.btn_color)
            x = self.vars_left + index * self.gap + index * self.btn_size[0]
            y = self.vars_top
            sprite.set_coords(x, y)

        self.sound_btn_sprite = SoundButtonSpriteType(self)
        self.sound_btn_sprite.set_data(path.join('data/games_data', self.active_data['sound_path']),
                                       main_constants.IMAGE_SOUND_IS_NOT_CLICKED,
                                       main_constants.IMAGE_SOUND_IS_CLICKED)
        if self.sound_btn_left is not None:
            self.sound_btn_sprite.rect.x = self.sound_btn_left
        else:
            self.sound_btn_sprite.rect.x = (self.screen_size[0] - self.sound_btn_sprite.rect.width) // 2
        if self.sound_btn_top is not None:
            self.sound_btn_sprite.rect.y = self.sound_btn_top
        else:
            self.sound_btn_sprite.rect.y = (self.screen_size[1] - self.sound_btn_sprite.rect.height) // 2

        # Creating check_up_button
        text_data = main_constants.TEXT_CHOICE_SOUND_SCREEN['button_check_up']
        self.check_up_button = ButtonTextSpriteType1(self)
        self.check_up_button.set_velocity(40, 5)
        self.check_up_button.set_background(self.background_color)
        self.check_up_button.set_text(text_data['strings'],
                                      text_data['size'], text_data['color'],
                                      main_constants.FONT_PATH_INTER_LIGHT)
        self.check_up_button.set_underline(2, text_data['color'], 4)
        width = self.check_up_button.rect.width
        self.check_up_button.rect.x = (main_constants.SCREEN_WIDTH - width) // 2
        self.check_up_button.rect.y = 720

    def is_sounds_data(self):
        if not self.is_sounds_data_empty:
            return True
        return False

    def set_start_pos_sound_btn(self):
        for sprite in self:
            if sprite.__class__.__name__ == 'SoundButtonSpriteType':
                sprite.set_first_img()
                pygame.mixer.music.stop()

    def update(self, *args, **kwargs):
        event = None
        if args:
            event = args[0]
        for sprite in self:
            if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                if event is not None:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if sprite.__class__.__name__ == 'ButtonTextSpriteType4':
                            self.now_pressed = sprite
                            break
                        elif sprite.__class__.__name__ == 'ButtonTextSpriteType1':
                            if self.now_pressed.text == self.active_data['animal_name']:
                                self.set_new_field()
                                self.is_correct_choice = True
                                break
                            self.is_correct_choice = False
        for sprite in self:
            if sprite.__class__.__name__ == 'ButtonTextSpriteType4':
                if sprite.text != self.now_pressed.text:
                    sprite.pressure = False
        super().update(*args, **kwargs)
