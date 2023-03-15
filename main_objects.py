# -*- coding: utf-8 -*-

import pygame
import sys
import time
import main_constants
from PIL import Image, ImageFilter, ImageEnhance, ImageColor

# Initializing pygame
pygame.init()
# Creating end sound pygame event
END_SOUND_EVENT = pygame.USEREVENT + 1


def terminate(error_message: str = None):
    pygame.quit()
    sys.exit(error_message)


def load_image(fullname: str, color_key: int = None):
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', fullname)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def pil_image_to_surface(pil_image: Image):
    return pygame.image.fromstring(
        pil_image.tobytes(), pil_image.size, pil_image.mode).convert()


def pygame_surface_to_image(pygame_surface: pygame.Surface):
    string_image = pygame.image.tostring(pygame_surface, "RGB", False)
    pil_image = Image.frombytes('RGB', pygame_surface.get_size(),
                                string_image)
    return pil_image


def get_blurred_darkened_surface(background: pygame.Surface):
    pil_image = pygame_surface_to_image(background)
    pil_image = pil_image.filter(ImageFilter.GaussianBlur(radius=7))
    pil_image = ImageEnhance.Brightness(pil_image).enhance(0.5)
    image = pil_image_to_surface(pil_image)
    return image


def render_multiline_text(strings: list = [], size: int = 25,
                          color: pygame.Color = pygame.Color('black'),
                          font: str = None):
    if font is None:
        font = pygame.font.SysFont('arial', size)
    else:
        try:
            font = pygame.font.Font(font, size)
        except pygame.error as message:
            print('Не удаётся загрузить:', font)
            raise SystemExit(message)
    width, height = 0, 0
    for string in strings:
        text = font.render(string, True, color)
        if text.get_rect().width > width:
            width = text.get_rect().width
        if text.get_rect().height > height:
            height = text.get_rect().height
    result = pygame.Surface((width, height * len(strings)), pygame.SRCALPHA)
    for string_num in range(len(strings)):
        text = font.render(strings[string_num], True, color)
        result.blit(text, ((width - text.get_rect().width) // 2,
                           string_num * text.get_rect().height))
    return result


def create_text_shadow(strings: list = [], size: int = 25,
                       color: pygame.Color = pygame.Color(main_constants.COLOR_SHADOW),
                       font: str = None,
                       background: pygame.Color = pygame.Color('white'),
                       radius: int = 0, left: int = 0, top: int = 0):
    text = render_multiline_text(strings, size, color, font)
    shadow = pygame.Surface((text.get_width(), text.get_height()))
    shadow.fill(background)
    shadow.blit(text, (left, top))
    pil = pygame_surface_to_image(shadow)
    pil = pil.filter(ImageFilter.GaussianBlur(radius=radius))
    shadow = pil_image_to_surface(pil)
    return shadow


class MainScreenType(pygame.Surface):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_sprites = pygame.sprite.Group()
        self.back_button_sprite = None
        self.exit_button_sprite = None
        self.new_screen = None
        self.timer = None
        self.backup = pygame.Surface(self.get_size())

    def init_introduction_design(self):
        color = pygame.Color(main_constants.COLOR_INTRODUCTION_DESIGN)
        self.fill(color)
        self.work_color = color

    def init_easy_game_design(self):
        color = pygame.Color(main_constants.COLOR_EASY_GAME_DESIGN)
        self.fill(color)
        self.work_color = color

    def init_medium_game_design(self):
        color = pygame.Color(main_constants.COLOR_MEDIUM_GAME_DESIGN)
        self.fill(color)
        self.work_color = color

    def init_hard_game_design(self):
        color = pygame.Color(main_constants.COLOR_HARD_GAME_DESIGN)
        self.fill(color)
        self.work_color = color

    def create_back_button_text(self):
        text_data = main_constants.TEXT_MAIN_SCREEN['back_button']
        text = render_multiline_text(text_data['strings'],
                                     text_data['size'], text_data['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.back_button_sprite = pygame.sprite.Sprite(self.all_sprites)
        self.back_button_sprite.image = text
        self.back_button_sprite.rect = text.get_rect()
        self.back_button_sprite.rect.x = 15
        self.back_button_sprite.rect.y = 15
        self.all_sprites.draw(self)

    def create_exit_button_text(self):
        text_data = main_constants.TEXT_MAIN_SCREEN['exit_button']
        text = render_multiline_text(text_data['strings'],
                                     text_data['size'], text_data['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.exit_button_sprite = pygame.sprite.Sprite(self.all_sprites)
        self.exit_button_sprite.image = text
        self.exit_button_sprite.rect = text.get_rect()
        self.exit_button_sprite.rect.x = 15
        self.exit_button_sprite.rect.y = 15
        self.all_sprites.draw(self)

    def create_back_button_sprite(self):
        self.back_button_sprite = pygame.sprite.Sprite(self.all_sprites)
        image = load_image(main_constants.IMAGE_MAIN_SCREEN['back_button'])
        self.back_button_sprite.image = pygame.transform.smoothscale(image,
                                                                     (60, 60))
        self.back_button_sprite.rect = image.get_rect()
        self.back_button_sprite.rect.x = 25
        self.back_button_sprite.rect.y = 25
        self.all_sprites.draw(self)

    def create_exit_button_sprite(self):
        self.exit_button_sprite = pygame.sprite.Sprite(self.all_sprites)
        image = load_image(main_constants.IMAGE_MAIN_SCREEN['exit_button'])
        self.exit_button_sprite.image = pygame.transform.smoothscale(image,
                                                                     (60, 60))
        self.exit_button_sprite.rect = image.get_rect()
        self.exit_button_sprite.rect.x = 25
        self.exit_button_sprite.rect.y = 25
        self.all_sprites.draw(self)

    def create_info_button_sprite(self):
        self.info_button_sprite = pygame.sprite.Sprite(self.all_sprites)
        image = load_image(main_constants.IMAGE_MAIN_SCREEN['info_button'])
        self.info_button_sprite.image = pygame.transform.smoothscale(image,
                                                                     (60, 60))
        self.info_button_sprite.rect = image.get_rect()
        self.info_button_sprite.rect.x = 25
        self.info_button_sprite.rect.y = 715
        self.all_sprites.draw(self)

    def try_to_change_screen(self, event: pygame.event.Event = None):
        mouse_pos = pygame.mouse.get_pos()
        if self.exit_button_sprite is not None:
            if self.exit_button_sprite.rect.collidepoint(mouse_pos):
                if event is not None:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        terminate()

    def set_timer(self):
        self.timer = GameTimer()

    def render_timer(self):
        if self.timer is None:
            return
        timer_surface = self.timer.get_pygame_surface_view()
        self.blit(timer_surface, (100, 725))

    def get_new_screen(self):
        return self.new_screen

    def clear_new_screen(self):
        self.new_screen = None

    def create_back_button(self):
        self.create_back_button_sprite()

    def create_exit_button(self):
        self.create_exit_button_sprite()

    def draw_sprites(self):
        self.blit(self.backup, (0, 0))
        self.all_sprites.draw(self)

    def update_sprites(self, event: pygame.event.Event = None):
        self.all_sprites.update(event)


class SecondaryScreenType(MainScreenType):
    def init_design(self, difficult: str = 'EASY',
                    object: pygame.Surface = pygame.Surface(main_constants.SCREEN_SIZE)):
        self.object = object
        if difficult == 'EASY':
            self.init_easy_game_design()
        elif difficult == 'MEDIUM':
            self.init_medium_game_design()
        elif difficult == 'HARD':
            self.init_hard_game_design()
        self.create_back_button_sprite()
        self.backup = self.copy()

    def try_to_change_screen(self, event: pygame.event.Event = None):
        super().try_to_change_screen(event)
        mouse_pos = pygame.mouse.get_pos()
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_sprite.rect.collidepoint(mouse_pos):
                    self.new_screen = self.object
                    if self.new_screen.timer is not None:
                        self.new_screen.timer.switch_pause()


class InfoScreenType(SecondaryScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_text(self, args):
        # Filling text
        description_text = render_multiline_text(args['strings'],
                                                 args['size'], args['color'],
                                                 main_constants.FONT_PATH_INTER_LIGHT)
        main_text = render_multiline_text(['Пояснениe'],
                                          96, pygame.Color('black'),
                                          main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(main_text, ((main_constants.SCREEN_WIDTH - main_text.get_width()) // 2,
                              50))
        self.blit(description_text, ((main_constants.SCREEN_WIDTH - description_text.get_width()) // 2,
                                     200))
        self.backup = self.copy()


class VictoryScreenType(SecondaryScreenType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def init_design(self, difficult: str = 'EASY',
                    object: pygame.Surface = pygame.Surface(main_constants.SCREEN_SIZE)):
        super().init_design(difficult, object)
        # Creating save_result_button

    def set_text(self, args):
        # Filling constant text
        text = render_multiline_text(['Результат'], 70, pygame.Color('black'),
                                     main_constants.FONT_PATH_INTER_REGULAR)
        self.blit(text, ((main_constants.SCREEN_WIDTH - text.get_width()) // 2,
                         50))
        text = render_multiline_text(['Уровень:'], args['size'], args['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (100, 200))
        text = render_multiline_text(['Игра:'], args['size'], args['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (100, 320))
        text = render_multiline_text(['Рейтинг:'], args['size'], args['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (100, 440))
        text = render_multiline_text(['Время:'], args['size'], args['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (100, 560))
        # Filling text from args
        text = render_multiline_text([args['strings'][0]], args['size'], args['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (550, 200))
        text = render_multiline_text([args['strings'][1]], args['size'], args['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (550, 320))
        text = render_multiline_text([args['strings'][2]], args['size'], args['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (550, 440))
        text = render_multiline_text([args['strings'][3]], args['size'], args['color'],
                                     main_constants.FONT_PATH_INTER_LIGHT)
        self.blit(text, (550, 560))
        # Creating backup
        self.backup = self.copy()


class GameTimer:
    def __init__(self):
        self.time = time.time()
        self.pause = False
        self.back_time = 0

    def get_current_time(self):
        if self.pause:
            return round(self.back_time - self.time)
        return round(time.time() - self.time)

    def switch_pause(self):
        if self.pause:
            self.time = time.time() - self.get_current_time()
            self.pause = False
        else:
            self.pause = True
            self.back_time = time.time()

    def get_string_view(self):
        time = self.get_current_time()
        if time < 60:
            string = f'00:{str(time).rjust(2, "0")}'
        elif time >= 60 and time < 3600:
            string = f'{str(time // 60).rjust(2, "0")}:' \
                     f'{str(time % 60).rjust(2, "0")}'
        else:
            string = f'{str(time // 3600).rjust(2, "0")}' \
                     f'{str(time // 60).rjust(2, "0")}:' \
                     f'{str(time % 60).rjust(2, "0")}'
        return string

    def get_pygame_surface_view(self):
        string = self.get_string_view()
        indent = 10
        text_data = main_constants.TEXT_TIMER['main_text']
        text = render_multiline_text([string], text_data['size'],
                                     text_data['color'], main_constants.FONT_PATH_INTER_EXTRABOLD)
        image = load_image(main_constants.IMAGE_MAIN_SCREEN['timer_icon'])
        image = pygame.transform.smoothscale(image, (text.get_height(), text.get_height()))
        result = pygame.Surface((text.get_width() + image.get_width() + indent,
                                 text.get_height()),
                                pygame.SRCALPHA)
        result.blit(image, (0, 0))
        result.blit(text, (image.get_width() + indent, 2))
        return result


class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

    def set_image(self, path):
        self.image = load_image(path)
        self.rect = self.image.get_rect()

    def set_pygame_surface(self, surface):
        self.image = surface
        self.rect = self.image.get_rect()


class ButtonTextSpriteType1(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.set_background()
        self.set_velocity()

    def set_background(self,
                       color: pygame.Color = pygame.Color('black')):
        self.background_color = color

    def set_velocity(self, velocity: int = 30, acceleration: int = 1):
        self.velocity = acceleration
        self.max_velocity = velocity
        self.acceleration = acceleration

    def set_text(self, text: list or str = None, size: int = 40,
                 color: pygame.Color = pygame.Color('white'),
                 font: str = None):
        if type(text) == str:
            self.image = render_multiline_text([text], size,
                                               color, font)
        elif type(text) == list:
            self.image = render_multiline_text(text, size,
                                               color, font)
        if text is not None:
            self.rect = self.image.get_rect()
            self.text_surface = self.image
        else:
            terminate('no text was passed to the set_text() '
                      'method of the ButtonTextSpriteType1 class')

    def set_underline(self, distance: int = 5,
                      color: pygame.Color = pygame.Color('white'),
                      thickness: int = 5):
        self.thickness = thickness
        self.distance = distance
        self.line_color = color
        self.line_progress = 0
        self.create_pattern()
        self.rect = self.image.get_rect()

    def create_pattern(self):
        if self.text_surface is None:
            terminate('the text was not set in the '
                      'ButtonTexSpriteType1 class')
        self.image = pygame.Surface((self.text_surface.get_width(),
                                    self.text_surface.get_height() + self.distance + self.thickness))
        self.image.fill(self.background_color)
        self.image.blit(self.text_surface, (0, 0))
        self.image.fill(self.line_color,
                        [0, self.rect.height - self.thickness,
                         self.line_progress, self.rect.height])

    def update(self, *args):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.line_progress < self.rect.width:
                self.line_progress += self.velocity
            if self.velocity < self.max_velocity:
                self.velocity += self.acceleration
        else:
            if self.line_progress > 0:
                self.line_progress -= self.velocity
            if sum(list(range(1, self.max_velocity, self.acceleration))) >= self.line_progress:
                if self.velocity > 0:
                    self.velocity -= self.acceleration
        self.create_pattern()


class ButtonTextSpriteType2(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.set_background()
        self.is_clicked = False

    def set_background(self, color: pygame.Color = pygame.Color('white')):
        self.background = color
        value = 100
        self.changed_background = [color.r, color.g, color.b]
        for color_index in range(len(self.changed_background)):
            if self.changed_background[color_index] - value >= 0:
                self.changed_background[color_index] -= value
        self.changed_background = pygame.Color(*self.changed_background)


    def set_text(self, text: str, font_size: int = 15,
                 font: str = None, color: pygame.Color = pygame.Color('black'),
                 size: tuple = (100, 50)):
        self.size = size
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.text_color = color
        main_text = render_multiline_text([text], font_size, color, font)
        self.text_surface = pygame.Surface(size, pygame.SRCALPHA)
        self.text_surface.blit(main_text,
                               ((size[0] - main_text.get_width()) // 2,
                                (size[1] - main_text.get_height()) // 2))
        shadow = create_text_shadow([text], font_size,
                                    pygame.Color(main_constants.COLOR_SHADOW),
                                    font, self.background, 2, top=3)
        self.shadow = pygame.Surface(size)
        self.shadow.fill(self.background)
        self.shadow.blit(shadow,
                         ((size[0] - shadow.get_width()) // 2,
                          (size[1] - shadow.get_height()) // 2))
        self.image.blit(self.text_surface, (0, 0))
        self.rect = self.image.get_rect()

    def set_coords(self, x: int = 0, y: int = 0):
        self.rect.x, self.rect.y = x, y

    def set_field_coords(self, row: int, col: int):
        self.row, self.col = row, col

    def update(self, *args):
        event = args[0]
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event is not None:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.is_clicked:
                        self.is_clicked = False
                    else:
                        self.is_clicked = True
            if not self.is_clicked:
                self.image = self.shadow.copy()
                self.image.blit(self.text_surface, (0, 0))
                return
        if self.is_clicked:
            self.image = self.shadow.copy()
            self.image.blit(self.text_surface, (0, 0))
            pygame.draw.rect(self.image, self.text_color,
                             (0, 0, *self.size), width=2,
                             border_radius=10)
        else:
            self.image = pygame.Surface((self.text_surface.get_width(),
                                         self.text_surface.get_height()))
            self.image.fill(pygame.Color(self.background))
        self.image.blit(self.text_surface, (0, 0))


class ButtonTextSpriteType3(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.set_background()
        self.visible = True
        self.border_color = pygame.Color('black')
        self.border_size = 0

    def set_border(self, color: pygame.Color = pygame.Color('black'), size: int = 1):
        self.border_color = color
        self.border_size = size

    def set_background(self, color: pygame.Color = pygame.Color('white')):
        self.background = color

    def set_text(self, text: str, font_size: int = 15,
                 font: str = None, color: pygame.Color = pygame.Color('black'),
                 size: tuple = (100, 100)):
        self.size = size
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.fill(self.background)
        self.text_color = color
        text = render_multiline_text([text], font_size, color, font)
        self.image.blit(text, ((size[0] - text.get_width()) // 2,
                               (size[1] - text.get_height()) // 2))
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, self.border_color,
                         (0, 0, self.rect.width, self.rect.height), self.border_size)

    def set_coords(self, x: int = 0, y: int = 0):
        self.rect.x, self.rect.y = x, y

    def set_field_coords(self, row: int, col: int):
        self.row, self.col = row, col

    def switch_visibility(self):
        if self.visible == True:
            self.visible = False
            self.image = pygame.Surface(main_constants.SCREEN_SIZE,
                                        pygame.SRCALPHA)

    def update(self, *args):
        event = args[0]
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event is not None:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass


class ButtonTextSpriteType4(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.set_colors()
        self.pressure = False
        self.rect_flag = True

    def set_colors(self, background_color: pygame.Color = pygame.Color('white'),
                   btn_color: pygame.Color = pygame.Color('grey'),
                   hover_color: pygame.Color = pygame.Color('grey'),
                   changed_color: pygame.Color = pygame.Color('grey'),
                   outline_color: pygame.Color = pygame.Color('white')):
        self.background = background_color
        self.btn_color = btn_color
        self.hover_background = hover_color
        self.changed_background = changed_color
        self.outline_color = outline_color

    def set_text(self, text: str, font_size: int = 15,
                 font: str = None, color: pygame.Color = pygame.Color('black'),
                 size: tuple = (100, 100), border_size: int = 0, outline_width: int = 5):
        self.text = text
        self.font_size = font_size
        self.font = font
        self.text_color = color
        self.size = size
        self.border_size = border_size
        self.outline_width = outline_width

    def render_btn(self, background_color: pygame.Color, is_outline: bool = True):
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.image.fill(self.background)
        if self.rect_flag:
            self.rect_flag = False
            self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, background_color,
                         (0, 0, self.rect.width, self.rect.height),
                         border_radius=self.border_size)
        if is_outline:
            pygame.draw.rect(self.image, self.outline_color,
                             (0, 0, self.rect.width, self.rect.height),
                             self.outline_width, self.border_size)
        text = render_multiline_text([self.text], self.font_size, self.text_color, self.font)
        self.image.blit(text, ((self.size[0] - text.get_width()) // 2,
                               (self.size[1] - text.get_height()) // 2))

    def set_coords(self, x: int = 0, y: int = 0):
        self.rect.x, self.rect.y = x, y

    def switch_pressure(self):
        self.pressure = not self.pressure

    def is_pressed(self):
        return self.pressure

    def update(self, *args):
        event = args[0]
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event is not None:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.switch_pressure()
                    return
        if self.pressure == True:
            self.render_btn(self.changed_background)
            return
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event is None:
                self.render_btn(self.hover_background)
        if not self.rect.collidepoint(pygame.mouse.get_pos()):
            self.render_btn(self.btn_color)


class SoundButtonSpriteType(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.is_playable = False

    def set_data(self, sound_path: str, first_image_path: str,
                 second_image_path: str):
        self.sound_path = sound_path
        self.first_image = load_image(first_image_path)
        self.second_image = load_image(second_image_path)
        self.set_first_img()
        self.rect = self.image.get_rect()

    def update(self, *args):
        event = args[0]
        if event is not None:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.do_sound()
                    return
            if event.type == END_SOUND_EVENT:
                self.is_playable = False
                self.set_first_img()

    def set_first_img(self):
        self.image = self.first_image

    def set_second_img(self):
        self.image = self.second_image

    def do_sound(self):
        if self.is_playable:
            pygame.mixer.music.stop()
            self.set_first_img()
        else:
            pygame.mixer.music.set_endevent(END_SOUND_EVENT)
            pygame.mixer.music.load(self.sound_path)
            pygame.mixer.music.play(0)
            self.set_second_img()
        self.is_playable = not self.is_playable


class TextInputSprite(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.condition = None
        self.text = []
        self.set_text_length()
        self.set_null_time()
        self.set_data()
        self.set_line_data()
        self.rect = pygame.Rect(0, 0, 0, 0)

    def set_text_length(self, length: int = None):
        self.text_length = length

    def set_line_data(self, width: int = 5, color: pygame.Color = pygame.Color('black'),
                      time: float = 1, line_height: int = None):
        self.line_width = width
        self.line_color = color
        self.line_time = time
        if line_height is not None:
            self.line_height = line_height

    def set_data(self, font: str = None, font_size: int = 15,
                 color: pygame.Color = pygame.Color('black')):
        self.font = font
        self.font_size = font_size
        self.color = color
        text = render_multiline_text(['A'], font_size, color, font)
        self.line_height = text.get_height()

    def set_condition(self, condition: str):
        if condition is not None and (condition != 'isdigit' and condition != 'isalpha'):
            raise ValueError('condition must be "isdigit" or "isalpha"')
        self.condition = condition

    def set_null_time(self):
        self.time = time.time()

    def update(self, *args):
        super().update(*args)
        event = args[0]
        if event is not None:
            if event.type == pygame.KEYDOWN:
                if self.condition == 'isalpha':
                    data = {eval(f'pygame.K_{letter}'): letter
                            for letter in main_constants.EN_ALPHABET}
                elif self.condition == 'isdigit':
                    data = {eval(f'pygame.K_{num}'): str(num) for num in range(0, 10)}
                else:
                    data = {eval(f'pygame.K_{letter}'): letter
                            for letter in main_constants.EN_ALPHABET}
                    for num in range(0, 10):
                        data[eval(f'pygame.K_{num}')] = str(num)
                if self.condition is not None:
                    if event.key in data:
                        if len(self.text) != self.text_length:
                            self.set_null_time()
                            self.text.append(data[event.key])
                if event.key == pygame.K_BACKSPACE:
                    if self.text:
                        self.set_null_time()
                        del self.text[-1]
        if time.time() - self.time < self.line_time:
            self.render(line=True)
        elif (time.time() - self.time >= self.line_time and
              time.time() - self.time < self.line_time * 2):
            self.render(line=False)
        elif time.time() - self.time >= self.line_time * 2:
            self.set_null_time()

    def render(self, line: bool):
        text = render_multiline_text([''.join(self.text)], self.font_size,
                                     self.color, self.font)
        height = max([text.get_height(), self.line_height])
        result = pygame.Surface((text.get_width() + self.line_width,
                                 height), pygame.SRCALPHA)
        result.blit(text, (0, 0))
        if line:
            line = pygame.Surface((self.line_width, self.line_height))
            pygame.draw.rect(line, self.line_color, (0, 0, self.line_width, self.line_height),
                             border_radius=10)
            result.blit(line, (text.get_width(), 0))
        self.image = result
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def set_coords(self, coords: tuple):
        self.rect.x, self.rect.y = coords

    def get_text(self):
        return ''.join(self.text)
