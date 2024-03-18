import pygame_textinput
import pygame

from pygame.font import Font  # Import Font class for custom font

from SceneManager import SceneManager
from Scene import Scene
from Button import Button

# Set screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

class GameScreen(Scene):
    def __init__(self, scene_manager):
        # Set window title
        pygame.display.set_caption("RATorical Quest - Game Screen")

        # Set Scene Manager Reference
        self.scene_manager = scene_manager

        # Set font and colors
        self.font = pygame.font.Font(None, 40)  # Choose a font or path to a font file
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.scale = 15

        # Load background image
        self.gameScreenImage = pygame.image.load("png/GameScreen.png")

        # Create text-input object
        self.textinput = pygame_textinput.TextInputVisualizer()

        # Initialize list of user inputted words
        self.user_words = []

        # Create timer
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 1000)  # 1 second timer
        self.countdown_time = 10  # countdown duration (seconds)
        self.time_remaining = self.countdown_time  # Keep track of remaining time

    def draw(self, screen, events):
        # Fill screen with color
        screen.fill(0)

        self.textinput.update(events)

        # Draw background image
        screen.blit(self.gameScreenImage, (0, 0))

        # Blit its surface onto the screen
        screen.blit(self.textinput.surface, ((screen_width // 2 - 50, screen_height // 2 + 80)))

        # Timer countdown
        if self.time_remaining > 0:
            time_surface = self.font.render(f"Time Remaining: {self.time_remaining}", True, (255, 255, 255))
            screen.blit(time_surface, (20, 50))  # Adjust position

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == self.timer_event:
            self.time_remaining -= 1

            # Check if countdown has reached 0
            if self.time_remaining == 0:
                # Perform actions when countdown finishes (e.g., game over)
                print("Game Over!")

                # Print list of user inputs
                for word in self.user_words:
                    print(f"{word}, ")

                # Optionally stop the timer here
                pygame.time.set_timer(self.timer_event, 0)

                # end_screen = EndScreen(self.scene_manager)
                self.scene_manager.set_scene("end_screen")


        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Print and capture user input
            print(f"Word inputted: {self.textinput.value}")
            self.user_words.append(self.textinput.value)
            
            # Decide if input is a match
            if self.textinput.value == "password":
                print(f"Correct Word!")
            
            # Reset user input
            self.textinput.value = ""
                