# -*- coding: utf-8 -*-

from os import path
import pygame

# Main Screen Display Settings
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
FPS = 50

# Fonts
FONT_PATH_INTER_LIGHT = path.join('fonts/Inter-Light.ttf')
FONT_PATH_INTER_REGULAR = path.join('fonts/Inter-Regular.ttf')
FONT_PATH_INTER_ITALIC = path.join('fonts/Inter-Italic.ttf')
FONT_PATH_INTER_EXTRABOLD = path.join('fonts/Inter-ExtraBold.ttf')

# Main Screen Text
TEXT_MAIN_SCREEN = {'back_button': {'strings': ['Вернуться',
                                                'назад'],
                                    'size': 35,
                                    'color': pygame.Color(30, 30, 30)},
                    'exit_button': {'strings': ['Выйти из',
                                                'игры'],
                                    'size': 35,
                                    'color': pygame.Color(30, 30, 30)}}

# Windows Texts
TEXT_START_SCREEN = {'main_text': {'strings': ['Добро пожаловать в игру на развитие',
                                               'мышления, логики и внимания'],
                                   'size': 60,
                                   'color': pygame.Color('black')},
                     'button_about_us': {'strings': ['О нашей команде'],
                                         'size': 40,
                                         'color': pygame.Color('white')},
                     'button_about_program': {'strings': ['О программе'],
                                              'size': 40,
                                              'color': pygame.Color('white')}}
TEXT_ABOUT_US_SCREEN = {'main_text': {'strings': ['История нашей команды!'],
                                      'size': 50,
                                      'color': pygame.Color('black')}}
TEXT_LEVEL_SELECTION_SCREEN = {'main_text': {'strings': ['Выберите уровень сложности:'],
                                             'size': 50,
                                             'color': pygame.Color('white')},
                               'games_choice_text': {'strings': ['Выберите игру, или можете'
                                                                 ' попробовать',
                                                                 'всё сразу!'],
                                                     'size': 50,
                                                     'color': pygame.Color('white')}}

# Games Windows Text
TEXT_COLORS_GAME_SCREEN = {'main_text': {'strings': ['Цвета'],
                                         'size': 96,
                                         'color': pygame.Color('white')},
                           'description': {'strings': ['Выбери нужные цвета!'],
                                           'size': 48,
                                           'color': pygame.Color('white')},
                           'button_check_up': {'strings': ['Проверить'],
                                               'size': 45,
                                               'color': pygame.Color('white')},
                           'error_message': {'strings': ['Не были выбраны', 'нужные цвета'],
                                             'size': 35,
                                             'color': pygame.Color('#eb0722')},
                           'info_screen': {'strings': ['Test', 'Test', 'Test'],
                                           'size': 50,
                                           'color': pygame.Color('black')}}

# Main Screen Images
IMAGE_MAIN_SCREEN = {'back_button': path.join('data/icons/turn-back.png'),
                     'exit_button': path.join('data/icons/exit.png'),
                     'info_button': path.join('data/icons/info.png')}

# Main Colors
COLOR_INTRODUCTION_DESIGN = '#E1CC4F'
COLOR_EASY_GAME_DESIGN = '#D0C3DE'
COLOR_MEDIUM_GAME_DESIGN = '#C3DBDE'
COLOR_HARD_GAME_DESIGN = '#DADEC3'
COLOR_SHADOW = '#474747'

# Images
IMAGE_BEE_1 = path.join('data/images/bee_1.png')
IMAGE_BEE_2 = path.join('data/images/bee_2.png')
IMAGE_BEE_3 = path.join('data/images/bee_3.png')
IMAGE_BEE_4 = path.join('data/images/bee_4.png')
IMAGE_OUR_TEAM_PHOTO = path.join('data/images/our_team_image.png')
IMAGE_ARROW_1 = path.join('data/icons/arrow_1.png')

# Games variables
# Colors Game fixed parameters
DATA_COLORS_GAME_FONT = FONT_PATH_INTER_REGULAR
DATA_COLORS_GAME_FONT_SIZE = 45
# Colors Game Medium Difficulty
DATA_COLORS_GAME_MEDIUM_DIFF_COLORS = {'Красный': '#DA1135',
                                       'Синий': '#0995E3',
                                       'Жёлтый': '#DECC2A',
                                       'Зелёный': '#29B537'}
DATA_COLORS_GAME_MEDIUM_DIFF_FIELD_SIZE = (3, 5)
DATA_COLORS_GAME_MEDIUM_DIFF_CORRECT_VALUES_COUNT = 3
# Colors Game Hard Difficulty
DATA_COLORS_GAME_HARD_DIFF_COLORS = {'Красный': '#DA1135',
                                     'Синий': '#0995E3',
                                     'Жёлтый': '#DECC2A',
                                     'Зелёный': '#29B537',
                                     'Фиолетовый': '#794BDC',
                                     'Белый': '#f0f0f0',
                                     'Оранжевый': '#ff8903'}
DATA_COLORS_GAME_HARD_DIFF_FIELD_SIZE = (4, 6)
DATA_COLORS_GAME_HARD_DIFF_CORRECT_VALUES_COUNT = 6
