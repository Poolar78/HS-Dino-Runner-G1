from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import Large_cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import pygame
import random 

class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        

    
    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_type = random.choice([SMALL_CACTUS, LARGE_CACTUS])
            if cactus_type == SMALL_CACTUS:
                self.obstacles.append(Cactus(cactus_type))
            else:
                self.obstacles.append(Large_cactus(cactus_type))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed , self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                print("BOOOOOOOOM")
                pygame.time.delay(500)
                game.playing = False

        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset(self):
        self.obstacles = []