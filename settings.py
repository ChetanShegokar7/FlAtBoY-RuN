class Settings:
    """All Settings For FlAtBoY RuN are stored in this class."""
    def __init__(self):
        # screen settings.
        self.screen_width = 800
        self.screen_heiht = 600
        
        # Background settings.
        self.scrolling_speed = 1
        self.bg_color = (0, 0, 0)

        # obstacles settings.
        self.obstacles_allowed = 1
        self.arrive_new_obstacle = 2
        self.obstacle_width = 10
        self.obstacle_height = 100  
        self.obstacle_color = (255, 255, 255)
        self.obstacle_speed = self.scrolling_speed

        # How quickly the game speeds up.
        self.speedup_scale = 1.2

        self._initialize_dynamic_settings()

    def _initialize_dynamic_settings(self):
        """The settings which change during the game are stored here."""
        self.scrolling_speed = 1
        self.arrive_new_obstacle = 2
        self.obstacle_speed = 1

    def increase_speed(self):
        """Increase the game speed."""
        self.scrolling_speed *= self.speedup_scale
        self.arrive_new_obstacle *= self.speedup_scale
        self.obstacle_speed *= self.speedup_scale

