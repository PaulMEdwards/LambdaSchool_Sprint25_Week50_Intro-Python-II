import sys
from room import Room
from player import Player
import textwrap
import random

wrapper = textwrap.TextWrapper()

# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}

# types
Armor=0
Weapon=1
# Magic=2
Key=3
Map=4
Torch=5
# Enemy=6

items = [
    {
        'name': "Belt",
        'description': "The Belt of Truth",
        'type': Armor,
        'HP': 100,
        'DP': 0,
        'AP': 100,
        'SP': 0,
        'AOG': 1,
    },
    {
        'name': "Chestpiece",
        'description': "The Body Armor of God's Righteousness",
        'type': Armor,
        'HP': 150,
        'DP': 0,
        'AP': 150,
        'SP': 100,
        'AOG': 1,
    },
    {
        'name': "Shoes",
        'description': "The Peace that comes from the Good News",
        'type': Armor,
        'HP': 50,
        'DP': 0,
        'AP': 50,
        'SP': 0,
        'AOG': 1,
    },
    {
        'name': "Shield",
        'description': "The Shield of Faith",
        'type': Armor,
        'HP': 400,
        'DP': 0,
        'AP': 500,
        'SP': 200,
        'AOG': 1,
    },
    {
        'name': "Helmet",
        'description': "The Helmet of Salvation",
        'type': Armor,
        'HP': 200,
        'DP': 0,
        'AP': 200,
        'SP': 200,
        'AOG': 1,
    },
    {
        'name': "Sword",
        'description': "The Sword of the Spirit",
        'type': Weapon,
        'HP': 0,
        'DP': 1000,
        'AP': 0,
        'SP': 500,
        'AOG': 1,
    },
    {
        'name': "Spear",
        'description': "Spear of Justice",
        'type': Weapon,
        'HP': 0,
        'DP': 250,
        'AP': 0,
        'SP': 0,
        'AOG': 0,
    },
    {
        'name': "Club",
        'description': "Caveman Club",
        'type': Weapon,
        'HP': 0,
        'DP': 100,
        'AP': 0,
        'SP': 0,
        'AOG': 0,
    },
    {
        'name': "Torch",
        'description': "A large stick doused on one end with a slow-burning combustible material which can be set ablaze to act as a source of light to illuminate dark places.",
        'type': Torch,
        'HP': 0,
        'DP': 0,
        'AP': 0,
        'SP': 0,
        'AOG': 0,
    },
    {
        'name': "Map",
        'description': "A map showing the region layout.",
        'type': Map,
        'HP': 0,
        'DP': 0,
        'AP': 0,
        'SP': 0,
        'AOG': 0,
    },
    {
        'name': "Key",
        'description': "A key which can be used to open a lock.",
        'type': Key,
        'HP': 0,
        'DP': 0,
        'AP': 0,
        'SP': 0,
        'AOG': 0,
    },
    # {
    #     'name': "",
    #     'description': "",
    #     'type': X,
    #     'HP': 0,
    #     'DP': 0,
    #     'AP': 0,
    #     'SP': 0,
    #     'AOG': 0,
    # },
]

enemies = [
    {
        'name': "Satan",
        'weapons': [
            {
                'name': "Fiery Arrows",
                'DP': 100,
                'SP': 100,
            },
        ],
        'HP': 10000,
        'AP': 1000,
        'XP': 10000,
    },
]


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

# Populate rooms with items

rl = len(rooms)
enumeratedRooms = list(enumerate(rooms))
# print(f"# rooms: {rl}")
for item in items:
    # print(f"Item: {item}")
    x = random.randrange(0, rl)
    # print(f"x: {x+1}")
    room = rooms[enumeratedRooms[x][1]]
    # print(room)
    room.items.append(item)
    # print(f"Room Items: {room.items}")

#
# Main
#

if (len(sys.argv) > 1):
    name = sys.argv[1]
else:
    name = input('What is your name, adventurer? ')

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
    if (len(player.location.items) > 0):
        print(f"\nItems nearby:")
        for item in player.location.items:
            print(f"{item['name']}")

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

def equip():
    print("NOT IMPLEMENTED!!")

def torch():
    print("NOT IMPLEMENTED!!")

def inventory():
    print("NOT IMPLEMENTED!!")
    print(f"Inventory: {player.inventory}")

def openItem(item):
    print("NOT IMPLEMENTED!!")

def fight():
    print("NOT IMPLEMENTED!!")

def get():
    if (len(player.location.items) > 0):
        targetItem = None
        itemName = input("Which nearby item would you like to get & put into inventory? ")
        for item in player.location.items:
            if (item['name'].lower() == itemName.lower()):
                targetItem = item
        if (targetItem == None):
            print(f"Couldn't find nearby item named '{itemName}'")
        else:
            player.inventory.append(targetItem)
            player.location.items.remove(targetItem)
    else:
        print(f"There are no items here.")

def drop():
    if (len(player.inventory) > 0):
        targetItem = None
        itemName = input("Which item would you like to drop from inventory? ")
        for item in player.inventory:
            if (item['name'].lower() == itemName.lower()):
                targetItem = item
        if (targetItem == None):
            print(f"Couldn't find inventory item named '{itemName}'")
        else:
            player.location.items.append(targetItem)
            player.inventory.remove(targetItem)

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
    print("Exiting...\n")
    game_active = False
    sys.exit()

commands = {
    'w': 'Move North',
    'north': 'Move North',
    's': 'Move South',
    'south': 'Move South',
    'a': 'Move East',
    'east': 'Move East',
    'd': 'Move West',
    'west': 'Move West',
    'e': 'Equip',
    'equip': 'Equip',
    # 'r': 'Retreat',
    # 'retreat': 'Retreat',
    't': 'Torch',
    'torch': 'Torch',
    # 'y': 'Yell',
    # 'yell': 'Yell',
    # 'u': 'Use',
    # 'use': 'Use',
    'i': 'Inventory',
    'inv': 'Inventory',
    'inventory': 'Inventory',
    'o': 'Open',
    'open': 'Open',
    'f': 'Fight',
    'fight': 'Fight',
    'g': 'Get',
    'get': 'Get',
    'dr': 'Drop',
    'drop': 'Drop',
    'l': 'Look',
    'look': 'Look',
    'm': 'Map',
    'map': 'Map',
    '?': 'Show Help',
    'h': 'Show Help',
    'help': 'Show Help',
    'q': 'Quit',
    'quit': 'Quit',
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
    elif (a == 'e' or a == 'equip'):
        equip()
    # elif (a == 'r' or a == 'retreat'):
    #     retreat()
    elif (a == 't' or a == 'torch'):
        torch()
    # elif (a == 'y' or a == 'yell'):
    #     yell()
    # elif (a == 'u' or a == 'use'):
    #     use()
    elif (a == 'i' or a == 'inv' or a == 'inventory'):
        inventory()
    elif (a == 'o' or a == 'open'):
        openItem()
    elif (a == 'f' or a == 'fight'):
        fight()
    elif (a == 'g' or a == 'get'):
        get()
    elif (a == 'dr' or a == 'drop'):
        drop()
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
