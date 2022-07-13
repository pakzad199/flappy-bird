import pygame
import sys
from config.configure import *
from src.extraModule import *
import config.configure as conf

globalInitConfigure()

create_pipe = pygame.USEREVENT
pygame.time.set_timer(create_pipe, 1300)
flap_bird = pygame.USEREVENT + 1
pygame.time.set_timer(flap_bird, 70)

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_status:
                movement = 0
                movement -= 4
            elif event.key == pygame.K_r and not game_status:
                movement = 0
                pipe_list.clear()
                bird_rect = bird_image.get_rect(center=(70, 360))
                score = 0
                game_status = True
        elif event.type == create_pipe:
            pipe_list.extend(create_pipes(pipe_green_image, width))
            pipe_color = switch_pipe()
        elif event.type == flap_bird:
            if index_bird < 2:
                index_bird += 1
            else:
                index_bird = 0
            bird_image, bird_rect = make_flap(index_bird, bird_list, bird_rect)
    movement += gravity
    bird_rect.centery += movement
    f1_x -= floor_speed
    f2_x -= floor_speed
    if f1_x <= -width:
        f1_x = width
    elif f2_x <= -width:
        f2_x = width
    surface.blit(bg_image, (0, 0))
    if game_status:
        pipe_list = move_pipe(pipe_list)
        surface_pipe(pipe_list, pipe_color, pipe_red_image, pipe_green_image, surface)
        surface.blit(bird_image, bird_rect)
        game_status = collision(pipe_list, bird_rect, hit_sound, game_over_sound, height)
        update_score(pipe_list, point_sound)
        surface_score(True, font_score, surface, font, text1, text2, message_image, message_rect, conf.score, conf.high_score)
    else:
        surface_score(False, font_score, surface, font, text1, text2, message_image, message_rect, conf.score, conf.high_score)
        pipe_list.clear()
    surface.blit(floor_image, (f1_x, height - 100))
    surface.blit(floor_image, (f2_x, height - 100))
    pygame.display.update()
    clock.tick(fps)
