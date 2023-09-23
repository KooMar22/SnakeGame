# Import required modules
from random import randint
from utils import *

# Food class
class Food():
    def __init__(self):
        self.regenerate()

    def regenerate(self):
        random_x = randint(FOOD_SIZE, SCREEN_WIDTH - FOOD_SIZE)
        random_y = randint(FOOD_SIZE, SCREEN_HEIGHT - FOOD_SIZE)
        self.position = (random_x, random_y)

    def draw(self):
        screen.blit(frog_img, (self.position[0] - FOOD_SIZE, self.position[1] - FOOD_SIZE))