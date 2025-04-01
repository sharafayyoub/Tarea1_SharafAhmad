class Game:
    def __init__(self):
        self.opponents = []
        self.boss = None
        self.boss_spawned = False

    def remove_opponent(self, opponent):
        if opponent in self.opponents:
            self.opponents.remove(opponent)
            if not self.opponents and not self.boss_spawned:
                self.spawn_boss()

    def spawn_boss(self):
        self.boss = Boss()  # Assuming a Boss class exists
        self.boss_spawned = True
        print("Boss has appeared!")
class GameOverException(Exception):
    pass

def respawn_player(player):
    time.sleep(2)  # Simulate brief respawn time
    player.is_alive = True
    player.x, player.y = player.game.starting_position  # Reset position

class Player(Character):
    def __init__(self, x, y, width, height, image_path, speed, game, lives=3, is_alive=True, score=0):
        super().__init__(x, y, width, height, image_path, speed, game, lives, is_alive)
        self.score = score
        self.lives = lives

    def take_damage(self):
        if self.is_alive:
            self.lives -= 1
            self.is_alive = False
            if self.lives <= 0:
                raise GameOverException("Game Over")
            else:
                respawn_player(self)
from character import Character

import pygame
import time
class Player(Character):
    def __init__(self, x, y, width, height, image_path, speed, game, lives=3, is_alive=True, score=0):
        super().__init__(x, y, width, height, image_path, speed, game, lives, is_alive)
        self.score = score
    
    def move(self, dx, dy):
        super().move(dx, dy)
    def shoot(self):
        super().shoot()

class Score:
    def __init__(self):
        self.points = 0

    def increment(self, value=1):
        self.points += value

    def reset(self):
        self.points = 0
    