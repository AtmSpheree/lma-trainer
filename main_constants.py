from pathlib import Path
from os import path
import pygame

# Working Directory Path
WORKING_DIRECTORY = Path(__file__).parent

# Main Screen Display Settings
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
FPS = 50

# Fonts
FONT_PATH_INTER_LIGHT = path.join(WORKING_DIRECTORY,
                                  'fonts/Inter-Light.ttf')
FONT_PATH_INTER_REGULAR = path.join(WORKING_DIRECTORY,
                                    'fonts/Inter-Regular.ttf')

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

# Main Screen Images
IMAGE_MAIN_SCREEN = {'back_button': path.join(WORKING_DIRECTORY,
                                              'data/icons/turn-back.png'),
                     'exit_button': path.join(WORKING_DIRECTORY,
                                              'data/icons/exit.png')}

# Images
IMAGE_BEE_1 = path.join(WORKING_DIRECTORY,
                        'data/images/bee_1.png')
IMAGE_BEE_2 = path.join(WORKING_DIRECTORY,
                        'data/images/bee_2.png')
IMAGE_BEE_3 = path.join(WORKING_DIRECTORY,
                        'data/images/bee_3.png')