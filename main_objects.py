# -*- coding: utf-8 -*-

import pygame
import sys
import main_constants


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


def pil_image_to_surface(pil_image):
    return pygame.image.fromstring(
        pil_image.tobytes(), pil_image.size, pil_image.mode).convert()


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


class MainScreenType(pygame.Surface):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_sprites = pygame.sprite.Group()
        self.back_button_sprite = None
        self.exit_button_sprite = None
        self.new_screen = None

    def init_introduction_design(self):
        color = pygame.Color(main_constants.COLOR_INTRODUCTION_DESIGN)
        self.fill(color)
        self.work_color = color

    def init_game_design(self):
        color = pygame.Color(main_constants.COLOR_GAME_DESIGN)
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

    def try_to_change_screen(self, event: pygame.event.Event = None):
        mouse_pos = pygame.mouse.get_pos()
        if self.exit_button_sprite is not None:
            if self.exit_button_sprite.rect.collidepoint(mouse_pos):
                if event is not None:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        terminate()

    def get_new_screen(self):
        return self.new_screen

    def create_back_button(self):
        self.create_back_button_sprite()

    def create_exit_button(self):
        self.create_exit_button_sprite()

    def draw_sprites(self):
        self.all_sprites.draw(self)

    def update_sprites(self, event: pygame.event.Event = None):
        self.all_sprites.update(event)


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


if __name__ == '__main__':
    pygame.init()
