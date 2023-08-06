import pygame
import pymunk
from segment import StaticSegment
from textinput import Input
import time
scr_wd, scr_ht = 800, 800
pygame.init()
display=pygame.display.set_mode((800,800))
clock=pygame.time.Clock()
space=pymunk.Space()
space.gravity = (0,0) 


FPS=100
def convert_coordinates(point):
    return point[0],600-point[1]
class Ball():
    def __init__(self,x,y,color,velocity,ball_radius,mass,elasticity):
        self.color=color
        self.body=pymunk.Body()
        self.body.position=x,y
        self.body.velocity=velocity
        self.shape=pymunk.Circle(self.body,ball_radius)
        self.shape.mass=mass
        self.shape.elasticity=elasticity
        self.ball_radius=ball_radius
        # self.shape.filter=pymunk.ShapeFilter(categories=category,mask=mask)
        space.add(self.body,self.shape)
    def draw(self):
        pos=self.body.position
        pygame.draw.circle(display,self.color,convert_coordinates(pos),self.ball_radius)

def game(B1_mass, B2_mass, B1_vel_x, B1_vel_y, B2_vel_x, B2_vel_y,B1_elas,B2_elas,B1_x,B1_y,B2_x,B2_y,B1_rad,B2_rad):
    ball1=Ball(B1_x,B1_y,(255,0,0),(B1_vel_x,B1_vel_y),B1_rad,B1_mass,B1_elas)
    ball2=Ball(B2_x,B2_y,(255,100,0),(B2_vel_x,B2_vel_y),B2_rad,B2_mass,B2_elas)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        display.fill((255,255,255))
        ball1.draw()
        ball2.draw()
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)
def userInput():
    pygame.init()
    display = pygame.display.set_mode((scr_wd, scr_ht))
    num = 14
    inputs = [Input("Ball1 mass = "),Input("Ball2 mass = "), Input("Velocity (x)  of Ball1= "),Input("Velocity (y) of Ball1 = "),
              Input("Velocity (x)  of Ball2= "),Input("Velocity (y) of Ball2 = "),Input("Elasticity Ball1= "),Input("Elasticity Ball2= "),
              Input("Initial position(x) of Ball1="),Input("Initial position(y) of Ball1="),Input("Initial position(x) of Ball2="),Input("Initial position(y) of Ball2="),
              Input("Radius of Ball1= "),Input("Radius of Ball2= ")]
    initial = 10,20
    temp=1
    x=0
    for box in inputs:
        box.setRect( initial[0], initial[1],width=50,height=40)
        if(temp):
            initial = initial[0]+400, initial[1]
            temp=0

        else:
            initial = initial[0]-400, initial[1]

            initial = initial[0], initial[1] + 80
            temp=1

        

    clock = pygame.time.Clock()

    active = True
    inp = []
    i = 0
    while active:
        inputs[i].drawCursor = True
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
                    inputs[i].drawCursor = False
                    i = (i + 1) % num
                    inputs[i].drawCursor = True

                elif event.key == pygame.K_UP:
                    inputs[i].drawCursor = False
                    if i > 0:
                        i -= 1
                    inputs[i].drawCursor = True

                elif event.key == pygame.K_DOWN:
                    inputs[i].drawCursor = False
                    if i < num - 1:
                        i += 1
                    inputs[i].drawCursor = True
                else:
                    inputs[i].text +=  event.unicode
        if active:
            display.fill((2, 2, 80))
            for rect in inputs:
                rect.draw(display)
            pygame.display.flip()
            clock.tick(FPS)

    # print(inp)
    inp = [ float(i) for i in inp]
    return inp[0], inp[1], inp[2] , inp[3] , inp[4], inp[5], inp[6], inp[7],inp[8], inp[9], inp[10] , inp[11] , inp[12], inp[13]
if __name__ == "__main__":
    B1_mass, B2_mass, B1_vel_x, B1_vel_y, B2_vel_x, B2_vel_y,B1_elas,B2_elas,B1_x,B1_y,B2_x,B2_y,B1_rad,B2_rad  = userInput()
    # print( ht, vel_x, vel_y)
    game(B1_mass, B2_mass, B1_vel_x, B1_vel_y, B2_vel_x, B2_vel_y,B1_elas,B2_elas,B1_x,B1_y,B2_x,B2_y,B1_rad,B2_rad)
    time.sleep(1)  # Pause30 seconds
    pygame.quit()
