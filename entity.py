import pygame

class Entity:
    def __init__(self, x, y, width, height, image_path, speed, game):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.game = game
        self.image= pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, width={self.width}, height={self.height}, speed={self.speed})"
    def __repr__(self):
        return self.__str__()
    
    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.rect.topleft = (self.x, self.y)
    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))
    def update(self):
        self.rect.topleft = (self.x, self.y)