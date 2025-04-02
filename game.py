import pygame
import random
from character import Player, Opponent
from boss import Boss
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.player = Player(400, 500)
        self.opponents = [Opponent(random.randint(0, 800), random.randint(-600, -50)) for _ in range(5)]
        self.boss = Boss(300, -100)
        self.shots = []
        self.running = True
    def start(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
    def update(self):
              keys = pygame.key.get_pressed()
              self.player.move(keys)

              for shot in self.shots[:]:
                    shot.move()
                    if shot.y < 0:
                         self.shots.remove(shot)

              for opponent in self.opponents[:]:
                    opponent.move()
                    if self.player.collide(opponent):
                         self.player.lives -= 1
                         self.opponents.remove(opponent)
                         if self.player.lives <= 0:
                              self.is_running = False

                    for shot in self.shots[:]:
                         if shot.hit_target(opponent):
                              self.shots.remove(shot)
                              self.opponents.remove(opponent)
                              self.score += 1
                              if self.score % 5 == 0 and not self.boss:
                                    self.boss = Boss(random.randint(0, 700), -100)

              if self.boss:
                    self.boss.move()
                    if self.player.collide(self.boss):
                         self.player.lives -= 1
                         if self.player.lives <= 0:
                              self.is_running = False

    def draw(self):
              screen = pygame.display.get_surface()
              screen.fill((0, 0, 0))
              self.player.draw(screen)
              for opponent in self.opponents:
                    opponent.draw(screen)
              for shot in self.shots:
                    shot.draw(screen)
              if self.boss:
                    self.boss.draw(screen)

              # Mostrar puntuación y vidas
              score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
              lives_text = self.font.render(f"Lives: {self.player.lives}", True, (255, 255, 255))
              screen.blit(score_text, (10, 10))
              screen.blit(lives_text, (10, 50))

              pygame.display.flip()

    def end_game(self):
              print("Game Over")
              pygame.quit()