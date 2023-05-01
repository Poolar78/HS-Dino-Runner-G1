import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING

JUMP_VELOCITY = 8.5
DINO_JUMPING = "jumping"
DINO_RUNNING = "running"
DINO_DUCKING = "ducking"

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310

    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y

        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velociti = JUMP_VELOCITY


    def update(self , user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()

        elif self.action == DINO_DUCKING:
             self.ducking()

        if self.step >= 10:
            self.step = 0

        if user_input[pygame.K_UP] and self.action != DINO_JUMPING:
            self.action = DINO_JUMPING
        elif user_input[pygame.K_DOWN] and self.action != DINO_JUMPING:
            self.action = DINO_DUCKING
        elif self.action != DINO_JUMPING:
            self.action = DINO_RUNNING 
    
    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velociti * 4
        self.jump_velociti -= 0.8
        if self.jump_velociti < -JUMP_VELOCITY:
            self.rect.y = self.POS_Y
            self.action = DINO_RUNNING
            self.jump_velociti = JUMP_VELOCITY
    
    def run(self):
        self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
        self.step += 1
        self.rect.y = self.POS_Y

    def ducking(self):   
        self.image = DUCKING[0]
        self.rect.y = 340
        self.rect.height = DUCKING[0].get_height()
    
    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    