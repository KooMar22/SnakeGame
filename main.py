# Import required modules
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from utils import *


# Instantiate objects
SPRITES = pygame.sprite.Group()
clock = pygame.time.Clock()
snake = Snake()
frog = Food()
scoreboard = Scoreboard()


def handle_game_end(scoreboard):
    """Handle game end events"""
    message = ""
    if scoreboard.score > scoreboard.high_score:
        message = f"""Congratulations! You have beaten the high score and WON!
                    New high score is: {scoreboard.score}.
                    Press 'ENTER' to play again or 'ESCAPE' to quit."""
    else:
        message = f"""Your score was {scoreboard.score}. You have LOST!
                    Press 'ENTER' to play again or 'ESCAPE' to quit."""

    display_message(message)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_RETURN:
                waiting = False
                return True  # Player wants to play again
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                waiting = False
                return False  # Player wants to quit


def game():
    """Run the game loop"""
    global SPEED, PAUSED
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                scoreboard.read_score()
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    scoreboard.reset_score()
                    running = False
                elif event.key == K_SPACE:
                    PAUSED = not PAUSED
                    if PAUSED:
                        pygame.mixer.music.pause()
                        snake.speed = 0
                    else:
                        pygame.mixer.music.unpause()
                        snake.speed = 3

        if not PAUSED:
            # Clear the screen
            screen.fill(BLACK)

            frog.draw()
            snake.draw()
            snake.move()
            snake.update()

            # Detect collision with food
            if snake.distance(frog.position) < FOOD_DISTANCE_THRESHOLD:
                frog.regenerate()
                snake.extend()
                scoreboard.increase_score()

            # Check for collision with wall or tail
            if snake.collide_with_wall() or snake.collision_with_body():
                result = handle_game_end(scoreboard)
                if not result:
                    running = False
                else:
                    scoreboard.reset_score()
                    snake.reset()

            # Display the score
            scoreboard.display_score()

            # Update the display
            pygame.display.update()

            clock.tick(FPS)


def main():
    """Main loop, responsible for welcome message"""
    global running
    running = True
    # Display the welcome message
    message = """Welcome to the Markanova zmijulja game.
                The goal is to beat the current high score.
                Use arrow keys to move, SPACE to (un)pause the game.
                Press "ENTER" to start the game."""

    display_message(message)

    while running:
        # Wait for the player to press ENTER
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_RETURN:
                    waiting = False
                elif event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    running = False
                    waiting = False
        
        if running:
            game()
        
    pygame.quit()


if __name__ == "__main__":
    main()