import pygame
from game import Game

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Juego de Disparos")
    game = Game()
    game.start()