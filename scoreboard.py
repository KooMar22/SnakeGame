# Import required modules
import sys
import os
from utils import *


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



# Define Scoreboard class
class Scoreboard():
    
    def __init__(self):
        self.score = 0
        self.read_score()
        self.display_score()

    def display_score(self):
        """Display score to the game"""
        # Render the text. "True" for anti-aliasing text. yellow color
        text = SCORE_FONT.render(f"Score: {self.score} High Score: {self.high_score}",
                                 True, YELLOW)
        # Put the image of the text on the screen at x-center, y-5
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 5))

    def read_score(self):
        """Read score from file"""
        with open(resource_path("score.txt")) as score_data:
            self.high_score = int(score_data.read())
    
    def write_score(self):
        """Write score to file"""
        with open(resource_path("score.txt"), mode="w") as score_data:
            score_data.write(f"{self.high_score}")

    def reset_score(self):
        """Reset the score on new game, set new high score if score is larger"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()
        self.score = 0
        self.display_score()
    
    def increase_score(self):
        """Increase score"""
        self.score += 1
        self.display_score()