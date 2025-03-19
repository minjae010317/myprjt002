import pygame
import random

class Obstacle:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = random.randint(0, 550)
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
