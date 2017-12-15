import pygame
import turtle
import matplotlib as plt
import numpy as np
import random
import time
import os


img_dir = os.path.join(os.path.dirname(__file__), "img")
WIDTH = 500
HEIGHT = 480
FPS = 30
size=1
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE=(255,165,0)
PURPLE=(160,32,240)
gamestart=1
score1=0
score2=0
game_folder=os.path.dirname(__file__)
img_folder= os.path.join(game_folder,"img")
img= img_folder
height = len(img)
width = len(img[0])
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,75))
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.center=(10,200)
        self.speedy=0
    def update(self):
        global size
        self.speedy=0


        if size>60:
           self.image = pygame.Surface((10, 10))
           self.image.fill(PURPLE)
        if size>50 and size<60:
           self.image = pygame.Surface((10, 20))
           self.image.fill(ORANGE)
        if size>40 and size<50:
           self.image = pygame.Surface((10, 30))
           self.image.fill(BLUE)
        if size>30 and size<40:
           self.image = pygame.Surface((10, 40))
           self.image.fill(WHITE)
        if size>20 and size<30:
           self.image = pygame.Surface((10, 50))
           self.image.fill(GREEN)
        if size>10 and size<20:
           self.image = pygame.Surface((10, 60))
           self.image.fill(BLUE)
        keystate= pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy=-10
        if keystate[pygame.K_s]:
            self.speedy=10
        self.rect.y += self.speedy

        if self.rect.bottom>HEIGHT:
            self.rect.bottom=HEIGHT
        if self.rect.top<0:
            self.rect.top=0

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        global size
        pygame.sprite.Sprite.__init__(self)
        if size>0 and size<11:
           self.image = pygame.Surface((10, 75))
           self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (490, 300)
        self.speedy = 0

    def update(self):
        global size
        self.speedy = 0
        if size>60:
           self.image = pygame.Surface((10, 10))
           self.image.fill(PURPLE)
        if size>50 and size<60:
           self.image = pygame.Surface((10, 20))
           self.image.fill(ORANGE)
        if size>40 and size<50:
           self.image = pygame.Surface((10, 30))
           self.image.fill(BLUE)
        if size>30 and size<40:
           self.image = pygame.Surface((10, 40))
           self.image.fill(WHITE)
        if size>20 and size<30:
           self.image = pygame.Surface((10, 50))
           self.image.fill(GREEN)
        if size>10 and size<20:
           self.image = pygame.Surface((10, 60))
           self.image.fill(BLUE)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -10
        if keystate[pygame.K_DOWN]:
            self.speedy = 10
        self.rect.y += self.speedy
        if self.rect.bottom>HEIGHT:
            self.rect.bottom=HEIGHT
        if self.rect.top<0:
            self.rect.top=0
# initialize pygame and create window
class Ball(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(os.path.join(img_folder, "Pac Man1.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()

    
        self.rect.center=(200,200)
        self.speedy=0
        global score
        self.speedy = 0
        self.speedx = 10
        self.rot_speed=10
        self.last_update=pygame.time.get_ticks()

    def update(self):
        global running
        global size



        collisionr=pygame.sprite.spritecollide(player2,ballg,False)
        if self.rect.top <= 0 and self.speedx<0:
            self.image.fill(GREEN)
            self.speedx = -12
            self.speedy = 8


        if self.rect.top <= 0 and self.speedx>0:
              self.image.fill(RED)
              self.speedx = 12
              self.speedy = 8
        if self.rect.bottom >= HEIGHT and self.speedx>0:
            self.image.fill(BLUE)
            self.speedx = 12
            self.speedy = -8
        if self.rect.bottom >= HEIGHT and self.speedx<0:

            self.speedx = -12
            self.image.fill(ORANGE)
            self.speedy = -8

        if self.rect.right == WIDTH:
            running = False

        if self.rect.left == 0:
            running = False

        if collisionr and self.speedy<=1:
            self.speedx=-10
            self.speedy=-10
            size=size+1
        if collisionr and self.speedy>=1:
            self.speedx = -12
            self.speedy = 8
            size=size+1
        collisionl = pygame.sprite.spritecollide(player, ballg, False)
        if collisionl and self.speedy<=1:
            self.speedx = 12
            self.speedy = -8
            size=size+1
        if collisionl and self.speedy >=1:
            self.speedx = 12
            self.speedy = 8
            size=size+1
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top<=0 and self.speedx<=1:
                self.speedx=-12
                self.speedy=8
        if self.rect.top<=0 and self.speedx>=1:
                self.speedx=12
                self.speedy=-8

        if self.rect.bottom>=HEIGHT and self.speedx>=1:
                self.speedx=12
                self.speedy=-8

        if self.rect.bottom>=HEIGHT and self.speedx<=1:
                self.speedx=-12
                self.speedy=8

        if self.rect.left >=500:
            running=False

        if self.rect.right <=0:
            running=False




pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
background=pygame.image.load(os.path.join(img_dir, "Pac Man Map.jpg")).convert()
background_rect=background.get_rect()
all_sprites = pygame.sprite.Group()
ballg=pygame.sprite.Group()
player=Player()
player2=Player2()
ball=Ball()

all_sprites.add(player,player2,ball)
ballg.add(ball)


# Game loop
running = True
while running==True:

    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
