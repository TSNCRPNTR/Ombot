#dadJoke.py

def makeDadJoke(message):
    #Setting up base variables
    finalString = ""                            #The old message, from "I'm" to period
    cont = 0                                    #Asking "Should I count this word?"

    msglist = message.split()                   #Splitting the message into a list, each word is seperate
    for x in msglist:                           #Goes through each word in the message
        if x == 'I\'m' or x == 'i\'m':          #Doesn't start 'counting' until it sees the "I'm" in the message (not case sensitive                   
                cont = 1
        elif bool(cont):                        #As soon as it passes the "I'm", it starts adding words to the new string.
            if "." in x or ',' in x:                   
                cont = 0                        #Makes sure it can only read one I'm
                x=x.replace(',' or '.', '')     #Old word is new word
                break
            finalString += " "+x                #Builds the final string with all the words combined (in the loop)
    return "Hi"+finalString+", I'm Dad!"        #Haha funee joke
