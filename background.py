import pygame

class Background:
    """Class to create scrolling background towards left."""
    
    def __init__(self, fbr):
        """Initialize the attributes."""
        self.screen = fbr.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = fbr.settings

        # load the background image and transform to fullscreen and set 
        # its initial position.
        self.bg_img = pygame.image.load('images/background.jpg').convert()
        self.bg_image = pygame.transform.scale(self.bg_img, (
            self.settings.screen_width, self.settings.screen_height))
        self.bg_image_rect = self.bg_image.get_rect()

        # x,y co-ordinates for background image.
        self.bgY1 = 0
        self.bgX1 = 0
        
        self.bgY2 = 0
        self.bgX2 = self.bg_image_rect.width

    def update(self):
        """Make the background scrolling toward left."""
        self.bgX1 -= self.settings.scrolling_speed
        self.bgX2 -= self.settings.scrolling_speed
        if self.bgX1 <= -self.bg_image_rect.width:
            self.bgX1 = self.bg_image_rect.width
        if self.bgX2 <= -self.bg_image_rect.width:
            self.bgX2 = self.bg_image_rect.width

    def render(self):
        """Display the background image to the screen."""
        self.screen.blit(self.bg_image, self.screen_rect) 
        self.screen.blit(self.bg_image, (self.bgX1, self.bgY1))
        self.screen.blit(self.bg_image, (self.bgX2, self.bgY2))
        