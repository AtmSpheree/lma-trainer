# -*- coding: utf-8 -*-

import pygame
import main_constants
import main_objects
from main_objects import MainScreenType, render_multiline_text
import screens.start_screen


class AboutUsScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_introduction_design()
        self.init_design()
        self.create_back_button()

    def init_design(self):
        pass

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = screens.start_screen.StartScreen(main_constants.SCREEN_SIZE)