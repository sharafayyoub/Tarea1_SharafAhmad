from entity import Entity
from shot import Shot
import pygame
class Character(Entity):
    def __init__(self, x, y, width, height, image_path, speed, game, lives, is_alive):
        super().__init__(x, y, width, height, image_path, speed, game)
        self.lives = lives
        self.is_alive = is_alive
    def move(self, dx, dy):
        super().move(dx, dy)
        self.update()
    def shoot(self):
        shot = Shot(self.x, self.y, 10, 10, "shot.png", self.speed, self.game)
        self.game.shots.append(shot)
    def collide(self, other):
        if self.rect.colliderect(other.rect):
            self.lives -= 1
            if self.lives <= 0:
                self.is_alive = False
    def draw(self):
        super().draw()
