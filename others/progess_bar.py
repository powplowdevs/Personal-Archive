import os

def make_bar(tasks):
    loc = 1
    progress = 0
    #make bar
    bar = ""
    for i in range(round(tasks/(tasks/50))):
        bar = bar + "#"
    #update bar
    for i in range(tasks):
        progress += 1
        if progress == (tasks/50):
            progress = 0
            bar = ""
            for z in range(loc):
                bar = bar + "#"
            for y in range(round(tasks/(tasks/50)) - loc):
                bar = bar + "~"
            loc += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(str("[" + bar + "] " + str(i) +  "/" + str(tasks) + " Done"))
    if i >= (tasks-1):  
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(str("[" + bar + "] " + str(tasks) +  "/" + str(tasks) + " Done"))

make_bar(100000)