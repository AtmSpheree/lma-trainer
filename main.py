# -*- coding: utf-8 -*-

import pygame
import main_objects
import main_constants
import screens.start_screen


def main():
    screen = pygame.display.set_mode(main_constants.SCREEN_SIZE)
    pygame.display.set_caption('LMA-trainer')
    pygame.display.set_icon(main_objects.load_image('favicon.png'))
    changing_screen = screens.start_screen.StartScreen(main_constants.SCREEN_SIZE)
    running = True
    clock = pygame.time.Clock()
    while running:
        saved_event = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type in [pygame.MOUSEBUTTONDOWN]:
                saved_event = event
        changing_screen.try_to_change_screen(saved_event)
        if changing_screen.get_new_screen() is not None:
            changing_screen = changing_screen.get_new_screen()
            changing_screen.clear_new_screen()
        changing_screen.update_sprites(saved_event)
        changing_screen.draw_sprites()
        screen.blit(changing_screen, (0, 0))
        pygame.display.flip()
        clock.tick(main_constants.FPS)


if __name__ == '__main__':
    pygame.init()
    main()
