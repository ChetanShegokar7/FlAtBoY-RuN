class GameStats:
    """Store Game Statistcs like score, level and game activity."""
    
    def __init__(self, fbr):
        """Initialize the attributes."""
        self.settings = fbr.settings
        self.game_active = False
        self.game_pause = False
        self.credits_active = False
        self.controlls_active = False
        self.score = 0
        self.high_score = 0
        self.reset_stats()

        self.level = 0
       
    def reset_stats(self):
        """Reset score and level."""
        self.score = 0
        self.level = 0




