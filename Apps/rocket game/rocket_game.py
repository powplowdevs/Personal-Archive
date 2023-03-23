import pygame
import pymunk

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
space.gravity = 0,-100

class Rocket(): 
    def __init__(self, mode, fule, direction, mass, height, width):
        #vars
        self.mode = mode
        self.fule = fule
        self.direction = direction
        self.mass = mass
        self.height = height
        self.width = width
        #A shape
        self.shape = pymunk.Poly.create_box(None, size=(50, 10))
        self.shape.elasticity = 0
        self.moment = pymunk.moment_for_poly(self.mass, self.shape.get_vertices())
        #A body
        self.body = pymunk.Body(self.mass, self.moment)
        self.shape.body = self.body
        self.shape.body.position = 240,10
        #add body and shape to space
        space.add(self.body,self.shape)
    
    def draw(self):
        #show the circle
        x,y = convert_cords(self.body.position)
        pygame.draw.polygon(display, [255, 0, 0], [ (int(x),int(y)) , (int(x)-self.width,int(y)) , (int(x)-self.width,int(y)-self.height), (int(x),int(y)-self.height)])
    
    def fly(self):
        if self.mode == False:
            if self.body.velocity[0] < 150 and self.body.velocity[1] < 150 and self.body.velocity[0] > -150 and self.body.velocity[1] > -150:
                self.shape.body.apply_force_at_local_point((0, 400), (0, -100))
    def steer(self,direction):
        if self.mode == True:
            if self.direction: #right
                if self.body.velocity[0] < 150 and self.body.velocity[1] < 150 and self.body.velocity[0] > -150 and self.body.velocity[1] > -150:
                    self.shape.body.apply_force_at_local_point((-400, 0), (100, 0))
            else: #left
                if self.body.velocity[0] < 150 and self.body.velocity[1] < 150 and self.body.velocity[0] > -150 and self.body.velocity[1] > -150:
                    self.shape.body.apply_force_at_local_point((400, 0), (100, 0))
    def brake(self):
        if self.mode == False:
            self.shape.body.apply_force_at_local_point((0, -400), (0, -100))
        else:
            if self.direction: #right
                self.shape.body.apply_force_at_local_point((400, 0), (100, 0))
            else: #left
                self.shape.body.apply_force_at_local_point((-400, 0), (100, 0))

class Floor():
    def __init__(self):
        #floor or segment or line segment or line. any one tbh
        self.segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.segment_shape = pymunk.Segment(self.segment_body,(0,5), (500, 5), 5)
        self.segment_shape.elasticity = 1
        #add floor to space
        space.add(self.segment_body,self.segment_shape)
    def draw(self):
        #show floor
        pygame.draw.line(display, (0,0,0), convert_cords(self.segment_shape._get_a()), convert_cords(self.segment_shape._get_b()), 5)

class Wall():
    def __init__(self, pos1, pos2):
        #floor or segment or line segment or line. any one tbh
        self.segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.segment_shape = pymunk.Segment(self.segment_body,pos1, pos2, 5)
        self.segment_shape.elasticity = 1
        #add floor to space
        space.add(self.segment_body,self.segment_shape)
    def draw(self):
        #show floor
        pygame.draw.line(display, (255,255,0), convert_cords(self.segment_shape._get_a()), convert_cords(self.segment_shape._get_b()), 5)



#CONVERT PYGAME CORDS TO PYMUNK CORDS FUNCTION
def convert_cords(point):
    return point[0], WITDH-point[1]

#GAME FUNCTION
def game():
    rocket = Rocket(True, 100,False, 1, 35, 15)
    floor = Floor()
    walls = []
    #Wall((100,5),(100,250)), Wall((100,250),(200,250)), Wall((200,250),(200,450))
    drawing = True
    second_click = False
    pos1 = None
    pos2 = None
    while drawing:
        ev = pygame.event.get()
        display.fill((255,255,255))#draw white background
        #draw objects
        rocket.draw()
        floor.draw()
        #Update display
        pygame.display.update()
        #FPS TICK
        clock.tick(FPS)
        space.step(1/FPS)
        for event in ev:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_e]:
                drawing = False
            if event.type == pygame.MOUSEBUTTONUP:
                if second_click == False:
                    pos1 = convert_cords(pygame.mouse.get_pos())
                    second_click = True
                else:
                    second_click = False
                    pos2 = convert_cords(pygame.mouse.get_pos())
                    walls.append(Wall(pos1,pos2))
            display.fill((255,255,255))#draw white background
            #draw objects
            rocket.draw()
            floor.draw()
            for wall in walls:
                wall.draw()
            #Update display
            pygame.display.update()
            #FPS TICK
            clock.tick(FPS)
            space.step(1/FPS)
    

    while True:
        #check to see if user wants to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w]:
                    rocket.fly()
            if pressed[pygame.K_z]:
                rocket.direction = True
                rocket.steer(True)
            if pressed[pygame.K_x]:
                rocket.direction = False 
                rocket.steer(False)
            if event.type == pygame.KEYDOWN:
                if pressed[pygame.K_p]:
                    rocket.mode = not rocket.mode
                    # if rocket.mode == False:
                    #     space.gravity = 0,-100
                    # else:
                    #     space.gravity = 0,-10
                    print(rocket.mode)
            
        # if pressed[pygame.K_s]:
        #     rocket.brake()

        display.fill((255,255,255))#draw white background

        #draw objects
        rocket.draw()
        floor.draw()
        for wall in walls:
            wall.draw()

        #game logic

        #slow down before hiting floor
        if rocket.shape.body.position.y < 200:
            rocket.shape.body.apply_force_at_local_point((0, 50), (0, -100))
        
        #speed cap
        if rocket.body.velocity[0] > 150:
            rocket.brake()
        if rocket.body.velocity[0] < -150:
            rocket.brake()

        #Update display
        pygame.display.update()

        #FPS TICK
        clock.tick(FPS)
        space.step(1/FPS)
        

#RUN GAME
game()

pygame.quit()





