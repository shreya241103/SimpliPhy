import pygame

class Input:
    def __init__(self,
                 name = "Input: ",
                 size = 40,
                 font_face = None,
                 color = (2, 2, 80)):
        self.name = name
        self.font = pygame.font.Font(font_face, size)
        self.text = ''
        self.color = color

    def setText(self, txt):
        self.text = txt

    def getText(self):
        return self.text

    def setRect(self, left, top, width = 400, height = 50):
        self.rect = pygame.Rect(left, top,
                                width, height)
    def draw(self, display):
        pygame.draw.rect(display,
                         self.color,
                         self.rect)
        txt_surface = self.font.render( self.name + " " + self.text,
                                       True,
                                       (255, 255, 255))
        display.blit(txt_surface,
                     (self.rect.x, self.rect.y))
        # print(self.rect.x, self.rect.y)
        self.rect.w = max( 400,
                           txt_surface.get_width()+10)
