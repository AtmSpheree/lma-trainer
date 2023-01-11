# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFilter
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
        # Creating out_team_image
        our_team_image = main_objects.load_image(main_constants.IMAGE_OUR_TEAM_PHOTO)
        self.blit(our_team_image, (15, 99))
        # Creating arrow_image
        arrow_image = main_objects.load_image(main_constants.IMAGE_ARROW_1)
        self.blit(arrow_image, (317, 534))
        # Creating pil background image with gaussian blur
        background_image = Image.new(mode='RGBA', size=(595, 638),
                                     color=main_constants.COLOR_INTRODUCTION_DESIGN)
        drawer = ImageDraw.Draw(background_image)
        drawer.rectangle((15, 15, 580, 623), '#222831')
        background_image = background_image.filter(ImageFilter.GaussianBlur(radius=2))
        background_image = main_objects.pil_image_to_surface(background_image)
        self.blit(background_image, (590, 85))
        # Creating bee_image
        bee_image = main_objects.load_image(main_constants.IMAGE_BEE_4)
        self.blit(bee_image, (29, 593))
        # Creating text
        text_data = main_constants.TEXT_ABOUT_US_SCREEN['main_text']
        text = render_multiline_text(text_data['strings'],
                                     text_data['size'], text_data['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        coords = ((main_constants.SCREEN_WIDTH - text.get_width()) // 2, 25)
        self.blit(text, coords)

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = screens.start_screen.StartScreen(main_constants.SCREEN_SIZE)