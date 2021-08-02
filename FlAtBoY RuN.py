# Created By : Chetan Shegokar
# Email : chetanshegokar777@gmail.com

import sys
import os
from time import sleep
import pygame
import json

from settings import Settings
from background import Background
from obstacles import Obstacle
import sound_effects as se
from character import Character
from game_stats import GameStats
from button import Button
from score_board import ScoreBoard
from credits_and_controls import CreditsAndControlsButton

class FlatBoyRun:
    """The main class for FlAtBoY RuN Game."""

    def __init__(self):
        """Initializing the attributes."""
        # Change the command prompt text color to green.
        os.system('color 0a')

        # Take name as an input from command prompt.
        text = "\nCreated By :\nChetan Eknath Shegokar\n\nEmail :"
        text += "\nchetanshegokar777@gmail.com\n\n\t\t\t*** Welcome to FlAtBoY"
        text += " RuN ***\t\t\t\n\n\t\tEnter Your Name :  "       
        self.player_name = input(text)

        pygame.init()
        self.settings = Settings()

        # Screen settings.
        self.screen = pygame.display.set_mode((1366, 786), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("FlAtBoY RuN")
        
        # Creating class instance.
        self.background = Background(self)
        self.obstacles = pygame.sprite.Group()
        
        self.character = Character(self)
        self.character_sprite = pygame.sprite.Group(self.character)

        self.stats = GameStats(self)
        self.credits_and_controls = CreditsAndControlsButton(self)
        
        # Try to import high score details if available.
        try:
            self.high_score_player = None
            self._load_name_and_high_score()
        except:
            None

        self.sb = ScoreBoard(self)

        self.level = 0

        # Varible to limit frames per second.
        self.clock = pygame.time.Clock()
        self.FPS = 240

        self._buttons()
        self._initialize_background()
        
    def _load_name_and_high_score(self):
        """Load the high score and player name if available."""
        with open('high_score/high_score.json') as file:
            high_score = json.load(file)
        
        for key, value in high_score.items():
            self.high_score_player = key
            self.stats.high_score = value

    def _buttons(self):
        """Create all buttons and set its position."""
        self.play_button = Button(self, "Play")
        self.play_button.msg_image_rect.top = self.screen_rect.top + 250

        self.controlls_button = Button(self, "Controls")
        self.controlls_button.msg_image_rect.top = (
            self.play_button.msg_image_rect.bottom)

        self.credits_button = Button(self, "Credits")
        self.credits_button.msg_image_rect.top = (
            self.controlls_button.msg_image_rect.bottom)
        
        self.quit_button = Button(self, "Quit")
        self.quit_button.msg_image_rect.top = (
            self.credits_button.msg_image_rect.bottom)

        self.back_button = Button(self, "Back")
        self.back_button.msg_image_rect.top = self.screen_rect.bottom - 300
    
    def _initialize_background(self):
        """Initialize the background."""
        self.base = pygame.Rect(0, self.character.character_y, 
            self.settings.screen_width, (self.settings.screen_height - 
                self.character.character_y)) 
        self.base_color = (255, 255, 255)
        
        if self.stats.game_active:
            self._create_obstacle()
            self._play_music()
        
        if not self.stats.game_active:
            se.menu.play(-1)
       
    def run(self):
        """The main loop for FlAtBoY RuN game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                if not self.stats.game_pause:
                    self.background.update()
                    self._update_character()
                    self._update_obstacles()
                    self._update_score()
                    self._update_level()
                    self._detect_collisions()
            
            self._update_screen()

    def _update_level(self):
        """As game progress level is increased."""
        if self.stats.score != 0 and self.stats.score % 500 == 0:
            level_up = self.stats.score / 500
            self.level = int(level_up)
            se.game_pause.set_volume(0.3)
            se.game_pause.play()
        
        # After evey level increase increase game speed.
        if self.stats.level < self.level:
            self.settings.increase_speed() 

        self.stats.level = self.level 
        self.sb.prep_level()

    def _update_score(self):
        """Update score as game progress."""
        # If you wan't to get points after jumping from an obstacle, remove 
        # the code from the comment given below.
        # Note enabling this comment may skip level.
        # [10] points per jump.

        # for obstacle in self.obstacles.sprites():
        #     if obstacle.rect.left == self.character.rect.left:
        #         self.stats.score += 10
        
        self.time = pygame.time.get_ticks()
        
        if self.time % 10 == 0:
            self.stats.score += 1
            
        self.sb.prep_score()

        # If score increase more than highscore replace highscore with score.
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.sb.high_score_player = self.sb.player_name
            self.sb.prep_high_score()
    
    def _dump_name_and_high_score(self):
        """Store name and high score of player in a file."""
        with open('high_score/high_score.json', 'w') as file:
            high_score = {
            self.sb.player_name : self.stats.score,
            }
            
            for key, value in high_score.items():
                json.dump(high_score, file)
                   
    def _play_music(self):
        """Play Background music."""
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)

    def _check_events(self):
        """Check for mouse and keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mousebuttondown_events(event, mouse_pos)
    
    def _check_keydown_events(self, event):
        """Check for keydown events."""
        if event.key == pygame.K_ESCAPE:
            if self.stats.score >= self.stats.high_score:
                self._dump_name_and_high_score()
                    
            sys.exit()
        
        elif event.key == pygame.K_SPACE:
            if self.stats.game_active:
                self._jump()
        
        elif event.key == pygame.K_p:
            self._game_pause()  

    def _check_mousebuttondown_events(self, event, mouse_pos):
        """Check for events when mouse button is clicked."""
        if not self.stats.game_active:
            if not self.stats.credits_active and not self.stats.controlls_active:
                self._check_quit_button(mouse_pos)

            if not self.stats.credits_active and not self.stats.controlls_active:
                self._check_play_button(mouse_pos)
                self._check_controll_button(mouse_pos)
                self._check_credits_button(mouse_pos)
            
            elif self.stats.credits_active:
                self._checK_back_button(mouse_pos)

            elif self.stats.controlls_active:
                self._checK_back_button(mouse_pos)      

    def _game_pause(self):
        """Pause the game."""
        if not self.stats.game_pause:
            self.stats.game_pause = True
            se.menu.stop()
            pygame.mixer.music.pause()
            se.game_pause.play()
        else:
            self.stats.game_pause = False
            pygame.mixer.music.unpause()
            se.game_pause.play()
            
            if not self.stats.game_active:
                se.menu.play(-1)

    def _check_quit_button(self, mouse_pos):
        """What will happen if clicked quit button is stored here."""
        # Detect mouse cursor and collision with any button.
        buttoun_clicked = self.quit_button.msg_image_rect.collidepoint(
            mouse_pos)
        
        if buttoun_clicked and not self.stats.game_active:
            se.click.play()
            sleep(0.5)
            sys.exit()

    def _check_play_button(self, mouse_pos):
        """What should happen if clicked play button is stored here."""
        buttoun_clicked = self.play_button.msg_image_rect.collidepoint(
            mouse_pos)

        if buttoun_clicked and not self.stats.game_active:
            pygame.mixer.fadeout(2000)
            se.click.play()
            sleep(2)
            
            self.stats.game_active = True       
            self._initialize_background()
            pygame.mouse.set_visible(False)

    def _check_controll_button(self, mouse_pos):
        """What should happen if controll button is clicked is stored here."""
        button_clicked = self.controlls_button.msg_image_rect.collidepoint(
            mouse_pos)

        if button_clicked and not self.stats.game_active:
            se.click.play()
            self.stats.controlls_active = True

    def _check_credits_button(self, mouse_pos):
        """What happen after clicking credits button is stored here."""
        button_clicked = self.credits_button.msg_image_rect.collidepoint(
            mouse_pos)

        if button_clicked and not self.stats.game_active:
            se.click.play()
            se.menu.stop()           
            se.credits.play(-1)
            self.stats.credits_active = True

    def _checK_back_button(self, mouse_pos):
        """What should happend after clicking back button is here."""
        button_clicked = self.back_button.msg_image_rect.collidepoint(
            mouse_pos)
        
        if button_clicked and self.stats.credits_active:
            se.click.play()
            se.credits.stop()
            se.menu.play(-1)
            self.stats.credits_active = False

        if button_clicked and self.stats.controlls_active:
            se.click.play()
            self.stats.controlls_active = False
            
    def _jump(self):
        """jump the character."""
        self.character.jump()

    def _update_character(self):
        """Update the character sprites."""
        self.character_sprite.update()     

    def _create_obstacle(self):
        """Create new obstacles."""
        new_obstacle = Obstacle(self)
        self.obstacles.add(new_obstacle)

    def _update_obstacles(self):
        """Update Position of obstacles."""
        self.obstacles.update()

        # If obstacle cross the screen remove the obstacle.
        for obstacle in self.obstacles.copy():
            if obstacle.rect.x <= 0:
                self.obstacles.remove(obstacle)

        # After specific distance create new obstacle.
        if len(self.obstacles) <= self.settings.obstacles_allowed:
            for obstacle in self.obstacles:
                if obstacle.rect.x <= (self.settings.screen_width / 
                    self.settings.arrive_new_obstacle):
                    self._create_obstacle()
                    break

    def _detect_collisions(self):
        """
        Detect character and obstacle collision and what should happen after 
        that is store here.
        """
        self.collisions = pygame.sprite.groupcollide(
            self.character_sprite, self.obstacles, False, False)
        
        if self.collisions:
            pygame.mixer.music.stop()
            se.down.set_volume(0.5)
            se.down.play()
            self.stats.game_active = False
            sleep(2)
            self.obstacles.empty()
            self.character.default_position()
            pygame.mouse.set_visible(True)
            
            # If the score is greter than high score store the high score .
            if self.stats.score >= self.stats.high_score:
                self._dump_name_and_high_score()
            
            self.stats.reset_stats()
            self.level = 0
            self.sb.prep_level()
            self.sb.prep_score()
            se.menu.play(-1)
            self.settings._initialize_dynamic_settings()         

    def _update_screen(self):
        """Display every object of the game to the screen."""
        # Fill the screen with backround color.
        self.screen.fill(self.settings.bg_color)
        pygame.draw.rect(self.screen, self.base_color, self.base)
        
        # Draw the background image to the screen.
        self.background.render()
        
        # Draw obstacles to the screen.
        for obstacle in self.obstacles.sprites():
            obstacle.draw_obstacles()

        # The above line will fill the background of character so you can test
        # the character and understand how it hits to obstacle.
        # pygame.draw.rect(self.screen, self.settings.bg_color, 
        #     self.character.rect)

        self.character_sprite.draw(self.screen)
        self.sb.show_score()

        if not self.stats.game_active:
            self._what_to_display_if_game_not_active()
 
        # Limit the frames per second.
        self.clock.tick(self.FPS)
        
        # Update the screen to the most recent event.
        pygame.display.flip()

    def _what_to_display_if_game_not_active(self):
        """If game not active draw buttons to the screen."""
        if not self.stats.credits_active and not self.stats.controlls_active:
            self.play_button.draw_button()
            self.quit_button.draw_button()
            self.credits_button.draw_button()
            self.controlls_button.draw_button()
            
        if self.stats.credits_active:
            self.credits_and_controls.display_credits()
            self.back_button.draw_button()
            
        if self.stats.controlls_active:
            self.credits_and_controls.display_controlls()
            self.back_button.draw_button() 

if __name__ == '__main__':
    """
    Instead of using main function, using this if statement makes program 
    less complicated.
    """
    fbr = FlatBoyRun()
    fbr.run()