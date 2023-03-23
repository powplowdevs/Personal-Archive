import os, sys, subprocess
import pygame
from pygame.locals import *
from pygame import mixer
import pymunk
import random
import moviepy.editor
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo

#Start pygame
pygame.init()
mixer.init()

#PLAY INTRO
video = moviepy.editor.VideoFileClip( __file__.replace("rickys_game.py","") + "duck.mp4")
video.preview()

#Make display
HEIGHT = 500
WITDH = 500
root = Tk()
display = pygame.display.set_mode((WITDH,HEIGHT))

#SET FPS
FPS = 50
clock = pygame.time.Clock()

#our pymunk simulation "world" or space
space = pymunk.Space()
space.gravity = 0,-100

#Game vars
balls = []
boxes = []
ball_life = 160
FORCE = -5
tick = 0
floor_state = 1
lives = 3
lvl = 0
ob = 1
spawn_rate = 20
won = False

#CONVERT PYGAME CORDS TO PYMUNK CORDS FUNCTION
def convert_cords(point):
    return point[0], WITDH-point[1]

class Ball(): 
    def __init__(self,x,y, collision_type, vel, color=(255,0,0), life=0):
        #A body
        self.body = pymunk.Body()
        self.body.position = x,y
        self.body.velocity = vel
        self.color = color
        self.life = life
        #A shape
        self.shape = pymunk.Circle(self.body,10)
        self.shape.density = 1
        self.shape.elasticity = 0.3
        #collisions
        self.shape.collision_type = collision_type 
        #add body and shape to space
        space.add(self.body,self.shape)
    
    def draw(self):
        #show the circle
        self.life += 1
        if self.life >= ball_life:
            try:
                space.remove(self.body,self.shape)
            except:
                pass
        else:
            x,y = convert_cords(self.body.position)
            pygame.draw.circle(display,self.color,(int(x),int(y)), 10)

class Box:
    def __init__(self, p1, d=2, life=0, color=(255,0,0)):
        #A body
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = p1[0],p1[1]
        self.color = color
        self.life = life
        #A shape
        self.shape = pymunk.Circle(self.body,50)
        self.shape.density = 1
        self.shape.elasticity = 0.3
        #collisions
        self.shape.collision_type = 2
    def draw(self):
        #show the circle
        self.life += 1
        if self.life >= ball_life:
            try:
                space.remove(self.body,self.shape)
            except:
                pass
        else:
            x,y = convert_cords(self.body.position)
            if self.life == 30:
                #add body and shape to space
                space.add(self.body,self.shape)
            if self.life < 30:
                pygame.draw.circle(display,(100, 75, 150),(int(x),int(y)), 50)
            else:
                pygame.draw.circle(display,self.color,(int(x),int(y)), 50)

class Player(): 
    def __init__(self,x,y, vel, color=(0,0,255)):
        #A body
        self.body = pymunk.Body()
        self.body.position = x,y
        self.body.velocity = vel
        self.color = color
        #A shape
        self.shape = pymunk.Circle(self.body,10)
        self.shape.density = 1
        self.shape.elasticity = 0.5
        #collisions
        self.shape.collision_type = 1 
        #add body and shape to space
        space.add(self.body,self.shape)
    
    def draw(self):
        #show the circle
        x,y = convert_cords(self.body.position)
        pygame.draw.circle(display,self.color,(int(x),int(y)), 10)
        
        
    def fly(self):
        if self.body.velocity[1] < 150:
            self.shape.body.apply_force_at_world_point((0,1000000),self.body.position)
    def steer(self,direction):
        if direction: #right
            if self.body.velocity[0] < 150 and self.body.velocity[1] < 150:
                self.shape.body.apply_force_at_world_point((1000000,0),self.body.position)
        else: #left
            if self.body.velocity[0] > -150 and self.body.velocity[1] > -150:
                self.shape.body.apply_force_at_world_point((-1000000,0),self.body.position)
    def brake(self):
        self.shape.body.apply_force_at_world_point((0,-1000000),self.body.position)

class Line():
    def __init__(self, p1,p2,size=10, color=(255,255,255)):
        #floor or segment or line segment or line. any one tbh
        self.segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.segment_shape = pymunk.Segment(self.segment_body,p1,p2, 5)
        self.segment_shape.elasticity = 1
        self.size = size
        self.color = color
        #collisions
        self.segment_shape.collision_type = 3
        #add floor to space
        space.add(self.segment_body,self.segment_shape)
    def draw(self):
        #show floor
        pygame.draw.line(display, self.color, convert_cords(self.segment_shape._get_a()), convert_cords(self.segment_shape._get_b()), 10)


def player_collide(arbiter, space, data):
    global lives
    lives -= 1
    
def floor_collide(arbiter, space, data):
    global lives
    if floor_state == 3:
        lives -= 1


#GAME FUNCTION
def game():
    global tick, floor_state, lvl, spawn_rate, won, lives, root, FORCE, ball_life, balls, tick, floor_state, lvl, spawn_rate, ob
    
    balls = [Ball(random.randint(30,WITDH-30),HEIGHT+30, 2,(0,FORCE))]
    floor = Line((0,10),(500,10))
    right_wall = Line((500,0),(500,HEIGHT+100))
    left_wall = Line((0,0),(0,HEIGHT+100))
    roof = Line((HEIGHT+50,0),(HEIGHT+50,HEIGHT+100))
    player = Player(WITDH/2,30,(0,0))
    #collisions handler
    player_handler = space.add_collision_handler(1,2) 
    player_handler.separate = player_collide
    floor_handler = space.add_collision_handler(1,3) 
    floor_handler.separate = floor_collide

    while True:
        #check to see if user wants to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w]:
                    player.fly()
            if pressed[pygame.K_a]:
                player.steer(False)
            if pressed[pygame.K_d]:
                player.steer(True)
            if pressed[pygame.K_s]:
                player.brake()
        
        display.fill((0,0,0))#draw black background

        #draw objects
        player.draw()
        if ob == 1:
            [ball.draw() for ball in balls]
        else:
            [box.draw() for box in boxes]
        floor.draw()
        right_wall.draw()
        left_wall.draw()
        roof.draw()
        
        #tick sim
        tick += 1
        
        if lives <= 0:
            lives = 3
            showinfo("Game over", "You dided to the duck kings red balls lmao L")
            root.destroy()
            pygame.quit()
            subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"') 
    
        
        if tick == 70:
            floor_state = 2
            floor.color = (255,165,0)
            right_wall.color = (255,165,0)
            left_wall.color = (255,165,0)
            roof.color = (255,165,0)
        if tick > 120:
            floor_state = 3
            floor.color = (255,255,0)
            right_wall.color = (255,255,0)
            left_wall.color = (255,255,0)
            roof.color = (255,255,0)

        if tick>=ball_life:
            tick = 0
            lvl+=1
            print(lvl, ob)
            spawn_rate -= 1
            floor_state = 1
            floor.color = (255,255,255)
            right_wall.color = (255,255,255)
            left_wall.color = (255,255,255)
            roof.color = (255,255,255)
            if lvl == 15 and ob==2:
                won = True
                break
            elif lvl == 18:
                lvl = 1
                ob+=1
                lives = 3
                spawn_rate = 20
                ball_life = 100
                for ball in balls:
                    try:
                        space.remove(ball.body,ball.shape)
                    except:
                        pass

        elif tick%spawn_rate == 0 and ob == 1:
            balls.append(Ball(random.randint(30,WITDH-30),HEIGHT+30, 2,(0,FORCE)))
        elif tick%spawn_rate == 0 and ob == 2:
            boxes.append(Box((random.randint(0,WITDH), random.randint(0,HEIGHT))))

        #Update display
        pygame.display.update()

        #FPS TICK
        clock.tick(FPS)
        space.step(1/FPS)

#RUN GAME
mixer.music.load( __file__.replace("rickys_game.py","") + "song.wav")
mixer.music.set_volume(0.3)
mixer.music.play()
game()
  

if won:
    # video = moviepy.editor.VideoFileClip( __file__.replace("rickys_game.py","") + "end.mp4")
    # video.preview()
    showinfo("Ending", "As the duck king sets fire to your home you take a moment out of the little time you have left to live, you relize that the duck king isnt a duck but a goose. All along he was just a misundersood biracial duck that was a goose that was also a king. As you sit there and watch you and your family burn alive you cant help but feel bad, not becuse of the duck king but because you are wathcing you family burn to death. Happy birthday ricky! (;")
    pygame.quit()


