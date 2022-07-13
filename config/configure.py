import pygame


pygame.init()

def globalInitConfigure():
    global score, high_score, switch_score
    score = 0
    high_score = 0
    switch_score = True


width, height = 460, 820
fps = 90
bg_image = pygame.image.load('./assets/image/bg2.png')
bg_image = pygame.transform.scale(bg_image, (width, height))
floor_image = pygame.image.load('./assets/image/floor.png')
floor_image = pygame.transform.scale(floor_image, (width, 100))
f1_x = 0
f2_x = width
floor_speed = 2
bird_up_image = pygame.image.load('./assets/image/bird_up.png')
bird_mid_image = pygame.image.load('./assets/image/red_bird_mid_flap.png')
bird_down_image = pygame.image.load('./assets/image/red_bird_down_flap.png')
bird_list = [bird_up_image, bird_mid_image, bird_down_image]
index_bird = 0
bird_image = bird_list[index_bird]
bird_rect = bird_image.get_rect(center=(70, 360))
gravity = 0.1
movement = 0
pipe_green_image = pygame.image.load('./assets/image/pipe_green.png')
pipe_green_image = pygame.transform.scale(pipe_green_image, (70, 500))
pipe_red_image = pygame.image.load('./assets/image/pipe_red.png')
pipe_red_image = pygame.transform.scale(pipe_red_image, (70, 500))
pipe_list = []
game_status = False
font_score = pygame.font.Font('./assets/font/Flappy.TTF', 40)
game_over_sound = pygame.mixer.Sound('./assets/music/smb_mariodie.wav')
point_sound = pygame.mixer.Sound('./assets/music/point.mp3')
hit_sound = pygame.mixer.Sound('./assets/music/hit.mp3')
pipe_color = 0
text1 = 'SPACE => FLAP'
text2 = 'R => reset'.upper()
font = pygame.font.Font("./assets/font/BoldItalic.ttf", 20)
message_image = pygame.image.load('./assets/image/message.png')
message_image = pygame.transform.scale(message_image, (280, 400))
message_rect = message_image.get_rect(center=(230, 360))

