# SECRET SANTA ALGORITHM
import random
def SecretSantaGenerator(file):
    # Take in a text file with an array of names with delimiter "|"
    inFile = open(file,"r")
    people = ""
    # Append the names to a list, a list of strings
    for line in inFile:
        people += line
    people = people.split("|")
    # We now have a list of strings, where each index contains a different participant

# Randomly assign a secret santa by parsing through list, making sure no name is repeated
    SecretSantaDict = {}
    takenRecievers = []
    for name in people:
        while (True):
            reciever = random.choice(people)
            if reciever != name:
                # Make sure reciever is not already taken
                if reciever not in takenRecievers:
                    break
            else:
                continue
        # Return a dictionary with the key = Secret Santa (giver) and value = receiver
        SecretSantaDict[name]= reciever
        takenRecievers.append(reciever)
    return SecretSantaDict


# Take user input so the Secret Santa can figure out who their receiver is
def findReciever(dictionary):
    print "Please enter your name to find out who you are Secret Santa to: "
    name = raw_input()
    if name in dictionary.keys():
        print dictionary[name]
    else:
        print "This name is not on our list. Try again."

#COMMANDS
fileLocation = "/Users/kristen/Documents/Kristen_Codes/Secret_Santa/SecretSantaParticipants.txt"
findReciever(SecretSantaGenerator(fileLocation))
