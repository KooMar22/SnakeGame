# Import required modules
import sys
import os
import pygame
from pygame.locals import (
    KEYDOWN,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_RETURN,
    K_ESCAPE,
    QUIT,
)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller.
    URL: https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2  # Adjust to MEIPASS2 if not working
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Load the music and ensure it keeps playing
music = pygame.mixer.music.load(resource_path("music\\Zmija_i_zaba.ogg"))
pygame.mixer.music.play(-1)

# Load some images
frog_img = pygame.image.load(resource_path("images\\frog.jpg"))

# Fonts - font, size, bold, italic
GAME_FONT = pygame.font.SysFont("Calibri", 30, True, False)
SCORE_FONT = pygame.font.SysFont("Calibri", 24, True, False)

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 580
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Markanova zmijulja")


# Global variables
FPS = 60
SPEED = 3
SNAKE_SIZE = 10
SNAKE_STARTING_POSITIONS = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                            (SCREEN_WIDTH // 2 - SNAKE_SIZE, SCREEN_HEIGHT // 2),
                            (SCREEN_WIDTH // 2 - 2 * SNAKE_SIZE, SCREEN_HEIGHT // 2)]
FOOD_SIZE = 5
FOOD_DISTANCE_THRESHOLD = 10
INCREASE_MULTIPLIER = 9
PAUSED = False
WON = False
LOST = False

# Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


def display_message(message):
    """Messages formating"""
    screen.fill(BLACK)
    lines = [line.strip() for line in message.split("\n")]
    line_height = GAME_FONT.get_height()
    y_position = (SCREEN_HEIGHT - line_height * len(lines)) // 2

    for line in lines:
        line_text = GAME_FONT.render(line, 1, YELLOW)
        x_position = (SCREEN_WIDTH - line_text.get_width()) // 2
        screen.blit(line_text, (x_position, y_position))
        y_position += line_height

    pygame.display.update()

    # Shorter time delay
    pygame.time.delay(100)