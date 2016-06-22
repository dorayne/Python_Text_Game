# http://learnpythonthehardway.org/book/ex36.html

import sys

SUPPLY_CONTENTS = []

def starting_point():
    """
    starts the entire game
    describes the scenario, rules, and goal
    results in unicorn()
    """
    print
    print "*********************************************************"
    print "             WELCOME TO THE MYTHICAL DUNGEON             "
    print "*********************************************************"
    print
    print "You find yourself in a clearing. To obtain safe"
    print "passage, you must navigate from this clearing to"
    print "a room full of treasure. Between the clearing and"
    print "the treasure is a dungeon of dangerous creatures."
    print "You must use your wits and knowledge of mythical"
    print "beasts to safely navigate through the dungeon."
    print
    print "The creatures may assist you on your journey by"
    print "providing supplies and knowledge. But beware! An"
    print "incorrect turning or action will bring your death."
    print
    unicorn()

def reset():
    count = len(SUPPLY_CONTENTS)
    while count > 0:
        SUPPLY_CONTENTS.pop(0)
        count = count - 1
    return SUPPLY_CONTENTS

def death(reason):
    """
    describes how the player dies
    exits the game
    """
    print reason, "Great job!"
    print "Do you want to play again?"
    selection = raw_input("Y/N ").lower()
    if selection == "y":
        reset()
        starting_point()
    else:
        sys.exit(0)

def supply_storage(item):
    """
    adds dropped/found items to the player's supplies
    """
    SUPPLY_CONTENTS.append(item)
    return SUPPLY_CONTENTS

def supply_list():
    """
    displays the contents of the player's supplies
    """
    if len(SUPPLY_CONTENTS) < 1:
        print "You currently do not have any supplies."
    else:
        print "You have these supplies:"
        for item in SUPPLY_CONTENTS:
            print item
    print

def unicorn():
    """
    reached from starting_point()
    results in hippogriff()
    """
    print
    print "*********************************************************"
    print "                 ENTERING UNICORN GROVE                  "
    print "*********************************************************"
    print
    print "You walk north into the trees surrounding the"
    print "clearing. After you can no longer see the clearing,"
    print "you catch a glimpse of white from behind a large"
    print "tree. You step forward cautiously to find a unicorn."
    print
    print "At the sound of your breathing, the unicorn runs"
    print "into the woods, revealing a small sign. The sign"
    print "stands between you and a door in a large tree."
    print
    print "Do you read the sign, Y/N"
    selection = raw_input(">> ").lower()
    if selection == "y":
        print
        print "You approach the sign to find faded writing."
        print
        print "'Good manners are their own reward'"
        print
        print "If all you need are good manners, the treasure"
        print "is sure to be easy to get."
        print
        print "You walk around the sign and through the door."
        hippogriff()
    elif selection == "n":
        print "Obviously, you're not a reader."
        hippogriff()
    else:
        death("You wander around the woods until you waste away and die.")

def hippogriff():
    """
    reached from unicorn()
    results in death() or minotaur()
    """
    print "*********************************************************"
    print "                     HIPPOGRIFF ENTRY                    "
    print "*********************************************************\n"
    supply_list()
    print "Description"
    print "Do you demand passage to the door or ask politely?"
    answer = raw_input(">> ").lower()
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
    print "*********************************************************"
    print "                    MINOTAUR'S MAZE                      "
    print "*********************************************************\n"
    supply_list()
    print "Description"
    print "Do you walk or run across the top of the labyrinth walls?"
    answer = raw_input(">> ").lower()
    if "run" in answer:
        death("Fall in and get gored by minotaur.")
    elif "walk" in answer:
        print "reach other side safely."
        print "You find a bow and quiver of arrows."
        selection = raw_input("Do you take them, Y/N? ").lower()
        if selection == "y":
            supply_storage("Bow and Quiver")
        elif selection == "n":
            return
        else:
            death("Minotaur leaps over wall and kills you.")
        print "Door to the left and door to the right."
        choice = raw_input("Which door do you go through? ").lower()
        if "right" in choice:
            centaur()
        elif "left" in choice:
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
    print "*********************************************************"
    print "                      MANTICORE ROOM                     "
    print "*********************************************************\n"
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
    print "*********************************************************"
    print "                        SPHINX ROOM                      "
    print "*********************************************************\n"
    supply_list()
    print "What has 4 legs at breakfast, 2 legs at lunch, and 3 legs at dinner?"
    answer = raw_input(">> ").lower()
    if answer == "man":
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
    print "*********************************************************"
    print "                       CHIMERA ROOM                      "
    print "*********************************************************\n"
    supply_list()
    print "description"
    print "how do i want to word your choices here?"
    choice = raw_input(">> ").lower()
    if "bow" and "hippogriff" in choice:
        print "something about killing a chimera"
        supply_storage("lyre")
        print "pick a door"
        selection = raw_input(">> ").lower()
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
    print "*********************************************************"
    print "                        MEDUSA ROOM                      "
    print "*********************************************************\n"
    supply_list()
    print "Vague description"
    print "Do you proceed to get a better look or close your eyes and hope for the best?"
    choice = raw_input(">> ").lower()
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
    print "*********************************************************"
    print "                        CIRCE ROOM                       "
    print "*********************************************************\n"
    supply_list()
    print "description"
    print "Do you have anything in your pack for Circe?"
    if "Bundle of herbs" in SUPPLY_CONTENTS:
        print "Something about circe not turning you into a pig"
        SUPPLY_CONTENTS.remove("Bundle of herbs")
        supply_storage("Food")
        harpies()
    else:
        death("Turned into a pig")

def harpies():
    """
    reached from medusa() or circe()
    results in death() or phoenix()
    """
    print "*********************************************************"
    print "                     ROOM OF HARPIES                     "
    print "*********************************************************\n"
    supply_list()
    if "Food" in SUPPLY_CONTENTS:
        print "Harpies steal your food and fly away"
        SUPPLY_CONTENTS.remove("Food")
        phoenix()
    else:
        death("The harpies peck out your eyes cause you didn't have any food for them.")

def phoenix():
    """
    reached from harpies()
    results in pegasus()
    """
    print "*********************************************************"
    print "                       PHOENIX ROOM                      "
    print "*********************************************************\n"
    supply_list()
    print "Description"
    print "Something something flame sword"
    supply_storage("Flaming sword")
    pegasus()

def pegasus():
    """
    reached from phoenix()
    results in cerberus()
    """
    print "*********************************************************"
    print "                       PEGASUS ROOM                      "
    print "*********************************************************\n"
    supply_list()
    print "Description"
    print "Do you need advice? Y/N"
    choice = raw_input(">> ").lower()
    if choice == "y":
        print "Here is some advice:"
        cerberus()
    else:
        print "You think you're so smart!"
        cerberus()

def cerberus():
    """
    reached from pegasus()
    results in death() or sirens()
    """
    print "*********************************************************"
    print "                       CERBERUS ROOM                     "
    print "*********************************************************\n"
    supply_list()
    print "Description"
    print "Which of your supplies would you like to use to get past Cerberus?"
    selection = raw_input(">> ").lower()
    if "lyre" in selection:
        print "The lyre lulls cerberus asleep and you tiptoe past"
        sirens()
    else:
        death("All the dog heads eat you!")

def sirens():
    """
    reached from cerberus()
    results in death() or boat()
    """
    print "*********************************************************"
    print "                      MANTICORE ROOM                     "
    print "*********************************************************\n"
    print "Description"
    print "Something something earmuffs"
    selection = raw_input(">> ").lower()
    if "earmuffs" in selection:
        print "You get the earmuffs on before you hear the sirens sing."
        print "You walk casually past the sirens and hop into the boat conveniently tied to the shore."
        boat()
    else:
        death("The siren song lures you to your death.")

def boat():
    """
    reached from sirens()
    results in death() or hydra()/scylla()/charybdis()
    """
    print "*********************************************************"
    print "                     TAKE TO THE SEAS                    "
    print "*********************************************************\n"
    supply_list()
    print "You're in a boat following the current."
    print "the river splits. Do you choose the right or left fork?"
    choice = raw_input(">> ").lower()
    if "right" in choice:
        print "Steer to the right"
        hydra()
    elif "left" in choice:
        print "Steer to the left"
        print "You have to choose Scylla or Charybdis"
        selection = raw_input(">> ").lower()
        if "Scylla" in selection:
            scylla()
        elif "Charybdis" in selection:
            charybdis()
        else:
            death("You dead.")
    else:
        death("You spend so much time not making a decision that your boat is dashed on the rocks.")

def hydra():
    """
    reached from sirens() via boat()
    results in death() or griffin()
    """
    print "*********************************************************"
    print "                        HYDRA AREA                       "
    print "*********************************************************\n"
    supply_list()
    print "Description"
    print "You must have some supplies that will help you get past the Hydra"
    selection = raw_input(">> ").lower()
    if "Flaming sword" in selection:
        print "You cut off a head and the flames cauterize the neck wound, preventing more heads from growing."
        griffin()
    else:
        death("The heads eat you and your poor, blameless hippogriff.")

def scylla():
    """
    reached from sirens() via boat()
    results in death() or griffin()
    """
    print "*********************************************************"
    print "                       SCYLLA AREA                       "
    print "*********************************************************\n"
    supply_list()
    print "Description"
    if "hippogriff" in SUPPLY_CONTENTS:
        print "At the sight of Scylla, your faithful hippogriff flies out of the boat in fear."
        print "Your companion's flight distracts all of the heads who pluck him easily out of the sky, allowing you to pass"
        SUPPLY_CONTENTS.remove("hippogriff")
        griffin()
    else:
        death("Scylla eats you and is still hungry.")

def charybdis():
    """
    reached from sirens() via boat()
    only results in death()
    """
    print "*********************************************************"
    print "                      CHARYBDIS AREA                     "
    print "*********************************************************\n"
    supply_list()
    print "There is no escaping Charybdis."
    death("Your boat cannot break free of the whirlpool and you drown.")

def griffin():
    """
    reached from hydra and scylla
    results in death() or treasure()
    """
    print "*********************************************************"
    print "                       GRIFFIN ROOM                      "
    print "*********************************************************\n"
    supply_list()
    print "Description"
    print "The griffin stands between you and the door clearly marked Treasure."
    print "The griffin demands a password"
    password = raw_input(">> ").lower()
    if "please" in password:
        print "The griffin steps aside, allowing you to get to the treasure."
        treasure()
    else:
        death("You died")

def treasure():
    """
    can only be reached from griffin()
    this is the winning room
    """
    print "*********************************************************"
    print "                      TREASURE ROOM                      "
    print "*********************************************************\n"
    print "You get all this treasure. You win!"
    print "Do you want to play again?"
    selection = raw_input("Y/N ").lower()
    if selection == "y":
        reset()
        starting_point()
    else:
        sys.exit(0)

starting_point()
