from time import sleep
import os
import random


def deathC():
    sleep(4)
    count = 0
    for i in range(10):
        count -= 1
        print('DEATH')
        i -= 1
        sleep(1)
    exit()

##########################################################################Level 0
##########################################################################instructions
##########################################################################


print('=====================================')
print('\                                   /')
print('\           Controls                /')
print('\            Yes = y                /')
print('\             No = n                /')
print('\                                   /')
print('\      If prompted with multiple    /')
print('\      questions, answer with       /')
print('\      a number corresponding       /')
print('\      with what question was       /')
print('\      asked first                  /')
print('\                                   /')
print('\                                   /')
print('\                                   /')
print('=====================================')

sleep(5)

##########################################################################Level 1
##########################################################################first chapter select, out of two chapters
##########################################################################
def chapter1():
    Op1 = ''
    while Op1 != 'y' and Op1 != 'n':
        Op1 = input("Move to the light from the darkness?: ") 

        if Op1 == "n": 
            print('You remain there until you wither away from dehydration or starvation or whatever dwells in the dark.') 
            sleep(4)
            count = 0
            deathC()
        elif Op1 == "y": 
            print('You leave the dark and move towards a fading lightbulb in the middle of the room')

    ##########################################################################Level 2
    ##########################################################################just some story explaining your feelings
    ##########################################################################


    sleep(3)
    print('As you emerge from the corner you start thinking to yourself')
    sleep(3)
    print("You've lived your whole life not harming anyone")
    sleep(3)     
    print("How could you have ended up here?")
    sleep(4)
    print('Who did you wrong you think to yourself what did I do to deserve this?')
    sleep(4)
    print("You start to think more about who put who you here and realize you don't remember a single thing.")
    sleep(4)
    print("It's as if when you went to bed last night, you just woke up here")
    sleep(4)
    print("You must ignore all these thoughts and figure out how to get out of here")
    sleep(4)
    print("If I do nothing, I die in here.")

    ##########################################################################Level 3
    ##########################################################################2nd chance to die
    ##########################################################################

    Op2 = ''
    while Op2 != '1' and Op2 != '2':
        Op2 = input("Try to look for a door through the darkness, or look for a way out through the ceiling: ") 

        if Op2 == "2": 
            print('You search the ceiling above the light, it appears to just be panels but you have no way of accessing them')
            sleep(2)
            print('You attempt to climb up the only visible thing in the room, the light')
            sleep(2)
            print('The light breaks and the room goes dark, you fall and your head hits the cold ground and you do not wake up.')
            sleep(2)
            deathC()
            

        elif Op2 == "1":
            print('You leave the dark to search for a door')
        
    sleep(2)

    print('You think to yourself that there has to be a way for you to get in here')
    sleep(3)
    print('One of these walls must have a door')

    ##########################################################################Level 4
    ##########################################################################First of many levels that require you to open many "doors" to find the answer(i saw "doors" because it's not always going to be doors)
    ##########################################################################
    Op3 = ''
    while Op3 != '1' and Op3 != '2' and Op3 != '3' and Op3 != '4':
        Op3 = input("Do you look left, right, forward or behind?: ") 

        while Op3 != 4:
            if Op3 == "1":
                print('You search the wall to the left of you for any kind of abnormalities')
                sleep(2)
                print('Nothing turns up')
                Op3 = input("Do you look left, right, forward or behind?: ")
            elif Op3 == "2":
                print('You search the wall to the right of you for any kind of abnormalities')
                sleep(2)
                print('Nothing turns up')
                Op3 = input("Do you look left, right, forward or behind?: ")
            elif Op3 == "3":
                print('You search the wall to the in front of you for any kind of abnormalities')
                sleep(2)
                print('Nothing turns up')
                Op3 = input("Do you look left, right, forward or behind?: ")
            elif Op3 == "4":
                print('You approach the wall behind you searching for a door')#the correct door
                sleep(2)
                print('Thank God, you found a door')
                break

    ##########################################################################Level 5
    ##########################################################################Story to get you from A to B
    ##########################################################################


    sleep(3)
    print('You open the door and find yourself staring down a long hallway')
    sleep(3)
    print('You feel calmed by the fact its much better lit than the room you were just in')
    sleep(3)
    print("In fact, theres even windows in this hallway.")
    sleep(3)
    print("You take time to go to them and look through them")
    sleep(2)
    print('The windows are hard to see through, it must be very dark outside of them')
    sleep(3)
    print("That tells you it's night still")
    sleep(2)
    print("Maybe it hasn't been that long since you were at your house")
    sleep(3)
    print("Still though, this window doesn't help you escape at all, all you can really tell by it is that it's dark and you seem really high up,")
    sleep(3)
    print("You see no ground, no trees, not a single thing")
    sleep(3)
    print("There's a door down the hallway, you start making your way down to it")
    sleep(3)
    print('Walking')
    sleep(1)
    print('Walking')
    sleep(1)
    print('Walking')
    sleep(1)
    print('Walking')
    sleep(1)
    print('SCORE!')
    sleep(3)
    print('You found a large broken piece of concrete')
    sleep(3)
    print("This opens up so many possibilities, you think to yourself")
    sleep(3)
    print('Instantly you think of an easy way to escape, you can break the window with this concrete and escape, right here and now')
    sleep(3)
    print('You smash the window with your rock but nothing breaks')
    sleep(3)
    print('You find yourself much weaker than you thought, as if you were drugged')
    sleep(3)
    print('You deduct your only chance of breaking this window is by throwing it')

    ##########################################################################Level 6
    ##########################################################################An easy way to die, shows that you are weak if you choose right
    ##########################################################################

    Op4 = ''
    while Op4 != 'y' and Op4 != 'n':
        Op4 = input("Throw the rock at the glass?: ") 

        if Op4 == "y": 
            print('You throw the rock through the window and it breaks')
            sleep(2)
            print('You jump through the window hoping its not that far')
            sleep(2)
            print('You fall to your death') 
            sleep(4)
            count = 0
            for i in range(10):
                count -= 1
                print('DEATH')
                i -= 1
                sleep(1)
            exit()

        elif Op4 == "n": 
            print('You save the rock for later, it will probably be useful')
    sleep(3)
    print('At the end of the hallway, there is door you see')
    sleep(2)
    print('You open it')
    sleep(2)
    print('As you open the door you see nothingness and feel a rush of cold air')
    sleep(3)
    print('It looks just like an a free fall down')
    sleep(2)
    print("No objects in sight, just lights going down many stories")
    sleep(3)
    print("There doesn't seem to be light at the bottom. They just stop after a couple stories.")

    ##########################################################################Level 7
    ##########################################################################An unimportant question just to trip the player up
    ##########################################################################

    Op5 = ''
    Op6 = ''
    while Op5 != 'y' and Op5 != 'n':
        Op5 = input("Throw rock down there to see what how it lands?: ") 

        if Op5 == "y": 
            print('You toss the rock down and it shoots back up near you, it falls back down again')
            sleep(2)
            print('You can tell there is a net or a trampoline or something down there to catch whatever hits it')
            sleep(2)

            while Op6 != 'Jump':
                Op6 = input("Type 'Jump' to jump down: ") 
                if Op6 == "Jump":
                    print('You jump down')
                    sleep(2)
                    print("You lived!")
                    sleep(2)
                    print('You landed on what seems to be a large stretchy net')
                    sleep(2)
                    print('You find your chunk of concrete on ground ')
                    sleep(2)
                    print('You pick it up for later because you never know what you will need')

        elif Op5 == "n":
            print("You take the jump without testing its safety and it proved safe")
            sleep(2)
            print('You lived and landed on what seems to a large stretchy net')
            sleep(2)
            print("I'm happy I didn't throw my rock down, it could've broken if I missed the net")

    ##########################################################################Level 8
    ##########################################################################Story to add depth and mystery
    ##########################################################################


    sleep(2)
    print('You get yourself off the net and on the even ground')
    sleep(3)
    print('You hear a noise')
    sleep(2)
    print("You're in the same building as you were before, but now you realize something")
    sleep(3)
    print("You're not alone.")
    sleep(3)
    print("Luckily it's not super dark where you're looking, theres quite an open room at the bottom here by the net")
    sleep(3)
    print("You see no one there")
    sleep(2)
    print("Yet you still hear something")
    sleep(3)

    ##########################################################################Level 9
    ##########################################################################interactive prompt for engagement
    ##########################################################################
    op1 = ' '
    while op1 != 'i':

        op1 = input("Type 'i' to investigate: ")

        if op1 == 'i':
            print('You leave the the net to find out what made that sound')

    print('You look around the large room before you')
    sleep(3)
    print('No sign of any animals or anything')
    sleep(3)
    print('You see that this room has 25 doors but no windows on the doors')
    sleep(2)

    ##########################################################################Level 10
    ##########################################################################first mountain of elif statements to get to the player to open the right door
    ##########################################################################
    op2 = ' '
    while op2 != '1' and op2 != '2' and op2 != '3' and op2 != '4' and op2 != '5' and op2 != '6' and op2 != '7' and op2 != '8' and op2 != '9' and op2 != '10' and op2 != '11' and op2 != '12' and op2 != '13' and op2 != '14' and op2 != '15' and op2 != '16' and op2 != '17' and op2 != '18' and op2 != '18' and op2 != '19' and op2 != '20' and op2 != '21' and op2 != '22' and op2 != '23' and op2 != '24' and op2 != '25':

        op2 = input("Which door do you open(Enter a number)?: ") 

        while op2 != '17':
            if op2 == "1":
                print('You open the first door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                sleep(1)
                op2 = input("What door do you open next?: ")
            elif op2 == "2":
                print('You open the second door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "3":
                print('You open the third door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "4":
                print('You open the fourth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "5":
                print('You open the fifth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "6":
                print('You open the sixth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "7":
                print('You open the seventh door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "8":
                print('You open the eigth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "9":
                print('You open the ninth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "10":
                print('You open the tenth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "11":
                print('You open the eleventh door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "12":
                print('You open the twelfth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "13":
                print('You open the thirteenth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "14":
                print('You open the fourteenth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "15":
                print('You open the fifteenth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "16":
                print('You open the sixteenth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the next door')
                op2 = input("What door do you open next?: ")
            elif op2 == "18":
                print('You open the eigthteenth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the door before it')
                op2 = input("What door do you open next?: ")
            elif op2 == "19":
                print('You open the ninteenth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the door before it')
                op2 = input("What door do you open next?: ")
            elif op2 == "20":
                print('You open the twentieth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the door before it')
                op2 = input("What door do you open next?: ")
            elif op2 == "21":
                print('You open the twenty first door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the door before it')
                op2 = input("What door do you open next?: ")
            elif op2 == "22":
                print('You open the twenty second door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the door before it')
                op2 = input("What door do you open next?: ")
            elif op2 == "23":
                print('You open the twenty third door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the door before it')
                op2 = input("What door do you open next?: ")
            elif op2 == "24":
                print('You open the twenty fourth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the door before it')
                op2 = input("What door do you open next?: ")
            elif op2 == "25":
                print('You open the twenty fifth door')
                sleep(2)
                print('There is a paper with an arrow drawn on it pointing towards the door before it')
                op2 = input("What door do you open next?: ")
            elif op2 == "17":
                print('You start to open the seventeenth door')
                break

    ##########################################################################Level 11
    ##########################################################################Start of fight
    ##########################################################################


    sleep(2)
    print('As you put your hand on the handle, the area around you violenty vibrates')
    sleep(3)
    op3 = ' '
    while op3 != '1' and op3 != '2':
        op3 = input('Let go of the handle or commit to opening it?: ')

        if op3 == '2':
            print('You fully open the door and an axe bearing monster stares at you as it cuts your head off')
            deathC()
        elif op3 == '1':
            print('You quickly take your hand off the handle and step back')

    ##########################################################################Level 12
    ##########################################################################Chance to die but fight continues
    ##########################################################################

    sleep(3)
    print("A tall grey monster bursts through the door in front of you")
    sleep(3)
    print("You see the monster has an axe in his right hand but his left arm seems smaller")
    sleep(3)
    print("You dont have much time to react, you need to think fast")
    op4 = ' '
    while op4 != '1' and op4 != '2':
        op4 = input('Run or fight?: ')

        if op4 == '1':
            print('You run to the net that you were at previously')
            sleep(2)
            op5 = input('Run around the net or jump on the net?: ')

        ##########################################################################Level 13
        ##########################################################################more in depth options are explored
        ##########################################################################
            op5 = ' '
            while op5 != '1' and op5 != '2':
                if  op5 == '1':
                    sleep(2)
                    print('You run around the net to try to bamboozle him')
                    sleep(2)
                    print('His axe gets caught in the net as he tries to chase you')
                    sleep(2)
                    print('You find yourself out of places to run and he bites your head off')
                    deathC()

                elif op5 == '2':
                    print('You jump on the net')
                    sleep(2)
                    print("The monster swings at you and misses")
                    sleep(2)
                    print('You find yourself in a bad situation, all you have is your rock')
                    sleep(2)
                    op6 = input('Throw the rock?: ')
                op6 = ' '
                while op6 != 'n' and op6 != 'y':
                    if op6 == 'n':
                        print('He catches you defenseless and eats you gruesomely')
                        sleep(2)
                        deathC()
                    
                    elif op6 == 'y':
                        print('You throw the rock at the monster and you actually manage to hit the beasts head')
                        sleep(2)
                        print('It hit at a bad angle and it was unphased')
                        sleep(2)
                        print('It ends up getting you and you die')
                        deathC()

        elif op4 == '2':
            print('You fight!')
            sleep(2)
            print('You are right up here close to him')
            sleep(2)
            
    ##########################################################################Level 14
    ##########################################################################Level where he dies
    ##########################################################################


    print('You know you have your rock, and agility')
    sleep(3)

    o1 = ' '
    while o1 != '1' and o1 != '2':

        o1 = input('Go for his left arm, or throw the rock at his head?: ')

        if o1 == '1':
            print('You push for the left smaller arm')
            sleep(3)
            print('He uses his mouth and bites your head off')
            deathC()
            
                
        elif o1 == '2':
            print('You throw the rock at his head and he becomes dazed')
            sleep(3)
            print("As he's dazed you go for the leg to knock him down")
            sleep(2)
            print('BAM')
            sleep(2)
            print('He hits the ground and slowly tries to get up')
            sleep(3)
            print('You take this chance to smash his head in with your rock')
            break
    ##########################################################################Level 15
    ##########################################################################Colored prompt to finish him
    ##########################################################################
    smashM = ' '
    while smashM != 'y':

        smashM = input("Use your rock to hit his head: ")

        if smashM == 'y':
                print("\033[31mSMASH\033[0m")

        smashM = input("Use your rock to hit his head: ")

        if smashM == 'y':
                print("\033[31mSMASH\033[0m")

        smashM = input("Use your rock to hit his head: ")

        if smashM == 'y':
                print("\033[31mSMASH\033[0m")

    ##########################################################################Level 16
    ##########################################################################Moving on to the second chapter
    ##########################################################################


    sleep(3)
    print("Unsuprisingly, he isn't moving anymore")
    sleep(3)
    print('As he lays there dead, you finally hear the silence that you started this hell with')
    sleep(3)

    axepickup = ' '
    while axepickup != '1' and axepickup != '2':

        axePickup = input('Pick up his axe, or continue on without bothering him again: ')

        if axePickup == '1':
            sleep(3)
            print('You go him again and try to pick up his axe')
            sleep(3)
            print("You pull and pull but you're exhausted from that fight")
            sleep(3)
            print('There is no way you can pick that up')

        elif axepickup == '2':
            sleep(3)
            print("You probably couldn't even pick it up if you tried")

    ##########################################################################Level 17
    ##########################################################################Small simple story information before end of chapter
    ##########################################################################


    sleep(3)
    print('You go to the door he came out of')
    sleep(3)
    print('When you get to his door you notice there is a hallway in his door')
    sleep(3)
    print("You don't really have much option so you go through it")
    sleep(3)
    print('This hallway is has some lights in it, but most seem broken from the size of the monster')
    sleep(3)
    print('At the end of the hallway theres a metal wall it seems')
    sleep(3)
    print('Upon further inspection it looks like an elevator, the call button light was burnt out')
    sleep(3)

    chapter2()

##########################################################################Level 18
##########################################################################Chapter 1 ends here
##########################################################################






#$%^&*@#$%^&*@#$%^&*@#$%^&*@#$%^&*@#$%^&*@#$%^&*@#$%^&*@#$%^&*



                    #CHAPTER 2



#$%^&*@#$%^&*@#$%^&*@#$%^&*@#$%^&*@#$%^&*@#$%^&*@#$%^&*@#$%^&*


def chapter2(): #Decided to make game into two chapters because it was to long to manage for the player if they had just one life, makes the game much easier plus interesting to code because this seemed harder to do in thought than in practice

    elevatorOpen = ''
    while elevatorOpen != 'Push':
        
        elevatorOpen = input('Type "Push" to summon the elevator')

        if elevatorOpen == 'Push':
            sleep(2)
            print("The Elevator takes a few seconds")

    sleep(2)
    print('The elevator opens in front of you, a bright light inside')
    sleep(3)
    print('You walk inside and see that there are 10 floors to this buidling')
    sleep(3)
    print('One these must get you out of here right?')

##########################################################################Level 19
##########################################################################A second mass of elif statement within a while loop
##########################################################################Needed for a set of options for the player to explore
    aaa = ''
    while aaa != '1' and aaa != '2' and aaa != '3' and aaa != '4' and aaa != '5' and aaa != '6' and aaa != '7' and aaa != '8' and aaa != '9' and aaa != '10':
    
        aaa = input('Which button do you push?: ')

        while aaa != '3':
            if aaa == "1":
                print('You push the button with a 1 on it')
                sleep(2)
                print('The elevavtor door opens but gets stuck half way')
                sleep(2)
                print('You decide not to risk trying to enter, its seem sketchy')
                aaa = input("What door do you attempt next?: ")
            elif aaa == "2":
                print('You push the button with a 2 on it')
                sleep(2)
                print('The elevator door makes a sound but does not budge at this floor')
                aaa = input("What door do you attempt next?: ")
            elif aaa == "3":
                print('You push the button with a 3 on it')
                sleep(2)
                print('This door opens fully')
                sleep(2)
                print('You see a hallway once again with full lighting')  #########You proceed from here 
            elif aaa == "4":
                print('You push the button with a 4 on it')
                sleep(2)
                print('You push this button but nothing happens')
                sleep(3)
                print('You conclude that this is your current floor')
                sleep(1.5)
                aaa = input("What door do you attempt next?: ")
            elif aaa == "5":
                print('You push the button with a 5 on it')
                sleep(2)
                print('This takes you up you feel')
                sleep(2.2)
                print('The door opens to you being sort of above the net from earlier')
                sleep(3)
                print("You can't really go out from here unless you jump to the net again")
                aaa = input("What door do you attempt next?: ")
            elif aaa == "6":
                print('You push the button with a 6 on it')
                sleep(2)
                print('You go higher to the sixth floor')
                sleep(3)
                print('The door opens to dim light, you look down and see the net under you')
                aaa = input("What door do you attempt next?: ")
            elif aaa == "7":
                print('You push the button with a 7 on it')
                sleep(2)
                print('The door opens to darkness')
                sleep(3)
                print('You are getting closer to where you began')
                aaa = input("What door do you attempt next?: ")
            elif aaa == "8":
                print('You push the button with a 8 on it')
                sleep(2)
                print('You go to the eigth floor, the door opens and you see absolutely nothing but lights down below')
                aaa = input("What door do you attempt next?: ")
            elif aaa == "9":
                print('You push the button with a 9 on it')
                sleep(2)
                print('The ninth door opens to nothingness, above and below you are lights though')
                aaa = input("What door do you attempt next?: ")
            elif aaa == "10":
                print('You push the button with a 10 on it')
                sleep(2)
                print('The tenth floor door opens')
                sleep(2)
                print('You see the hallway that you began in, you notice something though')
                sleep(3)
                print('The hallway you were once in is slightly different now')
                sleep(3)
                print('Not by much, but the lights are much dimmer now, and the windows appear to have disappeared')
                sleep(3)
                print('Is someone behind you?')
                sleep(4)
                aaa = input("Where do you go from here...?: ")#A fun eerie thought for added depth

    print('You push the button with a 3 on it')
    sleep(2)
    print('This door opens fully')
    sleep(2)
    print('You see a hallway once again with full lighting')
    sleep(3)
    print("You enter the hallway")
    sleep(2)
    print("You're quite cautious and nervous seeing as what has recently happened")
    sleep(3)
    print("The end of the hallway has a door")
    sleep(3)
    print('This is a reoccuring thing you think to yourself')
    sleep(3)
    print('But you have no other option seeing as the walls have no obscure features you decide to open it')

    ##########################################################################Level 20
    ##########################################################################a door that wasn't needed was added here to make opening doors seem not meaningful(useful for next level)
    ##########################################################################
    bbb = ''
    while bbb != 'Pull':
        
        bbb = input('Type "Pull" to pull door open')

        if bbb == 'Pull':
            sleep(.7)
            print('As you pull the door open you feel a rush of cold air emerge from the doorway')
        
    sleep(3)
    print('The door opens up to just a flight of steps')
    sleep(2.3)
    print('You conclude you have no option but to go down it')
    sleep(2.5)
    print('As you procede down, the silence you hear gets even more quieter somehow')
    sleep(3.1)
    print("You think to yourself that you must be close to getting out of here")
    sleep(2.5)
    print('Because you must at the very least be at level two if not one')
    sleep(2.5)
    print('At the bottom there is yet another door')
    sleep(2.5)
    print('You hear nothing at all except your own thoughts at this point')
    sleep(2.5)

##########################################################################Level 21
##########################################################################A consequential but deceivingly simple question that will take you the easy or the hard way out
##########################################################################
    ccc = ''
    while ccc != 'y' and ccc != 'n':
        ccc = input('Open the door?: ')

        if ccc == 'y':
            sleep(1)
            alternateE1()
            
            
        elif ccc == 'n':
            sleep(1)
            alternateE2()

##########################################################################Level 22
##########################################################################The normal expected ending proceeds here
##########################################################################

def alternateE1():
    #ending 1
    number = random.randint(1,5)

    
    sleep(3)
    print('You open the door and instantly it gets loud')
    sleep(3)
    print('It reminds you of the sounds of an indoor pool')
    sleep(3)
    print('The door opens to a very deep looking pool')
    sleep(3)
    print("On the other side of the pool, theres a door")
    sleep(3)
    print("There's 5 walk ways that lead to the other side")
    sleep(3)
    print('You think to yourself that you have seen something like this before')
    sleep(3)
    print("In movies and games this has been a thing, you know that one of these paths must lead you to the other side")
    sleep(2)
    print("And that the other 4 must be fake paths")
    sleep(3)
    
##########################################################################Level 23
##########################################################################Number game to get you across water
##########################################################################
    guess = ''
    while guess != '1' and guess != '2' and guess != '3' and guess != '4' and guess != '5':
    
        number = random.randint(1,5)

        number_of_guesses = 0
        

        while number_of_guesses < 2:
            print('Pick one of these paths:')
            guess = int(input())
            number_of_guesses += 1
            if guess != number:
                print('You try to step on that pathway, it crumbles beneath you')
            elif guess == number:
                break
        if guess != number:
            print('You step on that path, this time fully committing to it')
            sleep(3)
            print('You fall into the water and drown')
            sleep(3)
            deathC()
        else:
            print('You fully commit to stepping on that path')
            sleep(3)
            print('Fortunately it does not break below you')
            break
    
##########################################################################Level 24
##########################################################################Game ends and if you live you move on to the end path
##########################################################################
    
    sleep(3)
    print('You make it to the end of path')
    sleep(3)
    print('You open the door and find another staircase')
    sleep(3)
    print('You step out of the water room and shut the door behind you')
    sleep(3)
    print('Back to silence')
    sleep(2)
    print('You walk down the steps and find yourself')
    sleep(3)
    print('Since you know that this is the second floor your leaving')
    sleep(3)
    print('You must be on the first and final floor')
    sleep(3)
    print('At the end of the stairs there is a hallway')
    sleep(3)
    print('You see at the end of the hallway')
    sleep(3)
    print('That there are what seems to be curtains??')
    sleep(3)
    print('You go to the curtains')
    
##########################################################################Level 25
##########################################################################Some story happens then game ends
##########################################################################   
    
    jjj = ''
    while jjj != 'Open':
        
        jjj = input('Type "Open" the curtains?: ')
        
        if jjj == 'Open':
            sleep(3)
            print('You open the curtains and find yourself back in your bed')
        
    sleep(3)
    print('As if it were just a crazy dream')
    sleep(3)
    print('But that definitely happened')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(2)
    print('Right?')
        
    
        
##########################################################################Level (uncounted)
##########################################################################Second alternate ending for a second playthrough
##########################################################################more of a secret ending because the chances of you resting before the door is slim

def alternateE2():
    #ending 2
    sleep(3)
    print('You wait there on the stairwell waiting for a few minutes just to catch your breath')
    sleep(3)
    print('When you finally sit down and chill a bit')
    sleep(2)
    print('You notice that there is a button of the bottom half of one of these stairs')
    sleep(3)
    print("That's strange you think, you would've never noticed this button if you wouldn't have sat here and looked")
    sleep(3)
    print('You push the button and it opens a small corridor that you could maybe fit through in the wall')
    sleep(3)
    ddd = ''
    while ddd != 'y' and ddd != 'n':
        ddd = input('Go into the corridor?: ')
        
        if ddd == 'n':
            sleep(2)
            print('You walk back to the door from before')
            sleep(3)
            print('The silence is deafening')
            alternateE1()
            
        elif ddd == 'y':
            sleep(3)
            print('You enter the corridor and can barely fit into it')
            sleep(3)
            print('Just enough so you can crawl through')
            sleep(3)
            print('You make your way down this extremely dark corridor')
            sleep(3)
            print("There's only light coming from the stairs behind you")
        
##########################################################################Level (uncounted)
##########################################################################The goal for this area was to kinda confuse the player because there is seemingly two fully done routes here at the end
##########################################################################
        
    sleep(3)
    print('This feels exceptionally unsafe but you persist on because you feel like this could be the end')
    sleep(3)
    print('After crawling for a bit, now in complete darkness')
    sleep(3)
    print('You feel with your hands in front of you  what seems to be a slope down')
    sleep(3)
    print('At the bottom of this slope, you see light')
    sleep(3)
    print('You decide to continue down the corridor which means sliding down this')
    sleep(3)
    print('You make it to the bottom after sliding for a couple of seconds')
    sleep(3)
    print("You can tell you've moved downwards quite a bit")
    sleep(3)
    print("Maybe you've gotten to the first floor?")
    sleep(3)
    print('In front of you, is a grate with very bright light coming in from the other side of it')
    sleep(3)
    
##########################################################################Level (ucounted)
##########################################################################Kind of a quick and underwhelming ending but I left it off as to make it seem like a part two of this to be next
##########################################################################
    ggg = ''
    
    while ggg != 'y' and ggg != 'n':
    
        ggg = input('You still have time to turn back, do you choose to?: ')
        
        if ggg == 'y':
            print('You crawl back up the slope, and back through the tunnel to the stairs')
            alternateE1()
            
        else:
            hhh = input('Type "Stomp" to kick the grate open: ')
            
            if hhh == 'Stomp':
                print('You stomp on the grate with your foot and breaks')
                sleep(3)
                print('Before you is the outside of the building')
                sleep(3)
                print('You jump out the building')
                sleep(3)
                print('You must find the meaning of all of that')
                sleep(3)
                print('But where do you start?')   #game ending 2



chapterSelect = ' '
while chapterSelect != '1' and chapterSelect != '2':

    chapterSelect = input('Which chapter would you like to play?: ')

    if chapterSelect == '1':
        chapter1()
    elif chapterSelect == '2':
        chapter2()

      
print("\033[36mGAME OVER\033[0m")

'''count = 0
for i in range(10):
    count -= 1
    print(i)
    i -= 1
    sleep(1)'''

#sorry if all the bugs weren't hammered out, I had a lack of bug testers but I feel as if I did well

#personal notes VVVVVVV

#1 ending you enter the water portion and have to escape maybe using an easy riddle or random number game then takes you to an endless loop meaning you wake up in the starting room again
#2 ending you chose not to open that seemingly unconsequential door and you wait and see something, what you see is a button on  the bottom half of one of the steps
#you push it and it opens up a passage in the wall, surprised, you enter it and crawl through this small corridor just barely big enough for you to crawl through it
#it takes you to a slide down past the second floor and takes you to the first, all the while it is exceptionally dark
#you break through this grate at the end of the corridor and you (((find alternate ending)))