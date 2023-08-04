import pygame
import pymunk
import pymunk.pygame_util
import math

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
ball1_velocity = (200, 0)  # Initial velocity for ball 1 (positive x-direction)
ball2_velocity = (-100, 0)  # Initial velocity for ball 2 (negative x-direction)

# Set up the display window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Elastic Collision Simulation with Pymunk")

clock = pygame.time.Clock()

# Space for the physics simulation
space = pymunk.Space()
space.gravity = (0, 0)  # Set gravity to 0 to disable gravity

# Create the balls
ball1_body = pymunk.Body(1, 1)  # Mass and moment of inertia are set to 1 for simplicity
ball1_body.position = ball1_x, ball1_y
ball1_shape = pymunk.Circle(ball1_body, ball_radius)
ball1_shape.elasticity = 0.3 # Set the elasticity to 1 for an elastic collision
ball1_body.velocity = ball1_velocity
space.add(ball1_body, ball1_shape)

ball2_body = pymunk.Body(1, 1)
ball2_body.position = ball2_x, ball2_y
ball2_shape = pymunk.Circle(ball2_body, ball_radius)
ball2_shape.elasticity = 0.3
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
    pygame.draw.circle(screen, blue, (int(ball1_body.position.x), int(height - ball1_body.position.y)), ball_radius)
    pygame.draw.circle(screen, red, (int(ball2_body.position.x), int(height - ball2_body.position.y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Set frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
