import pygame
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

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))