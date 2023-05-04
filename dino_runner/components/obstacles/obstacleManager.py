from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import Large_cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import pygame
import random 

class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        

    
    def update(self, game_speed, player, on_death):
        if len(self.obstacles) == 0:
            cactus_type = random.choice([SMALL_CACTUS, LARGE_CACTUS])
            if cactus_type == SMALL_CACTUS:
                self.obstacles.append(Cactus(cactus_type))
            else:
                self.obstacles.append(Large_cactus(cactus_type))

        for obstacle in self.obstacles:
            obstacle.update(game_speed , self.obstacles)
            if player.rect.colliderect(obstacle.rect):
                on_death()

        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset(self):
        self.obstacles = []