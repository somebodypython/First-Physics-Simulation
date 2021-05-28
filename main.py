import pygame
import pymunk
import sys


# Classes
class Ball:
    def __init__(self, pos_x, pos_y, color):
        self.body = pymunk.Body(1, 1, body_type = pymunk.Body.DYNAMIC)
        self.body.position = (pos_x, pos_y)
        self.shape = pymunk.Circle(self.body, 20)
        self.shape.elasticity = 1
        space.add(self.body, self.shape)
        self.color = color

    def show(self):
        pygame.draw.circle(screen, self.color, self.body.position, 20)


class Static_wall:
    def __init__(self, p1, p2):
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, p1, p2, 5)
        self.shape.elasticity = 1
        space.add(self.body, self.shape)

    def show(self):
        pygame.draw.line(screen, item_color, self.shape.a, self.shape.b, 5)


# Initialization
pygame.init()

# Constants
WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()

# Colors
bg_color = 20, 20, 30
item_color = 200, 200, 200
red = 255, 100, 100
blue = 100, 100, 255

# Pymunk variables and shit
space = pymunk.Space()
space.gravity = (0, 500)

# Some more nerd shit
ball = Ball(100, 0, red)
ball2 = Ball(800, 0, blue)
wall = Static_wall([0, 300], [425, 500])
wall2 = Static_wall([900, 300], [475, 500])
wall_l = Static_wall([0, -50], [0, 300])
wall_r = Static_wall([900, -50], [900, 300])
wall_t = Static_wall([0, -50], [900, -50])


# Some Functions
def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def update():
    screen.fill(bg_color)
    clock.tick(FPS)


def draw():
    ball.show()
    ball2.show()
    wall.show()
    wall2.show()
    wall_l.show()
    wall_r.show()
    space.step(1/60)


# Loop
def main():
    running = True
    while running:
        quit()
        update()
        draw()
        pygame.display.flip()


main()
