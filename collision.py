import pygame
import pymunk
import pymunk.pygame_util
import math
from textinput import Input
import time
scr_wd, scr_ht = 800, 800

# Frames per second - frequency
FPS = 50
def simulate_collision(B1_mass, B2_mass, B1_vel_x, B1_vel_y, B2_vel_x, B2_vel_y,B1_elas,B2_elas ):
    # Initialize pygame
    pygame.init()

    # Window dimensions
    width, height = 800, 600

    # Colors
    white = (255, 255, 255)
    blue = (0, 0, 255)
    red = (255, 0, 0)

    # Ball parameters
    ball_radius = 20
    ball1_x, ball1_y = 100, height // 2  # Initial position of ball 1
    ball2_x, ball2_y = width - 100, height // 2  # Initial position of ball 2
    ball1_velocity = (B1_vel_x,B1_vel_y)  # Initial velocity for ball 1 (positive x-direction)
    ball2_velocity = (B2_vel_x, B2_vel_y)  # Initial velocity for ball 2 (negative x-direction)

    # Set up the display window
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Elastic Collision Simulation with Pymunk")

    clock = pygame.time.Clock()

    # Space for the physics simulation
    space = pymunk.Space()
    space.gravity = (0,0)  # Set gravity to 0 to disable gravity

    # Create the balls
    ball1_body = pymunk.Body(1, 1)  # Mass and moment of inertia are set to 1 for simplicity
    ball1_body.position = ball1_x, ball1_y
    ball1_shape = pymunk.Circle(ball1_body, ball_radius)
    ball1_shape.elasticity = B1_elas # Set the elasticity to 1 for an elastic collision
    ball1_body.velocity = ball1_velocity
    ball1_body.mass=B1_mass
    space.add(ball1_body, ball1_shape)

    ball2_body = pymunk.Body(1, 1)
    ball2_body.position = ball2_x, ball2_y
    ball2_shape = pymunk.Circle(ball2_body, ball_radius)
    ball2_shape.elasticity = B2_elas
    ball2_body.mass=B2_mass
    ball2_body.velocity = ball2_velocity
    space.add(ball2_body, ball2_shape)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the physics simulation
        space.step(1 / 60.0)

        # Check for collision
        distance = math.sqrt((ball2_body.position.x - ball1_body.position.x) ** 2 + (ball2_body.position.y - ball1_body.position.y) ** 2)
        if distance <= 2 * ball_radius:
            # Calculate new velocities after collision (elastic collision)
            normal = (ball2_body.position - ball1_body.position).normalized()
            relative_velocity = ball2_body.velocity - ball1_body.velocity
            impulse_magnitude = -pymunk.Vec2d.dot(relative_velocity, normal) * (1 + ball1_shape.elasticity) * (1 + ball2_shape.elasticity)
            impulse = impulse_magnitude * normal
            ball1_body.apply_impulse_at_local_point(impulse, (0, 0))  # Apply impulse to ball 1
            ball2_body.apply_impulse_at_local_point(-impulse, (0, 0))  # Apply impulse to ball 2

        # Clear the screen
        screen.fill(white)

        # Draw the balls
        pygame.draw.circle(screen, blue, (float(ball1_body.position.x), float(height - ball1_body.position.y)), ball_radius)
        pygame.draw.circle(screen, red, (float(ball2_body.position.x), float(height - ball2_body.position.y)), ball_radius)

        # Update the display
        pygame.display.flip()

        # Set frame rate
        clock.tick(120)

    # Quit pygame
    pygame.quit()

def userInput():
    pygame.init()
    display = pygame.display.set_mode((scr_wd, scr_ht))
    num = 8
    inputs = [ Input("Ball1 mass = "),Input("Ball2 mass = "), Input("Velocity (x)  of Ball1= "),Input("Velocity (y) of Ball1 = "),
              Input("Velocity (x)  of Ball2= "),Input("Velocity (y) of Ball2 = "),Input("Elasticity Ball1= "),Input("Elasticity Ball2= ")]
    initial = 300,20
    for box in inputs:
        box.setRect( initial[0], initial[1])
        initial = initial[0], initial[1] + 100

    clock = pygame.time.Clock()

    active = True
    inp = []
    i = 0
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    inputs[i].text = inputs[i].text[:-1]
                elif event.key == 13:
                    inp = [ box.text for box in inputs ]
                    active = False
                    break
                elif event.key == pygame.K_TAB:
                    i = (i + 1) % num
                elif event.key == pygame.K_UP:
                    if i > 0:
                        i -= 1
                elif event.key == pygame.K_DOWN:
                    if i < num - 1:
                        i += 1
                else:
                    inputs[i].text +=  event.unicode
        if active:
            display.fill((255, 255, 255))
            for rect in inputs:
                rect.draw(display)
            pygame.display.flip()
            clock.tick(FPS)

    # print(inp)
    inp = [ float(i) for i in inp]
    return inp[0], inp[1], inp[2] , inp[3] , inp[4], inp[5], inp[6], inp[7]
if __name__ == "__main__":
    B1_mass, B2_mass, B1_vel_x, B1_vel_y, B2_vel_x, B2_vel_y,B1_elas,B2_elas  = userInput()
    # print( ht, vel_x, vel_y)
    simulate_collision(B1_mass, B2_mass, B1_vel_x, B1_vel_y, B2_vel_x, B2_vel_y,B1_elas,B2_elas )
    time.sleep(1)  # Pause for 30 seconds
    pygame.quit()

