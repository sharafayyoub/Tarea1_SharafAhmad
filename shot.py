from entity import Entity
import pygame
class Shot(Entity):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)
    
    def move(self):
            self.y -= 10
    
    def hit_target(self, target):
            return self.rect.colliderect(target.rect)