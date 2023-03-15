# -*- coding: utf-8 -*-

import pygame
import main_constants
import main_objects
from main_objects import MainScreenType, render_multiline_text
import screens.start_screen as start_screen


class AboutProgramScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_introduction_design()
        self.init_design()
        self.create_back_button()

    def init_design(self):
        text = main_constants.TEXT_ABOUT_PROGRAM_SCREEN['main_text']
        text = render_multiline_text(text['strings'],
                                     text['size'], text['color'],
                                     main_constants.FONT_PATH_INTER_REGULAR)
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         20))
        text = main_constants.TEXT_ABOUT_PROGRAM_SCREEN['description_text']
        text = render_multiline_text(text['strings'],
                                     text['size'], text['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         140))
        text = main_constants.TEXT_ABOUT_PROGRAM_SCREEN['exit_button']
        text = render_multiline_text(text['strings'],
                                     text['size'], text['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (300, 220))
        text = main_constants.TEXT_ABOUT_PROGRAM_SCREEN['back_button']
        text = render_multiline_text(text['strings'],
                                     text['size'], text['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (300, 300))
        text = main_constants.TEXT_ABOUT_PROGRAM_SCREEN['second_description_text']
        text = render_multiline_text(text['strings'],
                                     text['size'], text['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         500))
        image = main_objects.load_image(main_constants.IMAGE_MAIN_SCREEN['back_button'])
        image = pygame.transform.smoothscale(image, (60, 60))
        self.blit(image, (230, 300))
        image = main_objects.load_image(main_constants.IMAGE_MAIN_SCREEN['exit_button'])
        image = pygame.transform.smoothscale(image, (60, 60))
        self.blit(image, (230, 220))
        # Creating backup
        self.backup = self.copy()

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = start_screen.StartScreen(main_constants.SCREEN_SIZE)
