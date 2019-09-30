import pygame
import time
import random
import sys

import pygame.mixer

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)

sprite_width = 60
sprite_height = 120

gameDisplay = pygame.display.set_mode((display_width, display_height))  # Creates a window
pygame.display.set_caption("Rock Fall")
gameIcon = pygame.image.load('assets/rock1.png')
pygame.display.set_icon(gameIcon)

clock = pygame.time.Clock()

bg = pygame.image.load('assets/wall.jpg')

spriteImg = pygame.image.load('assets/worker.png')

rockImg = pygame.image.load('assets/rock1.png')

rockImg2 = pygame.image.load('assets/rock2.png')

rockImg3 = pygame.image.load('assets/rock3.png')

crash_sound = pygame.mixer.Sound("assets/rocksound.wav")

def rock(x, y):
    gameDisplay.blit(rockImg, (x, y))


def rock2(x, y):
    gameDisplay.blit(rockImg2, (x, y))


def rock3(x, y):
    gameDisplay.blit(rockImg3, (x, y))


def sprite(x, y):
    gameDisplay.blit(spriteImg, (x, y))


def text_objects(text, font, color):
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 90)
    textsurf, textrect = text_objects(text, largetext, black)
    textrect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textsurf, textrect)

    pygame.display.update()
    pygame.event.get()
    time.sleep(1)


def god_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 70)
    textsurf, textrect = text_objects(text, largetext, bright_red)
    textrect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textsurf, textrect)

    pygame.display.update()
    pygame.event.get()
    time.sleep(1)


def score_display(score):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, (0, 0))


def final_score(score):
    pygame.draw.rect(gameDisplay, white, (40, 200, 720, 250))

    smalltext = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects("Score: " + str(score), smalltext, red)
    TextRect.center = ((display_width / 2), (display_height / 2 + 115))
    gameDisplay.blit(TextSurf, TextRect)


def get_high_score():
    high_score = 0

    # try to read the hs from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        # no hs
        print("No high score")
    except ValueError:
        # theres a file, but cant understand
        print("ValueError")

    return high_score


def save_high_score(new_high_score):
    try:
        # writes file to disk
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        print("Unable to save file")


def new_high_score(score, high_score):
    if score > high_score:
        print("New High score!")

        smltext = pygame.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects("New High Score!", smltext, red)
        TextRect.center = ((display_width / 2), (display_height / 2 + 70))
        gameDisplay.blit(TextSurf, TextRect)

        save_high_score(score)
        pygame.display.update()


def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    message_display("You Fell Off")

    time.sleep(2)
    menu()


def crash_rock():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    message_display("You Hit A Rock")

    time.sleep(2)
    menu()


def reset_button(msg, x, y, w, h, ic, ac, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = text_objects(msg, smallText, ac)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(textSurf, textRect)

        if click[0] == 1:
            action(0)
            menu()

    else:
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = text_objects(msg, smallText, ic)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()


def button(msg, x, y, w, h, ic, ac, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def menu():
    high_score = get_high_score()

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bg, (0, 0))

        pygame.draw.rect(gameDisplay, white, (100, 200, 600, 250))

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Rock Fall", largetext, black)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.draw.rect(gameDisplay, white, (0, 0, 250, 40))

        font = pygame.font.SysFont(None, 50)
        text = font.render("High Score:" + str(high_score), True, red)
        gameDisplay.blit(text, (0, 0))

        button("GO!", 200, 375, 100, 50, green, bright_green, game_loop)
        button("Quit", 500, 375, 100, 50, red, bright_red, quitgame)
        reset_button("Reset Score", 700, 550, 100, 50, black, white, save_high_score)

        pygame.display.update()
        clock.tick(15)


# main game loops

def god(): # Mode where spite can mover vertically too...bugs
    god_display("God Mode Activated")

    x = (display_width * 0.42)
    y = (display_height * 0.8)

    rock_size = 100
    rock_startx = random.randrange(0, display_width - rock_size)
    rock_starty = -300

    rock2_starty = random.randrange(0, display_height)
    rock2_startx = -300
    rock_speed = 11
    rock_speed2 = 21

    score = 0

    x_change = 0
    y_change = 0

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Moves sprite
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -20
                elif event.key == pygame.K_RIGHT:
                    x_change = 20
                elif event.key == pygame.K_UP:
                    y_change = -20
                elif event.key == pygame.K_DOWN:
                    y_change = 20

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
            # End of move logic

        gameDisplay.blit(bg, (0, 0))
        score_display(score)

        # Moves sprite
        x += x_change
        sprite(x, y)

        y += y_change
        sprite(x, y)

        # Calls in rock and moves it
        rock(rock_startx, rock_starty)
        rock_starty += rock_speed
        rock2(rock2_startx, rock2_starty)
        rock2_startx += rock_speed2

        # logic if sprite crosses left and right border
        if x > display_width - sprite_width or x < 0:
            crash()

        # logic that resets rock
        if rock_starty > display_height:
            rock_starty = 0 - rock_size
            rock_startx = random.randrange(0, display_width - rock_size)
            score += 1

        if rock2_startx > display_width:
            rock2_startx = 0 - rock_size
            rock2_starty = random.randrange(0, display_height - rock_size)
            score += 1

        # logic that sees if sprite crosses rock
        if y < rock_starty + rock_size - 20 and rock_starty < 500 or y + sprite_height > rock_starty and y + sprite_height < rock_starty + rock_size:
                print('y1 crossover')

                if x > rock_startx and x < rock_startx + rock_size or rock_startx < x + sprite_width < rock_startx + rock_size:
                    print('x1 crossover')
                    final_score(score)
                    crash_rock()

        if y < rock2_starty + rock_size - 10 and rock2_starty < 500 or y + sprite_height > rock2_starty and y + sprite_height < rock2_starty + rock_size:
                print('y2 crossover')

                if x > rock2_startx and x < rock2_startx + rock_size or x + sprite_width > rock2_startx and x + sprite_width < rock2_startx + rock_size:
                    print('x2 crossover')
                    final_score(score)
                    crash_rock()

        pygame.display.update()
        clock.tick(65)


def game_loop():  #main game
    pygame.mixer.music.load("assets/soundtrack1.wav")
    pygame.mixer.music.play(-1)

    x = (display_width * 0.42)
    y = (display_height * 0.8)

    rock_startx = random.randrange(0, display_width)
    rock_starty = -300
    rock2_startx = random.randrange(0, display_width)
    rock2_starty = -300
    rock_speed = 11
    rock_speed2 = 21
    rock3_startx = random.randrange(0, display_width)
    rock3_starty = -300
    rock_speed3 = random.randrange(10, 25)
    rock_size = 100

    high_score = get_high_score()
    score = 0

    x_change = 0

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Moves sprite
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -20
                elif event.key == pygame.K_RIGHT:
                    x_change = 20

                # God
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o:
                        god()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            # End of move logic

        gameDisplay.blit(bg, (0, 0))
        score_display(score)

        # Moves sprite
        x += x_change
        sprite(x, y)

        # Calls in rock and moves it
        rock(rock_startx, rock_starty)
        rock_starty += rock_speed
        rock2(rock2_startx, rock2_starty)
        rock2_starty += rock_speed2

        if score > 10:
            rock3(rock3_startx, rock3_starty)
            rock3_starty += rock_speed3

        # logic if sprite crosses left and right border
        if x > display_width - sprite_width or x < 0:
            final_score(score)
            new_high_score(score, high_score)
            crash()

        # logic that resets rock
        if rock_starty > display_height:
            rock_starty = 0 - rock_size
            rock_startx = random.randint(0, display_width - rock_size)
            score += 1

        if rock2_starty > display_height:
            rock2_starty = 0 - rock_size
            rock2_startx = random.randrange(0, display_width - rock_size)
            score += 1

        if rock3_starty > display_height:
            rock3_starty = 0 - rock_size
            rock3_startx = random.randrange(0, display_height - rock_size)
            score += 1

        # logic that sees if sprite crosses rock
        if y < rock_starty + rock_size - 20 and rock_starty < 500:
            print('y crossover')

            if x > rock_startx and x < rock_startx + rock_size or x + sprite_width > rock_startx and x + sprite_width < rock_startx + rock_size:
                print('x crossover')
                final_score(score)
                new_high_score(score, high_score)
                crash_rock()

        if y < rock2_starty + rock_size - 20 and rock2_starty < 500:
            print('y2 crossover')

            if x > rock2_startx and x < rock2_startx + rock_size or x + sprite_width > rock2_startx and x + sprite_width < rock2_startx + rock_size:
                print('x2 crossover')
                final_score(score)
                new_high_score(score, high_score)
                crash_rock()

        if y < rock3_starty + rock_size - 20 and rock3_starty < 500:
            print('y2 crossover')

            if x > rock3_startx and x < rock3_startx + rock_size or x + sprite_width > rock3_startx and x + sprite_width < rock3_startx + rock_size:
                print('x2 crossover')
                final_score(score)
                new_high_score(score, high_score)
                crash_rock()

        pygame.display.update()
        clock.tick(60)


def quitgame():
    pygame.quit()
    quit()

menu()
game_loop()
pygame.quit()
sys.exit()


# cd documents/programming/python/avoidergame
