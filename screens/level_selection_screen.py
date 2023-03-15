# -*- coding: utf-8 -*-

import pygame
import main_constants
import main_objects
from main_objects import MainScreenType, render_multiline_text
import screens.start_screen as start_screen
import screens.colors_game_screen as colors_game
import screens.order_game_screen as order_game
import screens.choice_game_screen as choice_game
import screens.count_game_screen as count_game


class LevelSelectionScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_introduction_design()
        self.init_design()
        self.create_back_button()

    def init_design(self):
        # Adding a blurred darkened background
        background = start_screen.StartScreen(main_constants.SCREEN_SIZE)
        image = main_objects.get_blurred_darkened_surface(background)
        self.blit(image, (0, 0))
        # Rendering main text
        text_data = main_constants.TEXT_LEVEL_SELECTION_SCREEN['main_text']
        text = render_multiline_text(text_data['strings'],
                                     text_data['size'], text_data['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         80))
        # Creating backup
        self.backup = self.copy()
        # Creating difficulty buttons
        btn_size = (470, 78)
        # Creating easy difficulty button sprite
        self.diff_easy_button_sprite = MenuButtonSprite(self.all_sprites)
        self.diff_easy_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                pygame.Color('#68397f'))
        self.diff_easy_button_sprite.set_text('Детский', 50, pygame.Color('white'),
                                              main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 221
        self.diff_easy_button_sprite.rect.x = x
        self.diff_easy_button_sprite.rect.y = y
        # Creating medium difficulty button sprite
        self.diff_medium_button_sprite = MenuButtonSprite(self.all_sprites)
        self.diff_medium_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                  pygame.Color('#68397f'))
        self.diff_medium_button_sprite.set_text('Подростковый', 50, pygame.Color('white'),
                                                main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 383
        self.diff_medium_button_sprite.rect.x = x
        self.diff_medium_button_sprite.rect.y = y
        # Creating hard difficulty button sprite
        self.diff_hard_button_sprite = MenuButtonSprite(self.all_sprites)
        self.diff_hard_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                pygame.Color('#68397f'))
        self.diff_hard_button_sprite.set_text('Взрослый', 50, pygame.Color('white'),
                                              main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 545
        self.diff_hard_button_sprite.rect.x = x
        self.diff_hard_button_sprite.rect.y = y
        # Drawing all sprites
        self.all_sprites.draw(self)

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = start_screen.StartScreen(main_constants.SCREEN_SIZE)
                elif self.diff_easy_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = EasyLevelSelectionScreen(main_constants.SCREEN_SIZE)
                elif self.diff_medium_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = MediumLevelSelectionScreen(main_constants.SCREEN_SIZE)
                elif self.diff_hard_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = HardLevelSelectionScreen(main_constants.SCREEN_SIZE)


class EasyLevelSelectionScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_introduction_design()
        self.init_design()
        self.create_back_button()

    def init_design(self):
        # Adding a blurred darkened background
        background = start_screen.StartScreen(main_constants.SCREEN_SIZE)
        image = main_objects.get_blurred_darkened_surface(background)
        self.blit(image, (0, 0))
        # Rendering main text
        text_data = main_constants.TEXT_LEVEL_SELECTION_SCREEN['games_choice_text']
        text = render_multiline_text(text_data['strings'],
                                     text_data['size'], text_data['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         50))
        # Creating backup
        self.backup = self.copy()
        # Creating game selection buttons
        btn_size = (470, 78)
        # Creating sounds game button sprite
        self.sounds_game_button_sprite = MenuButtonSprite(self.all_sprites)
        self.sounds_game_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                  pygame.Color('#68397f'))
        self.sounds_game_button_sprite.set_text('Звуки', 50, pygame.Color('white'),
                                                main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 221
        self.sounds_game_button_sprite.rect.x = x
        self.sounds_game_button_sprite.rect.y = y
        # Creating pictures game button sprite
        self.pictures_game_button_sprite = MenuButtonSprite(self.all_sprites)
        self.pictures_game_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                    pygame.Color('#68397f'))
        self.pictures_game_button_sprite.set_text('Картинки', 50, pygame.Color('white'),
                                                  main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 311
        self.pictures_game_button_sprite.rect.x = x
        self.pictures_game_button_sprite.rect.y = y
        # Creating order game button sprite
        self.order_game_button_sprite = MenuButtonSprite(self.all_sprites)
        self.order_game_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                 pygame.Color('#68397f'))
        self.order_game_button_sprite.set_text('Порядок', 50, pygame.Color('white'),
                                               main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 401
        self.order_game_button_sprite.rect.x = x
        self.order_game_button_sprite.rect.y = y
        # Drawing all sprites
        self.all_sprites.draw(self)

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = LevelSelectionScreen(main_constants.SCREEN_SIZE)
                elif self.order_game_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = order_game.OrderGameScreen(main_constants.SCREEN_SIZE)
                    self.new_screen.init_design('EASY',
                                                main_constants.DATA_ORDER_GAME_EASY_DIFF_FIELD_SIZE)
                elif self.sounds_game_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = choice_game.ChoiceSoundsGameScreen(main_constants.SCREEN_SIZE)
                    self.new_screen.init_design('EASY',
                                                main_constants.DATA_CHOICE_SOUNDS_GAME_LEVELS_COUNT,
                                                main_constants.DATA_CHOICE_SOUNDS_GAME_VARIANTS_COUNT)
                elif self.pictures_game_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = choice_game.ChoicePicturesGameScreen(main_constants.SCREEN_SIZE)
                    self.new_screen.init_design('EASY',
                                                main_constants.DATA_CHOICE_SOUNDS_GAME_LEVELS_COUNT,
                                                main_constants.DATA_CHOICE_SOUNDS_GAME_VARIANTS_COUNT)


class MediumLevelSelectionScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_introduction_design()
        self.init_design()
        self.create_back_button()

    def init_design(self):
        # Adding a blurred darkened background
        background = start_screen.StartScreen(main_constants.SCREEN_SIZE)
        image = main_objects.get_blurred_darkened_surface(background)
        self.blit(image, (0, 0))
        # Rendering main text
        text_data = main_constants.TEXT_LEVEL_SELECTION_SCREEN['games_choice_text']
        text = render_multiline_text(text_data['strings'],
                                     text_data['size'], text_data['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         50))
        # Creating backup
        self.backup = self.copy()
        # Creating game selection buttons
        btn_size = (470, 78)
        # Creating count game button sprite
        self.count_game_button_sprite = MenuButtonSprite(self.all_sprites)
        self.count_game_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                 pygame.Color('#68397f'))
        self.count_game_button_sprite.set_text('Посчитай', 50, pygame.Color('white'),
                                               main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 221
        self.count_game_button_sprite.rect.x = x
        self.count_game_button_sprite.rect.y = y
        # Creating colors game button sprite
        self.colors_game_button_sprite = MenuButtonSprite(self.all_sprites)
        self.colors_game_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                  pygame.Color('#68397f'))
        self.colors_game_button_sprite.set_text('Цвета', 50, pygame.Color('white'),
                                                main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 311
        self.colors_game_button_sprite.rect.x = x
        self.colors_game_button_sprite.rect.y = y
        # Creating order game button sprite
        self.order_game_button_sprite = MenuButtonSprite(self.all_sprites)
        self.order_game_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                 pygame.Color('#68397f'))
        self.order_game_button_sprite.set_text('Порядок', 50, pygame.Color('white'),
                                               main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 401
        self.order_game_button_sprite.rect.x = x
        self.order_game_button_sprite.rect.y = y
        # Drawing all sprites
        self.all_sprites.draw(self)

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = LevelSelectionScreen(main_constants.SCREEN_SIZE)
                elif self.colors_game_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = colors_game.ColorGameScreen(main_constants.SCREEN_SIZE)
                    self.new_screen.init_design('MEDIUM',
                                                main_constants.DATA_COLORS_GAME_MEDIUM_DIFF_FIELD_SIZE)
                elif self.order_game_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = order_game.OrderGameScreen(main_constants.SCREEN_SIZE)
                    self.new_screen.init_design('MEDIUM',
                                                main_constants.DATA_ORDER_GAME_MEDIUM_DIFF_FIELD_SIZE)
                elif self.count_game_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = count_game.CountGameScreen(main_constants.SCREEN_SIZE)
                    self.new_screen.init_design('MEDIUM',
                                                main_constants.DATA_COUNT_GAME_MEDIUM_DIFF_NUMS_RANGE)


class HardLevelSelectionScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_introduction_design()
        self.init_design()
        self.create_back_button()

    def init_design(self):
        # Adding a blurred darkened background
        background = start_screen.StartScreen(main_constants.SCREEN_SIZE)
        image = main_objects.get_blurred_darkened_surface(background)
        self.blit(image, (0, 0))
        # Rendering main text
        text_data = main_constants.TEXT_LEVEL_SELECTION_SCREEN['games_choice_text']
        text = render_multiline_text(text_data['strings'],
                                     text_data['size'], text_data['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         50))
        # Creating backup
        self.backup = self.copy()
        # Creating game selection buttons
        btn_size = (470, 78)
        # Creating count game button sprite
        self.count_game_button_sprite = MenuButtonSprite(self.all_sprites)
        self.count_game_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                 pygame.Color('#68397f'))
        self.count_game_button_sprite.set_text('Посчитай', 50, pygame.Color('white'),
                                               main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 221
        self.count_game_button_sprite.rect.x = x
        self.count_game_button_sprite.rect.y = y
        # Creating colors game button sprite
        self.colors_game_button_sprite = MenuButtonSprite(self.all_sprites)
        self.colors_game_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                  pygame.Color('#68397f'))
        self.colors_game_button_sprite.set_text('Цвета', 50, pygame.Color('white'),
                                                main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 311
        self.colors_game_button_sprite.rect.x = x
        self.colors_game_button_sprite.rect.y = y
        # Creating order game button sprite
        self.order_game_button_sprite = MenuButtonSprite(self.all_sprites)
        self.order_game_button_sprite.set_button(btn_size, pygame.Color('#C18EDA'),
                                                 pygame.Color('#68397f'))
        self.order_game_button_sprite.set_text('Порядок', 50, pygame.Color('white'),
                                               main_constants.FONT_PATH_INTER_EXTRABOLD)
        x, y = (main_constants.SCREEN_WIDTH - btn_size[0]) // 2, 401
        self.order_game_button_sprite.rect.x = x
        self.order_game_button_sprite.rect.y = y
        # Drawing all sprites
        self.all_sprites.draw(self)

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = LevelSelectionScreen(main_constants.SCREEN_SIZE)
                elif self.colors_game_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = colors_game.ColorGameScreen(main_constants.SCREEN_SIZE)
                    self.new_screen.init_design('HARD',
                                                main_constants.DATA_COLORS_GAME_HARD_DIFF_FIELD_SIZE)
                elif self.order_game_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = order_game.OrderGameScreen(main_constants.SCREEN_SIZE)
                    self.new_screen.init_design('HARD',
                                                main_constants.DATA_ORDER_GAME_HARD_DIFF_FIELD_SIZE)
                elif self.count_game_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = count_game.CountGameScreen(main_constants.SCREEN_SIZE)
                    self.new_screen.init_design('HARD',
                                                main_constants.DATA_COUNT_GAME_HARD_DIFF_NUMS_RANGE)


class MenuButtonSprite(pygame.sprite.Sprite):
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
