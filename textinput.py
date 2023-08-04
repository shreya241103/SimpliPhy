import pygame
import time
class Input:
    def __init__(self,
                 name = "Input: ",
                 size = 25,
                 font_face = None,
                 color = (2, 2, 80)):
        self.name = name
        self.font = pygame.font.Font(font_face, size)
        self.text = ''
        self.color = color
        self.drawCursor = False

    def setText(self, txt):
        self.text = txt

    def getText(self):
        return self.text

    def setRect(self, left, top, width = 400, height = 40):
        self.rect = pygame.Rect(left, top,
                                width, height)
        self.height = height
        x, y = self.rect.topright
        self.cursor = pygame.Rect(  (x, y),
                                    (3, self.rect.height + 20))

    def draw(self, display):
        pygame.draw.rect(display,
                         self.color,
                         self.rect)
        txt_surface = self.font.render( self.name + " " + self.text,
                                        True,
                                        (255, 255, 255))
        display.blit( txt_surface,
                      (self.rect.x, self.rect.y))
        self.cursor.topleft = self.rect.topright

        self.rect.w = max( self.height,
                           txt_surface.get_width() + 10)

        if self.drawCursor:
            if time.time() % 1 > 0.5:
                text_rect = txt_surface.get_rect(topleft = (self.rect.x + 5, self.rect.y + 10))
                self.cursor.midleft = text_rect.midright
                pygame.draw.rect(display,
                                (255, 255, 255),
                                 self.cursor)
