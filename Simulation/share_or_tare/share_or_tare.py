#every day each rabbit picks one tree to eat at
#each tree may only hold 2 rabbits and supply 1 to reproduce
#if one rabbit it at a tree is gets to reproduce the next day and pass on its trait with a mutation
#if 2 rabbits are at a tree and both would like to share then each gets to live but not reproduce
#if 2 rabbits are at a tree and both or just one would like to fight the rabbit with the most total food will win and reproduce the next day

import random
from matplotlib import pyplot as plt

class Rabbit:
    def __init__(self, sot, last_shared=False):
        self.sot = sot
        self.food = 0
        self.live = False
        self.reproduce = False
        self.last_shared = last_shared
    def reset(self):
        self.live = False
        self.reproduce = False
class Tree:
    def __init__(self, cap=2, uses=0):
        self.cap = cap
        self.uses = uses
        self.rabbits_useing = []
    def reset(self):
        self.rabbits_useing = []
        self.uses = 0


day = 0
day_list = []
sim_time = 10000
rabbits_start_amt = 100
trees_start_amt = 10000
rabbits = []
trees = []
liveing_rabbit_list =[]
shares = []
tares = []


#make trees and rabbits
for i in range(rabbits_start_amt):
    rabbits.append(Rabbit(random.choice([True, False])))
for i in range(trees_start_amt):
    trees.append(Tree())

while day < sim_time:
    try:
        #give every rabbit a tree or if a tree has to much compitition kill the rabbit
        for index, rabbit in enumerate(rabbits):
            tree_index = random.randint(0,len(trees)-1)
            tree = trees[tree_index]
            if tree.uses < 2:
                tree.uses += 1
                tree.rabbits_useing.append(rabbit)
            else:
                rabbits.remove(rabbit)
        
        #loop trough all trees and provide rabbits food
        for index, tree in enumerate(trees):
            rabbits_sots = []
            for rabbit in tree.rabbits_useing:
                rabbits_sots.append(rabbit.sot)

            if tree.uses == 2:        
                if rabbits_sots[0] == rabbits_sots[1]:
                    if rabbits_sots[0] == False: #share
                        for rabbit in tree.rabbits_useing:
                            rabbit.live = True
                            rabbit.food += 0.5
                            if rabbit.last_shared == True:
                                rabbits.remove(rabbit)
                            else:
                                rabbit.last_shaed = True
                    else: #tare
                        if tree.rabbits_useing[0].food > tree.rabbits_useing[1].food:
                            tree.rabbits_useing[0].live = True
                            tree.rabbits_useing[0].reproduce = True
                            tree.rabbits_useing[0].food += 1
                            rabbits.remove(tree.rabbits_useing[1])
                        elif tree.rabbits_useing[0].food < tree.rabbits_useing[1].food:
                            tree.rabbits_useing[1].live = True
                            tree.rabbits_useing[1].reproduce = True
                            tree.rabbits_useing[1].food += 1
                            rabbits.remove(tree.rabbits_useing[0])
                        else:
                            tree.rabbits_useing[0].live = False
                            tree.rabbits_useing[0].reproduce = False
                            tree.rabbits_useing[1].live = False
                            tree.rabbits_useing[1].reproduce = False
                            rabbits.remove(tree.rabbits_useing[0])
                            rabbits.remove(tree.rabbits_useing[1])
                else:
                    # if tree.rabbits_useing[0].sot == True:
                    #     tree.rabbits_useing[0].live = True
                    #     tree.rabbits_useing[0].reproduce = True
                    #     tree.rabbits_useing[0].food += 0
                    #     rabbits.remove(tree.rabbits_useing[1])
                    # elif tree.rabbits_useing[1].sot == True:
                    #     tree.rabbits_useing[1].live = True
                    #     tree.rabbits_useing[1].reproduce = True
                    #     tree.rabbits_useing[1].food += 0
                    #     rabbits.remove(tree.rabbits_useing[0])
                    if tree.rabbits_useing[0].food > tree.rabbits_useing[1].food:
                        tree.rabbits_useing[0].live = True
                        tree.rabbits_useing[0].reproduce = True
                        tree.rabbits_useing[0].food += 1
                        rabbits.remove(tree.rabbits_useing[1])
                    elif tree.rabbits_useing[0].food < tree.rabbits_useing[1].food:
                        tree.rabbits_useing[1].live = True
                        tree.rabbits_useing[1].reproduce = True
                        tree.rabbits_useing[1].food += 1
                        rabbits.remove(tree.rabbits_useing[0])
                    else:
                        tree.rabbits_useing[0].live = False
                        tree.rabbits_useing[0].reproduce = False
                        tree.rabbits_useing[1].live = False
                        tree.rabbits_useing[1].reproduce = False
                        rabbits.remove(tree.rabbits_useing[0])
                        rabbits.remove(tree.rabbits_useing[1])
                        
            elif tree.uses == 1:
                for rabbit in tree.rabbits_useing:
                        rabbit.live = True
                        rabbit.food += 1
                        rabbit.last_shared = False
                    
        #reproduce all rabbits that need to
        for index, rabbit in enumerate(rabbits):
            if rabbit.reproduce:
                rabbits.append(Rabbit(rabbit.sot))

        #get share to rate ratio
        share = 0
        tare = 0
        for rabbit in rabbits:
            if rabbit.sot == False:
                share += 1
            else:
                tare += 1
        shares.append(share)
        tares.append(tare)

        #reset rabbits and trees
        for rabbit in rabbits:
            rabbit.reset()
        for tree in trees:
            tree.reset()

        day += 1
        day_list.append(day)
        liveing_rabbit_list.append(len(rabbits))
        #print(f"Day: {day} Rabbits Alive: {len(rabbits)}")
    except KeyboardInterrupt:
        break



plt.plot(day_list,liveing_rabbit_list)
plt.title(f"Rabbit population over {sim_time} days", fontsize=10)
plt.xlabel("Day", fontsize=10)
plt.ylabel("Population", fontsize=10)
plt.show()
plt.cla()
plt.plot(day_list[0:len(day_list)],shares[0:len(day_list)])
plt.title(f"Shares population over {sim_time} days", fontsize=10)
plt.xlabel("Day", fontsize=10)
plt.ylabel("Population", fontsize=10)
plt.show()
plt.cla()
plt.plot(day_list[0:len(day_list)],tares[0:len(day_list)])
plt.title(f"Tares population over {sim_time} days", fontsize=10)
plt.xlabel("Day", fontsize=10)
plt.ylabel("Population", fontsize=10)
plt.show()
plt.cla()