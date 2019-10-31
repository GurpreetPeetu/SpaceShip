import pygame
import math
import random
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
score=0

#Enemy_data
enemyimg=pygame.image.load('en.PNG')
enemyx=random.randint(10,790)
enemyy=random.randint(30,100)
enemyx_c=1
enemyy_c=30

#Bullet_data
bulletimg=pygame.image.load('bullet.PNG')
bulletx=0
bullety=480
bulletx_c=0
bullety_c=10
bullet_status="ready"

def bullet_fire(x,y ):
    global bullet_status
    bullet_status="fire"
    gameWindow.blit(bulletimg,(x+16 , y+10))


def player(x,y):
    gameWindow.blit(playerimg,(playerx,playery))


def enemy(x,y):
    gameWindow.blit(enemyimg,(enemyx,enemyy))
    
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
                playerx_c=2
            if event.key == pygame.K_LEFT:  
                playerx_c=-2
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
     enemyx += enemyx_c 
     
     if enemyx <= 1:
         enemyx_c = 2
         enemyy += enemyy_c
     elif enemyx >=736:
         enemyx_c =-2
         enemyy += enemyy_c
         #goli
     if bullety <= 0:
         bullety=480
         bullet_status="ready"
         
     if bullet_status is "fire":
         bullet_fire(bulletx,bullety)
         bullety -= bullety_c
     #Distroy enemy
     collision =iscollied(enemyx,enemyy,bulletx,bullety)
     if collision:
         bullety=480
         bullet_status="ready"
         score +=1
         print(score)
         enemyx=random.randint(10,790)
         enemyy=random.randint(30,100)
         
             
          
     player(playerx,playery)
     enemy(enemyx,enemyy)
     pygame.display.update()
    
pygame.quit()
quit()
       
