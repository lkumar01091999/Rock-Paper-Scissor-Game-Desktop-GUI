import sys
import pygame
from pygame.locals import *
import random

# Global variables
FPS = 32
SCREENWIDTH = 852
SCREENHEIGHT = 480
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GAME_SPRITES = {}
GAME_OVER = False
# positions for images
welcome_x = 0
welcome_y = 0
h_position = 196
v_position = 95
# RGB Values for colors
red = (175, 0, 0)
bright_red = (255, 0, 0)
green = (0, 175, 0)
bright_green = (0, 255, 0)
brown = (153, 0, 0)
orange = (255, 85, 0)
bright_orange = (255, 150, 0)
cyan = (0, 153, 170)
# no. of trials
count = 0
# scores
computer_score = 0
your_score = 0
# lists
random_index = random.randint(0, 2)

Game_parameters = ['rock', 'paper', 'scissor']


def welcome_screen():
    pygame.mixer_music.load(r'Music\welcome_screen_audio.ogg')
    pygame.mixer_music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_F5):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.mixer_music.stop()
                return
            else:
                SCREEN.blit(welcome_IMG, (welcome_x, welcome_y))
                pygame.display.update()
                FPS_CLK.tick(FPS)


def text_objects(text, font):
    white = (255, 255, 255)
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()

# x, y are positions | w--> width, h--> height | ic --> inactive color , ac --> active color | text like 'START'


def button_or_text(text, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(SCREEN, ac, (x, y, w, h))
    else:
        pygame.draw.rect(SCREEN, ic, (x, y, w, h))
    start_text_font = pygame.font.Font('freesansbold.ttf', 22)
    text_surface, text_rect = text_objects(text, start_text_font)
    text_rect.center = ((x + (w // 2)), (y + (h // 2)))
    SCREEN.blit(text_surface, text_rect)


def restart():
    main_game_sound.stop()
    welcome_screen()
    main_game_sound.play(-1)
    pre_start_screen()


def rock():
    global computer_score, your_score
    x = random.randint(0, 8)
    if computer_img[x] == GAME_SPRITES['computer_rock']:
        pygame.mixer_music.load(r'Music\oh_no.mp3')
        pygame.mixer_music.play(1)
    
    elif computer_img[x] == GAME_SPRITES['computer_paper']:
        pygame.mixer_music.load(r'Music\oops.wav')
        pygame.mixer_music.play(1)
        computer_score += 10

    elif computer_img[x] == GAME_SPRITES['computer_scissor']:
        pygame.mixer_music.load(r'Music\winner.mp3')
        pygame.mixer_music.play(1)
        your_score += 10
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 718 <= pygame.mouse.get_pos()[0] <= 718 + 120 and 165 <= pygame.mouse.get_pos()[1] <= 165 + 50:
                    pygame.mixer_music.stop()
                    return
        SCREEN.blit(GAME_SPRITES['your_rock'], (h_position+240, v_position))
        SCREEN.blit(computer_img[x], (h_position, v_position))

        pygame.display.update()
        FPS_CLK.tick(FPS)


def paper():
    global computer_score, your_score
    x = random.randint(0, 8)
    if computer_img[x] == GAME_SPRITES['computer_paper']:
        pygame.mixer_music.load(r'Music\oh_no.mp3')
        pygame.mixer_music.play(1)
       
    elif computer_img[x] == GAME_SPRITES['computer_scissor']:
        pygame.mixer_music.load(r'Music\oops.wav')
        pygame.mixer_music.play(1)
        computer_score += 10
    elif computer_img[x] == GAME_SPRITES['computer_rock']:
        pygame.mixer_music.load(r'Music\winner.mp3')
        pygame.mixer_music.play(1)
        your_score += 10
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 718 <= pygame.mouse.get_pos()[0] <= 718 + 120 and 225 <= pygame.mouse.get_pos()[1] <= 225 + 50:
                    pygame.mixer_music.stop()
                    return
        SCREEN.blit(GAME_SPRITES['your_paper'], (h_position+240, v_position))
        SCREEN.blit(computer_img[x], (h_position, v_position))

        pygame.display.update()
        FPS_CLK.tick(FPS)


def scissor():
    global computer_score, your_score
    x = random.randint(0, 8)
    if computer_img[x] == GAME_SPRITES['computer_scissor']:
        pygame.mixer_music.load(r'Music\oh_no.mp3')
        pygame.mixer_music.play(1)
    elif computer_img[x] == GAME_SPRITES['computer_rock']:
        pygame.mixer_music.load(r'Music\oops.wav')
        pygame.mixer_music.play(1)
        computer_score += 10
    elif computer_img[x] == GAME_SPRITES['computer_paper']:
        pygame.mixer_music.load(r'Music\winner.mp3')
        pygame.mixer_music.play(1)
        your_score += 10
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 718 <= pygame.mouse.get_pos()[0] <= 718 + 120 and 285 <= pygame.mouse.get_pos()[1] <= 285 + 50:
                    pygame.mixer_music.stop()
                    return
        SCREEN.blit(GAME_SPRITES['your_scissor'], (h_position+240, v_position))
        SCREEN.blit(computer_img[x], (h_position, v_position))

        pygame.display.update()
        FPS_CLK.tick(FPS)


def get_high_score():  # For getting high score
    try:
        with open(r'Text file\high_score.txt', 'r') as rf:
            high_score = int(rf.read())
    except IOError:
        return 0
    return high_score


def save_high_score(new_high_score): # For saving high score
    try:
        with open(r'Text file\high_score.txt', 'w') as wf:
            wf.write(str(new_high_score))
    except IOError:
        return 0


def print_high_score():
    previous_score = get_high_score()
    if count == 10:
        current_score = your_score
        if current_score > previous_score:
            save_high_score(current_score)
    return get_high_score()


def end_game():
    global count, your_score, computer_score
    pygame.mixer_music.load(r'Music\game_over.mp3')
    pygame.mixer_music.play(1)
    display = 0
    if your_score > computer_score:
        winner_sound.play(-1)
    elif computer_score == your_score:
        tied_sound.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_F6):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    if 718 <= pygame.mouse.get_pos()[0] <= 718 + 120 and 165 <= pygame.mouse.get_pos()[1] <= 165 + 50:
                        pygame.quit()
                        sys.exit()
                    elif 718 <= pygame.mouse.get_pos()[0] <= 718 + 120 and 225 <= pygame.mouse.get_pos()[1] <= 225 + 50:
                        count = 0
                        your_score = 0
                        computer_score = 0
                        winner_sound.stop()
                        tied_sound.stop()
                        restart()

        SCREEN.blit(game_back_SCREEN, (welcome_x, welcome_y))
        # -------------------text -------------------------------------------
        button_or_text('YOUR SCORE', 10, 420, 180, 50, cyan, cyan)
        button_or_text('COMPUTER SCORE', 6, 6, 250, 30, bright_red, bright_red)
        button_or_text('HI$$SCORE', 620, 420, 135, 50, cyan, cyan)
        button_or_text('GAME OVER!!', 300, 100, 250, 100, bright_red, bright_red)

        if computer_score > your_score:
            button_or_text('COMPUTER WON', 318, 220, 218, 30, bright_red, bright_red)
            display += 1
            if 50 < display < 100:
                button_or_text('COMPUTER WON', 300, 220, 250, 40, bright_red, bright_red)
                display += 1
                if display == 100:
                    display = 0
        if computer_score < your_score:
            button_or_text('YOU WON', 318, 220, 218, 30, green, green)
            display += 1
            if 50 < display < 100:
                button_or_text('YOU WON', 300, 220, 250, 40, green, green)
                display += 1
                if display == 100:
                    display = 0

        if computer_score == your_score:
            button_or_text('Ooh! it\'s TIED ', 318, 220, 218, 30, bright_red, bright_red)
            display += 1
            if 50 < display < 100:
                button_or_text('Ooh! it\'s TIED ', 300, 220, 250, 40, bright_green, bright_green)
                display += 1
                if display == 100:
                    display = 0

        button_or_text(str(your_score), 200, 420, 60, 50, cyan, cyan)
        button_or_text(str(computer_score), 266, 6, 60, 30, bright_red, bright_red)
        button_or_text(str(print_high_score()), 765, 420, 20, 50, cyan, cyan)
        if print_high_score() >= 10:
            button_or_text(str(print_high_score()), 765, 420, 60, 50, cyan, cyan)
            button_or_text(f'$$ RPS $$ YOUR HIGHSCORE : {str(print_high_score())}', 210, 270, 450, 40, green, green)
            display += 1
            if 50 < display < 100:
                button_or_text(f'$$$$ RPS $$$$ YOUR HIGHSCORE : {str(print_high_score())}', 210, 270, 450, 40,
                               bright_green, bright_green)
                display += 1
                if display == 100:
                    display = 0

        # -------------------BUTTONS-------------------------------------------
        button_or_text('EXIT', 718, 165, 120, 50, orange, bright_orange)
        button_or_text('RESTART', 718, 225, 120, 50, green, bright_green)

        pygame.display.update()
        FPS_CLK.tick(FPS)


def start_screen():
    global count, your_score, computer_score
    while not GAME_OVER:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_F6):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    if 718 <= pygame.mouse.get_pos()[0] <= 718 + 120 and 95 <= pygame.mouse.get_pos()[1] <= 95 + 50:
                        count = 0
                        your_score = 0
                        computer_score = 0
                        restart()
                        return
                    elif 718 <= pygame.mouse.get_pos()[0] <= 718 + 120 and 165 <= pygame.mouse.get_pos()[1] <= 165 + 50:
                        rock()
                        count += 1

                    elif 718 <= pygame.mouse.get_pos()[0] <= 718 + 120 and 225 <= pygame.mouse.get_pos()[1] <= 225 + 50:
                        paper()
                        count += 1

                    elif 718 <= pygame.mouse.get_pos()[0] <= 718 + 120 and 285 <= pygame.mouse.get_pos()[1] <= 285 + 50:
                        scissor()
                        count += 1

                    elif 718 <= pygame.mouse.get_pos()[0] <= 718 + 120 and 42 <= pygame.mouse.get_pos()[1] <= 42 + 50:
                        pygame.quit()
                        sys.exit()
        # ------------------Images---------------------------------------
        SCREEN.blit(game_back_SCREEN, (welcome_x, welcome_y))
        SCREEN.blit(computer_player, (h_position, v_position))
        SCREEN.blit(you_player, (h_position+240, v_position))
        # -------------------text-----------------------------------------
        button_or_text('COMPUTER', 235, 300, 140, 30, brown, brown)
        button_or_text('YOU', 520, 300, 60, 30, brown, brown)
        button_or_text('YOUR SCORE', 10, 420, 180, 50, cyan, cyan)
        button_or_text('HI$$SCORE', 620, 420, 135, 50, cyan, cyan)
        button_or_text('COMPUTER SCORE', 6, 6, 250, 30, bright_red, bright_red)
        button_or_text(str(your_score), 200, 420, 20, 50, cyan, cyan)
        button_or_text(str(computer_score), 266, 6, 20, 30, bright_red, bright_red)
        button_or_text(str(print_high_score()), 765, 420, 20, 50, cyan, cyan)
        if print_high_score() >= 10:
            button_or_text(str(print_high_score()), 765, 420, 60, 50, cyan, cyan)
        if your_score >= 10:
            button_or_text(str(your_score), 200, 420, 60, 50, cyan, cyan)
        if computer_score >= 10:
            button_or_text(str(computer_score), 266, 6, 60, 30, bright_red, bright_red)
        # -------------BUTTONS---------------------------------------------
        # EXIT
        button_or_text('EXIT', 718, 42, 120, 50, orange, bright_orange)
        # Restart button
        button_or_text('RESTART', 718, 95, 120, 50, green, bright_green)
        # Rock button
        button_or_text('ROCK', 718, 165, 120, 50, red, bright_red)
        # Paper button
        button_or_text('PAPER', 718, 225, 120, 50, red, bright_red)
        # Scissor button
        button_or_text('SCISSOR', 718, 285, 120, 50, red, bright_red)
        if count == 10:
            end_game()
            return
        pygame.display.update()
        FPS_CLK.tick(FPS)


def pre_start_screen():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_F6):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (190, 380) <= pygame.mouse.get_pos() <= (190 + 100, 380 + 50):
                    start_screen()
                    return
        SCREEN.blit(game_back_SCREEN, (welcome_x, welcome_y))
        SCREEN.blit(computer_player, (h_position, v_position))
        SCREEN.blit(you_player, (h_position+240, v_position))
        # start button
        button_or_text('START', 190, 380, 100, 50, red, bright_red)
        pygame.display.update()
        FPS_CLK.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    FPS_CLK = pygame.time.Clock()
    pygame.display.set_caption('ROCK PAPER SCISSOR GAME WINDOW')

    # GAME SPRITES
    GAME_SPRITES['computer_rock'] = pygame.image.load(r'Images\computer_stone.png').convert_alpha()
    GAME_SPRITES['computer_paper'] = pygame.image.load(r'Images\computer_paper.png').convert_alpha()
    GAME_SPRITES['computer_scissor'] = pygame.image.load(r'Images\computer_scissor.png').convert_alpha()
    GAME_SPRITES['your_rock'] = pygame.image.load(r'Images\your_stone.png').convert_alpha()
    GAME_SPRITES['your_paper'] = pygame.image.load(r'Images\your_paper.png').convert_alpha()
    GAME_SPRITES['your_scissor'] = pygame.image.load(r'Images\your_scissor.png').convert_alpha()

    computer_img = [GAME_SPRITES['computer_rock'], GAME_SPRITES['computer_paper'], GAME_SPRITES['computer_scissor']
                    , GAME_SPRITES['computer_rock'], GAME_SPRITES['computer_paper'], GAME_SPRITES['computer_scissor']
                    , GAME_SPRITES['computer_rock'], GAME_SPRITES['computer_paper'], GAME_SPRITES['computer_scissor']]

    # welcome image, Game back screen and icon image
    welcome_IMG = pygame.image.load(r'Images\Rock_ppr_scissor_intro.png').convert_alpha()
    game_ICON = pygame.image.load(r'game_icon.ico').convert_alpha()
    game_back_SCREEN = pygame.image.load(r'Images\game_back_screen.jpg').convert_alpha()
    computer_player = pygame.image.load(r'Images\computer_player.png').convert_alpha()
    you_player = pygame.image.load(r'Images\you_player.png').convert_alpha()
    # Lets blit our icon
    pygame.display.set_icon(game_ICON)

    # Two sounds for end game function
    winner_sound = pygame.mixer.Sound(r'Music\winner.wav')
    tied_sound = pygame.mixer.Sound(r'Music\oops.wav')
# Function calls
    welcome_screen()
    # GAME Music play
    main_game_sound = pygame.mixer.Sound(r'Music\main_game_audio.ogg')
    main_game_sound.play(-1)
    pre_start_screen()