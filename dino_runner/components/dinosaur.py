import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING_HAMMER, DUCKING_SHIELD, HAMMER_TYPE, JUMPING, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING, DUCKING, RUNNING_HAMMER, RUNNING_SHIELD, SHIELD_TYPE

JUMP_VELOCITY = 8.5
DINO_JUMPING = "jumping"
DINO_RUNNING = "running"
DINO_DUCKING = "ducking"

DUCKING_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMPING_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUNNING_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = (RUNNING_IMG[self.type][0])
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
        self.image = JUMPING_IMG[self.type]
        self.rect.y -= self.jump_velociti * 4
        self.jump_velociti -= 0.8
        if self.jump_velociti < -JUMP_VELOCITY:
            self.rect.y = self.POS_Y
            self.action = DINO_RUNNING
            self.jump_velociti = JUMP_VELOCITY
    
    def run(self):
        self.image = (RUNNING_IMG[self.type][0]) if self.step < 5 else RUNNING[1]
        self.step += 1
        self.rect.y = self.POS_Y

    def ducking(self):   
        self.image = (DUCKING_IMG[self.type][0])
        self.rect.y = 340
        self.rect.height = (DUCKING_IMG[self.type][0]).get_height()
    
    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.draw_power_up(screen)

    def on_pick_power_up(self,power_up):
        self.type = power_up.type
        self.power_up_time_up = power_up.start_time +  (power_up.duration * 1000)
        print("powerup")
        print(power_up.type)
    
    def draw_message(self, message, screen, font_size, pos_y_center):
        font = pygame.font.Font(None, font_size)
        text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen.get_width() // 2, pos_y_center))
        screen.blit(text, text_rect)
    
    def draw_power_up(self, screen):
        if self.type != DEFAULT_TYPE:
            time_to_show = round(
                (self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0 :
                self.draw_message(
                    f"{self.type.capitalize()} enable for {time_to_show}seconds.",
                    screen,
                    font_size=22,  
                    pos_y_center=50  
            )
            else:
                self.type = DEFAULT_TYPE
                self.power_up_time_up = 0 