from pdb import line_prefix
import pygame
import pymunk
from tkinter import *
from tkinter import messagebox

#Start pygame
pygame.init()

#Make display
HEIGHT = 500
WITDH = 500
display = pygame.display.set_mode((WITDH,HEIGHT))

#SET FPS
FPS = 80
clock = pygame.time.Clock()

#our pymunk simulation "world" or space
space = pymunk.Space()
#gravity
space.gravity = 0,0

#colors
white = (255, 255, 255)
black = (0,0,0)
green = (0, 255, 0)
blue = (0, 0, 128)

#vars
lines = []
boosts = []
goals = []
player = None
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 15)
lvltext = None
lvltextRect = None
booststext = None
linestext = None
bootstextRect = None
linestextRect = None
level = 1
level_create = 0
makeing_level = False
drawing = True
on = 0
type_on = 1
mute = False
lines_drawn = 0
boosts_drawn = 0
max_boosts = 0
max_lines = 0

class Player(): 
    def __init__(self,pos):
        self.pos = pos
        #A body
        self.body = pymunk.Body()
        self.body.position = pos
        #A shape
        self.shape = pymunk.Circle(self.body,5)
        self.shape.density = 1
        self.shape.elasticity = 0.1
        #collisions
        self.shape.collision_type = 1 
        #add body and shape to space
        space.add(self.body,self.shape)
    
    def draw(self):
        #show the circle
        x,y = convert_cords(self.body.position)
        pygame.draw.circle(display,(65, 47, 108),(x,y), 10)

class Line():
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
        #Line or segment or line segment or line. any one tbh
        self.segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.segment_shape = pymunk.Segment(self.segment_body,pos1, pos2, 5)
        self.segment_shape.elasticity = 1
        #collisions
        self.segment_shape.collision_type = 2
        #add Line to space
        space.add(self.segment_body,self.segment_shape)
    def draw(self):
        #show line
        #x = convert_cords((int(self.segment_shape._get_a()[0]), int(self.segment_shape._get_a()[1])))
        #y = convert_cords((int(self.segment_shape._get_b()[0]), int(self.segment_shape._get_b()[1])))
        x = (self.segment_shape._get_a()[0], self.segment_shape._get_a()[1])
        y = (self.segment_shape._get_b()[0], self.segment_shape._get_b()[1])
        pygame.draw.line(display,(88, 53, 101), x,y, 5)

class Boost(): 
    def __init__(self,pos):
        self.pos = pos
        #A body
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = pos[0],pos[1]
        #A shape
        self.shape = pymunk.Circle(self.body,10)
        self.shape.density = 1
        self.shape.elasticity = 22.5
        #collisions
        self.shape.collision_type = 3 
        #add body and shape to space
        space.add(self.body,self.shape)
    
    def draw(self):
        #show the circle
        x,y = convert_cords(self.body.position)
        pygame.draw.circle(display,(149, 231, 155),(x,y), 10)

class Goal():
    def __init__(self, pos):
        self.pos = pos
        #A body
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = pos[0],pos[1]
        #A shape
        self.shape = pymunk.Circle(self.body,10)
        self.shape.density = 1
        self.shape.elasticity = 10
        #collisions
        self.shape.collision_type = 4 
        #add body and shape to space
        space.add(self.body,self.shape)
    
    def draw(self):
        #show the circle
        x,y = convert_cords(self.body.position)
        pygame.draw.circle(display,(143, 169, 240),(x,y), 10)
  
      
#CONVERT PYGAME CORDS TO PYMUNK CORDS FUNCTION
def convert_cords(point):
    return point[0], point[1]

#levels
def empty_level():
    global player, lines, boosts, goals, text, textRect

    text = font.render('level empty', True, green, blue)
 
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (WITDH // 2, 50)

    player = Player((50, 50))
    lines = []
    boosts = []
    goals = [Goal((WITDH-50,HEIGHT-50))]

def load_level(level):
    global player, lines, boosts, goals, lvltext, lvltextRect, linestext, booststext, bootstextRect, linestextRect, space, drawing, on, type_on, max_boosts, max_lines, lines_drawn, boosts_drawn
    
    boosts_drawn = 0
    lines_drawn = 0

    if level == 1:
        max_lines = 3
        max_boosts = 0
    if level == 2:
        max_lines = 1
        max_boosts = 0
    if level == 3:
        max_lines = 0
        max_boosts = 1
    if level == 4:
        max_lines = 1
        max_boosts = 2
    if level == 5:
        max_lines = 0
        max_boosts = 1
    if level == 6:
        max_lines = 1
        max_boosts = 1
    if level == 7:
        max_lines = 1
        max_boosts = 5
    if level == 8:
        max_lines = 3
        max_boosts = 2
    if level == 9:
        max_lines = 2
        max_boosts = 0
    if level == 10:
        max_lines = 3
        max_boosts = 1
    
    if level == 11:
        max_lines = 10000
        max_boosts = 10000
        Tk().wm_withdraw() #to hide the 
        messagebox.showinfo(':p','Check ur dms 4 prize ;)')
        pygame.quit()
        exit()
        
    space = pymunk.Space()

    lvltext = font.render('level ' + str(level), True, black)
    linestext = font.render('Lines:' + str(max_lines), True, black)
    booststext = font.render("Boots: " + str(max_boosts), True, black)
 
    # create a rectangular object for the
    # text surface object
    lvltextRect = lvltext.get_rect()
    linestextRect = linestext.get_rect()
    bootstextRect = booststext.get_rect()
    
    # set the center of the rectangular object.
    lvltextRect.center = ((WITDH / 2)-90, 20)
    linestextRect.center = (250, HEIGHT-20)
    bootstextRect.center = (100, HEIGHT-20)
    
    lines = []
    boosts = []
    goals = []
    player = None
    drawing = True
    on = 0
    type_on = 1
        
    with open("G:\My Drive\Programing\Personal scripts\others\jeses game\level" + str(level) + ".txt", "r") as f:
        
        content = f.readlines()
        
        #print( ((content[1].replace("\n","")).split("|")) )
        player = Player(( int(((content[0].replace("\n","")).split(","))[0]) , int(((content[0].replace("\n","")).split(","))[1]) ))
        for index,value in enumerate(((content[1].replace("\n","")).split("|"))):
            value = value.split(",")
            try:
                lines.append(Line((int(value[0]),int(value[1])),(int(value[2]),int(value[3]))))
            except:
                pass
        for index,value in enumerate(((content[2].replace("\n","")).split("|"))):
            value = value.split(",")
            try:
                boosts.append(Boost((int(value[0]),int(value[1]))))
            except:
                pass
        for index,value in enumerate(((content[3].replace("\n","")).split("|"))):
            value = value.split(",")
            try:
                goals.append(Goal((int(value[0]),int(value[1])))) 
            except:
                pass 
    
def save_level():
    global lines, boosts, goals, player, level, level_create
    with open("G:\My Drive\Programing\Personal scripts\others\jeses game\level" + str(level_create) + ".txt", "w") as f:
            f.truncate(0)
            
            line_data = ""
            boost_data = ""
            goal_data = ""
            
            for line in lines:
                line_data += "|" + str((str(line.pos1).replace(")",""))).replace("(","") + "," + str((str(line.pos2).replace(")",""))).replace("(","")
            
            for boost in boosts:
                boost_data += "|" + str((str(boost.pos).replace(")","")).replace("(","")) 
            
            for goal in goals:
                goal_data += "|" + str((str(goal.pos).replace(")","")).replace("(","")) 
            
            #save level
            f.write(str((str(player.pos).replace(")","")).replace("(","")) + "\n"  + line_data + "\n" + boost_data + "\n" + goal_data)
            
            f.close()
            
            with open("G:\My Drive\Programing\Personal scripts\others\jeses game\level" + str(level_create) + ".txt", 'r') as f:
                lines = f.readlines()
                lines = [line.replace(' ', '') for line in lines]
            with open("G:\My Drive\Programing\Personal scripts\others\jeses game\level" + str(level_create) + ".txt", 'w') as f:
                f.writelines(lines)
                f.close()
                
        
            level_create += 1

#colission
def collide_ball_boost(arbiter, space, data):
    pass
def collide_ball_goal(arbiter, space, data):
    global level
    level += 1
    load_level(level)          

#GAME FUNCTION
def game():
    global drawing, on, type_on, max_lines, max_boosts, mute, lines_drawn, boosts_drawn
    
    pos1 = (0,1)
    pos2 = (0,0)
    
    handler_ball_boost = space.add_collision_handler(1,3) 
    handler_ball_goal = space.add_collision_handler(1,4)
    handler_ball_boost.separate = collide_ball_boost
    handler_ball_goal.separate = collide_ball_goal
    
    bg = pygame.image.load("G:\My Drive\Programing\Personal scripts\others\jeses game\game_bg.png")
    
    while True:
        handler_ball_boost = space.add_collision_handler(1,3) 
        handler_ball_goal = space.add_collision_handler(1,4)
        handler_ball_boost.separate = collide_ball_boost
        handler_ball_goal.separate = collide_ball_goal
        #check to see if user wants to exit
        for event in pygame.event.get():
            #trun on gravity
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    drawing = False
                    space.gravity = 0,1000
                if event.key == pygame.K_m:
                    if not mute:
                        pygame.mixer.music.set_volume(0)
                        mute = True
                    else:
                        pygame.mixer.music.set_volume(0.3)
                        mute = False
                if event.key == pygame.K_b:
                    type_on = 2
                if event.key == pygame.K_l:
                    type_on = 1
                if event.key == pygame.K_r:
                    load_level(level)
                if event.key == pygame.K_RETURN and makeing_level:
                    save_level()
                    empty_level()
            if event.type == pygame.QUIT:
                return
            #drawing
            if event.type == pygame.MOUSEBUTTONUP and drawing:
                if type_on == 1 and lines_drawn < max_lines:
                    if on == 0:
                        pos1 = pygame.mouse.get_pos()
                        on+=1
                    else:
                        on = 0
                        pos2 = pygame.mouse.get_pos()
                        lines.append(Line(pos1,pos2))
                        lines_drawn += 1
                        
                elif type_on == 2 and drawing and boosts_drawn < max_boosts:
                    boosts.append(Boost(pygame.mouse.get_pos()))
                    boosts_drawn += 1


        display.fill((255,255,255))#draw white background

        #DRAW TEXT and bg
        linestext = font.render('Lines:' + str(max_lines - lines_drawn), True, black)
        booststext = font.render("Boots: " + str(max_boosts - boosts_drawn), True, black)
        display.blit(bg, (0, 0))
        display.blit(lvltext, lvltextRect)
        display.blit(booststext, bootstextRect)
        display.blit(linestext, linestextRect)
        #draw objects
        player.draw()
        for boost in boosts:
            boost.draw()
        for goal in goals:
            goal.draw()
        if on == 1 and drawing: #smth abt cord conversions idk lmao
            templine = Line(pos1, pygame.mouse.get_pos())
            templine.draw()
        for line in lines:
            line.draw()

        #Update display
        pygame.display.update()

        #FPS TICK
        clock.tick(FPS)
        space.step(1/FPS)
    
def tut():
    bg = pygame.image.load("G:\My Drive\Programing\Personal scripts\others\jeses game\game_bg.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                game()
            if event.type == pygame.QUIT:
                return
        
        tuttext1 = font.render("Welcome to GOBAL!", True, black)
        tuttextRect1 = tuttext1.get_rect()
        tuttextRect1.center = ((WITDH / 2), 50)
        tuttext2 = font.render("Controls:", True, black)
        tuttextRect2 = tuttext2.get_rect()
        tuttextRect2.center = ((WITDH / 2), 100)
        tuttext3 = font.render("L: Switch to drawing a line", True, black)
        tuttextRect3 = tuttext3.get_rect()
        tuttextRect3.center = ((WITDH / 2), 130)
        tuttext4 = font.render("B: Switch to drawing a boost", True, black)
        tuttextRect4 = tuttext4.get_rect()
        tuttextRect4.center = ((WITDH / 2), 160)
        tuttext5 = font.render("D: Turn on gravity R: Restart", True, black)
        tuttextRect5 = tuttext5.get_rect()
        tuttextRect5.center = ((WITDH / 2), 190)
        tuttext6 = font2.render("The goal of GOBAL is to get the redish ball to touch the blueish ball", True, black)
        tuttextRect6 = tuttext6.get_rect()
        tuttextRect6.center = ((WITDH / 2), 250)
        tuttext7 = font2.render("with a confined number of lines and boosts", True, black)
        tuttextRect7 = tuttext7.get_rect()
        tuttextRect7.center = ((WITDH / 2), 260)
        tuttext7 = font2.render("Play around with lines and boost to find out how they work", True, black)
        tuttextRect7 = tuttext7.get_rect()
        tuttextRect7.center = ((WITDH / 2), 270)
        tuttext8 = font2.render("Be warned the physics is intentionally scuffed! :) ", True, black)
        tuttextRect8 = tuttext8.get_rect()
        tuttextRect8.center = ((WITDH / 2), 290)
        tuttext9 = font2.render("sry abt how text is drawn", True, black)
        tuttextRect9 = tuttext9.get_rect()
        tuttextRect9.center = ((WITDH / 2), 400)
        tuttext10 = font2.render("smth abt pygame and not bein able to use \+n", True, black)
        tuttextRect10 = tuttext10.get_rect()
        tuttextRect10.center = ((WITDH / 2), 420)
        tuttext11 = font2.render("but it gets fixed after this.", True, black)
        tuttextRect11 = tuttext11.get_rect()
        tuttextRect11.center = ((WITDH / 2), 440)
        tuttext12 = font.render("HIT ANY KEY TO CONTINUE" , True, black)
        tuttextRect12 = tuttext12.get_rect()
        tuttextRect12.center = ((WITDH / 2), 470)
        
        display.blit(bg, (0, 0))
        display.blit(tuttext1, tuttextRect1)
        display.blit(tuttext2, tuttextRect2)
        display.blit(tuttext3, tuttextRect3)
        display.blit(tuttext4, tuttextRect4)
        display.blit(tuttext5, tuttextRect5)
        display.blit(tuttext6, tuttextRect6)
        display.blit(tuttext7, tuttextRect7)
        display.blit(tuttext8, tuttextRect8)
        display.blit(tuttext9, tuttextRect9)
        display.blit(tuttext10, tuttextRect10)
        display.blit(tuttext11, tuttextRect11)
        display.blit(tuttext12, tuttextRect12)
        
        clock.tick(60)
        pygame.display.update()
        
def start_screen():
    bg = pygame.image.load("G:\My Drive\Programing\Personal scripts\others\jeses game\start_screen_bg.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                tut()
            if event.type == pygame.QUIT:
                return

        display.blit(bg, (0, 0))

        clock.tick(60)
        pygame.display.update()

#music 
pygame.mixer.init() 
pygame.mixer.music.load("G:\My Drive\Programing\Personal scripts\others\jeses game\main.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1, 0)

#RUN GAME
load_level(level)
start_screen()

pygame.quit()