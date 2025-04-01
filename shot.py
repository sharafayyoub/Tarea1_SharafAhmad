from entity import Entity
import pygame
class Shot(Entity):
    def __init__(self, x, y, width, height, image_path, speed, game):
        super().__init__(x, y, width, height, image_path, speed, game)

    def move(self):
        self.x += self.speed
        self.rect.topleft = (self.x, self.y)
    def hit_target(self, target):
        if self.rect.colliderect(target.rect):
            target.lives -= 1
            if target.lives <= 0:
                target.is_alive = False
            return True
        return False