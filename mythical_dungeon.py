# http://learnpythonthehardway.org/book/ex36.html

from sys import exit

def pack_storage():
    """
    adds dropped items to the player's pack
    """
    
def pack_list():
    """
    displays the contents of the player's pack
    """
    
def death():
    """
    describes how the player dies
    exits the game
    """
    
    
def starting_point():
    """
    starts the entire game
    describes the scenario, rules, and goal
    results in unicorn()
    """
    
def unicorn():
    """
    reached from starting_point()
    results in hippogriff()
    """
    
def hippogriff():
    """
    reached from unicorn()
    results in death() or minotaur()
    """
    
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
    