import pygame

class GameOver:
    def __init__(self, score, deaths):
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.score_text = self.font.render(f"Score: {score}", True, (0, 0, 0))
        self.score_rect = self.score_text.get_rect()
        self.score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)

        self.deaths_text = self.font.render(f"Deaths: {deaths}", True, (0, 0, 0))
        self.deaths_rect = self.deaths_text.get_rect()
        self.deaths_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.restart_text = self.font.render("Press 'r' to restart", True, (0, 0, 0))
        self.restart_rect = self.restart_text.get_rect()
        self.restart_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

    def draw(self, screen):
        screen.blit(self.score_text, self.score_rect)
        screen.blit(self.deaths_text, self.deaths_rect)
        screen.blit(self.restart_text, self.restart_rect)