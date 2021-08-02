import pygame

pygame.mixer.init()

# Load background music.
background_music = pygame.mixer.music.load('sound/background_music.mp3')

# Load Sounds
jump = pygame.mixer.Sound('sound/player jump.wav')
down = pygame.mixer.Sound('sound/player down.wav')
game_pause = pygame.mixer.Sound('sound/game pause.wav')
click = pygame.mixer.Sound('sound/click.wav')
credits = pygame.mixer.Sound('sound/credits.mp3')

# Load menu music and set volume to 0.4.
menu = pygame.mixer.Sound('sound/menu music.mp3')
menu.set_volume(0.4)
