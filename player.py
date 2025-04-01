from character import Character
import pygame
class Player(Character):
    def __init__(self, x, y, width, height, image_path, speed, game, lives=3, is_alive=True, score=0):
        super().__init__(x, y, width, height, image_path, speed, game, lives, is_alive)
        self.score = score
    
    def move(self, dx, dy):
        super().move(dx, dy)
    def shoot(self):
        super().shoot()
    