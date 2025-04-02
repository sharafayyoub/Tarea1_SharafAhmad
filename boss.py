from character import Character
import random
import pygame

class Boss(Character):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/jefe.png", lives=3)
        self.is_star = False
        self.image = pygame.image.load("assets/jefe.png")
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    def move(self):
        self.y += 4
        if self.y > 600:
            self.y = -self.rect.height
            self.x = random.randint(0, 800 - self.rect.width)
    