# -*- coding: utf-8 -*-

from os import path
import pygame
import string

# Constants of Python
EN_ALPHABET = list(string.ascii_lowercase)

# Main Screen Display Settings
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
FPS = 50

# Fonts
FONT_PATH_INTER_LIGHT = path.join('fonts/Inter-Light.ttf')
FONT_PATH_INTER_REGULAR = path.join('fonts/Inter-Regular.ttf')
FONT_PATH_INTER_ITALIC = path.join('fonts/Inter-Italic.ttf')
FONT_PATH_INTER_EXTRABOLD = path.join('fonts/Inter-ExtraBold.ttf')

# Timer Text
TEXT_TIMER = {'main_text': {'strings': [],
                            'size': 35,
                            'color': pygame.Color('black')}}

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
TEXT_ABOUT_PROGRAM_SCREEN = {'main_text': {'strings': ['О программе'],
                                           'size': 80,
                                           'color': pygame.Color('black')},
                             'description_text': {'strings': ['Основные элементы управления:'],
                                                  'size': 45,
                                                  'color': pygame.Color('black')},
                             'exit_button': {'strings': ['- кнопка выхода из приложения'],
                                                         'size': 45,
                                                         'color': pygame.Color('black')},
                             'back_button': {'strings': ['- кнопка, возвращающая на',
                                                         'предыдущийэкран'],
                                             'size': 45,
                                             'color': pygame.Color('black')},
                             'second_description_text': {'strings': ['В игре присутствует поле для',
                                                                     'ввода текста, оно выделяется',
                                                                     'мигающей линией.'],
                                                         'size': 45,
                                                         'color': pygame.Color('black')}}
TEXT_LEVEL_SELECTION_SCREEN = {'main_text': {'strings': ['Выберите уровень сложности:'],
                                             'size': 50,
                                             'color': pygame.Color('white')},
                               'games_choice_text': {'strings': ['Выберите игру, или можете'
                                                                 ' попробовать',
                                                                 'всё сразу!'],
                                                     'size': 50,
                                                     'color': pygame.Color('white')}}
TEXT_VICTORY_SCREEN = {'info': {'strings': [],
                                'size': 60,
                                'color': pygame.Color('black')}}

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
                           'info_screen': {'strings': ['Перед вами перечень слов, написанных',
                                                       'разным цветом. Выберите те слова, ',
                                                       'которые выделены одним цветом',
                                                       'с его обозначением.'],
                                           'size': 50,
                                           'color': pygame.Color('black')}}
TEXT_ORDER_GAME_SCREEN = {'main_text': {'strings': ['Порядок'],
                                        'size': 96,
                                        'color': pygame.Color('white')},
                          'description': {'strings': ['Выбери числа по порядку!'],
                                          'size': 48,
                                          'color': pygame.Color('white')},
                          'button_check_up': {'strings': ['Проверить'],
                                              'size': 45,
                                              'color': pygame.Color('white')},
                          'info_screen': {'strings': ['Выберите все числа по порядку.',
                                                      '(От меньшего к большему)'],
                                          'size': 50,
                                          'color': pygame.Color('black')}}
TEXT_CHOICE_SOUND_SCREEN = {'main_text': {'strings': ['Угадай животное, которое',
                                                      'произносит этот звук!'],
                                          'size': 48,
                                          'color': pygame.Color('black')},
                            'button_check_up': {'strings': ['Проверить'],
                                                'size': 45,
                                                'color': pygame.Color('white')},
                            'error_message': {'strings': ['Выбрано неверное', 'животное'],
                                              'size': 35,
                                              'color': pygame.Color('#eb0722')},
                            'info_screen': {'strings': ['Выберите животное, издающее',
                                                        'указанный звук.',
                                                        '(Чтобы прослушать звук нажмите',
                                                        'на звуковую иконку)'],
                                            'size': 50,
                                            'color': pygame.Color('black')}}
TEXT_CHOICE_PICTURES_SCREEN = {'main_text': {'strings': ['Угадай животное, которое',
                                                         'изображено на картинке!'],
                                             'size': 48,
                                             'color': pygame.Color('black')},
                               'button_check_up': {'strings': ['Проверить'],
                                                   'size': 45,
                                                   'color': pygame.Color('white')},
                               'error_message': {'strings': ['Выбрано неверное', 'животное'],
                                                 'size': 35,
                                                 'color': pygame.Color('#eb0722')},
                               'info_screen': {'strings': ['Выберите животное, изображённое',
                                                           'на картинке.'],
                                               'size': 50,
                                               'color': pygame.Color('black')}}
TEXT_COUNT_GAME_SCREEN = {'main_text': {'strings': ['Посчитай'],
                                        'size': 96,
                                        'color': pygame.Color('black')},
                          'description': {'strings': ['Вычисли результат!'],
                                          'size': 48,
                                          'color': pygame.Color('black')},
                          'button_check_up': {'strings': ['Проверить'],
                                              'size': 45,
                                              'color': pygame.Color('white')},
                          'error_message': {'strings': ['Неверный', 'ответ'],
                                            'size': 35,
                                            'color': pygame.Color('#eb0722')},
                          'info_screen': {'strings': ['Перед вами логическая загадка,',
                                                      'чтобы её решить вам необходимо',
                                                      'вычислить все переменные, а ',
                                                      'затем напечатать результат.',
                                                      '(Поле ввода находится снизу, выделено',
                                                      'мигающей чертой)'],
                                          'size': 50,
                                          'color': pygame.Color('black')}}

# Main Screen Images
IMAGE_MAIN_SCREEN = {'back_button': path.join('data/icons/turn-back.png'),
                     'exit_button': path.join('data/icons/exit.png'),
                     'info_button': path.join('data/icons/info.png'),
                     'timer_icon': path.join('data/icons/timer.png')}

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
IMAGE_FIREFLY_1 = path.join('data/images/firefly_1.png')
IMAGE_FIREFLY_2 = path.join('data/images/firefly_2.png')
IMAGE_BUTTERFLY_1 = path.join('data/images/butterfly_1.png')
IMAGE_BUTTERFLY_2 = path.join('data/images/butterfly_2.png')
IMAGE_OUR_TEAM_PHOTO = path.join('data/images/our_team_image.png')
IMAGE_ARROW_1 = path.join('data/icons/arrow_1.png')
IMAGE_SOUND_IS_NOT_CLICKED = path.join('data/images/sound_image.png')
IMAGE_SOUND_IS_CLICKED = path.join('data/images/sound_image_clicked.png')

# Games variables
GAMES_DB_PATH = 'data/games_data/games_db.db'
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

# Order Game fixed parameters
DATA_ORDER_GAME_FONT = FONT_PATH_INTER_REGULAR
DATA_ORDER_GAME_FONT_SIZE = 45
# Order Game Easy Difficulty
DATA_ORDER_GAME_EASY_DIFF_FIELD_SIZE = 3
# Order Game Medium Difficulty
DATA_ORDER_GAME_MEDIUM_DIFF_FIELD_SIZE = 4
# Order Game Hard Difficulty
DATA_ORDER_GAME_HARD_DIFF_FIELD_SIZE = 5

# Choice Game fixed parameters
DATA_CHOICE_GAME_FONT = FONT_PATH_INTER_REGULAR
DATA_CHOICE_GAME_FONT_SIZE = 45

# Choice Sounds Game Easy Difficulty
DATA_CHOICE_SOUNDS_GAME_VARIANTS_COUNT = 3
DATA_CHOICE_SOUNDS_GAME_LEVELS_COUNT = 3
DATA_CHOICE_SOUNDS_GAME_COLOR_BUTTON = '#D0C3DE'
DATA_CHOICE_SOUNDS_GAME_COLOR_BUTTON_HOVER = '#A591BA'
DATA_CHOICE_SOUNDS_GAME_COLOR_BUTTON_CLICKED = '#624B7A'

# Choice Pictures Game Easy Difficulty
DATA_CHOICE_PICTURES_GAME_VARIANTS_COUNT = 3
DATA_CHOICE_PICTURES_GAME_LEVELS_COUNT = 3
DATA_CHOICE_PICTURES_GAME_COLOR_BUTTON = '#D0C3DE'
DATA_CHOICE_PICTURES_GAME_COLOR_BUTTON_HOVER = '#A591BA'
DATA_CHOICE_PICTURES_GAME_COLOR_BUTTON_CLICKED = '#624B7A'

# Count Game fixed parameters
DATA_COUNT_GAME_FONT = FONT_PATH_INTER_REGULAR
DATA_COUNT_GAME_FONT_SIZE = 45
DATA_COUNT_GAME_TEXT_COLOR = pygame.Color('black')
# Count Game Medium Difficulty
DATA_COUNT_GAME_MEDIUM_DIFF_NUMS_RANGE = (5, 15)
# Count Game Hard Difficulty
DATA_COUNT_GAME_HARD_DIFF_NUMS_RANGE = (20, 30)
