#danis game
#Game plan
#Intro
#go to the town can talk to shop keeper jack offman or shperd nicholas
#if you talk to shop keeper jack offman he will tell you that the bridge to the forest is broken and nobody will fix it becuse the town
#is now getting imports from the city off shore so there is no need to find food in the forest. He offers to sell you wood to fix it for
#50 gold but you have none.
#if you talk to shperd nicholas he will say there is a rat spooking his sheep and he will pay you 75$ to kill it
#You say yes and solve a riddle to kill it and gain 75$

#next you buy the wood from the shopkeeper and fix the bridge and move on to the forest
#in the forest you find 5 monkeys who ask you 5 riddles
#once you solve them all the last one gives you cotton a bannana and a  M1 Abrams is a third-generation American main battle tank

#in the last section the castle you find a knight gaurding the door
#you fight him and once you win you can enter
#in the castle you find bitches (jessie) and he hands you the giftcard code!

#################

#imports
import time
import sys
import msvcrt as m
import os
import random
from unittest import case

#Player class
class Player:
    def __init__(self, name, health, max_health, level, xp, inv, money):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.level = level
        self.xp = xp
        self.inv = inv
        self.money = money
    
    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
    
    def add_xp(self, amt):
        #check if xp is over cap to level up at over flow xp to next lvl
        if amt>(self.level*10):
            self.xp += amt-(self.level*10)
            self.level += 1
            self.xp = 0
            self.xp += amt
        else:
            self.xp += amt
    
    def reset(self):
        self.health = self.max_health
        self.xp = 0
        print("You have died!")
        for item in self.inv:
            if item.dropable == True:
                print(f"\nItems dropped:\n{item.desc}")
                self.inv.remove(item)

    def show_stats(self):
        return(f"Health: {self.health}/{self.max_health}\nInv:{self.inv}\nMoney: {self.money}\nLvl: {self.level} XP: {self.xp}")
        
class inv_item():
    def __init__(self, desc, type, dropable):
        self.desc = desc
        self.type = type
        self.dropable = dropable


#funtions
def wait():
    m.getch()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def sprint(y, c="yes wait"):
    for x in y:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.01)
    if c == "yes wait":
        wait()
        print("")
    else:
        print("")
def intro():
    lines = ["Welcome to the world of quantavion! - 'the old man'", "I see your are tired my friend... - 'the old man'", "No matter, follow me - 'the old man'", "choice","uhh.. huh? - 'the old man'", "Are you... - 'the old man'", "Are your bitchless?!?!?! - 'the old man'", "clear", "Oh my oh my this wont do - 'the old man'", "In this world you must have bitches! Its only natural - 'the old man'", "My friend I may not take you to the castle to gain your reward before the others-", "Huh? - 'the old man'", "The creator didnt tell you that others where going for the prize as well? - 'the old man'", "clear", "Well yes. There are others trying to reach the castle before you, you must act fast to gain the prize for yourself! - 'the old man'", "I myself would take you to the castle but... - 'the old man'", "You have no bitches.... - 'the old man'", "You must have bitches for me to be able to take you to the castle - 'the old man'", "And as you are kinda incapable of getting them youll have to get there on your own. - 'the old man'", "clear", "travel across the world towards the castle in a race to the end for the prize!\nGood luck my friend! And goodbye! - 'the old man'", "clear"]
    for y in lines:
        if y == "clear":
            clear()
            continue
        elif y == "choice":
            c = input("You have been given a choice!\nfollow them? y/n: ")
            if c == "y":
                print("You follow")
                wait()
                clear()
                continue
            elif c == "n":
                print("You dont follow")
                print("Come on man I know you knew you were ment to follow! ima just pretend you typed 'y'")
                wait()
                clear()
                continue
            else:
                print("Thats not y or n...")
                print("lets just say you typed y then")
                wait()
                clear()
                continue
        else:
            for x in y:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.01)
        wait()
        print("")

#vars
has_interacted_with_shopkeeper = False
has_killed_sheperd = False
has_interacted_with_knighter = False
#items
stick = inv_item("A stick", "W", False) 


#locations
def the_castle(player):
    global has_interacted_with_knighter
    clear()
    sprint("Welcome to the castle", "asd")
    sprint(player.show_stats(), "dsad")
    sprint("You may\nTalk to the knighter gaurding the door (type s)\nTend to your M1 Abrams is a third-generation American main battle tank equipped with radar based anti aircraft SP QUAD 23MM MOUNT; OPTICAL AND RADAR TRACKING/FIRE CONTROL; COMPUTERIZED ENGAGEMENT; WITH AMPHIBIOUS ASSULT CAPEABILITY (type e)", "No wait")
    command = input("Enter your choice: ")

    if command == "s" and not has_interacted_with_knighter:
        clear()
        sprint("I am the knight I do knighter things")
        sprint("I may not let you pass as u have no bitches!")
        sprint("Come back when you have that")
        clear()
        sprint("*you leave*")
    elif command == "s" and has_interacted_with_knighter:
        clear()
        sprint("You pull up to the knight with your M1 Abrams is a third-generation American main battle tank equipped with radar based anti aircraft SP QUAD 23MM MOUNT; OPTICAL AND RADAR TRACKING/FIRE CONTROL; COMPUTERIZED ENGAGEMENT; WITH AMPHIBIOUS ASSULT CAPEABILITY loaded with High-explosive Armor-piercing Chemical based Guided Nuclear artillery shells and send him to allah")
        clear()
        sprint("You did it! - 'the old man'")
        sprint("You made it to the castle!  - 'the old man'")
        sprint("And now your reward  - 'the old man'")
        clear
        sprint("BITCHES")
        sprint("You moan and climax in joy as jesse your new bitch come out from the closet to be with you")
        sprint("come on you sexey thing and get into this closet so we can get out together! he says :weary: *busts*")
        sprint("And what? he hands you a gift card code!")
        clear()
        sprint(" - Thanks for playing and happy one day late birthday dani!")
        quit()
    elif command == "e":
        has_interacted_with_knighter = True
        clear()
        sprint("You tend to your M1 Abrams is a third-generation American main battle tank equipped with radar based anti aircraft SP QUAD 23MM MOUNT; OPTICAL AND RADAR TRACKING/FIRE CONTROL; COMPUTERIZED ENGAGEMENT; WITH AMPHIBIOUS ASSULT CAPEABILITY")
        sprint("You load it with many High-explosive Armor-piercing Chemical based Guided Nuclear artillery shells")
        clear()
    else:
        sprint("Invalid option")
        the_castle(player)
    the_castle(player)



def the_forest(player):
    clear()
    sprint("You hear monkeys in the forest and approach them")
    sprint(player.show_stats(), "dsad")
    sprint("You may\nTalk to the first monkey (type s)\nBe racist (type e)", "No wait")
    command = command = input("Enter your choice: ")
    if command == "s":
       sprint("You talk to the first monkey and he explains how him and the following 4 monkeys will ask you a question! if you answer to there likeing they will let you pass!")
       clear()
       sprint("if not...")
       sprint("They will jump you, they are good at that kind of thing")
       clear()
       sprint("ANSWER IN LETTER FORM (A, B, OR C)", "sdasd")
       sprint("Monkey one: Whats big long and black?\n\tA:my dick\n\tB:the line to kfc\n\tC:a stick", "dasd")
       ans = input("Your answer: ")
       if not ans == "B":
           sprint("WRONG! the monkeys jump you and you die!")
           player.reset()
           the_forest(player)
       sprint("Correct!")
       clear()
       sprint("ANSWER IN LETTER FORM (A, B, OR C)", "sdasd")
       sprint("Monkey two: Whats hard long and has cum in the middle?\n\tA:my dick (again)\n\tB:you <3\n\tC:Cucumbers", "dasd")
       ans = input("Your answer: ")
       if not ans == "C":
           sprint("WRONG! the monkeys jump you and you die!")
           player.reset()
           the_forest(player)
       sprint("Correct!")
       clear()
       sprint("ANSWER IN LETTER FORM (A, B, OR C)", "sdasd")
       sprint("Monkey three: Whoese best?\n\tA:Ayoub\n\tB:Jack\n\tC:jesse", "dasd")
       ans = input("Your answer: ")
       if not ans == "A" and not ans == "B" and not ans == "C":
           print("Thats not even a choice! the monkeys jump you and you die!")
           player.reset()
           the_forest(player)
       sprint("Correct!")
       clear()
       sprint("ANSWER IN LETTER FORM (A, B, OR C)", "sdasd")
       sprint("Monkey four: Best monkey?\n\tA:monkey four\n\tB:monkey four\n\tC:monkey four", "dasd")
       ans = input("Your answer: ")
       if not ans == "A" and not ans == "B" and not ans == "C":
           print("Thats not even a choice! the monkeys jump you and you die!")
           player.reset()
           the_forest(player)
       sprint("Correct!")
       clear()
       sprint("ANSWER IN LETTER FORM (A, B, OR C)", "sdasd")
       sprint("Monkey five: Whats tallest\n\tA:my dick\n\tB:mt everest\n\tC:monkey fours ego", "dasd")
       ans = input("Your answer: ")
       if not ans == "A":
           sprint("WRONG! the monkeys jump you and you die!")
           player.reset()
           the_forest(player)
       sprint("Correct!")

       sprint("Congratz! you have passed the monkeys!")
       sprint("As a reward they hand you come cotton for no specific reason at all plus a bananna! (+cotton & banana)")            
       clear()
       sprint("On the way to the castle and out of the forest you pass my a man named rogger")
       sprint("*You excange greetings*")
       clear()
       sprint("A M1 Abrams is a third-generation American main battle tank equipped with radar based anti aircraft SP QUAD 23MM MOUNT; OPTICAL AND RADAR TRACKING/FIRE CONTROL; COMPUTERIZED ENGAGEMENT; WITH AMPHIBIOUS ASSULT CAPEABILITY; quietly falls out his pocket")
       sprint("You pick it up and hide it behind your back then useing a US LGM-118 Peacekeeper Intercontinental ballistic missile as a small and very minor tactical smoke screen to make a getaway")
       clear()
     
       the_castle(player)
        
    elif command == "e":
        sprint("You say the n-word then the monkeys eat you alive")
        sprint("You die")
        player.reset()
        the_forest(player)
    else:
        sprint("Invalid option")
        the_forest(player)


def the_town(player):
    global has_interacted_with_shopkeeper, has_killed_sheperd
    clear()
    sprint("Welcome to the town", "asd")
    sprint(player.show_stats(), "dsad")
    sprint("You may\nTalk to shop keeper jack offman (type s)\nTalk to shperd nicholas (type e)\nKYS (type f))", "No wait")
    command = input("Enter your choice: ")
    clear()
    if command == "f":
        sprint('Idiot')
        player.reset()
        the_town(player)
    elif command == "s":
        if not has_interacted_with_shopkeeper:
            has_interacted_with_shopkeeper = True
            sprint("Welcome to the store - 'shop keeper jack offman'")
            sprint("What do you seek? - 'shop keeper jack offman'")
            sprint("I want to cross the bridge to the forest and make it to the castle and find bitches")
            sprint("You are bitchless... - 'shop keeper jack offman'")
            sprint("Thats sad ngl... - 'shop keeper jack offman'")
            clear()
            sprint("...")
            clear()
            sprint("Well ive got bad news. The bridge to the forest is broken and nobody thinks to fix it nowadays because the town no longer needs to find wood and food over there as the city on the mainland ships it in for us - 'shop keeper jack offman'")
            sprint("But ill sell you the wood to fix it for 50$, come back when youve got that - 'shop keeper jack offman'")
        elif has_interacted_with_shopkeeper and player.money < 75:
            sprint("ill sell you the wood to fix it for 50$, come back when youve got that - 'shop keeper jack offman'")
        else:
            player.money -= 50
            sprint("The shop keeper sells you wood to fix the bridge for 50$ (-50$)")
            the_forest(player)
    elif command == "e":
        if not has_interacted_with_shopkeeper:
            sprint("I am shperd nicholas, my name is nicholas, I sheperd the sheep an shiz.... - 'shperd nicholas'")
            sprint("Tf u want... - 'shperd nicholas'")
            sprint("*You leave*")
        elif has_killed_sheperd:
            sprint("You hit a clip on the sheperd... remeber?")
            sprint("*You leave*")
        else:
            has_killed_sheperd = True
            sprint("You seek money?  - 'shperd nicholas'")
            sprint("OK well if you kill the rats spooking my sheep ill play u 75$ - 'shperd nicholas'")
            sprint("*You attack the rats*")
            clear()
            sprint(player.show_stats())
            sprint(f"Rats stats:\nHealth: 10\nDamage: 1\n")
            sprint("Its harder to lose than to win...")
            clear()

            #FIGHT
            for i in range(3):
                rath = 10
                while True:
                    damage = random.randint(0,7)
                    sprint(f"You hit the rat for {damage} damage and took 1 damage!")
                    rath -= damage
                    player.health -= 1
                    sprint(f"Your health: {player.health}\nRat health: {rath}")
                    if rath <= 0:
                        sprint(f"The rat died {i+1}/3")
                        break
                    if player.health <= 0:
                        sprint("HOW THE FUCK DID YOU DIE?????????? NAH IM KILLING THIS PROGEAM WHAT R THE ODDS?????")
                        quit()
            sprint("Thanks for killing all the rats here is 75$ (+75$) - 'shperd nicholas'")
            sprint("Now get outa my sight - 'shperd nicholas'")
            sprint("*You hit a 360 noscope on shperd nicholas and leave* (+42069xp)")
            player.money += 75
            player.level = 69
            player.add_xp(42069)
    else:
        sprint("Invalid option")
        the_town(player)

    the_town(player)

#intro()
player = Player(input("Enter your name: "), 100,100, 0,0,[stick],0)
#the_town(player)
the_castle(player)