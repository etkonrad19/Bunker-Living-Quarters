import random

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