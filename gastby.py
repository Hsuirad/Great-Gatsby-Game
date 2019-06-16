import pygame
import time
import array as arr
import random

pygame.init()

display_height = 600
display_width = 800

black = (0, 0, 0)
white = (255, 255, 255)
dark_red = (207, 3, 3)
green = (2, 230, 2)
dark_green = (5, 200, 5)

red = (232, 4, 4)

#start map stuff here

front_gate = pygame.image.load('leftmap.png')
nick = pygame.image.load('nick.png')
pause = pygame.image.load('pause.png')

nick_back = pygame.image.load('nickback.png')

lobby = pygame.image.load('middlemap.png')
library = pygame.image.load('rightmap.png')
gate = pygame.image.load('gate.png')
graveyard = pygame.image.load('upmap.png')
bibliography = pygame.image.load('leftmap.png')
table = pygame.image.load('righttable.png')

game_map = [front_gate, lobby, library, graveyard, bibliography]

nick_right = [pygame.image.load('nickright1.png'),
pygame.image.load('nickright2.png'),
pygame.image.load('nickright3.png'),
pygame.image.load('nickright2.png'),
pygame.image.load('nickright1.png'),
pygame.image.load('nickright5.png'),
pygame.image.load('nickright6.png'),
pygame.image.load('nickright5.png')]

nick_left = [pygame.image.load('nickleft1.png'),
pygame.image.load('nickleft2.png'),
pygame.image.load('nickleft3.png'),
pygame.image.load('nickleft2.png'),
pygame.image.load('nickleft1.png'),
pygame.image.load('nickleft5.png'),
pygame.image.load('nickleft6.png'),
pygame.image.load('nickleft5.png')]

owl_eyes = pygame.image.load('owleyes.png')

owl_back = pygame.image.load('owlback.png')

owl_right = [pygame.image.load('owleyesright1.png'),
pygame.image.load('owleyesright2.png'),
pygame.image.load('owleyesright3.png'),
pygame.image.load('owleyesright4.png'),
pygame.image.load('owleyesright3.png'),
pygame.image.load('owleyesright2.png'),
pygame.image.load('owleyesright1.png'),
pygame.image.load('owleyesright6.png'),
pygame.image.load('owleyesright5.png'),
pygame.image.load('owleyesright6.png')]

owl_left = [pygame.image.load('owleyesleft1.png'),
pygame.image.load('owleyesleft2.png'),
pygame.image.load('owleyesleft3.png'),
pygame.image.load('owleyesleft4.png'),
pygame.image.load('owleyesleft3.png'),
pygame.image.load('owleyesleft2.png'),
pygame.image.load('owleyesleft1.png'),
pygame.image.load('owleyesleft6.png'),
pygame.image.load('owleyesleft5.png'),
pygame.image.load('owleyesleft6.png')]

gatsby = pygame.image.load('gatsby.png')

gatsby_right = [pygame.image.load('gatsbyright1.png'),
pygame.image.load('gatsbyright2.png'),
pygame.image.load('gatsbyright3.png'),
pygame.image.load('gatsbyright2.png'),
pygame.image.load('gatsbyright1.png'),
pygame.image.load('gatsbyright4.png'),
pygame.image.load('gatsbyright5.png'),
pygame.image.load('gatsbyright4.png')]

gatsby_left = [pygame.image.load('gatsbyleft1.png'),
pygame.image.load('gatsbyleft2.png'),
pygame.image.load('gatsbyleft3.png'),
pygame.image.load('gatsbyleft2.png'),
pygame.image.load('gatsbyleft1.png'),
pygame.image.load('gatsbyleft4.png'),
pygame.image.load('gatsbyleft5.png'),
pygame.image.load('gatsbyleft4.png')]

#end map stuff here

disp = pygame.display.set_mode((display_width, display_height))

disp.fill(white)

pygame.display.set_caption("Great Gatsby")

clock = pygame.time.Clock()

def nick_move(x, y, direct, tick):
    if direct == "none":
        disp.blit(nick, (x, y))
    if direct == "right":
        disp.blit(nick_right[tick], (x, y))
    if direct == "left":
        disp.blit(nick_left[tick], (x, y))
    if direct == "back":
        disp.blit(nick_back, (x, y))

def gatsby_move(x, y, direct, tick):
    if direct == "none":
        disp.blit(gatsby, (x, y))
    if direct == "right":
        disp.blit(gatsby_right[tick], (x, y))
    if direct == "left":
        disp.blit(gatsby_left[tick], (x, y))
    if direct == "back":
        disp.blit(gatsby, (x, y))


intro = True

start = pygame.image.load('Untitled-12.jpg')

def start_screen():
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                     
        #eufm10.ttf
        #disp.fill(white)
        disp.blit(start, (0, 0))

        #intromusic += 1

        # if intromusic == 1:
        #     pygame.mixer.music.load('/home/daligholi/Desktop/Scarlet Letter/Purple Planet Music - Cinematic - Battle Plan.mp3')
        #     pygame.mixer.music.play(3, 0.0)
        #     pygame.mixer.music.set_volume(1.0)

        large_text = pygame.font.Font("fonts/nickerb1.ttf", 67)
        ltext = large_text.render("THE GREAT GATSBY", True, (240, 240, 240))
        disp.blit(ltext, (185, 145))
        ltext = large_text.render("GAME", True, (240,240,240))
        disp.blit(ltext,(334,208))

        #pygame.display.update()

        button("Start", 150, 450, 170, 80, green, dark_green, "start_game")
        button("Exit", 500, 450, 170, 80, red, dark_red, "exit")

        pygame.display.update()
        clock.tick(60)

def dialouge(msg):
    message = ""
    dessage = ""
    for i in range(0, len(msg)):
        if i <= 66:
            message += msg[i]
        else:
            dessage += msg[i]
        text = pygame.font.Font("fonts/nickerbockernf.ttf", 35)
        textr = text.render(message, True, white)
        texttwor = text.render(dessage, True, white)

        pygame.draw.rect(disp, black, [0, 400, 800, 200])
        disp.blit(textr, (10, 405))
        if len(msg) > 66:
            disp.blit(texttwor, (10, 440))
        pygame.display.update()
        time.sleep(0.05)

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def display_message(text):
    large_text = pygame.font.Font("fonts/GrenadierNF.ttf", 108)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    disp.blit(text_surf, text_rect)

    pygame.display.update()

def tinydialouge(msg):
    message = ""
    dessage = ""
    for i in range(0, len(msg)):
        if i <= 36:
            message += msg[i]
        else:
            dessage += msg[i]
        text = pygame.font.Font("fonts/GrenadierNF.ttf", 40)
        textr = text.render(message, True, white)
        texttwor = text.render(dessage, True, white)

        pygame.draw.rect(disp, black, [0, 150, 300, 300])
        disp.blit(textr, (10, 160))
        if len(msg) > 36:
            disp.blit(texttwor, (10, 177))
        pygame.display.update()
        time.sleep(0.5)

#button("play_hester", 150, 450, 170, 80, red, dark_red, "Hester")
def button(text, x, y, w, h, ic, ac, Action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    xw = x + w
    yh = y + h

    pygame.draw.rect(disp, ic, (x, y, w, h))

    if xw > mouse[0] > x:
        if yh > mouse[1] > y:
            pygame.draw.rect(disp, ac, (x, y, w, h))
            if click[0] == 1 and Action != None:
                if Action == "start_game":
                    start_game()
                elif Action == "exit":
                    exit()

    # for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_h:
    #             hester_loop()
    #         elif event.key == pygame.K_d:
    #             dimmesdale_loop()

    small_text_hester = pygame.font.Font("fonts/GrenadierNF.ttf", 70)
    shtext = small_text_hester.render(text, True, black)
    small_text_dimmesdale = pygame.font.Font("fonts/GrenadierNF.ttf", 60)
    sdtext = small_text_dimmesdale.render(text, True, black)

    if Action == "start_game":
        disp.blit(sdtext, (178, 460))
    elif Action == "exit":
        disp.blit(shtext, (540, 458))

def owl_move(x, y, direct, tick):
    if direct == "none":
        disp.blit(owl_eyes, (x, y))
    if direct == "right":
        disp.blit(owl_right[tick], (x, y))
    if direct == "left":
        disp.blit(owl_left[tick], (x, y))
    if direct == "back":
        disp.blit(owl_back, (x, y))

def credits():
    pygame.draw.rect(disp, black, [0, 0, 800, 600])
    textz_render = pygame.font.SysFont("Times New Roman", 40)
    textz = textz_render.render("Programming, character art, animations:", True, white)
    disp.blit(textz, (10, 0))
    textz = textz_render.render("Dariush Aligholizadeh", True, white)
    disp.blit(textz, (250, 50))
    text_render = pygame.font.SysFont("Times New Roman", 40)
    text = text_render.render("Background graphics, research:", True, white)
    disp.blit(text, (0, 300))
    text = text_render.render("Saphal Bhandari", True, white)
    disp.blit(text, (0, 350))

def start_game():

    playing = True
    x = display_width / 3
    spoken = False
    y = display_height / 2
    n_tick = 0
    walk = False
    booked = False
    tick = 0
    dx = 0
    dy = 0
    ndirect = "none"
    gdirect = "none"
    gdx = random.randint(-1, 1)
    gdy = random.randint(-1, 1)
    p = False
    g_tick = 0
    gx = 400
    drunk2 = False
    gy = 300
    background = lobby
    sober = False
    drunk = False
    soberspeak = False
    crashedspeak = False
    done = False
    deadspeak = False
    crashed = False
    nx = 70
    ny = 50
    ndx = random.randint(-1, 1)
    ndy = random.randint(-1, 1)
    

    while playing:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playing = False;
                    pygame.quit()
                    quit()
                if event.key == pygame.K_LEFT:
                    direct = "left"
                    walk = True
                    dx = -3
                elif event.key == pygame.K_RIGHT:
                    walk = True
                    direct = "right"
                    dx = 3
                elif event.key == pygame.K_UP:
                    if dx == 0:    
                        direct = "back"
                    dy = -3
                elif event.key == pygame.K_DOWN:
                    dy = 3
                elif event.key == pygame.K_p:
                    p = True

                    while p == True:
                        disp.blit(pause, (0, 0))

                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                p = False

                        pygame.display.update()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    #direct = "none"
                    dx = 0
                elif event.key == pygame.K_RIGHT:
                    walk = False
                    #direct = "none"
                    dx = 0
                elif event.key == pygame.K_UP:
                    if dx == 0:
                        direct = "none"
                    dy = 0
                elif event.key == pygame.K_DOWN:
                    dy = 0

        if dy == 0 and dx == 0:
            direct = "none"

        if walk:
            if tick >= len(nick_right) - 1:
                tick = tick - len(nick_right)
            tick += 0.1
        else:
            tick = 0

        if background == front_gate:
            drunk = True
            if x > display_width - 40:
                #change the map
                background = lobby
                x = 50
            if x < 50 and dx < 0:
                dx = 0
            if y < 78 and dy < 0:
                dy = 0
            if not(346 > y > 198) and 188 < x < display_width:
                if y > 346 and dy > 0:
                    dy = 0
                if y < 198 and dy < 0:
                    dy = 0
                if dx > 0:
                    dx = 0
            if y > display_height - 113 and dy > 0:
                dy = 0
            #npc collision
            if nx > display_width + 22:
                #change the map
                background = lobby
                nx = 0
            if nx < 50 and ndx < 0:
                ndx = 0
            if ny < 78 and ndy < 0:
                ndy = 0
            if not(346 > ny > 198) and 188 < nx < display_width:
                if ny > 346 and ndy > 0:
                    ndy = 0
                if ny < 198 and ndy < 0:
                    ndy = 0
                if ndx > 0:
                    ndx = 0
            if ny > display_height - 113 and ndy > 0:
                ndy = 0
            if x - 80 < nx < x + 80 and y - 500 < ny < y + 500 and not(spoken):
                spoken = True
                dialouge("NICK: You're the man from the library, how did you crash? Did you hit the tree?")
                time.sleep(0.8)
                dialouge("OWL EYES: (the criminal justified) Don't ask me... I don't even know how to drive. Someone else was driving for me.")
                time.sleep(0.9)
                dialouge("NICK: Well where are they?")
                time.sleep(0.6)
                dialouge("OWL EYES: I am not sure where they are... I have to be on my way now.")
                time.sleep(0.8)
        else:
            drunk = False
        #384 110 -> 740
        #274 476 -> 16
        #90 368 -> 18

        if soberspeak:
            soberspeak = False
            dialouge("OWL EYES: Hmm... maybe a walk in the library can sober me up.")
            time.sleep(0.7)

        if crashedspeak:
            crashedspeak = False
            dialouge("OWL EYES: Wh... What happened? How did the car get in a ditch?")
            time.sleep(0.9)
            dialouge("OWL EYES: I should probably get back to the house...")
            time.sleep(1)

        if deadspeak:
            deadspeak = False
            dialouge("OWL EYES: *breathing heavily* Hey... wait up!")
            time.sleep(1)

        if background == lobby:
            if gx < 0:
                gx = 400
                gy = 300
            if x > 740 and 118 < y < 384 and not(sober):
                background = library
                sober = True
                soberspeak = True
                dx = dy = 0
                direct = "none"
                x = 320
                y = 300
            if 274 < x < 476 and y < 16 and crashed:
                background = graveyard
                deadspeak = True
                ny = 50
                direct = "none"
                dx = dy = 0
                nx = 300
                x = 400
                y = 300
            if x < 18 and 90 < y < 268 and sober:
                background = front_gate
                crashed = True
                x = 100
                crashedspeak = True
                y = 100
                nx = 600
                ny = 260
            if x - 1 < gx < x + 1 and y - 1 < gy < y + 1:
                dialouge("GATSBY: Sorry Old Sport! Can't talk now I'm busy!")
                time.sleep(0.5)
            if y > 490 and dy > 0:
                dy = 0
        
        if background == library:
            #375 420 600
            #owl eyes detection
            if 375 < x < 425 and y > 420 and dx > 0:
                dx = 0
            if 500 < x < 600 and y > 420 and dx < 0:
                dx = 0 
            if 375 < x < 600 and y > 420 and dy > 0:
                dy = 0
            if y < 82 and dy < 0:
                dy = 0
            if y > 500:
                background = lobby
                x = 700
                y = 200
            if 430 < x < 655 and 145 < y < 195 and not(booked):
                booked = True
                dialouge("OWL EYES: These books... they're all real... he went through all this trouble?")
                time.sleep(0.6)
                nx = -50
                ny = 150
            if booked:
                ndx = 2
                ndy = 0
            else:
                nx = 0
                ny = 0
            if x - 100 < nx < x + 100 and y - 100 < ny < y + 100:
                dialouge("OWL EYES: What do you think?")
                time.sleep(0.5)
                dialouge("NICK: About what?")
                time.sleep(0.5)
                dialouge("OWL EYES: These books are real, pages and everything, nice durable cardboard. But they're uncut, they've never been read!")
                time.sleep(0.7)
                dialouge("OWL EYES: (thinking) Gatsby has created layers upon layers of detail to support his facade.")
                time.sleep(0.5)
                dialouge("OWL EYES: (thinking) This man is a fraud, a real Belasco!")
                time.sleep(1.5)
                background = lobby
            
            #nick detection
            if 375 < nx < 425 and ny > 420 and ndx > 0:
                ndx = 0
            if 500 < nx < 600 and ny > 420 and ndx < 0:
                ndx = 0 
            if 375 < nx < 600 and ny > 420 and ndy > 0:
                ndy = 0
        
        #325 420 25
        if background == graveyard:
            drunk2 = True
            if y > 500:
                background = lobby
                x = 350
                y = 17
            if y < 25 and dy < 0:
                dy = 0    
            if x < 325 and dx < 0:
                dx = 0
            if x > 420 and dx > 0:
                dx = 0
            if x - 500 < 300 < x + 500 and y - 35 < 50 < y + 35 and not(done):
                done = True
                dialouge('NICK: So... he\'s really gone, isn\'t he?')
                time.sleep(0.5)
                dialouge("OWL EYES: We were the only ones who saw him for who he was.")
                time.sleep(0.8)
                dialouge("OWL EYES: Now he's gone... nobody at his parties or even daring to say his name.")
                time.sleep(2)
                dialouge("OWL EYES: The poor son-of-a-bitch...")
                time.sleep(3)
                #credits()
                pygame.display.update()
                time.sleep(0.2)
                start_screen()
        else:
            drunk2 = False

        #owl eyes collision detection
        if x > display_width + 30 and dx > 0:
            dx = 0
        elif x < 0 and dx < 0:
            dx = 0
        elif y < 0 and dy < 0:
            dy = 0
        elif y > display_height + 110 and dy > 0:
            dy = 0

        #owl eyes collision detection
        if nx > display_width - 44:
            ndx = random.randint(-1, 0)
        elif nx < 0 and background != library:
            ndx = random.randint(0, 1)
        elif ny > display_height - 113:
            ndy = random.randint(-1, 0)
        elif ny < 0:
            ndy = random.randint(0, 1)
        #owl eyes random movement
        elif background != library:
            if round(n_tick, 1) == 5:
                ndx = random.randint(-1, 1)
            elif round(n_tick, 1) == 10:
                ndy = random.randint(-1, 1)
                n_tick = 0
            n_tick += 0.1
        
        if gx > display_width - 44:
            gdx = random.randint(-1, 0)
        elif gx < 0:
            gdx = random.randint(0, 1)
        elif gy > display_height - 113:
            gdy = random.randint(-1, 0)
        elif gy < 0:
            gdy = random.randint(0, 1)
        #owl eyes random movement
        else:
            if round(g_tick, 1) == 5:
                gdx = random.randint(-1, 1)
            elif round(g_tick, 1) == 10:
                gdy = random.randint(-1, 1)
                g_tick = 0
            g_tick += 0.1;

        if drunk:
            if random.randint(0, 1) == 1:
                x += dx + (random.random() - 0.5) * 1
                y += dy + (random.random() - 0.5) * 1
        elif drunk2:
            if random.randint(-1, 1) == 1:
                x += dx + (random.random() - 0.5) * 5
                y += dy + (random.random() - 0.5) * 5        
        else:    
            x += dx# + (random.random() - 0.5) * 1
            y += dy# + (random.random() - 0.5) * 1
        nx += (ndx)
        ny += (ndy)
        if background == lobby:    
            gx += gdx
            gy += gdy

        if ndx > 0:
            ndirect = "right"
        elif ndx < 0:
            ndirect = "left"
        elif ndy < 0:
            ndirect = "back"
        else:
            ndirect = "none"
        
        if gdx > 0:
            gdirect = "right"
        elif gdx < 0:
            gdirect = "left"
        elif gdy < 0:
            gdirect = "back"
        else:
            gdirect = "none"
        
        disp.blit(background, (0, 0))
        if background == graveyard:
            disp.blit(nick, (300, 50))
        if background == front_gate or (background == library and booked):
            nick_move(nx, ny, ndirect, round(tick))
        if background == lobby:
            gatsby_move(gx, gy, gdirect, round(tick))
        owl_move(x, y, direct, round(tick))
        #print(x, y)
        if background == front_gate:
            disp.blit(gate, (0, 0))
        #print(len(nick_right))
        if background == library:
            disp.blit(table, (0, 0))

        
        ##this is where the cool stuff is, uncomment it
        #credits()

        
        pygame.display.update()
        #print(x, y)
        clock.tick(60)

start_screen()
start_game()

time.sleep(5)
pygame.quit()
quit()