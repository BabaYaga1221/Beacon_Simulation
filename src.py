''' simulating the locatization of wifi emitting signal beacon.
**Note - this is the simulation that how the bot will trace the beacon, real practical model is 
little bit different then this simulation.'''

# from cProfile import label
import matplotlib.pyplot as plt
from matplotlib import style
import globalVariables as gv
import method as md

plt.ion()
style.use('fivethirtyeight')
# Global variables import from globalVariables files
bot=gv.bot
beacon=gv.beacon
pathX=gv.X
pathY=gv.Y

# main function of the execution.
def main():
    global bot
    while True:
        plt.clf()
        
        if md.check(bot,beacon)==True:
            print("Captured")
            break

        if md.check(bot,beacon)==False:
            md.move(bot,beacon)
            pathX.append(bot[0])
            pathY.append(bot[1])

        plt.scatter(bot[0],bot[1],label="bot")
        plt.scatter(beacon[0],beacon[1],label="beacon")
        plt.plot(pathX,pathY)
        plt.legend(bbox_to_anchor=(0.75,1.15),ncol=2)

        plt.xlim(0,50)
        plt.ylim(0,50)

        plt.show()
        plt.pause(1)


if __name__ == "__main__":
    main()