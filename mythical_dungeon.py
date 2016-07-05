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
    print "You find yourself in a clearing with an empty satchel. To obtain safe passage,"
    print "you must navigate from this clearing to a room full of treasure. Between the"
    print "clearing and the treasure is a dungeon of dangerous creatures. You must use"
    print "your wits and knowledge of mythical beasts to safely get through the dungeon."
    print
    print "The creatures may assist you on your journey by providing supplies and"
    print "knowledge. But beware! An incorrect turning or action will bring your death."
    unicorn()

def reset():
    """
    resets the game state
    this absolutely should be changed at some point
    """
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
    print "You walk north into the trees surrounding the clearing. After you can no"
    print "longer see the clearing, you catch a glimpse of white from behind a large"
    print "tree. You step forward cautiously to find a unicorn."
    print
    print "*********************************************************"
    print "                 ENTERING UNICORN GROVE                  "
    print "*********************************************************"
    print
    print "At the sound of your breathing, the unicorn runs into the woods, revealing a"
    print "small sign. The sign stands between you and a door in a large tree."
    print
    print "Do you read the sign, Y/N"
    selection = raw_input(">> ").lower()
    if selection == "y":
        print
        print "You approach the sign to find faded writing."
        print
        print "'Good manners are their own reward'"
        print
        print "If all you need are good manners, the treasure is sure to be easy to get."
        print
        print "You walk around the sign and through the door."
        hippogriff()
    elif selection == "n":
        print "Obviously, you're not a reader."
        print "You ignore the sign and walk through the door."
        hippogriff()
    else:
        death("You wander around the woods until you waste away and die.")

def hippogriff():
    """
    reached from unicorn()
    results in death() or minotaur()
    """
    print
    print "On the other side of the door, you find yourself in a medium-sized room with"
    print "soft grass below your feet. The ceiling is high enough to almost feel like you"
    print "are still outdoors, except for the clearly visible walls."
    print
    print "There is another door directly across from the one you just came through. As"
    print "As you step closer to the exit, a hippogriff lands between you and the door."
    print
    print "*********************************************************"
    print "                     HIPPOGRIFF ENTRY                    "
    print "*********************************************************"
    print
    supply_list()
    print "Do you demand passage to the door or ask politely?"
    answer = raw_input(">> ").lower()
    if "politely" in answer:
        print
        print "The hippogriff moves aside, allowing you to walk through the door. It"
        print "follows you through the door and is now your companion through this dungeon."
        supply_storage("Hippogriff")
        minotaur()
    elif "demand" in answer:
        death("The hippogriff does not appreciate your tone and kills you.")
    else:
        death("You sit down in front of the hippogriff, never to rise again.")

def minotaur():
    """
    reached from hippogriff()
    results in death() or manticore()/centaur()
    """
    print
    print "You and your hippogriff without a name walk through the door to find yourself"
    print "on a narrow stone ledge. Looking around the room, you see that the floor is"
    print "made up of many ledges in a labyrinthine pattern."
    print
    print "The room is large and you can make out what looks to be two doors in the wall"
    print "across from you. You hear the bellow of a bull and something that sounds like"
    print "human feet moving across dusty ground, not hoof beats."
    print
    print "*********************************************************"
    print "                    MINOTAUR'S MAZE                      "
    print "*********************************************************"
    print
    supply_list()
    print "It appears that the ledges will allow you to cross to the other side of the"
    print "room. Do you walk or run across the top of the labyrinth walls?"
    answer = raw_input(">> ").lower()
    if "run" in answer:
        death("You trip and fall off the wall. The minotaur gores and then eats you.")
    elif "walk" in answer:
        print
        print "As you cross, you hear but never see the minotaur. Some of the walls appear to"
        print "be in poor repair, with pieces falling into the maze as you walk past. It is"
        print "slow going, but you safely reach the other side where you find a bow and a quiver"
        print "of arrows between two doors. Do you take the bow and quiver, Y/N?"
        selection = raw_input(">> ").lower()
        if selection == "y":
            supply_storage("Bow and Quiver")
            print "You have added 'Bow and Quiver' to your list of supplies."
        elif selection == "n":
            pass
        else:
            death("The Minotaur leaps over wall and kills you while you were making a decision.")
        print
        print "There is a door to the left and a door to the right. Which door do you go through?"
        choice = raw_input(">> ").lower()
        if "right" in choice:
            print
            print "You and your hippogriff move to the right and walk through the door."
            centaur()
        elif "left" in choice:
            print
            print "You and your hippogriff move to the left and walk through the door."
            manticore()
        else:
            death("You are so bad at deciding that the Minotaur leaps over wall and kills you.")
    else:
        death("Your hippogriff headbutts you into the labyrinth where the Minotaur eats you.")

def manticore():
    """
    reached from minotaur()
    results in death()
    """
    print "Hey look, a manticore!"
    print
    print "*********************************************************"
    print "                      MANTICORE ROOM                     "
    print "*********************************************************"
    print
    supply_list()
    death("You get devoured whole. No evidence of your body or possessions remain.")

def centaur():
    """
    reached from minotaur()
    results in sphinx()
    """
    print "You and your hippogriff walk cautiously through the door to find lush grass"
    print "and many trees. You cannot see through the trees, so you turn to the left and"
    print "follow the wall. After walking for a few minutes, you realize that the wall is"
    print "curved and that this is a round room with high walls and no ceiling. You hear"
    print "hoofbeats and turn to see a centaur approaching you from the trees."
    print
    print "*********************************************************"
    print "                      CENTAUR ROOM                       "
    print "*********************************************************"
    print
    supply_list()
    print "The centaur hands you a small bundle of green stems and leaves tied up with"
    print "string. He stares at you while pawing at the ground until you place the bundle"
    print "in your satchel."
    supply_storage("Bundle of herbs")
    print "After the bundle is safely in your satchel, the centaur turns and trots away."
    print "Rather than follow him, you continue to follow the wall until you find a door."
    sphinx()

def sphinx():
    """
    reached from centaur
    results in death() or chimera()
    """
    print "You follow the hippogriff through the door to find yourself in a bright room."
    print "After your eyes adjust, you see a four-legged figure with a feminine face. Is"
    print "that a sphinx?"
    print
    print "*********************************************************"
    print "                        SPHINX ROOM                      "
    print "*********************************************************"
    supply_list()
    print "'You may not pass until you answer my riddle. What has four legs at breakfast,"
    print "two legs at lunch, and three legs at dinner?'"
    answer = raw_input(">> ").lower()
    if answer == "man":
        print "'You answered my riddle correctly. You may proceed. Please take this gift.'"
        supply_storage("Earmuffs")
        print "You have added 'Earmuffs' to your supplies."
        chimera()
    else:
        print "The sphinx grins. 'You answered my riddle incorrectly and I am hungry.'"
        death("The sphinx eats you.")

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
