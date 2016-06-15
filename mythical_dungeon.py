# http://learnpythonthehardway.org/book/ex36.html

import sys

supply_contents = []

def starting_point():
    """
    starts the entire game
    describes the scenario, rules, and goal
    results in unicorn()
    """
    print "\nYou find yourself in a clearing. To obtain safe"
    print "passage, you must navigate from this clearing to"
    print "a room full of treasure. Between the clearing and"
    print "the treasure is a dungeon of dangerous creatures."
    print "You must use your wits and knowledge of mythical"
    print "beasts to safely navigate through the dungeon.\n"
    print "The creatures may assist you on your journey by"
    print "providing supplies and knowledge. But beware! An"
    print "incorrect turning or action will bring your death.\n"
    unicorn()

def death(reason):
    """
    describes how the player dies
    exits the game
    """
    print reason, "Great job!"
    print "Do you want to play again?"
    selection = raw_input("Y/N ")
    if selection == "y" or selection == "Y":
        starting_point()
    else:
        sys.exit(0)

def supply_storage(item):
    """
    adds dropped/found items to the player's supplies
    """
    supply_contents.append(item)
    return supply_contents

def supply_list():
    """
    displays the contents of the player's supplies
    """
    if len(supply_contents) < 1:
        print "You currently do not have any supplies."
    else:
        print "You have these supplies:"
        for item in supply_contents:
            print item
    print

def unicorn():
    """
    reached from starting_point()
    results in hippogriff()
    """
    print "You walk north into the trees surrounding the"
    print "clearing. After you can no longer see the clearing,"
    print "you catch a glimpse of white from behind a large"
    print "tree. You step forward cautiously to find a unicorn.\n"
    print "At the sound of your breathing, the unicorn runs"
    print "into the woods, revealing a small sign. The sign"
    print "stands between you and a door in a large tree.\n"
    print "Do you read the sign, Y/N"
    selection = raw_input(">> ")
    if selection == "y" or selection == "Y":
        print "The sign says:"
        hippogriff()
    elif selection == "n" or selection == "N":
        print "something pithy"
        hippogriff()
    else:
        death("You wander around the woods until you waste away and die.")

def hippogriff():
    """
    reached from unicorn()
    results in death() or minotaur()
    """
    supply_list()
    print "Description"
    print "Do you demand passage to the door or ask politely?"
    answer = raw_input(">> ")
    if answer == "supplies":
        supply_list()
    if "politely" in answer:
        print "The hippogriff moves aside, allowing you to walk through the door."
        print "The hippogriff is now your companion through this dungeon."
        supply_storage("hippogriff")
        minotaur()
    elif "demand" in answer:
        death("Hippogriff")
    else:
        death("You die some other way")

def minotaur():
    """
    reached from hippogriff()
    results in death() or manticore()/centaur()
    """
    supply_list()
    print "Description"
    print "Do you walk or run across the top of the labyrinth walls?"
    answer = raw_input(">> ")
    if "run" in answer:
        death("Fall in and get gored by minotaur.")
    elif "walk" in answer:
        print "reach other side safely."
        print "You find a bow and quiver of arrows."
        selection = raw_input("Do you take them, Y/N? ")
        if selection == "y" or selection == "Y":
            supply_storage("Bow and Quiver")
        elif selection == "n" or selection == "N":
            return
        else:
            death("Minotaur leaps over wall and kills you.")
        print "Door to the left and door to the right."
        choice = raw_input("Which door do you go through? ")
        if "right" or "Right" in choice:
            centaur()
        elif "left" or "Left" in choice:
            manticore()
        else:
            death("Minotaur leaps over wall and kills you.")
    else:
        death("Some other way.")

def manticore():
    """
    reached from minotaur()
    results in death()
    """
    supply_list()
    print "Hey look, a manticore"
    death("You get devoured whole. No evidence of your body or possessions remain.")

def centaur():
    """
    reached from minotaur()
    results in sphinx()
    """
    supply_list()
    print "\nDescription"
    supply_storage("Bundle of herbs")
    sphinx()

def sphinx():
    """
    reached from centaur
    results in death() or chimera()
    """
    supply_list()
    print "What has 4 legs at breakfast, 2 legs at lunch, and 3 legs at dinner?"
    answer = raw_input(">> ")
    if answer == "man" or answer == "Man":
        print "some message about besting the sphinx"
        supply_storage("earmuffs")
        chimera()
    else:
        death("how should the sphinx kill you?")

def chimera():
    """
    reached from sphinx()
    results in death() or medusa()/circe()
    """
    supply_list()
    print "description"
    print "how do i want to word your choices here?"
    choice = raw_input(">> ")
    if "bow" and "hippogriff" in choice:
        print "something about killing a chimera"
        supply_storage("lyre")
        print "pick a door"
        selection = raw_input(">> ")
        if selection == "left":
            medusa()
        elif selection == "right":
            circe()
        else:
            death("smoldering body gets you!")
    else:
        death("fire death from above")

def medusa():
    """
    reached from chimera()
    results in death() or harpies()
    """
    supply_list()
    print "Vague description"
    print "Do you proceed to get a better look or close your eyes and hope for the best?"
    choice = raw_input(">> ")
    if "close" in choice:
        print "Medusa confirmation"
        harpies()
    else:
        death("Turned to stone.")

def circe():
    """
    reached from chimera()
    results in death() or harpies()
    """
    supply_list()
    print "description"
    print "Do you have anything in your pack for Circe?"
    if "Bundle of herbs" in supply_contents:
        print "Something about circe not turning you into a pig"
        supply_storage("Food")
        harpies()
    else:
        death("Turned into a pig")

def harpies():
    """
    reached from medusa() or circe()
    results in death() or phoenix()
    """
    supply_list()
    if "Food" in supply_contents:
        print "Harpies steal your food and fly away"
    else:
        death("The harpies peck out your eyes cause you didn't have any food for them.")

def phoenix():
    """
    reached from harpies()
    results in pegasus()
    """

def pegasus():
    """
    reached from phoenix()
    results in cerberus()
    """

def cerberus():
    """
    reached from pegasus()
    results in death() or sirens()
    """

def sirens():
    """
    reached from cerberus()
    results in death() or boat()
    """

def boat():
    """
    reached from sirens()
    results in death() or hydra()/scylla()/charybdis()
    """

def hydra():
    """
    reached from sirens() via boat()
    results in death() or griffin()
    """

def scylla():
    """
    reached from sirens() via boat()
    results in death() or griffin()
    """

def charybdis():
    """
    reached from sirens() via boat()
    only results in death()
    """

def griffin():
    """
    reached from hydra and scylla
    results in death() or treasure()
    """

def treasure():
    """
    can only be reached from griffin()
    this is the winning room
    """

starting_point()
