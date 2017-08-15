# Manor Escape! This program, while simple is a text game intended to simulate an environment
# where you must try to escape by making a few simple choices. Each method will have a brief description of what 
# its purpose is. -S.Johnson August 01, 2017

import random
import time

#first method to iniate user interaction, simple yes answer input, "*" denotes a user choice
def methodGreeting():
    
    print "Hello, would you like to play a game?"
    y = input
    input("* press Y for yes: ")   
    
    if (input == y):
        methodIntro()
        
     
         
        
#this method gives the user a brief description of what they are in for, mostly print, "==>" denotes read here
def methodIntro():
    time.sleep(2)
    print ""                                                                                                      
    print "==> You wake up to a damp, and cool musty room. The smell of mold is pungent in the air,"
    print "and from the looks of your surroundings, it could be a run-down house."
    print "You don't recollect how you came to be there."
    print "You start to panic, but realize you aren't bound or injured, so escape is your next best option.."
    print ""
    time.sleep(7)
    print "There is a note next to you on the floor, written on parchment, it says: You have a choice to make. Get up "
    print "or wait for rescue!"
    print "As you read, you think that something is off... Could this be a dream?"
    print ""
    print ""
    time.sleep(7)
    print "* You have to choose now. Should you get up, or lie on the floor and wait for help?"

    
# this is a while loop method that prompts to user to only select 1 or 2
def choosePath():    
     path = 0
     while(1):
        path = input("Press 1 to get up, or 2 to wait on the floor for help: ")
        
        if (path == 1) or (path == 2):
            return path
    
    
def checkPath(choosePath):
        
        correctPath = random.randint(1, 2)
        
        
        if choosePath == correctPath:
            print " "
            print "==> You sit up feeling groggy, realizing that you may very well perish in this mansion if you do not get it" 
            print "together and escape. You think to yourself that it may only take a short while,"
            print "after all, how big can this place be? Just then, you hear a mocking laughter... In the corner you see a pair of glowing"
            print "yellow eyes, and ivory white rows of teeth.. coming towards you!!"
            
        else:
            print " "
            print " "
            print "==> You sit up feeling very groggy and realize that the room has an unreal quality to it, almost like a dream..."
            print "You hear a mocking laughter coming from everywhere suddenly, it's taking over all your senses..."
            
            
def gameOutro():
    
    print " "
    print " "
    print "==> You shoot up out of your bed and realize it was all just a bad dream! After you take a moment to look around"
    print "you see you are safe and sound back at home with no danger... Until you hear that same mocking laughter"
    print "just out of earshot... MWAHAHAHA! IS THIS A DREAM OR REALITY!?!?"
    




playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    methodGreeting()
    choice = choosePath()
    checkPath(choice)
    gameOutro()
    playAgain = raw_input("Do you want to play again? (yes to continue playing) : ")
        
     
        
        
   
        
             
             
        
        
        

    
    





        
        
    
    
         
         
         
         
         
         
        