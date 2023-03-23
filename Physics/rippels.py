import enum
from re import L
from numpy import mat
import pygame
import pymunk
from pymunk.body import Body
import time

#Start pygame
pygame.init()

#Make display
HEIGHT = 600
WITDH = 1000
display = pygame.display.set_mode((WITDH,HEIGHT))

#SET FPS
FPS = 1
clock = pygame.time.Clock()

#vars
matrix_x = 20
matrix_y = 20
buffer_sizeX = 25
buffer_sizeY = 25
start = (20,(buffer_sizeY*matrix_y)+20)
balls = []
SIZE = 8


#our pymunk simulation "world" or space
space = pymunk.Space()
#space.gravity = (0,-900)

#CONVERT PYGAME CORDS TO PYMUNK CORDS FUNCTION
def convert_cords(point):
    return point[0], WITDH-point[1]

class Ball(): 
    def __init__(self,x,y, vel, height, direction, force, size=10):
        self.size = size
        self.height = height
        self.direction = direction
        self.force = force
        #A body
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = x,y
        self.body.velocity = vel
        #A shape
        self.shape = pymunk.Circle(self.body,size)
        self.shape.height = 1
        self.shape.elasticity = 1
        self.shape.filter = pymunk.ShapeFilter(group=1)
        #add body and shape to space
        space.add(self.body,self.shape)
    
    def draw(self):
        #show the circle
        x,y = convert_cords(self.body.position)
        if self.direction == "u":
            pygame.draw.circle(display,(0,255,255),(int(x),int(y)), self.height + self.force/10)
        else:
            pygame.draw.circle(display,(0,255,255),(int(x),int(y)), self.height - self.force/10)

#GAME FUNCTION
def game():
    x,y = convert_cords(start)#(300,600))

    for i in range(matrix_y):
        y += buffer_sizeY
        x = start[0]
        for j in range(matrix_x):
            if i == matrix_y-1 and j == 0 or i == matrix_y-1 and j == matrix_x-1:
                balls.append(Ball(x,y,(0,0),10,"u",0,(SIZE)))
            else:
                balls.append(Ball(x,y,(0,0),10,"d",0,(SIZE)))
            x += buffer_sizeX
    
    #PUSH FORCE IS 20
    push_force = 0
    #BALL TO START CYCLE
    og_ball = balls[50]
    #SET FIRST BALLS FORCE
    og_ball.force = push_force

    while True:
        #check to see if user wants to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        display.fill((255,255,255))#draw white background

        mouse_pos = pygame.mouse.get_pos()

        #draw
        for ball in balls:
            ball.draw()
            
        
        #click one ball forceing it down
        #then every ball touching it gets pushed up half its force down
        #then every ball toching them gets pushed down half and so on till force is less than 0.5
        #next the balls will be loop again and the first one will now go up restarting the process

    

        for index, ball in enumerate(balls):
            if ball.direction == "u": #force ball down
                ball.direction = "d"

                #################
                #31 31 33 34 35#
                #26 27 28 29 30#
                #21 22 23 24 25#
                #16 17 18 19 20#
                #11 12 13 14 15#
                #################

                adj_balls = []

                #check for ball next to our ball and give force
                for i in range(8):
                    try:
                        if i == 0:
                            adj_balls.append(balls[index-1])
                        if i == 1:
                            adj_balls.append(balls[index+1])
                        if i == 2:
                            adj_balls.append(balls[index-matrix_x])
                        if i == 3:
                            adj_balls.append(balls[index+matrix_x])
                        if i == 4:
                            adj_balls.append(balls[index-(matrix_x-1)])
                        if i == 5:
                            adj_balls.append(balls[index+(matrix_x+1)])
                        if i == 6:
                            adj_balls.append(balls[index-(matrix_x+1)])
                        if i == 7:
                            adj_balls.append(balls[index+(matrix_x-1)])
                    except:
                        pass


                #add logic to other balls
                for adj_ball in adj_balls:
                    if adj_ball.direction == "u":
                        adj_ball.direction = "d"
                    else:
                        adj_ball.direction = "u"
                    
                    adj_ball.force = ball.force/2
                
                ball.force = ball.force/2
                if ball.force < 1:
                    ball.force = 0
            

        #Update display
        pygame.display.update()

        #FPS TICK
        clock.tick(FPS)
        space.step(1/FPS)

#RUN GAME
game()

pygame.quit()