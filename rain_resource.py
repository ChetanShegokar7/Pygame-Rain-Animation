import pygame
from pygame.sprite import Sprite
from random import randint

class RainDrop(Sprite):
    """Create RainGrid Class."""
    def __init__(self, rd_grid):
        """Initialize the attributes."""
        super().__init__()
        self.screen = rd_grid.screen
        self.raindrop_speed = randint(4, 8)

        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        """Move the raindrops downwards."""
        self.y += self.raindrop_speed 
        self.rect.y = self.y

    def check_edges(self):
        """Check for the bottom edge."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True