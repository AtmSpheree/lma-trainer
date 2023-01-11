# -*- coding: utf-8 -*-

import pygame
import main_constants
import main_objects
from PIL import Image, ImageFilter, ImageEnhance
from main_objects import MainScreenType, render_multiline_text
import screens.start_screen


class LevelSelectionScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_introduction_design()
        self.init_design()
        self.create_back_button()

    def init_design(self,
                    background: pygame.Surface = None):
        # Adding a blurred darkened background
        if background is not None:
            string_image = pygame.image.tostring(background, "RGB", False)
            pil_image = Image.frombytes('RGB', background.get_size(),
                                         string_image)
            pil_image = pil_image.filter(ImageFilter.GaussianBlur(radius=7))
            pil_image = ImageEnhance.Brightness(pil_image).enhance(0.5)
            image = main_objects.pil_image_to_surface(pil_image)
            self.blit(image, (0, 0))
        # Rendering main text
        text_data = main_constants.TEXT_LEVEL_SELECTION_SCREEN['main_text']
        text = render_multiline_text(text_data['strings'],
                                     text_data['size'], text_data['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         80))
        # Creating difficulty buttons
        btn_size = (450, 78)
        # Creating easy difficulty button sprite
        self.diff_easy_button_sprite = DifficultyButtonSprite(self.all_sprites)
        self.diff_easy_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                pygame.Color('#68397f'))
        self.diff_easy_button_sprite.set_text('Детский', 50, pygame.Color('white'),
                                              main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 221
        self.diff_easy_button_sprite.rect.x = x
        self.diff_easy_button_sprite.rect.y = y
        # Creating medium difficulty button sprite
        self.diff_medium_button_sprite = DifficultyButtonSprite(self.all_sprites)
        self.diff_medium_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                  pygame.Color('#68397f'))
        self.diff_medium_button_sprite.set_text('Подростковый', 50, pygame.Color('white'),
                                                main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 383
        self.diff_medium_button_sprite.rect.x = x
        self.diff_medium_button_sprite.rect.y = y
        # Creating hard difficulty button sprite
        self.diff_hard_button_sprite = DifficultyButtonSprite(self.all_sprites)
        self.diff_hard_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                  pygame.Color('#68397f'))
        self.diff_hard_button_sprite.set_text('Взрослый', 50, pygame.Color('white'),
                                                main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 545
        self.diff_hard_button_sprite.rect.x = x
        self.diff_hard_button_sprite.rect.y = y
        # Drawing all sprites
        self.all_sprites.draw(self)

    def set_background(self, background):
        self.init_design(background)

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = screens.start_screen.StartScreen(main_constants.SCREEN_SIZE)


class DifficultyButtonSprite(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

    def set_button(self, size: tuple = (300, 70),
                   background_color: pygame.Color = pygame.Color('white'),
                   changed_background_color: pygame.Color = pygame.Color(200, 200, 200),
                   ):
        self.background_color = background_color
        self.changed_background_color = changed_background_color
        self.size = size
        self.is_button_active = False
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect()

    def set_text(self, text: str = None, size: int = 40,
                 color: pygame.Color = pygame.Color('black'),
                 font: str = None):
        if type(text) == str:
            self.text = render_multiline_text([text], size,
                                              color, font)
        else:
            main_objects.terminate('no text was passed to the set_text() '
                                   'method of the DifficultyButtonSprite class')

    def draw_button(self):
        if self.is_button_active:
            background_color = self.changed_background_color
        else:
            background_color = self.background_color
        pygame.draw.rect(self.image, background_color, (0, 0, *self.size),
                         border_radius=50)
        self.image.blit(self.text,
                        ((self.rect.width - self.text.get_width()) // 2,
                         (self.rect.height - self.text.get_height()) // 2 - 3))

    def update(self, *args):
        mouse_pos = pygame.mouse.get_pos()
        last_x, last_y = self.rect.x, self.rect.y
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.is_button_active = True
            self.draw_button()
        else:
            self.is_button_active = False
            self.draw_button()

    def is_active(self):
        return self.is_button_active