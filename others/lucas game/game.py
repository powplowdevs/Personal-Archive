from playsound import playsound
from pygame.locals import*
import pygame
import pyautogui
import subprocess, os, time, random, string, sys 


width = 1200
height = 1000
screen_color = (0, 0, 150)
lazer_color = (255, 0, 0)
lvl = 0
lazer_size = 15
lazer_time = 100
red_cap = 2
re_time = 30
box_size = 150
box_time = 20
bre_time = 12


cake = None
hammer = None
alpabet = string.ascii_lowercase + string.digits + string.ascii_uppercase 

clock = pygame.time.Clock()
 
lazers = []
boxs = []

FILE = ""# __file__.replace("game.py","")

class lazer():
    def __init__(self, x1, y1, x2, y2, ori=1, typ = 1, fa=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.ori = ori
        self.typ = typ
        self.fa = fa
        
    def draw(self, screen):
        global re_time
        if self.fa < re_time:
            pygame.draw.line(screen,(100, 75, 150), (self.x1, self.y1), (self.x2, self.y2), width=lazer_size)
        else:
            pygame.draw.line(screen,lazer_color, (self.x1, self.y1), (self.x2, self.y2), width=lazer_size)
        
        if self.typ == 1:
            if self.ori == 1:
                self.y2 -= 2
                self.y1 -= 2
            else:
                self.x2 -= 2
                self.x1 -= 2
            
            self.fa += 1
        elif self.typ == 2:
            self.y2 -= 2
            self.y1 -= 2

            self.fa += 1
        else:
            self.x2 -= 2
            self.x1 -= 2

            self.fa += 1

class box():
    def __init__(self, x1, y1, ori=1, fa=0, temp_size=box_size-bre_time):
        self.x1 = x1
        self.y1 = y1
        self.ori = ori
        self.fa = fa
        self.ts = temp_size
        
    def draw(self, screen):
        global bre_time
        if self.fa < bre_time:
            self.ts = box_size
            pygame.draw.rect(screen,(100, 75, 150), pygame.Rect(self.x1, self.y1, self.ts, self.ts))
            #self.ts+=1
        else:
            pygame.draw.rect(screen,lazer_color, pygame.Rect(self.x1, self.y1, box_size, box_size))
        
        self.fa += 1
            
    
def anoying(let):
    pyautogui.write(let)

def main():
    global cake, hammer
    #play intro
    playsound(FILE + "start1.wav") 
    playsound(FILE + "list.wav") 
    playsound(FILE + "drop.wav") 
    playsound(FILE + "ends.wav") 
    #create cake file and hide it and open file explorer for user
    os.mkdir("C:/THE-CAKES-IN-HERE")
    cake = open("C:/THE-CAKES-IN-HERE/cake.txt", 'w')
    cake.write("Password: ")
    cake.close()
    subprocess.Popen(r'explorer /select,"C:"')

    #wait for user to open cake file
    while True:
        if "Notepad" in subprocess.getoutput('powershell "gps | where {$_.MainWindowTitle } | select Description'):
            break

    #play cake file dialog
    playsound(FILE + "joy.wav")

    #wait for use to type and mess with them 3 times and play sound every time we mess them up

    for i in range(3):
        anoying(random.choice(alpabet))
        #play audio
        if i == 1:
            playsound(FILE + "hey.wav")
        if i == 2:
            playsound(FILE + "what.wav")
        if i == 3:
            playsound(FILE + "come.wav")
        
    for i in range(20):
        pyautogui.press('backspace')
        
    #play destory cake file dialog
    subprocess.call("TASKKILL /F /IM Notepad.exe", shell=True)
    playsound(FILE + "ohno.wav")

    #create hammer on desktop
    p = os.path.join(r'C:\Users', str(os.getlogin()))
        
    p = r"C:\Users\lucas\OneDrive\Desktop\hammer.txt"

    hammer = open(p, "w")
    hammer.write(": ")
    hammer.close()

    #wait for user to open hammer
    while True:
        if "Notepad" in subprocess.getoutput('powershell "gps | where {$_.MainWindowTitle } | select Description'):
            break

    #play hammer diolog
    playsound(FILE + "great.wav")

    #play hammer use diolog
    hammer = open(p, "r")
    t=0
    while True:
        if "use" in hammer.read() or t > 200:
            break
        t+= 1
    playsound(FILE + "metal.wav")
    playsound(FILE + "mad.wav")

def win(screen):
    global lazers, re_time, bre_time
    #font = pygame.font.Font('freesansbold.ttf', 32)
    screen.fill((0,0,0))
    
    #text = font.render('You win! take ur prize', True, (255,255,255))
    # textRect = text.get_rect()
    # textRect.center = (width // 2, height // 2)
    # screen.blit(text, textRect)
    
    pygame.display.flip()
    pygame.display.update()
    
    pygame.time.delay(5000)

    lazers = []
    re_time = 30
    boxs = []
    bre_time = 15

    ending()

def death(screen):
    global lazers, re_time, bre_time
    # font = pygame.font.Font('freesansbold.ttf', 32)
    screen.fill((0,0,0))
    
    # text = font.render('You lose', True, (255,255,255))
    # textRect = text.get_rect()
    # textRect.center = (width // 2, height // 2)
    # screen.blit(text, textRect)
    
    pygame.display.flip()
    pygame.display.update()
    
    pygame.time.delay(5000)

    lazers = []
    re_time = 30
    boxs = []
    bre_time = 15

    virus()
    
def virus():
    global lazers, boxs, re_time, bre_time, lvl, height, width

    screen=pygame.display.set_mode((width, height))
    info = pygame.display.Info()
    width, height = info.current_w, info.current_h

    # for i in range(10):
    #     height_l = random.randint(0,height)
    #     lazers.append(lazer(0, height_l, width, height_l, random.randint(1,2), 2))
    #     boxs.append(box(random.randint(0,width), random.randint(0,height)))
        
    pygame.init()
    count = 0
    waves = 0
    d2 = 0
    
    while True:
        count += 1
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)   
           
        screen.fill(screen_color)
        
        if lvl == 0:
            for l in lazers:
                if l.fa > 100:
                    lazers.remove(l)
                l.draw(screen)
            if count > 25:
                waves += 1
                re_time-=1
                for i in range(random.randint(1,3)):
                    typ = random.randint(1,2)
                    if typ == 1:
                        height_l = random.randint(0,height)
                        lazers.append(lazer(0, height_l, width, height_l, random.randint(1,2), 2))
                    else:
                        witdh_l = random.randint(0,width)
                        lazers.append(lazer(witdh_l, 0, witdh_l, height, random.randint(1,2), 3))
                count = 0
        elif lvl == 1:
            for b in boxs:
                if b.fa > box_time:
                    boxs.remove(b)
                b.draw(screen)
            if count > 10:
                waves += 1
                for i in range(random.randint(10,25)):
                   boxs.append(box(random.randint(0,width), random.randint(0,height)))
                count = 0
        else:   
            for l in lazers:
                if l.fa > lazer_time:
                    lazers.remove(l)
                l.draw(screen)
            if count > 25:
                waves += 1
                re_time-=1
                for i in range(random.randint(7,17)):
                    lazers.append(lazer(random.randint(0,width), random.randint(0,height), random.randint(0,width), random.randint(0,height), random.randint(1,2)))
                count = 0
          
        #check if users mouse is blue if not then they are out
        mouse_pos = pyautogui.position()
        margin = (mouse_pos[0]-1,mouse_pos[1]+1,2,2)
        ss = pyautogui.screenshot(region=(margin))
        ss.save(os.path.join(os.getcwd(), "GAME_SS.png"))
        if ss.getpixel((0, 0))[0] > 101 or ss.getpixel((1, 0))[0] > 101 or ss.getpixel((0, 1))[0] > 101 or ss.getpixel((1, 1))[0] > 101:
            death(screen)
        elif ss.getpixel((0, 0))[2] != 150 or ss.getpixel((1, 0))[2] != 150 or ss.getpixel((0, 1))[2] != 150 or ss.getpixel((1, 1))[2] != 150:
            d2+=1
            if d2>5:
             death(screen)

        if waves == 30:
            lvl += 1
            if lvl > 2:
                print("win")
                win(screen)
            else:
                count = 0
                re_time = 30
                waves = 0
        
        pygame.display.flip()
        pygame.display.update() 
        clock.tick(1000)

def ending():
    os.system("start \"\" https://www.youtube.com/watch?v=mFzDfnFwf-Y&ab_channel=Z0")
    quit()
        


virus()
