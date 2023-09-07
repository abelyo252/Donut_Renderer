import pygame
import colorsys
import math
import itertools
import cv2
import numpy as np

pygame.init()

class DonutAnimation:
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 640
        self.x_separator = 10
        self.y_separator = 20
        self.rows = self.HEIGHT // self.y_separator
        self.columns = self.WIDTH // self.x_separator
        self.screen_size = self.rows * self.columns
        self.x_offset = self.columns / 2
        self.y_offset = self.rows / 2
        self.theta_spacing = 10
        self.phi_spacing = 1
        self.chars = ".,-~:;=!*#$@"
        self.rotation_speed = 0.03
        self.A = 0
        self.B = 0

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Donut')
        self.font = pygame.font.SysFont('Arial', 18, bold=True)

    def hsv2rgb(self, h, s, v):
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return int(r * 255), int(g * 255), int(b * 255)

    def text_display(self, letter, x_start, y_start, color):
        text = self.font.render(str(letter), True, color)
        self.screen.blit(text, (x_start, y_start))





    def run_animation(self):
        run = True
        clock = pygame.time.Clock()

        # Create a video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_out = cv2.VideoWriter('donut_animation.mp4', fourcc, 30.0, (self.WIDTH, self.HEIGHT))

        while run:
            self.screen.fill((0, 0, 0))

            z = [0] * self.screen_size
            b = [(' ', (0, 0, 0))] * self.screen_size

            cos_A = math.cos(self.rotation_speed * self.A)
            sin_A = math.sin(self.rotation_speed * self.A)
            cos_B = math.cos(self.rotation_speed * self.B)
            sin_B = math.sin(self.rotation_speed * self.B)

            hue = (self.A + self.B) / (2 * math.pi)  # Calculate hue based on rotation angle

            for i, j in itertools.product(range(0, 628, self.phi_spacing), range(0, 628, self.theta_spacing)):
                c = math.sin(i)
                d = math.cos(j)
                e = math.sin(self.A)
                f = math.sin(j)
                g = math.cos(self.A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = math.cos(i)
                m = math.cos(self.B)
                n = math.sin(self.B)
                t = c * h * g - f * e
                x = int(self.x_offset + 40 * D * (l * h * m - t * n))
                y = int(self.y_offset + 20 * D * (l * h * n + t * m))
                o = int(x + self.columns * y)
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                if self.rows > y > 0 < x < self.columns and D > z[o]:
                    z[o] = D
                    color = self.hsv2rgb(hue, 1, 1)  # Convert hue to RGB color
                    b[o] = (self.chars[N if N > 0 else 0], color)

            for i, (char, color) in enumerate(b):
                x_start = (i % self.columns) * self.x_separator
                y_start = (i // self.columns) * self.y_separator
                self.text_display(char, x_start, y_start, color)

            pygame.display.update()

            # Convert Pygame surface to numpy array
            frame = pygame.surfarray.array3d(self.screen)
            frame = np.rot90(frame)  # Rotate the frame 90 degrees (optional)

            # Convert the frame to BGR format (required by OpenCV)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            if cv2.waitKey(30) & 0xFF == ord('s'):
                break


            # Save the frame to the video file
            video_out.write(frame)

            self.A += self.rotation_speed
            self.B += self.rotation_speed

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False

            clock.tick(30)
        # Release the video writer
        video_out.release()
 

donut_animation = DonutAnimation()
donut_animation.run_animation()