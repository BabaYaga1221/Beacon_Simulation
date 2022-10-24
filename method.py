value=0

def check(bot:list,beacon:list):
    if bot[0]==beacon[0] and bot[1]==beacon[0]:
        return True
    else:
        return False

def move(bot:list,beacon:list):
    global value
    checker=False
    if(bot[0]==beacon[0]):
        checker=True
        if(bot[1]<beacon[1]):
            bot[1]+=1
        elif(bot[1]>beacon[1]):
            bot[1]-=1
    elif(bot[1]==beacon[1]):
        checker=True
        if(bot[0]<beacon[0]):
            bot[0]+=1
        elif(bot[0]>beacon[0]):
            bot[0]-=1
    else:
        if(bot[1]<beacon[1]):
            bot[1]+=1
        elif(bot[1]>beacon[1]):
            bot[1]-=1
        if(bot[0]<beacon[0]):
            bot[0]+=1
        elif(bot[0]>beacon[0]):
            bot[0]-=1
    value+=1
    if(value%2==0 and checker==False):
        move2(bot,beacon)
        return bot
    if(value%3==0 and checker==False):
        move3(bot,beacon)
        return bot 
    return bot

def move2(bot:list,beacon:list):
    bot[0]+=2
    return bot

def move3(bot:list,beacon:list):
    bot[1]+=2
    return bot