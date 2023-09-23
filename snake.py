# Import required modules
import math
import pygame
from utils import *


# Snake class
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.segments = []
        self.prev_positions = []  # Store previous positions of segments
        self.create_snake()
        self.head = self.segments[0]
        self.direction = RIGHT

    def create_snake(self):
        """Create the snake"""
        for position in SNAKE_STARTING_POSITIONS:
            self.add_segment(position)

    def reset(self):
        """Reset the snake"""
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def draw(self):
        """Draw the snake to the screen"""
        # Draw the snake using images for head and body
        for segment in self.segments:
            pygame.draw.rect(screen, GREEN, segment)

    def add_segment(self, position):
        """Add new segments to the snake"""
        new_segment = pygame.Rect(position[0], position[1], SNAKE_SIZE, SNAKE_SIZE)
        self.segments.append(new_segment)
        self.prev_positions.append(position)  # Store the initial position

    def extend(self):
        """Extend using the last previous position"""
        for _ in range(INCREASE_MULTIPLIER):
            self.add_segment(self.prev_positions[-1])

    def move(self):
        """Move the snake"""
        # Store the previous positions of the segments
        self.prev_positions = [segment.topleft for segment in self.segments]

        if self.direction == UP:
            self.head.y -= SPEED
        elif self.direction == DOWN:
            self.head.y += SPEED
        elif self.direction == LEFT:
            self.head.x -= SPEED
        elif self.direction == RIGHT:
            self.head.x += SPEED

        # Move the rest of the segments based on the previous positions
        for i in range(1, len(self.segments)):
            self.segments[i].topleft = self.prev_positions[i - 1]

    def up(self):
        if self.direction != DOWN:
            self.direction = UP

    def down(self):
        if self.direction != UP:
            self.direction = DOWN

    def left(self):
        if self.direction != RIGHT:
            self.direction = LEFT

    def right(self):
        if self.direction != LEFT:
            self.direction = RIGHT

    def update(self):
        key = pygame.key.get_pressed()
        if key[K_UP]:
            self.up()
        elif key[K_DOWN]:
            self.down()
        elif key[K_LEFT]:
            self.left()
        elif key[K_RIGHT]:
            self.right()

    def distance(self, point):
        """Check distance"""
        return math.sqrt((float(self.head.left) - point[0]) ** 2
                         + (float(self.head.top) - point[1]) ** 2)

    def collide_with_wall(self):
        """Check for collision with wall"""
        if (self.head.x >= SCREEN_WIDTH or self.head.x <= 0 or
                self.head.y >= SCREEN_HEIGHT or self.head.y <= 0):
            return True
        return False

    def collision_with_body(self):
        """Check for collision with tail (exclude the head)"""
        return self.head in self.segments[1:]