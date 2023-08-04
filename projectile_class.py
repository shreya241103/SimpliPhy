import pygame
import pymunk
import math
pygame.init()
space = pymunk.Space()
space.gravity = 0, -1000
SCREEN = WIDTH, HEIGHT = 600, 600
u = 50
g = 9.8
display = pygame.display.set_mode(SCREEN)
clock = pygame.time.Clock()
FPS = 60
BLACK = (18, 18, 18)
WHITE=(255,255,255)
origin = (150, 350)
radius = 250
font = pygame.font.SysFont('arial', 20)
class Projectile:
    def __init__(self, u, theta):
        super(Projectile, self).__init__()

        self.u = u
        self.theta = convert_radian(abs(theta))
        self.x, self.y = origin
        self.color = WHITE
        self.k = self.path()
        self.range = self.x + abs(self.range1())
        self.path = []
        self.temp=0
        self.len = 3
        self.body = pymunk.Body()
        self.body.position = self.x, HEIGHT - self.y  # Invert y-coordinates for pymunk
        self.body.velocity = self.u * math.cos(self.theta), self.u * math.sin(self.theta)
        self.shape = pymunk.Circle(self.body, 5)
        self.range = self.x + abs(self.range1())
        self.shape.density = 1
        self.shape.elasticity = 1
        space.add(self.body, self.shape)

    def range1(self):
        range_ = ((self.u ** 2) * 2 * math.sin(self.theta) * math.cos(self.theta)) / g
        return round(range_, 2)

    def path(self):
        return round(g /  (2 * (self.u ** 2) * (math.cos(self.theta) ** 2)), 4)

    def position(self, x):
        return x * math.tan(self.theta) - self.k * x ** 2

    def update(self):
        if self.x >= self.range:
            self.len = 0
        self.x += self.len
        self.temp = self.position(self.x - origin[0])
        
        self.path.append((int(self.x), int(self.y-abs(self.temp))))
        self.path = self.path[-50:]

        pygame.draw.circle(display, self.color, self.path[-1], 5)
        for pos in self.path[:-1]:
            pygame.draw.circle(display, WHITE, pos, 1)

def convert_radian(angle):
    return math.radians(angle)
def get_angle(pos, origin):
        x, y = pos
        ox, oy = origin
        return math.degrees(math.atan2(y-oy, x-ox))

