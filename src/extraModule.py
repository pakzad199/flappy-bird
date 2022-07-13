import random
import pygame
import time
import config.configure as conf

def create_pipes(pipe_green_image, width):
    pipe_y = random.randrange(270, 630)
    pipe_top_rect = pipe_green_image.get_rect(midtop=(width, pipe_y))
    pipe_bottom_rect = pipe_green_image.get_rect(midbottom=(width, pipe_y - 150))
    return pipe_top_rect, pipe_bottom_rect


def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
        if pipe.centerx <= -19:
            pipes.pop(0)
    return pipes


def surface_pipe(pipes, switch, pipe_red_image, pipe_green_image, surface):
    if switch == 0:
        pipe_image = pipe_red_image
    else:
        pipe_image = pipe_green_image
    for pipe in pipes:
        if pipe.centery > 250:
            surface.blit(pipe_image, pipe)
        else:
            reversed_pipe = pygame.transform.flip(pipe_image, False, True)
            surface.blit(reversed_pipe, pipe)
            

def collision(pipes, bird_rect, hit_sound, game_over_sound, height):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            game_over_sound.play()
            time.sleep(3)
            return False
        elif bird_rect.centery > height - 100 or bird_rect.centery < -2:
            hit_sound.play()
            game_over_sound.play()
            time.sleep(3)
            return False
    return True


def make_flap(index, bird_list, bird_rect):
    new_bird = bird_list[index]
    new_bird_rect = new_bird.get_rect(center=(70, bird_rect.centery))
    return new_bird, new_bird_rect


def surface_score(status, font_score, surface, font, text1, text2, message_image, message_rect, score, high_score):
    if status:
        score_text = font_score.render(str(score), False, (255, 255, 255))
        score_text_rect = score_text.get_rect(center=(215, 80))
        surface.blit(score_text, score_text_rect)
    else:
        score_text = font_score.render(f'Last score: {score}', False, (255, 255, 255))
        score_text_rect = score_text.get_rect(center=(215, 80))
        surface.blit(score_text, score_text_rect)
        high_score_text = font_score.render(f'High Score: {high_score}', False, (255, 255, 255))
        high_score_text_rect = high_score_text.get_rect(center=(215, 670))
        surface.blit(high_score_text, high_score_text_rect)
        text1_s = font.render(text1, False, (0, 0, 0))
        text1_s_rect = text1_s.get_rect(center=(100, 600))
        surface.blit(text1_s, text1_s_rect)
        text2_s = font.render(text2, False, (0, 0, 0))
        text2_s_rect = text2_s.get_rect(center=(380, 600))
        surface.blit(text2_s, text2_s_rect)
        surface.blit(message_image, message_rect)


def update_score(pipe_list, point_sound):
    # global score, high_score, switch_score
    if pipe_list:
        for pipe in pipe_list:
            if 55 <= pipe.centerx <= 85 and conf.switch_score:
                conf.score += 1
                point_sound.play()
                conf.switch_score = False
            elif pipe.centerx < 0:
                conf.switch_score = True
    if conf.high_score < conf.score:
        conf.high_score = conf.score


def switch_pipe():
    return random.randint(0, 3)
