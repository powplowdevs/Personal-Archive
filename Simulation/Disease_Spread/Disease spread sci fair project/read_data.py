import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from numpy import array, average

#display stacked error, bar, and line chart of data with error bars on bar and line chart

Slist = []
Ilist = []
Rlist = []
days_list = []
path = ""

def single_read(LINE):
        Sdata = []
        Idata = []
        Rdata = []
        days = []

        with open("G:\My Drive\Programing\Personal scripts\Simulation\Disease_Spread\Disease spread sci fair project" + path + "\DayData.txt", "r") as f:
            content = f.readlines()
            
            #format
            content = content[0].split(", ")
            
            for day in content:
                days.append(float((day.replace("[","")).replace("]","")))
        with open("G:\My Drive\Programing\Personal scripts\Simulation\Disease_Spread\Disease spread sci fair project" + path + "\Sdata.txt", "r") as f:
            try:
                content = f.readlines()
                content = content[LINE]
            except:
                print("Invalid index")
                return None
            #format
            content = content.split(", ")
            
            for s in content:
                Sdata.append(float((s.replace("[","")).replace("]","")))
        with open("G:\My Drive\Programing\Personal scripts\Simulation\Disease_Spread\Disease spread sci fair project" + path + "\Idata.txt", "r") as f:
            content = f.readlines()
            content = content[LINE]
            
            #format
            content = content.split(", ")
            
            for i in content:
                Idata.append(float((i.replace("[","")).replace("]","")))
        with open("G:\My Drive\Programing\Personal scripts\Simulation\Disease_Spread\Disease spread sci fair project" + path + "\Rdata.txt", "r") as f:
            content = f.readlines()
            content = content[LINE]
            
            #format
            content = content.split(", ")
            
            for r in content:
                Rdata.append(float((r.replace("[","").replace("]",""))))
        
        return Sdata, Idata, Rdata, days

def average_read():
    savg = []
    iavg = []
    ravg = []
    d = []

    for i in range(9):
        Sdata,Idata,Rdata,days = single_read(i)

        savg.append(Sdata)
        iavg.append(Idata)
        ravg.append(Rdata)
        d = days

    sarray = array(savg)
    sAvgData = average(sarray, axis=0)
    iarray = array(iavg)
    iAvgData = average(iarray, axis=0)
    rarray = array(ravg)
    rAvgData = average(rarray, axis=0)

    # Rmi = np.amin(ravg, axis = 0)
    # Rma = np.amax(ravg, axis = 0)
    # Imi = np.amin(iavg, axis = 0)
    # Ima = np.amax(iavg, axis = 0)
    # Smi = np.amin(savg, axis = 0)
    # Sma = np.amax(savg, axis = 0)

    Sstd = np.std(savg, axis=0)
    Istd = np.std(iavg, axis=0)
    Rstd = np.std(ravg, axis=0)

    #Sma,Smi,Ima,Imi,Rma,Rmi,
    return sAvgData, iAvgData, rAvgData,Sstd,Istd,Rstd, d
    
def show_err_graph(d, avg, std, let):
    plt.cla()
    plt.plot(d, avg, color="#0000ff")
    plt.errorbar(d, avg, yerr=std, elinewidth=1)
    plt.title(let + " over x days", fontsize=10)
    plt.xlabel("Moves", fontsize=10)
    plt.ylabel("Population", fontsize=10)
    plt.legend([let])
    plt.show()

while True:
    p = int(input("Version 1, 2, or 3: "))
    if p == 1:
        path = "\LEVEL_0_DATA"
    elif p == 2:
        path = "\LEVEL_1_DATA"
    else:
        path = "\LEVEL_1_DATA_TYPE_1"
    
    command = input("Enter your command: ")
    stack_plot = plt.figure()
    ax1 = stack_plot.add_subplot(111)
    
    if command == "help":
        print("Commands:\nsingle read -- view a single trials graph\naverage read -- view a graph of the average of all trials data\nQUIT -- quit or exit program")

    elif command == "single read":
        LINE = int(input("Enter a index: "))
        
        data = single_read(LINE)
        if not data == None:
            Sdata,Idata,Rdata,days = data

            ax1.stackplot(range(0,len(days)), Idata,Sdata,Rdata, colors = ["#ff0000","#0000ff","#669999"], labels=["I","S","R"])
            plt.title("SIR over x days", fontsize=10)
            plt.xlabel("Day", fontsize=10)
            plt.ylabel("Population", fontsize=10)
            plt.show()
        
            plt.cla()
            plt.cla()
            plt.plot(d, Sdata, color="#0000ff")
            plt.plot(d, Idata, color="#ff0000")
            plt.plot(d, Rdata, color="#669999")
            plt.title("SIR over x days", fontsize=10)
            plt.xlabel("Day", fontsize=10)
            plt.ylabel("Population", fontsize=10)
            plt.legend(["S","I","R"])
            plt.show()
            plt.cla()
            
    elif command == "average read" or command=="":
        sAvgData,iAvgData,rAvgData,Sstd,Istd,Rstd,d = average_read()

        ax1.stackplot(range(0,len(d)), iAvgData,sAvgData,rAvgData, colors = ["#ff0000","#0000ff","#669999"], labels=["I","S","R"])
        plt.title("SIR over x days", fontsize=10)
        plt.xlabel("Moves", fontsize=10)
        plt.ylabel("Population", fontsize=10)
        plt.legend(["Susceptible","Infected","Recoverd"])
        plt.show()


        plt.cla()
        plt.plot(d, sAvgData, color="#0000ff")
        plt.plot(d, iAvgData, color="#ff0000")
        plt.plot(d, rAvgData, color="#669999")
        plt.title("SIR over x days", fontsize=10)
        plt.xlabel("Moves", fontsize=10)
        plt.ylabel("Population", fontsize=10)
        plt.legend(["S","I","R"])
        plt.show()
        
        for i in range(len(Sstd)):
            if not i%1000 == 0:
                Sstd[i] = 0
                Istd[i] = 0
                Rstd[i] = 0
                
        show_err_graph(d, sAvgData, Sstd, "Susceptible")
        show_err_graph(d, iAvgData, Istd, "Infected")
        show_err_graph(d, rAvgData, Rstd, "Recoverd")   


    elif command == "QUIT":
        quit()
    else:
        print("Invalid input, try again")
