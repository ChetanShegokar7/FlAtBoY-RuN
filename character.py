import pygame
from pygame.sprite import Sprite
import sound_effects as se

class Character(Sprite):
    """Class to create Game Character."""
    
    def __init__(self, fbr):
        """Initialize the attributes."""
        super().__init__()

        # screen settings.
        self.screen = fbr.screen
        self.screen_rect = self.screen.get_rect()

        # This variable decides the character bottom heght of the character
        # from the bottom of the screen.
        self.correction = (fbr.background.bg_image_rect.bottom * 12.60)/100

        # Character x, y positions.
        self.character_x = 80
        self.character_y = self.screen_rect.height - self.correction

        # Load character sprites.
        self._load_character_sprites()

        # Index refers to the number of sprite and set image equal to index.
        self.index = 0
        self.image = self.images[self.index]

        # Set the height of the character.
        self.image_rect_y = self.character_y - self.image.get_rect().height
        self.rect = pygame.Rect(self.character_x, self.image_rect_y, 65, 136)
        self.rect.bottom = self.character_y
        
        # variables for gravity and limit the character frames to be updated.
        self.changey = 0
        self.elapsed = 0
        self.elapsed_2 = 0

        self.isjump = False

    def _load_character_sprites(self):
        """Load the character sprites."""
        # Load the character sprites.
        self.images = [
        pygame.image.load('sprites/1.png').convert_alpha(),
        pygame.image.load('sprites/2.png').convert_alpha(),
        pygame.image.load('sprites/3.png').convert_alpha(),
        pygame.image.load('sprites/4.png').convert_alpha(),
        pygame.image.load('sprites/5.png').convert_alpha(),
        pygame.image.load('sprites/6.png').convert_alpha(),
        pygame.image.load('sprites/7.png').convert_alpha(),
        pygame.image.load('sprites/8.png').convert_alpha(),
        pygame.image.load('sprites/9.png').convert_alpha(),
        pygame.image.load('sprites/10.png').convert_alpha(),
        pygame.image.load('sprites/11.png').convert_alpha(),
        pygame.image.load('sprites/12.png').convert_alpha(),
        pygame.image.load('sprites/13.png').convert_alpha(),
        pygame.image.load('sprites/14.png').convert_alpha(),
        pygame.image.load('sprites/15.png').convert_alpha(),
        ]

        # Load the character jump sprite.
        self.image_jump = [
        pygame.image.load('sprites/01.png').convert_alpha(),
        pygame.image.load('sprites/02.png').convert_alpha(),
        pygame.image.load('sprites/03.png').convert_alpha(),
        pygame.image.load('sprites/04.png').convert_alpha(),
        pygame.image.load('sprites/05.png').convert_alpha(),
        pygame.image.load('sprites/06.png').convert_alpha(),
        pygame.image.load('sprites/07.png').convert_alpha(),
        pygame.image.load('sprites/08.png').convert_alpha(),
        pygame.image.load('sprites/09.png').convert_alpha(),
        pygame.image.load('sprites/010.png').convert_alpha(),
        pygame.image.load('sprites/011.png').convert_alpha(),
        pygame.image.load('sprites/012.png').convert_alpha(),
        pygame.image.load('sprites/013.png').convert_alpha(),
        pygame.image.load('sprites/014.png').convert_alpha(),
        pygame.image.load('sprites/015.png').convert_alpha(),
        ]
    
    def update(self):
        """Update the character sprites."""
        self.gravity()

        self.rect.y += self.changey
        self.elapsed += 1
        
        if self.elapsed >= 10:
            # Update the index.
            self.index += 1

            self._switch_sprites()

            self.elapsed = 0

    def _switch_sprites(self):
        """Switch the sprite depending on the condition."""
        # set running sprite to the character.
        if not self.isjump:
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

        # Set jumping sprite to the character.
        if self.isjump:  
            if self.index >= len(self.image_jump):
                self.index = 0
            self.image = self.image_jump[self.index]        
    
    def jump(self):
        """Jump the character."""
        if self.rect.bottom == int(self.character_y):
            self.isjump = True
            self.index = 0
            se.jump.set_volume(1)
            se.jump.play()
            self.changey = -8
   
    def gravity(self):
        """Apply gravity to the character."""
        self.elapsed_2 += 0.2
        
        if self.changey == 0:
            self.changey = 0
        else:
            if self.elapsed_2 >= 0.8:
                self.changey += 0.4
                self.elapsed_2 = 0

        if self.rect.bottom >= self.character_y and self.changey >= 0:
            self.changey = 0
            self.rect.y = self.character_y - self.rect.height
            self.isjump = False

    def default_position(self):
        """Set the character to its default position."""
        self.rect.bottom = self.character_y

        

   
