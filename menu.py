import pygame
import pymunk
from main import *
from projectile import running
from collision import *
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
    ht, vel_x, vel_y = userInput()
    # print( ht, vel_x, vel_y)
    simulate_bounce(ht, (vel_x, vel_y))

# Function for application2
def application2():
    running()
    return_to_menu = False

# Function for application3
def application3():
    # Add your code for game 3 here
    B1_mass, B2_mass, B1_vel_x, B1_vel_y, B2_vel_x, B2_vel_y,B1_elas,B2_elas,B1_x,B1_y,B2_x,B2_y,B1_rad,B2_rad  = userInput()
    # print( ht, vel_x, vel_y)
    game(B1_mass, B2_mass, B1_vel_x, B1_vel_y, B2_vel_x, B2_vel_y,B1_elas,B2_elas,B1_x,B1_y,B2_x,B2_y,B1_rad,B2_rad)
    time.sleep(1)  # Pause for 30 seconds
    return_to_menu = False

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
                elif 200 < x < 400 and 300 < y < 350:  # Button for Game 3
                    current_application = "app3"

        menu_screen.fill(WHITE)  # Fill the menu screen with a background color

        # Draw menu buttons or other UI elements
        pygame.draw.rect(menu_screen, (0, 0, 255), pygame.Rect(200, 100, 200, 50))
        pygame.draw.rect(menu_screen, (0, 0, 255), pygame.Rect(200, 200, 200, 50))
        pygame.draw.rect(menu_screen, (0, 0, 255), pygame.Rect(200, 300, 200, 50))  # Button for Game 3

        # Draw text on buttons
        font = pygame.font.SysFont(None, 30)
        text1 = font.render("Game 1", True, (255, 255, 255))
        text2 = font.render("Game 2", True, (255, 255, 255))
        text3 = font.render("Game 3", True, (255, 255, 255))  # Text for Game 3
        menu_screen.blit(text1, (240, 110))
        menu_screen.blit(text2, (240, 210))
        menu_screen.blit(text3, (240, 310))  # Position for Game 3

        pygame.display.flip()

        # Handle logic and rendering for the selected application
        if current_application == "app1":
            application1()
            current_application = None  # Reset the current_application to None when returning to the menu

        elif current_application == "app2":
            application2()
            current_application = None  # Reset the current_application to None when returning to the menu

        elif current_application == "app3":  # Handle Game 3
            application3()
            current_application = None  # Reset the current_application to None when returning to the menu

if __name__ == "__main__":
    main_menu()