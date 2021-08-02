import pygame.font

class CreditsAndControlsButton:
    """Display the credits and controlls to the screen."""

    def __init__(self, fbr):
        """Initialize the attributes."""
        # Screen settings.
        self.screen = fbr.screen
        self.screen_rect = self.screen.get_rect()
        
        # Text colors
        self.black = (0, 0, 0)
        self.color1 = (23, 45, 66)
        self.color2 = (42, 73, 102)

        # Text fonts.
        self.font1 = pygame.font.SysFont('Gabriola', 48)
        self.font2 = pygame.font.SysFont('Gabriola', 36)

        # create message 1 and set its position.
        self.msg1 = "     Created By :     "
        self.msg_image1 = self.font1.render(self.msg1, True, self.color1)
        self.msg_image_rect1 = self.msg_image1.get_rect()
        self.msg_image_rect1.center = self.screen_rect.center
        self.msg_image_rect1.top = self.screen_rect.top + 150

        # create message 2 and set its position.
        self.msg2 = "   Chetan Eknath Shegokar   "
        self.msg_image2 = self.font2.render(self.msg2, True, self.color2)
        self.msg_image_rect2 = self.msg_image2.get_rect()
        self.msg_image_rect2.center = self.screen_rect.center
        self.msg_image_rect2.top = self.msg_image_rect1.bottom

        # create message 3 and set its position. 
        self.msg3 = "   Contact Deatils :   "
        self.msg_image3 = self.font1.render(self.msg3, True, self.color1)
        self.msg_image_rect3 = self.msg_image3.get_rect()
        self.msg_image_rect3.center = self.screen_rect.center
        self.msg_image_rect3.top = self.msg_image_rect2.bottom + 20

        # create message 4 and set its position.
        self.msg4 = "   chetanshegokar777@gmail.com   "
        self.msg_image4 = self.font2.render(self.msg4, True, self.color2)
        self.msg_image_rect4 = self.msg_image4.get_rect()
        self.msg_image_rect4.center = self.screen_rect.center
        self.msg_image_rect4.top = self.msg_image_rect3.bottom 
        
        # create message 5 and set its position.
        self.msg5 = "   Images, Sounds & Sprites By :    "
        self.msg_image5 = self.font1.render(self.msg5, True, self.color1)
        self.msg_image_rect5 = self.msg_image5.get_rect()
        self.msg_image_rect5.center = self.screen_rect.center
        self.msg_image_rect5.top = self.msg_image_rect4.bottom + 20

        # create message 6 and set its position.
        self.msg6 = "   Vector Stocks, Game Art 2D, Mixkit   "
        self.msg_image6 = self.font2.render(self.msg6, True, self.color2)
        self.msg_image_rect6 = self.msg_image4.get_rect()
        self.msg_image_rect6.center = self.screen_rect.center
        self.msg_image_rect6.top = self.msg_image_rect5.bottom 

        # Create control 1 and set its position.
        self.ctrl_1 = "Controls"
        self.ctrl_1_image = self.font1.render(self.ctrl_1, True, self.color1)
        self.ctrl_1_rect = self.ctrl_1_image.get_rect()
        self.ctrl_1_rect.center = self.screen_rect.center
        self.ctrl_1_rect.top = self.screen_rect.top + 200

        # Create control 2 and set its position.
        self.ctrl_2 = "   JUMP - SPACE   "
        self.ctrl_2_image = self.font2.render(self.ctrl_2, True, self.color2)
        self.ctrl_2_rect = self.ctrl_2_image.get_rect()
        self.ctrl_2_rect.center = self.screen_rect.center
        self.ctrl_2_rect.top = self.ctrl_1_rect.bottom + 50

        # Create control 3 and set its position.
        self.ctrl_3 = "   PAUSE - P   "
        self.ctrl_3_image = self.font2.render(self.ctrl_3, True, self.color2)
        self.ctrl_3_rect = self.ctrl_3_image.get_rect()
        self.ctrl_3_rect.center = self.screen_rect.center
        self.ctrl_3_rect.top = self.ctrl_2_rect.bottom 

        # Create control 4 and set its position.
        self.ctrl_4 = "   Exit To Desktop - ESC   "
        self.ctrl_4_image = self.font2.render(self.ctrl_4, True, self.color2)
        self.ctrl_4_rect = self.ctrl_4_image.get_rect()
        self.ctrl_4_rect.center = self.screen_rect.center
        self.ctrl_4_rect.top = self.ctrl_3_rect.bottom 

    def display_credits(self):
        """Display Credits to the screen."""
        self.screen.blit(self.msg_image1, self.msg_image_rect1)
        self.screen.blit(self.msg_image2, self.msg_image_rect2)
        self.screen.blit(self.msg_image3, self.msg_image_rect3)
        self.screen.blit(self.msg_image4, self.msg_image_rect4)
        self.screen.blit(self.msg_image5, self.msg_image_rect5)
        self.screen.blit(self.msg_image6, self.msg_image_rect6)

    def display_controlls(self):
        """Display Controlls to the screen."""
        self.screen.blit(self.ctrl_1_image, self.ctrl_1_rect)
        self.screen.blit(self.ctrl_2_image, self.ctrl_2_rect)
        self.screen.blit(self.ctrl_3_image, self.ctrl_3_rect)
        self.screen.blit(self.ctrl_4_image, self.ctrl_4_rect)


