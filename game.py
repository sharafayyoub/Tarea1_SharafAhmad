def end_game(self, player_lives, boss_defeated):
    if boss_defeated and player_lives > 0:
        print("¡Victoria! Has derrotado al jefe final y ganado el juego.")
    else:
        print("Juego terminado. Mejor suerte la próxima vez.")
import pygame
from player import Player
from opponent import Opponent
from boss import Boss
from shot import Shot
class Game:
    def __init__(self):
        self.score = 0
    def __score__(self):
        return self.score
    def __str__(self):
        return f"Game(score={self.score})"
    def __vidas__(self):
        return self.vidas
    def __repr__(self):
        return self.__str__()  