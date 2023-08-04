import pymunk
import pygame

class Ball:
    def __init__(self, space,
                 radius = 30,
                 pos = (100, 100),
                 color = (255, 0, 0),
                 velocity = (0, 0),
                 collision_type = 1,
                 density = 1,
                 elasticity = 1):
        self.body = pymunk.Body()
        self.body.position = pos
        self.body.velocity = velocity
        self.shape = pymunk.Circle( self.body,
                                    radius)
        self.shape.density = density
        self.shape.elasticity = elasticity
        self.shape.collision_type = collision_type
        self.color = color
        self.vel_history = {}
        self.pos_history = {}
        self.pos_history = {}
        space.add(self.body, self.shape)

    def getPosition(self):
        return self.body.position

    def drawBall(self, display):
        _ , scr_ht = display.get_size()
        x, y = self.trans_coord(self.getPosition(), scr_ht)
        pygame.draw.circle(display,
                           self.color,
                           (x, y),
                           self.shape.radius)

    def trans_coord(self, coord, scr_ht):
        return int(coord[0]), int(scr_ht - coord[1])
