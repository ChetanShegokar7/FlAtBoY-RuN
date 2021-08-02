import pygame
from pygame.sprite import Sprite
from random import randint

class Obstacle(Sprite):
    """Class to create number of obstacles."""
    def __init__(self, fbr):
        """Initialize the attributes."""
        super().__init__()
        # Screen Settings.
        self.screen = fbr.screen
        self.settings = fbr.settings
        self.screen_rect = self.screen.get_rect()

        # Decide the character bottom height according to screen height.
        self.correction = (fbr.background.bg_image_rect.bottom * 12.60)/100
        self.settings.correction = self.correction
        
        # Obstacle color and set its position.
        self.color = self.settings.obstacle_color
        self.rect = pygame.Rect(0, 0, self.settings.obstacle_width,
            self.settings.obstacle_height)
        self.rect.bottom = fbr.background.bg_image_rect.bottom - self.correction
        self.rect.left = self.screen_rect.right

        # convert the x co-ordinate of obstacle into decimal.
        self.x = float(self.rect.x)

        # Create random Obstacles.
        self.random_obstacle()

    def update(self):
        """Update the obstacles position."""
        # Move the obstacles to the left side of the screen.
        self.x -= self.settings.obstacle_speed
        self.rect.x = self.x

    def draw_obstacles(self):
        """Draw the obstacle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def random_obstacle(self):
        """Create obstacles with random height and color."""
        self.settings.obstacle_width = 12
        self.settings.obstacle_height = randint(80, 200)
        random_r = randint(0, 255)
        random_g = randint(0, 255)
        random_b = randint(0, 255)
        self.settings.obstacle_color = (random_r, random_g, random_b)