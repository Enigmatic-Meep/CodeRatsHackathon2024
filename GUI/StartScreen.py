import pygame

from SceneManager import SceneManager
from Scene import Scene
from Button import Button
from GameScreen import GameScreen

class StartScreen(Scene):
    def __init__(self, scene_manager):
        # Set window title
        pygame.display.set_caption("RATorical Quest - Start Screen")

        # Set Scene Manager Reference
        self.scene_manager = scene_manager

        # Set font and colors
        self.font = pygame.font.Font(None, 40)  # Choose a font or path to a font file
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.scale = 15

        # Load title image
        self.startScreenImage = pygame.image.load("png/StartScreen.png")

        # Set game to be running
        self.running = True

        # Create buttons using the Button class
        self.start_button = Button("Start", (scene_manager.screen_width // 2 - 50, scene_manager.screen_height // 2 + 80), self.white, (100, 100, 100), self.handle_start_click)

    def draw(self, screen, events):
        # Fill screen with color
        screen.fill(0)

        # Draw background image
        screen.blit(self.startScreenImage, (0, 0))

        # Draw buttons
        self.start_button.draw(screen)  # Call the Button class's draw method

    def handle_events(self, event):
        # Check for button clicks only upon mouse button events
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.start_button.handle_click(event)  # Pass the event to handle click state

    def handle_start_click(self):
        # Perform action when start button is clicked
        print("Start button clicked!")
        # game_screen = GameScreen(self.scene_manager)  # Create GameScreen instance
        self.scene_manager.set_scene("game_screen")  # Switch scene using scene manager