import pygame
from player import Player
from obstacle import Obstacle
import random

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        self.obstacles = [Obstacle() for _ in range(3)]
        self.score = 0
        self.lives = 3

    def update(self):
        self.player.update()
        for obstacle in self.obstacles:
            obstacle.update()
            if self.player.rect.colliderect(obstacle.rect):
                self.lives -= 1
                self.obstacles.remove(obstacle)
                self.obstacles.append(Obstacle())
                if self.lives <= 0:
                    print("Game Over!")
                    pygame.quit()
                    exit()
            if obstacle.rect.right < 0:
                self.obstacles.remove(obstacle)
                self.obstacles.append(Obstacle())
                self.score += 1

    def draw(self):
        self.screen.fill((0, 0, 0))  # 검은색 배경
        self.player.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        self.draw_score()
        self.draw_lives()

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def draw_lives(self):
        font = pygame.font.Font(None, 36)
        lives_text = font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        self.screen.blit(lives_text, (10, 50))
