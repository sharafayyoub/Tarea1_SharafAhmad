from character import Character
import pygame
class Player(Character):
    def __init__(self, x, y, width, height, image_path, speed, game, lives, is_alive,is_star=False):
        super().__init__(x, y, width, height, image_path, speed, game, lives, is_alive)
        self.is_star = is_star
    def move(self, dx, dy):
        super().move(dx, dy)
    def shoot(self):
        super().shoot()