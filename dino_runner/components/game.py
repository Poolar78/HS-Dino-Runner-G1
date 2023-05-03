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

        self.deaths = 0
        self.game_over = None

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

            if self.player.is_dead:
                self.deaths += 1
                self.game_over = GameOver(self.score.get_score(), self.deaths)
                while True:
                    self.handle_game_over_events()
                    self.game_over.draw(self.screen)
                    pygame.display.update()

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
        #cambiar fondo de pantalla ,
        self.screen.fill((255, 255, 255))  
        #agrgar un texto de inicio en la pantalla 
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("press any key to start.", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (center_x , center_y)
        self.screen.blit(text, text_rect)
        #agregar una imagen en la pantalla
        self.screen.blit(DINO_START, (center_x -49 ,center_y - 121))
        #refrescar pantalla
        pygame.display.update()
        #manejar eventos
        self.handle_menu_events()
        

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.play()


    def handle_game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset_game()
    
    def reset_game(self):
        self.player.reset()
        self.obstacle_manager.reset()
        self.score.reset()
        self.game_over = None
    
