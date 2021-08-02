import pygame.font

class Button:
    """Take the message from user and create buttons."""

    def __init__(self, fbr, msg):
        """Initialize the attributes."""
        self.screen = fbr.screen
        self.screen_rect = self.screen.get_rect()
        
        # Text color to black.
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('Comic Sans MS', 48)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Convert the string into an image and set the image position."""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        """Display all buttons to the screen."""
        self.screen.blit(self.msg_image, self.msg_image_rect)

