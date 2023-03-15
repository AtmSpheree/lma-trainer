# -*- coding: utf-8 -*-

import pygame
import main_constants
import main_objects
import screens.about_us_screen as about_us_screen
import screens.about_program_screen as about_program_screen
import screens.level_selection_screen as levels_screen
from main_objects import MainScreenType, render_multiline_text
from math import sqrt


class StartScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_introduction_design()
        self.init_design()
        self.create_exit_button()

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
        # Creating backup
        self.backup = self.copy()
        # Creating buttons
        # Creating about_program_button
        text_data = main_constants.TEXT_START_SCREEN['button_about_program']
        self.about_program_button_sprite = main_objects.ButtonTextSpriteType1(self.all_sprites)
        self.about_program_button_sprite.set_velocity(40, 5)
        self.about_program_button_sprite.set_background(self.work_color)
        self.about_program_button_sprite.set_text(text_data['strings'],
                                             text_data['size'], text_data['color'],
                                             main_constants.FONT_PATH_INTER_LIGHT)
        self.about_program_button_sprite.set_underline(2, text_data['color'], 4)
        self.about_program_button_sprite.rect.x = 898
        self.about_program_button_sprite.rect.y = 20
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

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.about_program_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = about_program_screen.AboutProgramScreen(main_constants.SCREEN_SIZE)
                elif self.play_button_sprite.is_active():
                    self.new_screen = levels_screen.LevelSelectionScreen(main_constants.SCREEN_SIZE)


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
        self.is_button_active = False
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
            self.is_button_active = True
        else:
            self.draw_button()
            self.is_button_active = False
        self.rect.x, self.rect.y = last_x, last_y

    def is_active(self):
        return self.is_button_active


if __name__ == '__main__':
    pygame.init()
