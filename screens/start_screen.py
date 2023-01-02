# -*- coding: utf-8 -*-

import pygame
import main_constants
import main_objects
from main_objects import MainScreenType, render_multiline_text
from math import sqrt


pygame.init()


class StartScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_introduction_design()
        self.init_design()
        self.create_back_button()

    def init_design(self):
        # Filling text
        text_data = main_constants.TEXT_START_SCREEN['main_text']
        text = render_multiline_text(text_data['strings'],
                                     text_data['size'], text_data['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (41, 155))
        # Filling images
        image = main_objects.load_image(main_constants.IMAGE_BEE_1)
        self.blit(image, (69, 445))
        image = main_objects.load_image(main_constants.IMAGE_BEE_2)
        self.blit(image, (917, 224))
        image = main_objects.load_image(main_constants.IMAGE_BEE_3)
        self.blit(image, (483, -24))
        # Creating buttons
        # Creating about_us_button
        text_data = main_constants.TEXT_START_SCREEN['button_about_us']
        self.about_us_button_sprite = main_objects.ButtonTextSpriteType1(self.all_sprites)
        self.about_us_button_sprite.set_velocity(40, 5)
        self.about_us_button_sprite.set_background(self.work_color)
        self.about_us_button_sprite.set_text(text_data['strings'],
                                             text_data['size'], text_data['color'],
                                             main_constants.FONT_PATH_INTER_LIGHT)
        self.about_us_button_sprite.set_underline(2, text_data['color'], 4)
        self.about_us_button_sprite.rect.x = 776
        self.about_us_button_sprite.rect.y = 20
        # Creating about_program_button
        text_data = main_constants.TEXT_START_SCREEN['button_about_program']
        self.about_program_button_sprite = main_objects.ButtonTextSpriteType1(self.all_sprites)
        self.about_program_button_sprite.set_velocity(40, 5)
        self.about_program_button_sprite.set_background(self.work_color)
        self.about_program_button_sprite.set_text(text_data['strings'],
                                             text_data['size'], text_data['color'],
                                             main_constants.FONT_PATH_INTER_LIGHT)
        self.about_program_button_sprite.set_underline(2, text_data['color'], 4)
        self.about_program_button_sprite.rect.x = 818
        self.about_program_button_sprite.rect.y = 80
        # Creating Play Button
        self.play_button_sprite = PlayButtonSprite(self.all_sprites)
        self.play_button_sprite.set_button((348, 348),
                                           pygame.Color('white'),
                                           pygame.Color(200, 200, 200),
                                           pygame.Color('black'),
                                           (426, 342))
        self.play_button_sprite.rect.x = 426
        self.play_button_sprite.rect.y = 342
        # Drawing all sprites
        self.all_sprites.draw(self)

    def render_play_button(self, is_active: bool = True):
        if is_active:
            circle_color = pygame.Color('white')
            triangle_color = pygame.Color('black')
        else:
            circle_color = pygame.Color(200, 200, 200)
            triangle_color = pygame.Color('black')
        button = pygame.Surface((348, 348), pygame.SRCALPHA)
        pygame.draw.circle(button, circle_color, (174, 174),
                           174)
        pygame.draw.polygon(button, triangle_color,
                            [(115, 73), (115, 275), (290, 174)])
        self.blit(button, (426, 342))


class PlayButtonSprite(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

    def set_button(self, size: tuple = (200, 200),
                   background_color: pygame.Color = pygame.Color('white'),
                   changed_background_color: pygame.Color = pygame.Color(200, 200, 200),
                   button_color: pygame.Color = pygame.Color('black'),
                   pos_for_check: tuple = None):
        self.background_color = background_color
        self.changed_background_color = changed_background_color
        self.button_color = button_color
        self.size = size
        self.pos_for_check = pos_for_check
        self.draw_button()

    def draw_button(self, is_active=False):
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        if is_active:
            background_color = self.changed_background_color
        else:
            background_color = self.background_color
        button_color = self.button_color
        pygame.draw.circle(self.image, background_color,
                           (self.size[0] // 2, self.size[1] // 2),
                           (self.size[0] // 2 + self.size[1] // 2) // 2)
        coords = [(115 / 348 * self.size[0], 73 / 348 * self.size[1]),
                  (115 / 348 * self.size[0],
                   self.size[1] - 73 / 348 * self.size[1]),
                  (self.size[0] - 58 / 348 * self.size[0],
                   0.5 * self.size[1])]
        pygame.draw.polygon(self.image, button_color, coords)

    def update(self, *args):
        mouse_pos = pygame.mouse.get_pos()
        last_x, last_y = self.rect.x, self.rect.y
        if self.pos_for_check is None:
            flag_check = True
        else:
            x = mouse_pos[0] - self.pos_for_check[0] - self.size[0] // 2
            y = -(mouse_pos[1] - self.pos_for_check[1] - self.size[1] // 2)
            radius = ((self.size[0] / 2 + self.size[1] / 2) / 2)
            flag_check = sqrt(x ** 2 + y ** 2) <= radius
        if self.rect.collidepoint(pygame.mouse.get_pos()) and flag_check:
            self.draw_button(is_active=True)
        else:
            self.draw_button()
        self.rect.x, self.rect.y = last_x, last_y
