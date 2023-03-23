#Imports
import random
from matplotlib import pyplot as plt
import time
import os

#HAVE UI?
ui = False

#messure time to run scirpt
startTime = time.time()

#graph vars
stack_plot = plt.figure()
ax1 = stack_plot.add_subplot(111)

#base vars 
city = (10, 10, 800, 650)
speed = 0
day = 1
population = []
Spopulation = []
Ipopulation = []
directions_level0 = ["right", "left", "up", "down", "ur", "ul", "dr", "dl"]
directions_level1 = ["right", "left", "up", "down"]
directions_level2 = ["right", "left", "up", "down"]
directions = []
loop_increment = 1
masks = False
#sim vars
sim_time = 18000# *6 months 36500 = 1 year
will_to_always_distance = False
time_to_social_distance = sim_time/2
starting_infected_people = 1
population_size = 500
infected_radius = 1
lockdown_level = 1 #0 = no distance 1 = yes distance
infected_chance = 100
max_days_infected = 1400 #1000 #20 days
loops = 250

#UI vars
if ui:
    import pygame
    # Initializing Pygame
    pygame.init()
    # Initializing surface
    surface = pygame.display.set_mode((810,660))
else:
    surface = None  

# Initialing Color
color = (255,255,255)

#vars for roaming
time_spent_going_one_way = None
time_spent_going_one_way0 = (75,200)
time_spent_going_one_way1 = (1,15)
time_spent_going_one_way2 = (1,5)
spaceing = 50

#vars for graphing
days_list = []
Slist = []
Ilist = []
Rlist = []
Population_list = []
show_graph = False
save_data = True
sims = 0

#UI vars
SIZE = 1

#day bar
loc = 1
prog = 0
bar = ""
for i in range(round(sim_time/(sim_time/50))):
    bar = bar + "~"

#class's
class human():
    def __init__(self, food_points, infected, days_since_infected, age, imunity, spot, surface, pos, color="BLUE", size=SIZE, loop_increment=0):
        self.food_points = food_points
        self.infected = infected
        self.days_since_infected = days_since_infected
        self.age = age
        self.imunity = imunity
        self.spot = spot
        self.surface = surface
        self.color = color 
        self.pos = pos
        self.size = size
        self.current_direction = "down"
        self.loop_increment = loop_increment
        
    def draw(self):
        
        #Change direction we are moveing
        #up
        if self.current_direction == "up":
            if self.pos[1] <= city[0]:
                self.current_direction = "down"
            else:
                self.pos = (self.pos[0],self.pos[1]-1)
        #down
        elif self.current_direction == "down":
            if self.pos[1] >= city[3]:
                self.current_direction = "up"
            else:
                self.pos = (self.pos[0],self.pos[1]+1)
        #left  
        elif self.current_direction == "left":
            if self.pos[0] <= city[1]:
                self.current_direction = "right"
            else:
                self.pos = (self.pos[0]-1,self.pos[1])
        #right      
        elif self.current_direction == "right":
            if self.pos[0] >= city[2]:
                self.current_direction = "left"
            else:
                self.pos = (self.pos[0]+1,self.pos[1])
                
        #diagnoals
        #up and right
        if self.current_direction == "ur":
            if self.pos[1] <= 40 or self.pos[0] >= city[2]:
                self.current_direction = "down"
            else:
                self.pos = (self.pos[0]+1,self.pos[1]-1)
        #up and left
        if self.current_direction == "ul":
            if self.pos[1] <= 40 or self.pos[0] <= 30:
                self.current_direction = "down"
            else:
                self.pos = (self.pos[0]-1,self.pos[1]-1)
        #down and right
        if self.current_direction == "dl":
            if self.pos[0] <= 30 or self.pos[1] >= city[3]:
                self.current_direction = "up"
            else:
                self.pos = (self.pos[0]-1,self.pos[1]+1)
        #down and left
        if self.current_direction == "dr":
            if self.pos[0] >= city[2] or self.pos[1] >= city[3]:
                self.current_direction = "up"
            else:
                self.pos = (self.pos[0]+1,self.pos[1]+1)
        
        if ui:
            pygame.draw.circle(self.surface, self.color, self.pos, self.size)

    def update(self):
        self.loop_increment += 1
        if self.infected:
            self.age+=1
            if self.age >= max_days_infected:
                self.infected = False
                self.color = "GREY"
                self.imunity = True

def create_population():    
    global population_size, population, time_spent_going_one_way, directions
    #create population
    x=0
    y=50
    for i in range(population_size):
        person = human(10,False, 0, 0, False, 0, surface, ((x*25)+spaceing,y))
        population.append(person)
        Spopulation.append(person)
        x+=1
        if x == spaceing/2:
            y+=spaceing
            x=0
        if y > city[3]:
            y = 50
        
    x=10
    y=population_size
    #add infected peopople
    for i in range(starting_infected_people):
        person = human(10, True, 0, 0, False, 0, surface, ((x*25)+100,y), "RED")
        population.append(person)
        Ipopulation.append(person)
        #infected_poulation.append(person)
        x += 1
        if x == spaceing/2:
            y+=spaceing
            x=0

    #set up vars for SIR scenarios
    if lockdown_level == 0:
        time_spent_going_one_way = time_spent_going_one_way0
        directions = directions_level0
    if lockdown_level == 1:
        time_spent_going_one_way = time_spent_going_one_way1
        directions = directions_level1
    else:
        time_spent_going_one_way = time_spent_going_one_way2
        directions = directions_level2

#MAIN LOOP
def main():
    global sims, day, time_spent_going_one_way, prog, bar, loc, directions, lockdown_level
    sims += 1
    for p in range(sim_time): 

        try:
            #save data for graph
            s = 0
            i = 0
            r = 0
            days_list.append(day)
            for person in population:
                if person.imunity:
                    r+=1
                elif person.infected:
                    i+=1
                else:
                    s+=1
            
            if s == 0:
                Slist.append(0.0001)
                Ilist.append(i)
                Rlist.append(r)
            elif i == 0:
                Slist.append(s)
                Ilist.append(0.0001)
                Rlist.append(r)
            elif r == 0:
                Slist.append(s)
                Ilist.append(i)
                Rlist.append(0.0001)
            else:
                Slist.append(s)
                Ilist.append(i)
                Rlist.append(r)

            if ui:
                #draw city walls
                pygame.draw.rect(surface, color, pygame.Rect(city),  2)

            # if s == 0 and i == 0:
            #     days_list[]
            
            #draw humans and edit human pos
            for person in population:
                if not person.imunity:
                    person.draw()
                    person.update()
                    if i > 0:
                        if person.loop_increment > random.randint(time_spent_going_one_way[0], time_spent_going_one_way[1]):
                            person.current_direction = random.choice(directions)
                            person.loop_increment = 0

            #collision
            if i > 0 and s > 0:
                    for person in Spopulation:
                        for person2 in Ipopulation:
                                if not person.imunity and not person.infected and person2.infected and person.pos[0] in range(person2.pos[0]-infected_radius,person2.pos[0]+infected_radius) and person.pos[1] in range(person2.pos[1]-infected_radius,person2.pos[1]+infected_radius):
                                    person.color = "RED" 
                                    person.infected = True
                                    Spopulation.remove(person)
                                    Ipopulation.append(person)


            #18250    
            #stop social distansing
            if will_to_always_distance == False and day == time_to_social_distance and lockdown_level == 1:
                time_spent_going_one_way = time_spent_going_one_way0
                directions = directions_level0
                lockdown_level = 0

            #refresh screen
            if ui:
                pygame.display.flip()
                surface.fill((0,0,0)) 
                
            day+=1
            prog+=1
            #update bar
            # if prog == (sim_time/35):
            #     prog = 0
            #     bar = ""
            #     for z in range(loc):
            #         bar = bar + "#"
            #     for y in range(round(sim_time/(sim_time/25)) - loc):
            #         bar = bar + "~"
            #     loc += 1
            #     os.system('cls' if os.name == 'nt' else 'clear')
            #     print(str("[" + bar + "] " + str(day) +  "/" + str(sim_time) + " Done"))
            
            #os.system('cls' if os.name == 'nt' else 'clear')
            #print("\n" + str(round((day/sim_time),2)) + f"% done")
            
            # if speed > 0:
            #     pygame.time.wait(speed)
                          
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print(str("[" + bar + "] " + str(sim_time) +  "/" + str(sim_time) + " Done"))
            executionTime = (time.time() - startTime)
            print('Execution time in seconds: ' + str(executionTime))
            print("Suseptiable: ", s ,"\nInfected: ", i, "\nRecoverd: ", r)
            try:
                ax1.stackplot(range(1,day), Ilist,Slist,Rlist, colors = ["#ff0000","#0000ff","#669999"], labels=["I","S","R"])
            except:
                ax1.stackplot(range(1,day+1), Ilist,Slist,Rlist, colors = ["#ff0000","#0000ff","#669999"], labels=["I","S","R"])
            plt.show()
            quit()


    os.system('cls' if os.name == 'nt' else 'clear') 
    print(str("[" + bar + "] " + str(sim_time) +  "/" + str(sim_time) + " Done"))

    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))

    print("Suseptiable: ", s ,"\nInfected: ", i, "\nRecoverd: ", r)
    
    if show_graph:
        if (will_to_always_distance == False):
            plt.annotate("",xy=(int(sim_time/2), 0), xycoords='data',xytext=(time_to_social_distance, population_size+5), textcoords='data',arrowprops=dict(arrowstyle="-",connectionstyle="arc3,rad=0."), )
        try:
            ax1.stackplot(range(0,day), Ilist,Slist,Rlist, colors = ["#ff0000","#0000ff","#669999"], labels=["I","S","R"])
        except:
            ax1.stackplot(range(0,day-1), Ilist,Slist,Rlist, colors = ["#ff0000","#0000ff","#669999"], labels=["I","S","R"])
        plt.title("SIR over x days", fontsize=10)
        plt.xlabel("Day", fontsize=10)
        plt.ylabel("Population", fontsize=10)
        plt.show()
    
        plt.cla()
        plt.plot(days_list, Slist, color="#0000ff")
        plt.plot(days_list, Ilist, color="#ff0000")
        plt.plot(days_list, Rlist, color="#669999")
        plt.title("SIR over x days", fontsize=10)
        plt.xlabel("Day", fontsize=10)
        plt.ylabel("Population", fontsize=10)
        plt.legend(["S","I","R"])
        plt.show()
        plt.cla()

def run():
    global startTime, day, population, Population_list, Spopulation, Ipopulation, loc, prog, Slist, Ilist, Rlist, will_to_always_distance, lockdown_level, days_list, bar, sim_time
    create_population()
    for i in range(loops):
        executionTime = (time.time() - startTime)
        print("Sim: " + str(sims) + "/250" + "\nTime: " + str(executionTime))
        main()
        
        #save data
        if save_data:
            with open("G:\My Drive\Programing\Personal scripts\Simulation\Disease_Spread\Disease spread sci fair project\LEVEL_1_DATA_TYPE_1\Sdata.txt", "a") as f:
                f.write("".join(str(Slist)))
                f.write("\n")
            with open("G:\My Drive\Programing\Personal scripts\Simulation\Disease_Spread\Disease spread sci fair project\LEVEL_1_DATA_TYPE_1\Idata.txt", "a") as f:    
                f.write("".join(str(Ilist)))
                f.write("\n")
            with open("G:\My Drive\Programing\Personal scripts\Simulation\Disease_Spread\Disease spread sci fair project\LEVEL_1_DATA_TYPE_1\Rdata.txt", "a") as f:
                f.write("".join(str(Rlist)))
                f.write("\n")
            with open("G:\My Drive\Programing\Personal scripts\Simulation\Disease_Spread\Disease spread sci fair project\LEVEL_1_DATA_TYPE_1\DayData.txt", "w") as f:    
                f.write("".join(str(days_list)))
                
            f.close()

        #reset vars

        #messure time to run scirpt
        startTime = time.time()

        #base vars
        day = 1
        population = []

        #vars for graphing
        days_list = []
        Slist = []
        Ilist = []
        Rlist = []
        Population_list = []
        Spopulation = []
        Ipopulation = []
        
        loc = 1
        prog = 0
        bar = ""

        will_to_always_distance = False
        lockdown_level = 1
        
        for i in range(round(sim_time/(sim_time/50))):
            bar = bar + "#"
        
        create_population()

run()