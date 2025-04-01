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

    class Opponent(Character):
        def __init__(self, x, y, width, height, image_path, speed, game, lives, is_alive):
            super().__init__(x, y, width, height, image_path, speed, game, lives, is_alive)

        def collide(self, projectile):
            if self.rect.colliderect(projectile.rect):
                self.lives -= 1
                if self.lives <= 0:
                    self.is_alive = False
                    self.game.score += 1  # Increment the score
                return True
            return False
        class Boss(Opponent):
            def __init__(self, x, y, width, height, image_path, speed, game, lives, is_alive, special_attack_power):
                super().__init__(x, y, width, height, image_path, speed, game, lives, is_alive)
                self.special_attack_power = special_attack_power

            def collide(self, projectile):
                if self.rect.colliderect(projectile.rect):
                    self.lives -= 1
                    if self.lives <= 0:
                        self.is_alive = False
                        self.game.score += 5  # Increment the score more for defeating the boss
                    return True
                return False

            def special_attack(self):
                    # Implement the special attack logic
                    print("Boss is using a special attack!")
                    # Example: Reduce player lives or create a powerful projectile
                    if self.game.player.is_alive:
                        self.game.player.lives -= self.special_attack_power