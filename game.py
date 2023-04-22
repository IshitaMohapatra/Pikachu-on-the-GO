#importing library
import pygame
import random
from pygame.locals import *

#initializing the game
pygame.init()

display_width = 800
display_height = 500
gameDisplay = pygame.display.set_mode((display_width,display_height)) #game screen
pygame.display.set_caption('Pikachu on the Go!') #title of the game
#BG (RGB formatting) #to define colours
black = (0,0,0)
white = (255,255,255)
crashed = False

#loading the image
pika = pygame.image.load('pikachu.png')
pika = pygame.transform.scale(pika, (70, 80)) #resizing image
bomb = pygame.image.load('bomb.png')
bomb = pygame.transform.scale(bomb, (40, 40)) #resizing image
bomb1 = pygame.image.load('bomb.png')
bomb1 = pygame.transform.scale(bomb1, (40, 40))
ash = pygame.image.load('Ash.png')
ash = pygame.transform.scale(ash, (50, 100))
pokeball = pygame.image.load('pokeball.png')
pokeball = pygame.transform.scale(pokeball, (40, 40))
#background
bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (800, 500))

#defining values for width and height of image
pika_width = 80
pika_height = 90
bomb_width = 40
bomb_height = 40
bomb1_width = 40
bomb1_height = 40
ash_width = 50
ash_height = 100
pokeball_width = 40
pokeball_height = 40
bg_width = 800
bg_height = 500

#defining functions
def player(x,y):
    gameDisplay.blit(pika,(x,y))
def frnd(x1,y1):
    gameDisplay.blit(ash,(x1,y1))
def obj(objx,objy):
    gameDisplay.blit(bomb,(objx,objy))
def obj(objx1,objy1):
    gameDisplay.blit(bomb1,(objx1,objy1))
def ball(bx1,by1):
    gameDisplay.blit(pokeball,(bx1,by1))
def background(xb,yb):
    gameDisplay.blit(bg,(xb,yb))

def crash():
    pygame.mixer.music.stop() #music stops
    print('Pikachu got burnt!')
    print('Game over!')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
def collision():
    print('Pikachu found Ash!')
    print('Well Done!')

    while True:
        for event in pygame.event.get():
             game_loop() 
        pygame.display.update()
        
def ballcol():
    pygame.mixer.music.stop() #music stops
    print('Oh no!')
    print("Pikachu doesn't like pokeballs!")
    print('Game over!')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def game_loop():
    print()
    print('Pikachu is on the GO! Help Pikachu find its trainer, Ash.')
    print('But be careful of obstacles!')
    print('Remember: Pikachu doesn’t like pokeballs, so be sure to keep them as far as possible.')
    print('Hurry up Ash is waiting!')
    print('Press escape to exit the game anytime.')
    print('Use the arrows keys to move Pikachu.')
    print('The game restarts after Pikachu finds Ash.')
    print()
    pygame.mixer.music.load('music.wav')
    pygame.mixer.music.play(-1) #music plays

    x = 0 #aligning or locating the image
    y = 0
    hitbox = (x,y,pika_width-30,pika_height-20) #making hitbox
    x_change = 0
    y_change = 0

    #background
    xb = 0
    yb = 0
    
    #ash
    x1 = random.randrange(0,display_width - ash_width)
    y1 = random.randrange(0,display_height - ash_height)
    hitbox1 = (x1,y1,ash_width,ash_height)
    #bomb
    objx = random.randrange(0,display_width - bomb_width)
    objy = random.randrange(0,display_height - bomb_height)
    objhitbox = (objx,objy,bomb_width,bomb_height)
    #bomb1
    objx1 = random.randrange(0,display_width - bomb1_width)
    objy1 = random.randrange(0,display_height - bomb1_height)
    objhitbox1 = (objx1,objy1,bomb1_width,bomb1_height)
    #pokeball
    bx1 = random.randrange(0,display_width - pokeball_width)
    by1 = random.randrange(0,display_height - pokeball_height)
    ball_hitbox1 = (bx1,by1,pokeball_width,pokeball_height)

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #quitting the game
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN: #controls
                if event.key == pygame.K_LEFT:
                    x_change = -3
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 3
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -3
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 3
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        #valid move (adding boundaries)
        if(x+x_change)>= 0 and (x+x_change)<=(display_width - (pika_width-10)):
            x += x_change
            hitbox = (x,y,pika_width-30,pika_height-20)
        if(y+y_change)>= 0 and (y+y_change)<=(display_height - (pika_height-20)):
            y+= y_change
            hitbox = (x,y,pika_width-30,pika_height-20)

        #condition for crash
        #bomb with player
        if (x >= objx and x+10 <= objx+bomb_width) or (x+pika_width-40 >= objx and x+pika_width-60 <= objx+bomb_width):
            if (y >= objy  and y <= (objy+bomb_height)) or (y+pika_height-20 >= objy and y+pika_height-20 <= (objy+bomb_height)):
                crash()
            elif ((y + pika_height/2 -20) >= objy and (y + pika_height/2 -20) <= (objy+bomb_height)):
                crash()
        #bomb1 with player
        elif (x >= objx1 and x+10 <= objx1+bomb1_width) or (x+pika_width-40 >= objx1 and x+pika_width-60 <= objx1+bomb1_width):
            if (y >= objy1  and y <= (objy1+bomb1_height)) or (y+pika_height-20 >= objy1 and y+pika_height-20 <= (objy1+bomb1_height)):
                crash()
            elif ((y + pika_height/2 -20) >= objy1 and (y + pika_height/2 -20) <= (objy1+bomb1_height)):
                crash()
        #ash with player
        elif  (x >= x1 and x+10 <= x1+ash_width) or (x+pika_width-40 >= x1 and x+pika_width-60 <= x1+ash_width):
            if (y >= y1  and y <= (y1+ash_height)) or (y+pika_height-20 >= y1 and y+pika_height-20 <= (y1+ash_height)):
                collision()
            elif ((y + pika_height/2 -20) >= y1 and (y + pika_height/2 -20) <= (y1+ash_height)):
                collision()
        #pokeball with player
        elif  (x >= bx1 and x+10 <= bx1+pokeball_width) or (x+pika_width-40 >= bx1 and x+pika_width-60 <= bx1+pokeball_width):
            if (y >= by1  and y <= (by1+pokeball_height)) or (y+pika_height-20 >= by1 and y+pika_height-20 <= (by1+pokeball_height)):
                ballcol()
            elif ((y + pika_height/2 -20) >= by1 and (y + pika_height/2 -20) <= (by1+pokeball_height)):
                ballcol()

        gameDisplay.fill(white) #filling the rest of the space
        background(xb,yb) #background

        #for hitboxes
        pygame.draw.rect(gameDisplay,(0,0,255),hitbox,2) #pygame.draw.rect(Surface,color(RGB),[x,y,width,height],border)
        pygame.draw.rect(gameDisplay,(0,0,255),objhitbox,2)
        pygame.draw.rect(gameDisplay,(0,0,255),objhitbox1,2)
        pygame.draw.rect(gameDisplay,(0,0,255),hitbox1,2)
        pygame.draw.rect(gameDisplay,(0,0,255),ball_hitbox1,2)

        #calling the functions
        player(x,y)
        obj(objx,objy)
        obj(objx1,objy1)
        frnd(x1,y1)
        ball(bx1,by1)

        pygame.display.update() #or flip() #to update the surface ie gameDisplay

game_loop()
pygame.quit()
quit()
