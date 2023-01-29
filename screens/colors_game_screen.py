# -*- coding: utf-8 -*-

import pygame
import main_constants
import main_objects
from main_objects import (InfoScreenType, MainScreenType, VictoryScreenType,
                          render_multiline_text, create_text_shadow)
import screens.level_selection_screen as level_screen
import games.colors_game as colors_game


class ColorGameScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def init_design(self, difficult: str, field_size: tuple = (1, 1)):
        # Initializing colors game object
        self.difficult = difficult
        self.error_message = False
        if difficult == 'MEDIUM':
            self.init_medium_game_design()
            colors = main_constants.DATA_COLORS_GAME_MEDIUM_DIFF_COLORS
            font = main_constants.DATA_COLORS_GAME_FONT
            font_size = main_constants.DATA_COLORS_GAME_FONT_SIZE
            correct_values = main_constants.DATA_COLORS_GAME_MEDIUM_DIFF_CORRECT_VALUES_COUNT
        else:
            self.init_hard_game_design()
            colors = main_constants.DATA_COLORS_GAME_HARD_DIFF_COLORS
            font = main_constants.DATA_COLORS_GAME_FONT
            font_size = main_constants.DATA_COLORS_GAME_FONT_SIZE
            correct_values = main_constants.DATA_COLORS_GAME_HARD_DIFF_CORRECT_VALUES_COUNT
        # Rendering main text
        text_data = main_constants.TEXT_COLORS_GAME_SCREEN['main_text']
        text = render_multiline_text(text_data['strings'], text_data['size'],
                                     text_data['color'],
                                     main_constants.FONT_PATH_INTER_REGULAR)
        shadow = create_text_shadow(text_data['strings'], text_data['size'],
                                    main_constants.COLOR_SHADOW,
                                    main_constants.FONT_PATH_INTER_REGULAR,
                                    self.work_color, radius=3, top=3)
        self.blit(shadow, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                           0))
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         0))
        # Rendering description text
        text_data = main_constants.TEXT_COLORS_GAME_SCREEN['description']
        text = render_multiline_text(text_data['strings'], text_data['size'],
                                     text_data['color'],
                                     main_constants.FONT_PATH_INTER_REGULAR)
        shadow = create_text_shadow(text_data['strings'], text_data['size'],
                                    main_constants.COLOR_SHADOW,
                                    main_constants.FONT_PATH_INTER_REGULAR,
                                    self.work_color, radius=1, top=3)
        self.blit(shadow, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                           119))
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         119))
        # Creating check_up_button
        text_data = main_constants.TEXT_COLORS_GAME_SCREEN['button_check_up']
        self.check_up_button_sprite = main_objects.ButtonTextSpriteType1(self.all_sprites)
        self.check_up_button_sprite.set_velocity(40, 5)
        self.check_up_button_sprite.set_background(self.work_color)
        self.check_up_button_sprite.set_text(text_data['strings'],
                                                  text_data['size'], text_data['color'],
                                                  main_constants.FONT_PATH_INTER_LIGHT)
        self.check_up_button_sprite.set_underline(2, text_data['color'], 4)
        width = self.check_up_button_sprite.rect.width
        height = self.check_up_button_sprite.rect.height
        self.check_up_button_sprite.rect.x = (main_constants.SCREEN_WIDTH - width) // 2
        self.check_up_button_sprite.rect.y = 720
        # Creating backup
        self.backup = self.copy()
        # Creating and rendering timer
        self.set_timer()
        self.render_timer()
        # Creating colors game object
        self.colors_game = colors_game.ColorsGameObject()
        self.colors_game.set_data(colors, field_size,
                                  font_size, font, 20, main_constants.SCREEN_SIZE,
                                  top=220, background_color=self.work_color)
        self.colors_game.set_field(correct_values)
        self.create_back_button_sprite()
        self.create_info_button_sprite()
        # Drawing all sprites
        self.all_sprites.draw(self)

    def update_sprites(self, event: pygame.event.Event = None):
        super().update_sprites(event)
        self.colors_game.update(event)

    def draw_sprites(self):
        super().draw_sprites()
        if self.error_message:
            self.print_error_message()
        self.render_timer()
        self.colors_game.draw(self)

    def print_error_message(self):
        text_data = main_constants.TEXT_COLORS_GAME_SCREEN['error_message']
        text = render_multiline_text(text_data['strings'],
                                     text_data['size'], text_data['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (860, 30))

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_sprite.rect.collidepoint(mouse_pos):
                    if self.difficult == 'MEDIUM':
                        self.new_screen = level_screen.MediumLevelSelectionScreen(main_constants.SCREEN_SIZE)
                    elif self.difficult == 'HARD':
                        self.new_screen = level_screen.HardLevelSelectionScreen(main_constants.SCREEN_SIZE)
                elif self.check_up_button_sprite.rect.collidepoint(mouse_pos):
                    if self.colors_game.check_field():
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
                        args_list += ['Цвета']
                        args_list += ['']
                        args_list += [self.timer.get_string_view()]
                        args['strings'] = args_list
                        self.new_screen.set_text(args)
                    else:
                        self.error_message = True
                elif self.info_button_sprite.rect.collidepoint(mouse_pos):
                    self.timer.switch_pause()
                    self.new_screen = InfoScreenType(main_constants.SCREEN_SIZE)
                    self.new_screen.init_design(self.difficult, self)
                    self.new_screen.set_text(main_constants.TEXT_COLORS_GAME_SCREEN['info_screen'])
