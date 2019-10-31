import pygame
import math
import random
import time
pygame.init()

# Creating_window
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
# Game_Title
pygame.display.set_caption("Air Force Game GURPREET MANN")
icon=pygame.image.load('g.JPG')
pygame.display.set_icon(icon)
#bckgroundwalipicimpoet
bg=pygame.image.load('bcg.JPG')
#Player_data
playerimg=pygame.image.load('sp4.PNG')
playerx=370
playery=480
playerx_c=0

# text scrun
score = 0
font = pygame.font.Font('freesansbold.ttf',30)
textx=10
texty=10


fontg = pygame.font.Font('freesansbold.ttf',64)


def show_score(x,y):
    scor=font.render("Score :"+str(score) , True ,(255,255,255))
    gameWindow.blit(scor,(x,y))
    g=font.render("Gurpreet Mann", True ,(255,255,0))
    gameWindow.blit(g,(280,14))
def gameover():
    gameov=fontg.render("GAME OVER..",True ,(255,245,230))
    gameWindow.blit(gameov,(240,240))
     

#Enemy_data
enemyimg =[]
enemyx =[]
enemyy =[]
enemyx_c =[]
enemyy_c =[]
no_of_anti =12

for i in range(no_of_anti):
    enemyimg.append(pygame.image.load('en.PNG'))
    enemyx.append(random.randint(10,790))
    enemyy.append(random.randint(30,100))
    enemyx_c.append(1)
    enemyy_c.append(30)

#Bullet_data
bulletimg=pygame.image.load('bullet.PNG')
bulletx=0
bullety=480
bulletx_c=0
bullety_c=15
bullet_status="ready"

def bullet_fire(x,y ):
    global bullet_status
    bullet_status="fire"
    gameWindow.blit(bulletimg,(x+16 , y+10))


def player(x,y):
    gameWindow.blit(playerimg,(playerx,playery))


def enemy(x,y,i):
    gameWindow.blit(enemyimg[i],(x,y))
    
def iscollied(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt((math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2)))
    if distance <=27:
        return True
    else:
        return False


exit_game = False
#Game_da_Loop
while not exit_game:
    #RGB RED GREEN BLUE
     gameWindow.fill((25,100,101))
     gameWindow.blit(bg,(0,0))
    
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:  
                playerx_c=4
            if event.key == pygame.K_LEFT:  
                playerx_c=-4
            if event.key == pygame.K_SPACE:
                if bullet_status is "ready":
                    bulletx=playerx
                    bullet_fire(bulletx,bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                    playerx_c=0
      #Player_movement and control the screen 0 to 800 pixcels  
     playerx += playerx_c 

     if playerx <= 1:
         playerx=1
     elif playerx >=735:
        playerx=735
    # enemy_movement
     for i in range(no_of_anti):
         #Finishing
         if enemyy[i] > 400:
             for j in range(no_of_anti):
                 enemyy[j]=2000
             gameover()
             break
             
         
         enemyx[i] += enemyx_c[i] 
         
         if enemyx[i] <= 1:
             enemyx_c[i] = 3
             enemyy[i] += enemyy_c[i]
         elif enemyx[i] >=736:
             enemyx_c[i] =-3
             enemyy[i] += enemyy_c[i]
         #Distroy enemy
         collision =iscollied(enemyx[i],enemyy[i],bulletx,bullety)
         if collision:
             bullety=480
             bullet_status="ready"
             score +=2
             enemyx[i]=random.randint(10,790)
             enemyy[i]=random.randint(30,100)
             
         enemy(enemyx[i],enemyy[i],i)

         #goli
     if bullety <= 0:
         bullety=480
         bullet_status="ready"
         
     if bullet_status is "fire":
         bullet_fire(bulletx,bullety)
         bullety -= bullety_c
              
             
          
     player(playerx,playery)
     show_score(textx,texty)
     pygame.display.update()
    
pygame.quit()
quit()
       
