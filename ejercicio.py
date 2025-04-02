import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Disparos")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clase base Entity
class Entity:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

# Clase Character
class Character(Entity):
    def __init__(self, x, y, image_path, lives):
        super().__init__(x, y, image_path)
        self.lives = lives
        self.is_alive = True

    def shoot(self):
        return Shot(self.x + self.rect.width // 2, self.y, "assets/shot.png")

    def collide(self, other):
        return self.rect.colliderect(other.rect)

# Clase Player
class Player(Character):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/player.png", lives=3)
        self.score = 0

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.move(-5, 0)
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.rect.width:
            self.move(5, 0)
        if keys[pygame.K_UP] and self.y > 0:
            self.move(0, -5)
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.rect.height:
            self.move(0, 5)

# Clase Opponent
class Opponent(Character):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/opponent.png", lives=1)
        self.is_star = False

    def move(self):
        self.y += 2
        if self.y > HEIGHT:
            self.y = -self.rect.height
            self.x = random.randint(0, WIDTH - self.rect.width)

# Clase Boss
class Boss(Opponent):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("assets/boss.png")
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self):
        self.y += 4
        if self.y > HEIGHT:
            self.y = -self.rect.height
            self.x = random.randint(0, WIDTH - self.rect.width)

# Clase Shot
class Shot(Entity):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)

    def move(self):
        self.y -= 10

    def hit_target(self, target):
        return self.rect.colliderect(target.rect)

# Clase Game
class Game:
    def __init__(self):
        self.player = Player(WIDTH // 2, HEIGHT - 100)
        self.opponents = [Opponent(random.randint(0, WIDTH - 50), random.randint(-150, -50)) for _ in range(5)]
        self.shots = []
        self.score = 0
        self.is_running = True
        self.font = pygame.font.Font(None, 36)
        self.boss = None

    def start(self):
        while self.is_running:
            self.update()
            self.draw()
        self.end_game()

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
                        self.boss = Boss(random.randint(0, WIDTH - 100), -100)

        if self.boss:
            self.boss.move()
            if self.player.collide(self.boss):
                self.player.lives -= 1
                if self.player.lives <= 0:
                    self.is_running = False

    def draw(self):
        screen.fill(BLACK)
        self.player.draw(screen)
        for opponent in self.opponents:
            opponent.draw(screen)
        for shot in self.shots:
            shot.draw(screen)
        if self.boss:
            self.boss.draw(screen)

        # Mostrar puntuación y vidas
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        lives_text = self.font.render(f"Lives: {self.player.lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))

        pygame.display.flip()

    def end_game(self):
        print("Game Over")
        pygame.quit()

# Ejecutar el juego
if __name__ == "__main__":
    game = Game()
    game.start()