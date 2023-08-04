import pymunk
import pygame

class StaticSegment:
    def __init__(self,
                 space,
                 p1,
                 p2,
                 width = 0,
                 collision_type = None,
                 elasticity = 1
                 ):
        self.body = pymunk.Body( body_type= pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body,
                                    p1,
                                    p2,
                                    width)
        self.shape.elasticity = elasticity
        if collision_type: self.shape.collision_type = collision_type
        space.add(self.body, self.shape)

    def trans_coord(self, coord, scr_ht):
        return int(coord[0]), int(scr_ht - coord[1])

    def drawSegment(self, display, color = (0, 0, 0)):
        ''' Draws Horizontal Segment '''
        _, scr_ht = display.get_size()
        left_end = self.shape.a
        right_end = self.shape.b
        width = int(self.shape.radius)
        # coord_left = shape.body.position + shape.a.rotated(shape.body.angle)
        # coord_right = shape.body.position + shape.b.rotated(shape.body.angle)
        coord_left = left_end[0], left_end[1] + width/2
        coord_right = right_end[0], right_end[1] + width/2
        pygame.draw.line(   display,
                            color,
                            self.trans_coord(coord_left, scr_ht),
                            self.trans_coord(coord_right, scr_ht),
                            width)