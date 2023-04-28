import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import JUMPING, RUNNING


class Dinosaur(Sprite):
    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 310

        self.step = 0
        self.action = "running"
        self.jump_velociti = 8.5


    def update(self , user_input):
        if self.action == "running":
            self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
            self.step += 1
        elif self.action == "jumping":
            self.image = JUMPING
            self.rect.y -= self.jump_velociti * 4
            self.jump_velociti -= 0.8
            if self.jump_velociti < -8.5:
                self.rect.y = 310
                self.action = "running"
                self.jump_velociti = 8.5

        if self.step >= 10:
            self.step = 0
        if user_input[pygame.K_UP] and self.action != "jumping":
            self.action = "jumping"
        elif self.action != "jumping":
            self.action = "running"
    

    
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    