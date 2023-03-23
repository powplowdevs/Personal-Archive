  ####################################################################################################################################################################################
 
#Diease spred sim
 
#####START OF SIM#####
#Useing the Population_size var we make a population
#Every day the enitre population will be given a random amt of food points form 1 to max_food_points
#start_infected_amt% of the population will be infected to.
 
#####DAYS######
#Every person will lose one food. If they still have 1 or more food they will stay home if the lock_down_level is 0. If its 1 they will have a will_to_leave_home% chance to leave.
#If the lock_down_level is more than 1 then they will not leave there home
#max lock down level 2
 
####INFECTION#####
#If a person leaves there home they will always go to the supermarket. When a person decided to go to the super market a random number from 1 to max_food_points-random number
#That number is how long they will walk around the market. ie. the number is 5 so they stay there for 5 mins.
#When people are roaming around the market every min they are there they will have a chance (infected_chance)
 
#####POST INFECTION#####
#After getting infected the infected person will have days_till_sypmt days until they will die or live on with imunity (only if imunity is enabled)
#During this days_till_sypmt period they will act normal but be infected and able to spred the disease
 
####################################################################################################################################################################################
 
#rec limt over ride
import sys
sys.setrecursionlimit(10000000)

import random
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import os
import time
 
#Vars
Population_size = 100
Population = []
to_market = []
max_food_points = 10
start_infected_amt = 5
lock_down_level = 0
will_to_leave_home = 1
can_spread_with_birth = True
imunity_with_birth = True
chance_to_give_birth = 9
air_spread = False
#infect_dist = 6
infect_chance_cap = 1
days_still_sypmt = 5
sim_time = 365
save_data = True
max_age = 10
lethalness = 9
 
 
#base stats
infected_people = 0
healthy_people = 0
dead_people = 0
imune_people = 0
day = 0
 
#plot vars
days_list = []
healthy_list = []
infected_list = []
dead_list = []
Population_list = []
imune_list = []
 
#progess bars
loc = 1
progress = 0 

#make bar
bar = ""
for i in range(round(sim_time/(sim_time/50))):
    bar = bar + "~" 

#setup base stats
if air_spread:
    infect_chance_cap += 10 

#CLASS'S
class human():
    def __init__(self, food_points, infected, days_since_infected, age, imunity, spot):
        self.food_points = food_points
        self.infected = infected
        self.days_since_infected = days_since_infected
        self.age = age
        self.imunity = imunity
        self.spot = spot
 
    def checkup(self):
        self.age += 1
        self.food_points -= 1
        if self.infected:
            self.days_since_infected += 1
    
    def reset(self):
        self.infected = False
        self.days_since_infected = 0
        self.imunity = True
           
#FUNTIONS
def main():
    global day, infected_people, dead_people, healthy_people, days_list, infected_list, healthy_list, dead_list, Population_list, progress, loc, imune_people, imune_list
    
    #progess bar
    progress += 1
    if progress == round(sim_time/50):
        progress = 0
        bar = ""
        for z in range(loc):
            bar = bar + "#"
        for y in range(round(sim_time/(sim_time/50)) - loc):
            bar = bar + "~"
        loc += 1
        #print(str("[" + bar + "] " + str(day-1) +  "/" + str(sim_time) + " Done"))
        #time.sleep(0.01)
        
    day += 1
    days_list.append(day)
    #print("DAY:", day, "\nINFECTED:", infected_people, "\nHEALTHY:", healthy_people, "\nDEAD:", dead_people, "\n")
    #time.sleep(0.01)

    Population_list.append(infected_people+healthy_people)
    infected_list.append(infected_people)
    dead_list.append(dead_people)
    healthy_list.append(healthy_people)
    imune_list.append(imune_people)
       
    
    if day == sim_time or healthy_people == 0 and imune_people == 0:
        print("done")
        #PLOT DATA
        plt.plot(days_list,Population_list)
        plt.title("Human population over x days", fontsize=10)
        plt.xlabel("Day", fontsize=10)
        plt.ylabel("Population", fontsize=10)
        plt.show()
        plt.cla()
        plt.plot(days_list, healthy_list)
        plt.title("Healthy humans population over x days", fontsize=10)
        plt.xlabel("Day", fontsize=10)
        plt.ylabel("Population", fontsize=10)
        plt.show()
        plt.cla()
        plt.plot(days_list, infected_list)
        plt.title("infected humans population over x days", fontsize=10)
        plt.xlabel("Day", fontsize=10)
        plt.ylabel("Population", fontsize=10)
        plt.show()
        plt.cla()
        plt.plot(days_list, imune_list)
        plt.title("imune humans population over x days", fontsize=10)
        plt.xlabel("Day", fontsize=10)
        plt.ylabel("Population", fontsize=10)
        plt.show()
        plt.cla()
        plt.plot(days_list, dead_list)
        plt.title("dead humans population over x days", fontsize=10)
        plt.xlabel("Day", fontsize=10)
        plt.ylabel("Population", fontsize=10)
        plt.show()
        plt.cla()
 
        input("hit enter to end:")
 
        #save data
        if save_data:
            f = open("data.txt","w")
            headder = str(("day:", str(len(days_list)), "\npop:", str(len(Population)), "\nhealthy:",str(len(healthy_list)), "\ninfected:", str(len(infected_list)), "\ndead:", str(len(dead_list))))
            f.write(headder)
            for element in days_list:
                f.write(str(element) + "\n")
            for element in Population:
                f.write(str(element) + "\n")
            for element in healthy_list:
                f.write(str(element) + "\n")
            for element in infected_list:
                f.write(str(element) + "\n")
            for element in dead_list:
                f.write(str(element) + "\n")
 
            f.close()
 
        #exit()
 
    #run day logic
    for spot,person in enumerate(Population):   
        #eat at start of day
        person.checkup()
        
        #infect death
        if person.days_since_infected >= 5 and random.randint(0,10) > lethalness:
            Population.pop(spot)
            infected_people -= 1
            dead_people += 1
            continue
        elif person.days_since_infected >= 5:
            Population.pop(spot)
            infected_people -= 1
            imune_people += 1
            person.reset()
            continue
        
        #age death
        if person.age > max_age:
            if person.infected:
                infected_people -= 1
                dead_people += 1
                Population.pop(spot)
            else:
                healthy_people -= 1
                dead_people += 1
                Population.pop(spot)
            continue

        #birth spread   
        if can_spread_with_birth:
            if person.food_points > chance_to_give_birth and person.infected:
                Population.append(human(random.randint(1,10), True, 0, 0, False, i))
                infected_people += 1
            elif person.food_points > chance_to_give_birth and not person.infected:
                if imunity_with_birth:
                    Population.append(human(random.randint(1,10), False, 0, 0, True, i))
                    healthy_people += 1
                    
                else:
                    Population.append(human(random.randint(1,10), False, 0, 0, False, i))
                    healthy_people += 1

        

        #go to market
        if person.food_points == 0:
            to_market.append(Population[spot])
        #stay home
        else:
            pass
 
    market()
 
def market():
    global infected_people, healthy_people, to_market, healthy_list, infected_list
 
    market_infect_chance = 0
    for spot, person in enumerate(to_market):
        if person.infected:
            market_infect_chance += 0.5
    
    #cap infect chance
    if market_infect_chance > infect_chance_cap:
        market_infect_chance = infect_chance_cap
    
    market_infect_chance = market_infect_chance/10
    #print(market_infect_chance)

    for spot, person in enumerate(to_market):
        #how long to stay
        stay_len = max_food_points-random.randint(1, 9)
       
        if not person.infected:
            for i in range(stay_len):
                person.food_points += 1
                #infected logic
                infected_or_not = random.randint(0,100)
 
                #healthy person
                if infected_or_not < market_infect_chance:
                    #break
                    continue
                #infected person
                if infected_or_not >= market_infect_chance and person.imunity == False and infected_people != 0:
                    person.infected = True
                    infected_people += 1
                    healthy_people -= 1
           
                   
     
    to_market = []
    if day < sim_time:
        main()
 
#create population
for i in range(Population_size):
    health_status = random.randint(0,100)
 
    #healthy person
    for i in range(Population_size-start_infected_amt):
        Population.append(human(random.randint(1,10), False, 0, 0, False, i))
        healthy_people += 1
    #infected person
    for i in range(start_infected_amt):
        Population.append(human(random.randint(1,10), True, 0, 0, False, i))
        infected_people += 1
 
print(infected_people)
if __name__ == '__main__':
    main()

#C:\Program Files\Python39\lib\runpy.py

