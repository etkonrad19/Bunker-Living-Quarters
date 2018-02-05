import random
def hallway():
    print("You're in a dark hallway")
    choice = str(input(" True or False: Do you want to walk down the dark hallway?"))
    if choice == "Yes":
        print ("Walk down the hallway.")
        print ("The secret door opens up and you fall in.")
        bathroom()
    else:
        print ("You dont have any other option my Dude still send it.")
        print ("Caution we have detected unknown creature.")
        print ("There is no going back!!")
        print ("The secret door opens up and you fall in.")
        bathroom()

def bathroom():
    FirstHalf = False
    SecondHalf = False
    Taken = False
    print ("You stand up dazed and you realize you are in the bathroom")
    print("(this is the command list,search north,search east,search south,search west,move north ,move east ,move south ,move west,look north ,look east ,look south ,look west ,interact north ,interact east ,interact south ,interact west)")
    pl = "square1"
    escaped = False
    searchNorth = ""
    searchEast = ""
    searchSouth = ""
    searchWest = ""
    moveNorth = ""
    moveEast = ""
    moveSouth = ""
    moveWest= ""
    lookNorth = ""
    lookEast = ""
    lookSouth = ""
    lookWest = ""
    interactNorth = ""
    interactEast = ""
    interactSouth = ""
    interactWest = ""
    moveNorthText = ""
    moveEastText = ""
    moveSouthText = ""
    moveWestText = ""
    while escaped != True:
        pc = str(input("what would you like to do: "))
        if pl == "square1":
            searchNorth = "there's nothing there"
            searchEast = "there's nothing there"
            searchSouth = "there's nothing there"
            searchWest = "there's nothing there"
            moveNorth = "square4"
            moveEast = "square6"
            moveSouth = "square8"
            moveWest= "square2"
            lookNorth = "you see a shower and a toilet just a few steps away"
            lookEast = "you see a door"
            lookSouth = "there is a cupboard"
            lookWest = "the sink and light switch is there"
            interactNorth = "there's nothing there"
            interactEast = "there's nothing there"
            interactSouth = "there's nothing there"
            interactWest = "there's nothing there"
            moveNorthText = "you moved closer to the shower and toilet"
            moveEastText = "walking closer to the door"
            moveSouthText = "now your near the cupboard"
            moveWestText = "the sink and light switch are right infrount of you"
        if pl == "square2":
            searchNorth = "there's nothing there"
            searchEast = "there's nothing there"
            searchSouth = "there's nothing there"
            searchWest = "searching sink" and "and found"
            moveNorth = "square3"
            moveEast = "square1"
            moveSouth = "square9"
            moveWest= "wall"
            lookNorth = "you see a shower and a toilet"
            lookEast = "you see a door on the other side of the room"
            lookSouth = "theres a wall in the distence"
            lookWest = "the sink and light switch is there"
            interactNorth = "there's nothing there"
            interactEast = "there's nothing there"
            interactSouth = "there's nothing there"
            interactWest = "you turned on the lights"
            moveNorthText = "you moved closer to the shower and toilet"
            moveEastText = "walking closer to the door"
            moveSouthText = "now your near the cupboard"
            moveWestText = "the sink and light switch are right infrount of you"
        if pl == "square3":
            searchNorth = "searching bath tub"
            searchEast = "theres nothing there"
            searchSouth ="theres nothing there"
            searchWest = "theres a wall"
            moveNorth ="wall"
            moveEast ="square4"
            moveSouth ="square2"
            moveWest ="wall"
            lookNorth ="your breathing down a bath tub"
            lookEast = "you see ther wall with the door on it"
            lookSouth ="you see the wall with the cupboard on it"
            lookWest ="your gazing at a beautiful wall"
            interactNorth ="there is the tub"
            interactEast ="there is not a thing there to interact with"
            InteractSouth = "wow... theres nothing"
            interactWest ="you touched the wall"
            moveNorthText ="theres a bath tub there"
            moveEastText ="you moved to square 4"
            moveSouthText ="you moved to square 2"
            moveWestText ="you bumbed the wall"
        if pl == "square4":
            searchNorth = "searching bath tub"
            searchEast = "nothing there"
            searchSouth = "nothing there"
            searchWest = "nothing there"
            moveNorth = "wall"
            moveEast = "square5"
            moveSouth = "square1"
            moveWest= "square3"
            lookNorth = "theres the bath tub still"
            lookEast = "you can see the toilet next to the bath tub and the wall with the locked door on it"
            lookSouth = "you see the open room"
            lookWest = "you see the wall witht the sink non it just a few steps away"
            interactNorth = "there is the tub"
            interactEast = "nothing there"
            interactSouth = "nothing there"
            interactWest = "nothing there"
            moveNorthText = "there is a wall there"
            moveEastText = "you moved to squre 5 the farthest east you can go"
            moveSouthText = "you moved back to the middle of the room"
            moveWestText = "you went back to the west wall near the sink"
        if pl == "square5":
            searchNorth = "you found half of a key"
            searchEast = "theres nothing there"
            searchSouth = "theres nothing there"
            searchWest = "theres nothing there"
            moveNorth = "wall"
            moveEast = "wall"
            moveSouth = "square6"
            moveWest= "sqare4"
            lookNorth = "you see the toilet"
            lookEast = "you see the wall with the locked door on it"
            lookSouth = "you see the other side of the room"
            lookWest = "you see the sink on the rother side of the room"
            interactNorth = "you flushed the toilet"
            interactEast = "you touched the wall"
            interactSouth = "theres nothing there"
            interactWest = "theres nothing there"
            moveNorthText = "theres a wall there"
            moveEastText = "theres a wall there"
            moveSouthText = "you moved to square6"
            moveWestText = "you moved to square4"
        if pl == "square6":
            searchNorth = "theres nothing there"
            searchEast = "theres a locked door there and it seems you need a key"
            searchSouth = "theres nothing there"
            searchWest = "theres nothing there"
            moveNorth = "square5"
            moveEast = "wall"
            moveSouth = "square7"
            moveWest= "square1"
            lookNorth = "you see the toilet"
            lookEast = "you see the locked door"
            lookSouth = "you see the cupboard"
            lookWest = "you see the sink on the other side of the room"
            interactNorth = "theres nothing there"
            interactEast =""
            interactSouth = "nothing is there"
            interactWest = "nothing is there"
            moveNorthText = "you moved to square5"
            moveEastText = "theres a wall there"
            moveSouthText = "you moved to square7"
            moveWestText = "you moved to square1"
        if pl =="square7":
            searchNorth = "nothing is there"
            searchEast = "theres a wall"
            searchSouth = ("you search the cupboard and find half a key!")
            searchWest = "nothing is there"
            moveNorth = "square6"
            moveEast = "wall"
            moveSouth = "wall"
            moveWest= "square8"
            lookNorth = "theres nothing there"
            lookEast = "theres a wall"
            lookSouth = "theres the cupboard"
            lookWest = "theres nothing there"
            interactNorth = "theres nothing there"
            interactEast = "theres a wall there"
            interactSouth = "you opened and closed the door repeatedly"
            interactWest = "theres nothing there"
            moveNorthText = "you moved to square6"
            moveEastText = "theres a wall there"
            moveSouthText = "theres a wall there"
            moveWestText = "you moved to square8"
        if pl == "square8":
            searchNorth = "theres nothing there"
            searchEast = "theres nothing"
            searchSouth = "theres a wall"
            searchWest = "theres nothing"
            moveNorth = "square1"
            moveEast = "square7"
            moveSouth = "wall"
            moveWest= "square9"
            lookNorth = "you see the bath tub on the other side of the room"
            lookEast = "you see the wall a step away"
            lookSouth = "you stare at the wall for a couple of seconds"
            lookWest = "you see the wall with the sink on it a square away"
            interactNorth = "theres nothing"
            interactEast = "theres a wall"
            interactSouth = "theres nothing"
            interactWest = "theres nothing"
            moveNorthText = "you moved to the middle of the room"
            moveEastText = "you moved the to 7th square"
            moveSouthText = "theres a wall there dummy"
            moveWestText = "you moved to square 9"
        if pl == "square9":
            searchNorth = "you search the sink to find a half eaten burrito"
            searchEast = "theres nothing"
            searchSouth = "nope nothing"
            searchWest = "nothing"
            moveNorth = "square2"
            moveEast = "square8"
            moveSouth = "wall"
            moveWest= "wall"
            lookNorth = "you see the sink and the shower on the other side of the room"
            lookEast = "you see a cup board on the other side of the room "
            lookSouth = "theres a wall"
            lookWest = "theres a wall"
            interactNorth = "you turn on the sink"
            interactEast = "theres nothing"
            interactSouth = "theres a wall you touch"
            interactWest = "theres another wall wow"
            moveNorthText = "you moved to the second square where the sink is"
            moveEastText = "you moved to the 8th square "
            moveSouthText = "theres a wall there bud"
            moveWestText = "teres a wall here"
        if pc == "search north":
            print(searchNorth)
        if pl == "square5":
            SecondHalf = True
        if pc == "search east":
            print(searchEast)
        if pc == "search south":
            print(searchSouth)
        if pl == "square7":
            FirstHalf = True
        if pc == "search west":
            print(searchWest)
        if pc == "look north":
            print(lookNorth)
        if pc == "look south":
            print(lookSouth)
        if pc == "look west":
            print(lookWest)
        if pc == "look east":
            print(lookEast)
        if pc == "move north":
            if moveNorth != "wall":
                pl = moveNorth
                print(moveNorthText)
            elif moveNorth == "wall":
            print(moveNorthText)
        if pc == "move south":
            if moveSouth != "wall":
                pl = moveSouth
                print(moveSouthText)
            elif moveSouth == "wall":
                print(moveSouthText)
        if pc == "move east":
            if moveEast != "wall":
                pl = moveEast
                print(moveEastText)
            elif moveEast == "wall":
                print(moveEastText)
        if pc == "move west":
            if moveWest != "wall":
                pl = moveWest
                print(moveWest)
            elif moveWest == "wall":
                print(moveWest)
        if pc == "interact north":
            print(interactNorth)
        if pc == "interact south":
            print(interactSouth)
        if pc == "interact west":
            print(interactWest)
        if pc == "interact east":
            print(interactEast)
        if pl == "square6":
            if FirstHalf and SecondHalf == True:
                print("you unlocked the door")
                livingquarters()
                Break
            else:
                print("you need to find the key to unlocked it")
def livingquarters():
    #Variables
    escaped = False
    pl = "square1"
    pi = []
    code1 = False
    code2 = False
    lookNorth = ""
    lookSouth = ""
    lookWest = ""
    lookEast = ""
    moveNorth = ""
    moveSouth = ""
    moveWest = ""
    moveEast = ""
    moveNorthText = ""
    moveSouthText = ""
    moveWestText = ""
    moveEastText = ""
    interactNorth = ""
    interactSouth = ""
    interactWest = ""
    interactEast = ""
    while escaped != True:
        pc = str(input("What do you do? "))
        if pl == "square1":
            lookNorth = "You can make out a corner of the room a few feet away."
            lookSouth = "You can see a lamp in a corner of the room a few feet away."
            lookEast = "The door you came through."
            lookWest = "You see two sofas and a table in between."
            moveNorth = "square2"
            moveSouth = "square3"
            moveWest = "wall"
            moveEast = "wall"
            moveNorthText = "You move into the corner of the room"
            moveSouthText = "You move into a corner of the room."
            moveWestText = "There is a sofa in your way."
            moveEastText = "That's the door you came through"
            interactNorth = "There is nothing there"
            interactSouth = "There is nothing there"
            interactEast = "You don't want to go back."
            interactWest = "You poke the couch. It's soft and firm."
        elif pl == "square2":
            lookNorth = "You see a wall right infront of you."
            lookSouth = "Across the room you see a corner of the room"
            lookWest = "Across the room you see the other corner with a old bookshelf in it."
            lookEast = "You see a wall right infront of you."
            moveNorth = "wall"
            moveSouth = "square1"
            moveWest = "square5"
            moveEast = "wall"
            moveNorthText = "There is a wall there."
            moveSouthText = "You move back behind the couch next to the door you came in through."
            moveWestText = "You move next to the sofas and table."
            moveEastText = "There is a wall there."        
            interactNorth = "There is a wall there"
            interactSouth = "There is nothing there"
            interactWest = "There is nothing there"
            interactEast = "There is a wall there"
        elif pl == "square3":
            lookNorth = "You see the door you came through and the oposite corner"
            lookSouth = "You see a wall right infront of you"
            lookWest = "Across the room you see the a corner"
            lookEast = "You see a wall right infront of you"
            moveNorth = "square1"
            moveSouth = "wall"
            moveWest = "square6"
            moveEast = "wall"
            moveNorthText = "You move back infront of the door you came in behind one of the sofas"
            moveSouthText = "There is a wall there"
            moveWestText = "You move next to one of the couches"
            moveEastText = "There is a wall there"
            interactNorth = "There is nothing there"
            interactSouth = "There is a wall there"
            interactWest = "There is nothing there"
            interactEast = "There is a wall there"
        elif pl == "square5":
            lookNorth = "There is a wall there"
            lookSouth = "You see a sofa"
            lookWest = "You see the door to get out a few feet away along the wall"
            lookEast = "You see a corner of the room"
            moveNorth = "wall"
            moveSouth = "wall"
            moveWest = "square8"
            moveEast = "square2"
            moveNorthText = "There is a wall there"
            moveSouthText = "The sofa is there"
            moveWestText = "You move infront of the door"
            moveEastText = "You see move into the corner of the room"
            interactNorth = "There is a wall there"
            interactSouth = "You poke the couch. It is soft and firm"
            interactWest = "There is nothing there"
            interactEast = "There is nothing there"
        elif pl == "square6":
            lookNorth = "You see a sofa there"
            lookSouth = "There is a wall there"
            lookWest = "You see a corner across the room"
            lookEast = "You see a corner a few feet away"
            moveNorth = "wall"
            moveSouth = "wall"
            moveWest = "square9"
            moveEast = "square3"
            moveNorthText = "There is a sofa there"
            moveSouthText = "There is a wall there"
            moveWestText = "You move to the middle bottom of the room"
            moveEastText = "You move to the corner of the room"
            interactNorth = "You poke the couch. It is soft and firm"
            interactSouth = "There is a wall there"
            interactWest = "There is nothing there"
            interactEast = "There is nothing there"
        elif pl == "square7":
            lookNorth = "You see the door to get out a few feet away"
            lookSouth = "You see a wall a few feet away"
            lookWest = "You see a sofa"
            lookEast = "You see a sofa"
            moveNorth = "square8"
            moveSouth = "square9"
            moveWest = "wall"
            moveEast = "wall"
            moveNorthText = "You move to the door to get out"
            moveSouthText = "You move to the wall"
            moveWestText = "There is a sofa there"
            moveEastText = "There is a sofa there"
            interactNorth = "There is nothing there"
            interactSouth = "There is nothing there"
            interactWest = "You poke the sofa. It is soft and firm"
            interactEast = "You poke the sofa. It is soft and firm"
        elif pl == "square8":
            lookNorth = "The door to get out"
            lookSouth = "You see the table between the sofas"
            lookWest = "You see a bookshelf a few feet away."
            lookEast = "You see a corner of the room"
            moveNorth = "wall"
            moveSouth = "square7"
            moveWest = "square11"
            moveEast = "square5"
            moveNorthText = "There is a wall there"
            moveSouthText = "You move between the sofas"
            moveWestText = "You move next to the sofa"
            moveEastText = "You move next to a sofa"
            interactNorth = "The door has a passcode lock"
            interactSouth = "The table has nothing no it"
            interactWest = "There is nothing there"
            interactEast = "There is nothing there"
        elif pl == "square9":
            lookNorth = "You see the table between the sofas"
            lookSouth = "There is a wall there"
            lookWest = "You see a corner of the room"
            lookEast = "You see a corner of the room"
            moveNorth = "square7"
            moveSouth = "wall"
            moveWest = "square12"
            moveEast = "square6"
            moveNorthText = "You move between to two sofas"
            moveSouthText = "There is a wall there"
            moveWestText = "You move next to one of the sofas"
            moveEastText = "You move next to one of the sofas"
            interactNorth = "The table has nothing on it"
            interactSouth = "There is a wall there"
            interactWest = "There is nothing there"
            interactEast = "There is nothing there"
        elif pl == "square11":
            lookNorth = "There is a wall there"
            lookSouth = "There is a sofa there"
            lookWest = "There is a bookshelf a few feet away"
            lookEast = "There is the door to escape along the wall"
            moveNorth = "wall"
            moveSouth = "wall"
            moveWest = "square14"
            moveEast = "square8"
            moveNorthText = "There is a wall there"
            moveSouthText = "There is a sofa there"
            moveWestText = "You move to the bookshelf"
            moveEastText = "You move infront of the door to escape"
            interactNorth = "There is a wall there"
            interactSouth = "You poke the sofa. It is soft and squishy"
            interactWest = "There is nothing there"
            interactEast = "There is nothing there"
        elif pl == "square12":
            lookNorth = "There is a sofa there"
            lookSouth = "There is a wall there "
            lookWest = "There is the corner of the room a few feet away"
            lookEast = "You see a corner across the room"
            moveNorth = "wall"
            moveSouth = "wall"
            moveWest = "square15"
            moveEast = "square9"
            moveNorthText = "A sofa is there"
            moveSouthText = "A wall is there"
            moveWestText = "You move next to the center table"
            moveEastText = "You move in the corner of the room"
            interactNorth = "You poke the sofa. It soft and firm"
            interactSouth = "There is a wall there"
            interactWest = "There is nothing there"
            interactEast = "There is nothing there"
        elif pl == "square13":
            lookNorth = "You see a bookshelf in the corner of the room"
            lookSouth = "You see a corner of the room"
            lookWest = "You see a wall"
            lookEast = "There is a sofa there"
            moveNorth = "square14"
            moveSouth = "square15"
            moveWest = "wall"
            moveEast = "wall"
            moveNorthText = "You move into the corner of the room with the bookshelf"
            moveSouthText = "You move into a corner"
            moveWestText = "There is a wall there"
            moveEastText = "There is a sofa there"
            interactNorth = "There is nothing there"
            interactSouth = "There is nothing there"
            interactWest = "There is a wall there"
            interactEast = "You poke the sofa. It is soft and firm."
        elif pl == "square14":
            lookNorth = "There is a wall there"
            lookSouth = "You see a corner of the room"
            lookWest = "There is a bookshelf there"
            lookEast = "You see the door to leave along the wall"
            moveNorth = "wall"
            moveSouth = "square13"
            moveWest = "wall"
            moveEast = "square11"
            moveNorthText = "There is a wall there"
            moveSouthText = "You move behind a sofa"
            moveWestText = "There is a bookshelf there"
            moveEastText = "You move next to a sofa"
            interactNorth = "There is a wall there"
            interactSouth = "There is nothing there"
            interactWest = "There are some old books in the shelf"
            interactEast = "There is nothing there"
        elif pl == "square15":
            lookNorth = "You can see the bookshelf across the room"
            lookSouth = "There is a wall there"
            lookWest = "There is a wall there"
            lookEast = "You see a corner across the room"
            moveNorth = "square13"
            moveSouth = "wall"
            moveWest = "wall"
            moveEast = "square12"
            moveNorthText = "You move behind a sofa"
            moveSouthText = "There is a wall there"
            moveWestText = "There is a wall there"
            moveEastText = "You move next to a sofa"
            interactNorth = "There is nothing there"
            interactSouth = "There is a wall there"
            interactWest = "There is a wall there"
            interactEast = "There is nothing there"
        if pc == "look north":
            print(lookNorth)
        elif pc == "look south":
            print(lookSouth)
        elif pc == "look west":
            print(lookWest)
        elif pc == "look east":
            print(lookEast)
        elif pc == "move north":
            if moveNorth != "wall":
                pl = moveNorth
                print(moveNorthText)
            elif moveNorth == "wall":
                print(moveNorthText)
        elif pc == "move south":
            if moveSouth != "wall":
                pl = moveSouth
                print(moveSouthText)
            elif moveSouth == "wall":
                print(moveSouthText)
        elif pc == "move east":
            if moveEast != "wall":
                pl = moveEast
                print(moveEastText)
            elif moveEast == "wall":
                print(moveEastText)
        elif pc == "move west":
            if moveWest != "wall":
                pl = moveWest
                print(moveWestText)
            elif moveWest == "wall":
                print(moveWestText)
        elif pc == "interact north":
            print(interactNorth)
            if pl == "square8":
                if code1 and code2 == True:
                    print("You put in the code and escape!")
                    escaped = True
                elif code1 and code2 != True:
                    print("You need a 8 character code to open this door.")
                    print("Maybe you can find it somewhere in the room.")
        elif pc == "interact south":
            print(interactSouth)
        elif pc == "interact west":
            print(interactWest)
        elif pc == "interact east":
            print(interactEast)
        elif pc == "search east":
            if pl == "square7":
                if code1 == False:
                    print("You found a slip of paper with 4 numbers!")
                    print("4291")
                    code1 = True
                elif code1 == True:
                    print("You found nothing")
            else:
                print("You find nothing.")
        elif pc == "search west":
            if pl == "square1":
                if code1 == False:
                    print("You found a slip of paper with 4 numbers!")
                    print("4291")
                    code1 = True
                elif code1 == True:
                    print("You found nothing")
            elif pl == "square14":
                if code2 == False:
                    print("You found a slip of paper with 4 numbers!")
                    print("8633")
                    code2 = True
                elif code2 == True:
                    print("You find nothing")
            else:
                print("You find nothing")
        elif pc == "search north":
            if pl == "square6":
                if code1 == False:
                    print("You found a slip of paper with 4 numbers!")
                    print("4291")
                    code1 = True
                elif code1 == True:
                    print("You found nothing")
            else:
                print("You found nothing")
        elif pc == "search south":
            if moveSouth == "square7":
                if code1 == False:
                    print("You found a slip of paper with 4 numbers!")
                    print("4291")
                    code1 = True
                elif code1 == True:
                    print("You found nothing")
            else:
                print("You found nothing")
        else:
            print("Typo")
