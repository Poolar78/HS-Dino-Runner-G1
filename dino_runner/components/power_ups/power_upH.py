import random
import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


class PowerUpH:
    
    def __init__(self , image: pygame.Surface, power_up_type): 

        self.type = power_up_type
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800 , 1000)
        self.rect.y = random.randint(100, 150)

        self.start_time = 0
        self.duration = random.randint(3 , 5)


    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x <= self.rect.width:
            power_ups.pop()

    def draw(self , screen):
        screen.blit(self.image, self.rect)