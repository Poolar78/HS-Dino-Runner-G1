import pygame
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, FPS


class GameOver:
    def __init__(self, score, deaths):
        self.score = score
        self.deaths = deaths
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.running = False
        self.restart_button_rect = pygame.Rect(self.center_x - 50, self.center_y + 50, 100, 50)
        self.restart_button_text = self.font.render("Restart", True, (0,0,0))
        self.game_over_text = self.font.render("Game Over", True, (0,0,0))
        self.score_text = self.font.render("Score: " + str(self.score), True, (0,0,0))
        self.deaths_text = self.font.render("Deaths: " + str(self.deaths), True, (0,0,0))

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if self.restart_button_rect.collidepoint(pos):
                    self.running = False

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))

        game_over_text_rect = self.game_over_text.get_rect()
        game_over_text_rect.center = (self.center_x, self.center_y - 50)
        self.screen.blit(self.game_over_text, game_over_text_rect)

        score_text_rect = self.score_text.get_rect()
        score_text_rect.center = (self.center_x, self.center_y)
        self.screen.blit(self.score_text, score_text_rect)

        deaths_text_rect = self.deaths_text.get_rect()
        deaths_text_rect.center = (self.center_x, self.center_y + 25)
        self.screen.blit(self.deaths_text, deaths_text_rect)

        pygame.draw.rect(self.screen, (0,0,0), self.restart_button_rect)
        restart_button_text_rect = self.restart_button_text.get_rect()
        restart_button_text_rect.center = self.restart_button_rect.center
        self.screen.blit(self.restart_button_text, restart_button_text_rect)

        pygame.display.update()