import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Torus")

# Define ASCII luminance characters
ascii_chars = "@%#*+=-:. "

# Define rotation matrices
def rotate_x(angle):
    return np.array([[1, 0, 0],
                     [0, math.cos(angle), -math.sin(angle)],
                     [0, math.sin(angle), math.cos(angle)]])

def rotate_y(angle):
    return np.array([[math.cos(angle), 0, math.sin(angle)],
                     [0, 1, 0],
                     [-math.sin(angle), 0, math.cos(angle)]])

def rotate_z(angle):
    return np.array([[math.cos(angle), -math.sin(angle), 0],
                     [math.sin(angle), math.cos(angle), 0],
                     [0, 0, 1]])

class Torus:
    def __init__(self, R1, R2, R, r, speed_x, speed_y, speed_z):
        self.R1 = R1
        self.R2 = R2
        self.R = R
        self.r = r
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_z = speed_z
        self.A = 0  # Initial value for rotation around X-axis
        self.B = 0  # Initial value for rotation around Y-axis

    def calculate_torus_points(self):
        torus_points = []
        for theta in range(0, 360, 10):
            for phi in range(0, 360, 10):
                # Create circle
                x_circle = self.R1 * math.cos(math.radians(theta))
                y_circle = self.R1 * math.sin(math.radians(theta))

                # Create torus vector
                x = (self.R + self.r * math.cos(math.radians(phi))) * math.cos(math.radians(theta))
                y = (self.R + self.r * math.cos(math.radians(phi))) * math.sin(math.radians(theta))
                z = self.r * math.sin(math.radians(phi))
                torus_vector = np.array([[x], [y], [z]])

                # Rotate the torus
                rotation_matrix = rotate_x(self.A) @ rotate_y(self.B) @ rotate_z(self.speed_z)
                rotated_vector = rotation_matrix @ torus_vector

                # Apply projection
                f = 500  # Focal length
                scale = f / (f + rotated_vector[2][0])
                x_proj = int(rotated_vector[0][0] * scale) + self.R2[0]
                y_proj = int(rotated_vector[1][0] * scale) + self.R2[1]

                # Determine illumination (surface normal calculation)
                light_source = np.array([[0], [0], [-1]])  # Light source direction
                surface_normal = torus_vector - np.array([[0], [0], [0]])  # Center of the torus is at the origin
                surface_normal /= np.linalg.norm(surface_normal)
                illumination = np.dot(surface_normal.flatten(), light_source.flatten())
                brightness = int(max(0, illumination) * (len(ascii_chars) - 1))

                # Update color based on rotation
                color_hue = (theta + phi + self.speed_x * 100) % 360  # Use the sum of theta, phi, and X-axis rotation speed for color variation
                color = pygame.Color(0)
                color.hsva = (color_hue, 100, 100, 100)

                # Get the ASCII character based on the brightness
                ascii_char = ascii_chars[brightness]

                torus_points.append((x_proj, y_proj, color, ascii_char))

        return torus_points

# Define torus parameters
R1 = 250  # Radius of the circle
R2 = (width // 2, height // 2)  # Center of the circle
R = 100  # Major radius of the torus
r = 50  # Minor radius of the torus
speed_x = 0.02  # Rotation speed around the X-axis
speed_y = 0.03  # Rotation speed around the Y-axis
speed_z = 0.04  # Rotation speed around the Z-axis

# Main game loop
clock = pygame.time.Clock()
running = True

# Create an instance of the Torus class
torus = Torus(R1, R2, R, r, speed_x, speed_y, speed_z)
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Calculate torus points
    torus_points = torus.calculate_torus_points()

    # Draw the torus
    for point in torus_points:
        x, y, color, ascii_char = point
        screen.set_at((x, y), color)
        pygame.draw.rect(screen, color, (x, y, 1, 1))

    # Update rotation angles
    torus.A += torus.speed_x
    torus.B += torus.speed_y

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(30)

# Quit the game
pygame.quit()