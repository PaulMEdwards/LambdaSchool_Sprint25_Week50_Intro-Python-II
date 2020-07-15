import sys
from room import Room
from player import Player
import textwrap

# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Main
#

if (len(sys.argv) > 1):
    name = sys.argv[1]
else:
    name = input('What is your name, adventurer?\n')

# Make a new player object that is currently in the 'outside' room.
player = Player(name, rooms['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

game_active = True

wrapper = textwrap.TextWrapper()

def move(direction):
    if(direction.lower() == 'n'):
        try:
            player.location = player.location.n_to
        except AttributeError:
            print('Cannot move North!')
    elif(direction.lower() == 's'):
        try:
            player.location = player.location.s_to
        except AttributeError:
            print('Cannot move South!')
    elif(direction.lower() == 'e'):
        try:
            player.location = player.location.e_to
        except AttributeError:
            print('Cannot move East!')
    elif(direction.lower() == 'w'):
        try:
            player.location = player.location.w_to
        except AttributeError:
            print('Cannot move West!')
    else:
        print(f'Unknown move direction: {direction}')

def lookAround():
    print()
    try:
        if(player.location.n_to):
            print(f"To the North: {player.location.n_to.name}")
    except:
        pass
    try:
        if(player.location.s_to):
            print(f"To the South: {player.location.s_to.name}")
    except:
        pass
    try:
        if(player.location.e_to):
            print(f"To the East:  {player.location.e_to.name}")
    except:
        pass
    try:
        if(player.location.w_to):
            print(f"To the West:  {player.location.w_to.name}")
    except:
        pass

def showHelp():
    maxCommandChars = 0
    maxResultChars = 0
    for key, value in commands.items():
        if len(key) > maxCommandChars: maxCommandChars = len(key)
        if len(value) > maxResultChars: maxResultChars = len(value)
    print()
    print(f"{'Command'.ljust(maxCommandChars+1, ' ')}: Result")
    print(f"{''.ljust(maxCommandChars+3+maxResultChars, '=')}")
    for key, value in commands.items():
        print(f"{key.ljust(maxCommandChars+1, ' ')}: {value}")

def quit_game():
    game_active = False
    sys.exit()

commands = {
    'q': 'Quit',
    'quit': 'Quit',
    'w': 'Move North',
    'north': 'Move North',
    's': 'Move South',
    'south': 'Move South',
    'a': 'Move East',
    'east': 'Move East',
    'd': 'Move West',
    'west': 'Move West',
    # 'e': 'Equip',
    # 'equip': 'Equip',
    # 'r': 'Retreat',
    # 'retreat': 'Retreat',
    # 't': 'Torch',
    # 'torch': 'Torch',
    # 'y': 'Yell',
    # 'yell': 'Yell',
    # 'u': 'Use',
    # 'use': 'Use',
    # 'i': 'Inventory',
    # 'inv': 'Inventory',
    # 'inventory': 'Inventory',
    # 'o': 'Open',
    # 'open': 'Open',
    # 'f': 'Fight',
    # 'fight': 'Fight',
    # 'g': 'Get',
    # 'get': 'Get',
    # 'drop': 'Drop',
    'l': 'Look',
    'look': 'Look',
    # 'm': 'Map',
    # 'map': 'Map',
    '?': 'Show Help',
    'h': 'Show Help',
    'help': 'Show Help',
}

def inputSwitcher(arg):
    a = arg.lower()
    if (a == 'q' or a == 'quit'):
        quit_game()
    elif (a == 'w' or a == 'north'):
        move('n')
    elif (a == 's' or a == 'south'):
        move('s')
    elif (a == 'a' or a == 'east'):
        move('e')
    elif (a == 'd' or a == 'west'):
        move('w')
    elif (a == '?' or a == 'h' or a == 'help'):
        showHelp()
    # elif (a == 'e' or a == 'equip'):
    #     equip()
    # elif (a == 'r' or a == 'retreat'):
    #     retreat()
    # elif (a == 't' or a == 'torch'):
    #     torch()
    # elif (a == 'y' or a == 'yell'):
    #     yell()
    # elif (a == 'u' or a == 'use'):
    #     use()
    # elif (a == 'i' or a == 'inv' or a == 'inventory'):
    #     inventory()
    # elif (a == 'o' or a == 'open'):
    #     openItem()
    # elif (a == 'f' or a == 'fight'):
    #     fight()
    # elif (a == 'g' or a == 'get'):
    #     get()
    # elif (a == 'drop'):
    #     drop()
    elif (a == 'l' or a == 'look'):
        lookAround()
    # elif (a == 'm' or a == 'map'):
    #     map()
    else:
        # raise Exception(f"Unknown input: {arg}")
        print(f"Unknown input: {arg}")
        pass    # Do nothing, re-prompt


while(game_active):
    print(f"\n{player}")
    # print(wrapper.fill(player))
    inputSwitcher(input('What would you like to do? '))
