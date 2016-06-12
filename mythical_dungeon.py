# http://learnpythonthehardway.org/book/ex36.html

from sys import exit

def starting_point():
    """
    starts the entire game
    describes the scenario, rules, and goal
    results in unicorn()
    """
    # empty list that will be the player's pack
    supply_contents = []
    print "Description of the scenario"
    print "Here are the rules:"
    print "Here is the goal"
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
        exit(0)

def supply_storage(item):
    """
    adds dropped items to the player's pack
    """
    supply_contents.append(item)
    return supply_contents

def supply_list():
    """
    displays the contents of the player's pack
    """
    if len(supply_contents) < 0:
        print "You currently do not have any supplies."
    else:
        print "You have these supplies:"
        for item in supply_contents:
            print item

def unicorn():
    """
    reached from starting_point()
    results in hippogriff()
    """
    print "Description"
    print "Do you read the sign?"
    selection = raw_input("Y/N ")
    if selection == "supplies":
        supply_list()
    if selection == "y" or selection == "Y":
        print "The sign says:"
        hippogriff()
    elif selection == "n" or selection == "N":
        print "something pithy"
        hippogriff()
    else:
        death("You wander around the grove until you waste away and die.")

def hippogriff():
    """
    reached from unicorn()
    results in death() or minotaur()
    """
    print "Description"
    answer = raw_input("Do you demand passage to the door or ask politely? ")
    if answer == "supplies":
        supply_list()
    if "politely" in answer:
        print "The hippogriff moves aside, allowing you to walk through the door."
        print "The hippogriff is now your companion through this dungeon."
        supply_storage("hippogriff")
        minotaur()
    elif "demand" in answer:
        death("Hippogriff")

def minotaur():
    """
    reached from hippogriff()
    results in death() or manticore()/centaur()
    """

def manticore():
    """
    reached from minotaur()
    results in death()
    """

def centaur():
    """
    reached from minotaur()
    results in sphinx()
    """

def sphinx():
    """
    reached from centaur
    results in death() or chimera()
    """

def chimera():
    """
    reached from sphinx()
    results in death() or medusa()/circe()
    """

def medusa():
    """
    reached from chimera()
    results in death() or harpies()
    """

def circe():
    """
    reached from chimera()
    results in death() or harpies()
    """

def harpies():
    """
    reached from medusa() or circe()
    results in death() or phoenix()
    """

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
