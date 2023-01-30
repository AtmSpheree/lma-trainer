# -*- coding: utf-8 -*-

import pygame
import main_constants
import main_objects
from main_objects import (InfoScreenType, MainScreenType, VictoryScreenType,
                          render_multiline_text, create_text_shadow)
import screens.level_selection_screen as level_screen
import games.order_game as order_game


class OrderGameScreen(MainScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def init_design(self, difficult: str, field_size: int = 1):
        # Initializing order game object
        self.difficult = difficult
        self.error_message = False
        if difficult == 'MEDIUM':
            self.init_medium_game_design()
        else:
            self.init_hard_game_design()
        font = main_constants.DATA_ORDER_GAME_FONT
        font_size = main_constants.DATA_ORDER_GAME_FONT_SIZE
        # Rendering main text
        text_data = main_constants.TEXT_ORDER_GAME_SCREEN['main_text']
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
        text_data = main_constants.TEXT_ORDER_GAME_SCREEN['description']
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
        # Filling images
        image = main_objects.load_image(main_constants.IMAGE_BUTTERFLY_1)
        self.blit(image, (155, 353))
        image = main_objects.load_image(main_constants.IMAGE_BUTTERFLY_2)
        self.blit(image, (950, 261))
        # Creating backup
        self.backup = self.copy()
        # Creating and rendering timer
        self.set_timer()
        self.render_timer()
        # Creating order game object
        self.order_game = order_game.OrderGameObject()
        self.order_game.set_data(font_size, font, field_size, 10,
                                 main_constants.SCREEN_SIZE)
        self.order_game.set_field()
        # Creating buttons
        self.create_back_button_sprite()
        self.create_info_button_sprite()
        # Drawing all sprites
        self.all_sprites.draw(self)

    def update_sprites(self, event: pygame.event.Event = None):
        super().update_sprites(event)
        self.order_game.update(event)

    def draw_sprites(self):
        super().draw_sprites()
        if self.error_message:
            self.print_error_message()
        self.render_timer()
        self.order_game.draw(self)

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if self.order_game.check_field():
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
            args_list += ['Порядок']
            args_list += ['']
            args_list += [self.timer.get_string_view()]
            args['strings'] = args_list
            self.new_screen.set_text(args)
        elif event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_sprite.rect.collidepoint(mouse_pos):
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
                    self.new_screen.set_text(main_constants.TEXT_ORDER_GAME_SCREEN['info_screen'])
