# -*- coding: utf-8 -*-

import pygame
import main_constants
import sqlite3
from main_objects import (InfoScreenType, MainScreenType, VictoryScreenType,
                          render_multiline_text, ButtonTextSpriteType1)
import screens.level_selection_screen as level_screen
import games.count_game as count_game
from random import choice


class CountGameScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def init_design(self, difficult: str, nums_range: tuple = (1, 10)):
        # Initializing count game object
        self.difficult = difficult
        self.error_message = False
        if difficult == 'MEDIUM':
            self.init_medium_game_design()
        else:
            self.init_hard_game_design()
        font = main_constants.DATA_COUNT_GAME_FONT
        font_size = main_constants.DATA_COUNT_GAME_FONT_SIZE
        # Rendering main text
        text_data = main_constants.TEXT_COUNT_GAME_SCREEN['main_text']
        text = render_multiline_text(text_data['strings'], text_data['size'],
                                     text_data['color'],
                                     main_constants.FONT_PATH_INTER_REGULAR)
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         0))
        # Rendering description text
        text_data = main_constants.TEXT_COUNT_GAME_SCREEN['description']
        text = render_multiline_text(text_data['strings'], text_data['size'],
                                     text_data['color'],
                                     main_constants.FONT_PATH_INTER_REGULAR)
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         119))
        # Creating check_up_button
        text_data = main_constants.TEXT_COUNT_GAME_SCREEN['button_check_up']
        self.check_up_button_sprite = ButtonTextSpriteType1(self.all_sprites)
        self.check_up_button_sprite.set_velocity(40, 5)
        self.check_up_button_sprite.set_background(self.work_color)
        self.check_up_button_sprite.set_text(text_data['strings'],
                                             text_data['size'], text_data['color'],
                                             main_constants.FONT_PATH_INTER_LIGHT)
        self.check_up_button_sprite.set_underline(2, text_data['color'], 4)
        width = self.check_up_button_sprite.rect.width
        self.check_up_button_sprite.rect.x = (main_constants.SCREEN_WIDTH - width) // 2
        self.check_up_button_sprite.rect.y = 720
        # Creating backup
        self.backup = self.copy()
        # Creating and rendering timer
        self.set_timer()
        self.render_timer()
        # Creating count game object
        self.count_game = count_game.CountGameObject()
        self.count_game.set_text_params(main_constants.DATA_COUNT_GAME_FONT,
                                        main_constants.DATA_COUNT_GAME_FONT_SIZE,
                                        main_constants.DATA_COUNT_GAME_TEXT_COLOR)
        # Getting data from games sqlite database
        db_connection = sqlite3.connect(main_constants.GAMES_DB_PATH)
        db_cursor = db_connection.cursor()
        game_data = db_cursor.execute('''SELECT count_game.pattern_path, count_game.variables,
                                         count_game.operations, count_game.result_operation,
                                         count_game.coordinates, count_game.condition
                                         FROM count_game''').fetchall()
        game_data = choice(game_data)
        db_connection.close()
        self.count_game.set_data(game_data[0], game_data[1].split(', '),
                                 game_data[2].split(', '), game_data[3],
                                 [tuple(item.split(',')) for item in game_data[4].split(';')],
                                 game_data[5], nums_range, 100, 200)
        # Creating buttons
        self.create_back_button_sprite()
        self.create_info_button_sprite()
        # Drawing all sprites
        self.all_sprites.draw(self)

    def print_error_message(self):
        text_data = main_constants.TEXT_COUNT_GAME_SCREEN['error_message']
        text = render_multiline_text(text_data['strings'],
                                     text_data['size'], text_data['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (980, 30))

    def update_sprites(self, event: pygame.event.Event = None):
        super().update_sprites(event)
        self.count_game.update(event)

    def draw_sprites(self):
        super().draw_sprites()
        if self.error_message:
            self.print_error_message()
        self.render_timer()
        self.count_game.draw(self)

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.check_up_button_sprite.rect.collidepoint(mouse_pos):
                    if self.count_game.check_result():
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
                        args_list += ['Посчитай']
                        args_list += ['']
                        args_list += [self.timer.get_string_view()]
                        args['strings'] = args_list
                        self.new_screen.set_text(args)
                    else:
                        self.error_message = True
                elif self.back_button_sprite.rect.collidepoint(mouse_pos):
                    if self.difficult == 'EASY':
                        self.new_screen = level_screen.EasyLevelSelectionScreen(main_constants.SCREEN_SIZE)
                    if self.difficult == 'MEDIUM':
                        self.new_screen = level_screen.MediumLevelSelectionScreen(main_constants.SCREEN_SIZE)
                    elif self.difficult == 'HARD':
                        self.new_screen = level_screen.HardLevelSelectionScreen(main_constants.SCREEN_SIZE)
                elif self.info_button_sprite.rect.collidepoint(mouse_pos):
                    self.timer.switch_pause()
                    self.new_screen = InfoScreenType(main_constants.SCREEN_SIZE)
                    self.new_screen.init_design(self.difficult, self)
                    self.new_screen.set_text(main_constants.TEXT_COUNT_GAME_SCREEN['info_screen'])
