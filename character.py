import random
from entity import Entity
import pygame

class Character(Entity):
    def __init__(self, x, y, image_path, lives):
        super().__init__(x, y, image_path)
        self.lives = lives
        self.is_alive = True
    def shoot(self):
        from shot import Shot
        return Shot(self.x + self.rect.width // 2, self.y, "assets/shot1.png")
    def collide(self, other):
        return self.rect.colliderect(other.rect)
class Player(Character):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/bueno.png", lives=3)
        self.score = 0
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.move(-5, 0)
        if keys[pygame.K_RIGHT] and self.x < 800 - self.rect.width:
            self.move(5, 0)
        if keys[pygame.K_UP] and self.y > 0:
            self.move(0, -5)
        if keys[pygame.K_DOWN] and self.y < 600 - self.rect.height:
            self.move(0, 5)
class Opponent(Character):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/malo.png", lives=1)
        self.is_star = False
    def move(self):
        self.y += 2
        if self.y > 600:
            self.y = -self.rect.height
            self.x = random.randint(0, 800 - self.rect.width)