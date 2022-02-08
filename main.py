import sys

import pygame
import os
import random
from bird import *
from obstacle import *
from points import *

def main():
    pygame.init()

    W, H = 1000, 600

    # Images and Sounds
    icon = pygame.image.load(os.path.join('Files/Photos', 'icon.png'))
    bg = pygame.transform.scale(pygame.image.load(os.path.join('Files/Photos', 'bg.png')), (W, H))
    gameOver = pygame.transform.scale(pygame.image.load(os.path.join('Files/Photos', 'gameOver.png')), (800, 500))
    getReady = pygame.image.load(os.path.join('Files/Photos', 'getReady.png'))

    wind = pygame.mixer.music.load(os.path.join('Files/Sounds', 'wind.wav'))
    pygame.mixer.music.play(-1)

    die = pygame.mixer.Sound(os.path.join('Files/Sounds', 'die.wav'))
    hit = pygame.mixer.Sound(os.path.join('Files/Sounds', 'hit.wav'))
    points_inc = pygame.mixer.Sound(os.path.join('Files/Sounds', 'point.wav'))  # succesffully passed a pipe
    swoosh = pygame.mixer.Sound(os.path.join('Files/Sounds', 'swooshing.wav'))  # for speed increment
    wing_flap = pygame.mixer.Sound(os.path.join('Files/Sounds', 'wing_flap.wav'))

    # Create Screen
    pygame.display.set_caption('Flappy Bird')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((W, H))
    screen.fill((255, 255, 255))
    pygame.display.update()

    # creating player
    bird = Bird(screen)
    bird_mask = bird.mask

    # Fonts
    f = pygame.font.SysFont('arial', 30)
    f1 = pygame.font.SysFont('arial', 40)

    play_again = True
    while (play_again):
        main_window = True

        txt = f.render("Press space to start", True, (0, 0, 255))
        while main_window:
            screen.blit(bg, (0, 0))
            screen.blit(getReady, (400, 200))
            screen.blit(txt, (400, 300))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    main_window = False

        play_again = False
        bird.x = 200
        bird.y = 300
        FPS = 60
        lives = 3
        jump = False
        jumptime = 0
        pipe_gentime = 0
        clock = pygame.time.Clock()
        pipe = []
        speed = 3
        maxspeed = 4
        collisions = 0
        point = 0
        land = []
        land.append(ground(screen))
        last_land = 0
        show_point = points_img(screen)
        show_life = life(screen)
        decide = decision(screen)

        # to genrate up or down pipe
        def gen_pipe():
            x = 1000
            y = random.randint(0, 100)
            choice = random.randint(0, 1)
            if choice == 0:
                pipe.append(pipe_up(screen, x, -1 * y))
            else:
                pipe.append(pipe_down(screen, x, 300 + y))

        def gen_land():
            if land[last_land].x < -40:
                land.append(ground(screen, land[last_land].x + 1049))
            for a in land[:]:
                if a.x < -1060:
                    land.remove(a)
            pass

        ###########################  loop  ###########################################################################
        running = True
        while (running):
            clock.tick(FPS)
            screen.blit(bg, (0, 0))
            show_point.show_point(point)
            show_life.show_life(lives)
            running = decide.check_status(lives, point)
            ########## To make bird jump or fall##################

            if jump:
                if jumptime < 20 and bird.y > 0:
                    bird.jump()
                    jumptime += 1

                else:
                    jumptime = 0
                    jump = False
            else:
                if bird.y < H - 80:
                    bird.move()
                else:
                    lives = 0

            ######### pipe Genration ################################

            if pipe_gentime > FPS * 3 / 4:
                gen_pipe()
                pipe_gentime = 0
            else:
                pipe_gentime += 1

            ###############move Pipes###########################

            for a in pipe[:]:
                if a.x > -20:
                    a.move(speed)
                    if a.x < bird.x + a.width + 10:
                        offset = ((a.x - bird.x), (a.y - bird.y))
                        if bird.mask.overlap(a.mask, offset) and (not a.collision_happened):
                            a.collision_happened = True
                            collisions += 1
                            lives -= 1
                    if a.x < bird.x and (not a.passed) and (not a.collision_happened):
                        a.passed = True
                        point += 1
                        points_inc.play()

                else:
                    pipe.remove(a)

            ###############################land###################################
            gen_land()
            for a in land:
                a.move(speed)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jump = True
                        jumptime = 0
                        wing_flap.play()

                key = pygame.key.get_pressed()
                if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
                    speed = maxspeed
                    swoosh.play()
                else:
                    speed = 3

            pygame.display.update()

        run = True
        while (run):
            screen.blit(gameOver, (100, 50))

            pygame.draw.rect(screen, (255, 255, 200), (200, 200, 600, 200))
            text = f.render('Score :', True, (255, 0, 0))
            score = f.render(str(point), True, (0, 0, 200))
            Restart = f.render("Press Space if you want to", True, (0, 0, 0))
            play = f1.render("Play Again !!!", True, (0, 255, 0))
            screen.blit(text, (350, 250))
            screen.blit(score, (600, 250))
            screen.blit(Restart, (300, 315))
            screen.blit(play, (350, 350))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    run = False
                    running = True
                    play_again = True
                    pass

            pygame.display.update()



if __name__ == '__main__':
    main()