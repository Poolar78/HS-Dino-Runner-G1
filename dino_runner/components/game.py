import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.game_over import GameOver
from dino_runner.components.obstacles.obstacleManager import ObstacleManager
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS , DINO_START


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.game_over = GameOver(score=0, deaths=0)

    def run(self):
        self.running = True 
        while self.running:
            self.show_menu()

        pygame.quit()

    def play(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing: 
            self.events()
            self.update()
            self.draw()
        self.game_over.score = self.score.score
        self.game_over.deaths = self.score.deaths
        self.game_over.run()
        self.play()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        center_x = SCREEN_WIDTH // 2 
        center_y = SCREEN_HEIGHT // 2
        self.screen.fill((255, 255, 255))   
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("press any key to start.", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (center_x , center_y)
        self.screen.blit(text, text_rect)
        self.screen.blit(DINO_START, (center_x -49 ,center_y - 121))
        pygame.display.update()
        self.handle_menu_events()
        

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.play()