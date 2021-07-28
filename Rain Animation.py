# Pygame program to create infinite rain Animation.

# ***Instructions***
# Press q to Exit.
# Press SPACE for Thunder.

import sys
import pygame

from rain_resource import RainDrop
from random import randint
import sound_effect as se

class RainGrid:
    """Class to create infinite rain."""

    def __init__(self):
        """Initialize the attributes."""
        pygame.init()
        
        # Create screen.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.bg_color = (0, 0, 0) # Black color

        # Set Caption to the screen.
        pygame.display.set_caption('Raindrop Grid')

        # Create sprite Group holding raindrops.
        self.raindrops = pygame.sprite.Group()

        self._create_rain()
        self._music()
    
    def rain(self):
        """Main loop for infinite rain."""
        while True:
            self._check_events()
            self._update_rain()
            self._update_screen()

    def _music(self):
        """Play the background music."""
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)

    def _check_events(self):
        """Check for events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # Set key Q to exit.
                if event.key == pygame.K_q:
                    sys.exit()

                # Set the background color to white and play thunder sound.    
                elif event.key == pygame.K_SPACE:
                    self.bg_color = (255, 255, 255)
                    se.thunder.play()

            elif event.type == pygame.KEYUP:
                # Set the background to black after releasing the SPACE Key.
                if event.key == pygame.K_SPACE:
                    self.bg_color = (0, 0, 0)

    def _create_rain(self):
        """Create rain drop Grid."""
        # Instance of RainDrop class
        raindrop = RainDrop(self)

        # Calculate horizontal available space and number of drops per row.
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.screen_width 
        number_drops = available_space_x // (2 * raindrop_width)

        # Calculate vertical available space and number of rows.
        available_space_y = self.screen_height // 2
        number_rows = available_space_y // (2 * raindrop_height)

        # Nested loop to create rain Grid.
        for row_number in range(number_rows):
            for drop_number in range(number_drops):
                self._create_raindrop(drop_number, row_number)
 
    def _create_raindrop(self, drop_number, row_number):
        """Create raindrop and it to raindrops Group."""
        raindrop = RainDrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        # randint() function used to get random value.
        raindrop.x = randint(0, self.screen_width)
        raindrop.rect.x = raindrop.x
        raindrop.y = randint(0, self.screen_height)
        raindrop.rect.y =  raindrop.y
        self.raindrops.add(raindrop)

    def _update_rain(self):
        """Update raindrop position."""
        self.raindrops.update()

        for raindrop1 in self.raindrops.sprites():
            if raindrop1.check_edges():
                self._change_position(raindrop1)

    def _change_position(self, raindrop1):
        """
        if the raindrop disapper from the bottom it moves the drop to top again.
        """
        raindrop1.y = 0

    def _update_screen(self):
        """Update the screen."""
        self.screen.fill(self.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    rg = RainGrid()
    rg.rain()