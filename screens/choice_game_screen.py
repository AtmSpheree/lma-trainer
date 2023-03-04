# -*- coding: utf-8 -*-


import pygame
import sqlite3
from random import sample, randrange
import main_objects
import main_constants
import games.sounds_game as sounds_game
from main_objects import (InfoScreenType, MainScreenType, VictoryScreenType,
                          render_multiline_text, create_text_shadow, terminate)
import screens.level_selection_screen as level_screen


class LevelStatusBar(pygame.sprite.Sprite):
    def __init__(self, *args):
        super().__init__(*args)
        self.set_background()

    def init_sprite(self, width: int = 200, height: int = 10,
                    color: pygame.Color = pygame.Color('white'),
                    border_radius: int = 0, steps: int = 2, velocity: int = 10):
        self.width = width
        self.height = height
        self.color = color
        self.border_radius = border_radius
        self.steps = steps
        self.current_step = 0
        self.current_width = 0
        self.velocity = velocity
        self.create_pattern()
        self.rect = self.image.get_rect()

    def set_background(self, color: pygame.Color = pygame.Color('black')):
        self.background_color = color

    def change_position(self, value):
        if self.current_step + value < 0 or self.current_step + value > self.steps:
            terminate('incorrect value')
        self.current_step += value

    def set_position(self, value):
        if value < 0 or value > self.steps:
            terminate('incorrect value')
        self.current_step = value

    def create_pattern(self):
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.background_color)
        pygame.draw.rect(self.image, self.color,
                         (0, 0, self.current_width, self.height),
                         border_radius=self.border_radius)

    def update(self, *args):
        if self.current_width < self.width * (self.current_step / self.steps):
            self.current_width += self.velocity
            if self.current_width > self.width * (self.current_step / self.steps):
                self.current_width = self.width * (self.current_step / self.steps)
        else:
            self.current_width -= self.velocity
            if self.current_width < self.width * (self.current_step / self.steps):
                self.current_width = self.width * (self.current_step / self.steps)
        self.create_pattern()


class ChoiceGameScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def init_design(self, difficult: str):
        # Initializing colors game object
        if difficult == 'EASY':
            self.init_easy_game_design()
            self.font = main_constants.DATA_CHOICE_GAME_FONT
            self.font_size = main_constants.DATA_CHOICE_GAME_FONT_SIZE
        self.difficult = difficult


class ChoiceSoundsGameScreen(ChoiceGameScreen):
    def init_design(self, difficult: str, levels_count: int = 3,
                    variants_count: int = 3):
        super().init_design(difficult)
        self.error_message = False
        # Rendering main text
        text_data = main_constants.TEXT_CHOICE_SOUND_SCREEN['main_text']
        text = render_multiline_text(text_data['strings'], text_data['size'],
                                     text_data['color'],
                                     main_constants.FONT_PATH_INTER_REGULAR)
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         138))
        # Creating backup
        self.backup = self.copy()
        # Creating and rendering timer
        self.set_timer()
        self.render_timer()
        # Creating status_bar
        self.status_bar = LevelStatusBar(self.all_sprites)
        self.status_bar.set_background(main_constants.COLOR_EASY_GAME_DESIGN)
        self.status_bar.init_sprite(852, 27, pygame.Color('white'), 19, 3, 10)
        self.status_bar.rect.x = 174
        self.status_bar.rect.y = 58
        # Creating colors game object
        self.sounds_game = sounds_game.SoundsGameObject()
        # Getting data from games sqlite database
        db_connection = sqlite3.connect(main_constants.GAMES_DB_PATH)
        db_cursor = db_connection.cursor()
        game_data = db_cursor.execute('''SELECT animals.animal_name, sounds_game.sound_path
                                         FROM sounds_game LEFT JOIN animals ON
                                         animals.id = sounds_game.id''')
        game_data = sample(game_data.fetchall(), levels_count)
        variants = db_cursor.execute('''SELECT animal_name FROM animals''').fetchall()
        db_connection.close()
        sounds_data = []
        for collection in game_data:
            dictionary = dict()
            dictionary['animal_name'] = collection[0]
            dictionary['sound_path'] = collection[1]
            dictionary['variants'] = sample([i[0] for i in variants], variants_count)
            if collection[0] not in dictionary['variants']:
                dictionary['variants'][randrange(0, len(dictionary['variants']))] = collection[0]
            sounds_data.append(dictionary)
        self.sounds_game.set_data(sounds_data,
                                 self.font_size, self.font, 50,
                                 main_constants.SCREEN_SIZE,
                                 background_color=self.work_color,
                                 vars_top=520, sound_btn_top=320)
        self.sounds_game.set_btn_colors(main_constants.DATA_CHOICE_SOUNDS_GAME_COLOR_BUTTON,
                                        main_constants.DATA_CHOICE_SOUNDS_GAME_COLOR_BUTTON_HOVER,
                                        main_constants.DATA_CHOICE_SOUNDS_GAME_COLOR_BUTTON_CLICKED)
        self.sounds_game.set_new_field()
        # Creating buttons
        self.create_back_button_sprite()
        self.create_info_button_sprite()
        # Drawing all sprites
        self.all_sprites.draw(self)

    def print_error_message(self):
        text_data = main_constants.TEXT_CHOICE_SOUND_SCREEN['error_message']
        text = render_multiline_text(text_data['strings'],
                                     text_data['size'], text_data['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (860, 690))

    def update_sprites(self, event: pygame.event.Event = None):
        super().update_sprites(event)
        self.sounds_game.update(event)
        mouse_pos = pygame.mouse.get_pos()
        self.status_bar.set_position(self.sounds_game.current_status_bar_position)
        for sprite in self.sounds_game:
            if sprite.rect.collidepoint(mouse_pos):
                if sprite.__class__.__name__ == 'ButtonTextSpriteType1':
                    if event is not None:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if not self.sounds_game.is_correct():
                                self.error_message = True
                            else:
                                self.error_message = False

    def draw_sprites(self):
        super().draw_sprites()
        if self.error_message:
            self.print_error_message()
        self.render_timer()
        self.sounds_game.draw(self)

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if not self.sounds_game.is_sounds_data():
            self.new_screen = VictoryScreenType(main_constants.SCREEN_SIZE)
            if self.difficult == 'EASY':
                obj = level_screen.EasyLevelSelectionScreen(main_constants.SCREEN_SIZE)
            elif self.difficult == 'MEDIUM':
                obj = level_screen.MediumLevelSelectionScreen(main_constants.SCREEN_SIZE)
            elif self.difficult == 'HARD':
                obj = level_screen.HardLevelSelectionScreen(main_constants.SCREEN_SIZE)
            self.new_screen.init_design(self.difficult, obj)
            args = main_constants.TEXT_VICTORY_SCREEN['info'].copy()
            args_list = []
            if self.difficult == 'EASY':
                args_list = args_list + ['Детский']
            elif self.difficult == 'MEDIUM':
                args_list = args_list + ['Подростковый']
            elif self.difficult == 'HARD':
                args_list = args_list + ['Взрослый']
            args_list += ['Звуки']
            args_list += ['']
            args_list += [self.timer.get_string_view()]
            args['strings'] = args_list
            self.new_screen.set_text(args)
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = level_screen.EasyLevelSelectionScreen(main_constants.SCREEN_SIZE)
                    pygame.mixer.music.stop()
                elif self.info_button_sprite.rect.collidepoint(mouse_pos):
                    self.timer.switch_pause()
                    self.new_screen = InfoScreenType(main_constants.SCREEN_SIZE)
                    self.new_screen.init_design(self.difficult, self)
                    self.new_screen.set_text(main_constants.TEXT_CHOICE_SOUND_SCREEN['info_screen'])
                    self.sounds_game.set_start_pos_sound_btn()