import pygame
import pymunk
from main import simulate_bounce

# Initialize Pygame
pygame.init()

# Set up screen dimensions for the menu and applications
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
menu_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu Bar")

# Define colors
WHITE = (255, 255, 255)

# Pymunk space for application1
space1 = pymunk.Space()

# Frames per second for applications
FPS = 50

# Function for application1
def application1():
    simulate()

# Function for application2
def application2():
    return_to_menu = False

    while not return_to_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return_to_menu = True

        # Your application2 code here

# Main menu loop
def main_menu():
    current_application = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Check if the user clicked on a button in the menu
                if 200 < x < 400 and 100 < y < 150:
                    current_application = "app1"
                elif 200 < x < 400 and 200 < y < 250:
                    current_application = "app2"

        menu_screen.fill(WHITE)  # Fill the menu screen with a background color

        # Draw menu buttons or other UI elements
        pygame.draw.rect(menu_screen, (0, 0, 255), pygame.Rect(200, 100, 200, 50))
        pygame.draw.rect(menu_screen, (0, 0, 255), pygame.Rect(200, 200, 200, 50))

        # Draw text on buttons
        font = pygame.font.SysFont(None, 30)
        text1 = font.render("Application 1", True, (255, 255, 255))
        text2 = font.render("Application 2", True, (255, 255, 255))
        menu_screen.blit(text1, (240, 110))
        menu_screen.blit(text2, (240, 210))

        pygame.display.flip()

        # Handle logic and rendering for the selected application
        if current_application == "app1":
            application1()
            current_application = None  # Reset the current_application to None when returning to the menu

        elif current_application == "app2":
            application2()
            current_application = None  # Reset the current_application to None when returning to the menu

if __name__ == "__main__":
    main_menu()
