import pygame.font

class ScoreBoard:
    """Class to prepare score board."""

    def __init__(self, fbr):
        """Initialize the attributes."""
        self.screen = fbr.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = fbr.settings
        self.stats = fbr.stats
        
        # set the player name and high score plyer name to variables.
        self.player_name = fbr.player_name.title()
        self.high_score_player = f"*** {fbr.high_score_player} ***"

        # Set text color and text font.
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('Comic Sans MS', 28)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        
    def prep_score(self):
        # Prepare player Name and score images and set its position.
        # prepare the name image.
        self.player_name_image = self.font.render(self.player_name, True, 
            self.text_color)
        self.player_name_rect = self.player_name_image.get_rect()
        self.player_name_rect.right = self.screen_rect.right - 20
        self.player_name_rect.top = 20

        # Prepare Score image.
        rounded_score = round(self.stats.score, 500)
        score_str = str(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.player_name_rect.bottom 

    def prep_high_score(self):
        # High score Name image and its position.
        self.high_score_player_image = self.font.render(
            self.high_score_player, True, self.text_color)
        self.high_score_player_rect = self.high_score_player_image.get_rect()

        self.high_score_player_rect.center = self.screen_rect.center
        self.high_score_player_rect.top = 20

        # High Score image and its position.
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.center = self.screen_rect.center
        self.high_score_rect.top = self.high_score_player_rect.bottom

    def prep_level(self):
        """Prepare level image from string and set level image position."""
        # level image and its position.
        self.level_image = self.font.render(
            'Level', True, self.text_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.left = self.screen_rect.left + 20
        self.level_image_rect.top = 20

        # level number and its position.
        level_number = str(self.stats.level)
        self.level = self.font.render(level_number, True, self.text_color)
        self.level_rect = self.level.get_rect()
        self.level_rect.top = self.level_image_rect.bottom
        self.level_rect.left = self.screen_rect.left + 20


    def show_score(self):
        """Show the High Scaore to the screen."""
        self.screen.blit(self.player_name_image, self.player_name_rect)
        self.screen.blit(self.score_image, self.score_rect)

        self.screen.blit(self.high_score_player_image, 
            self.high_score_player_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

        self.screen.blit(self.level_image, self.level_image_rect)
        self.screen.blit(self.level, self.level_rect)