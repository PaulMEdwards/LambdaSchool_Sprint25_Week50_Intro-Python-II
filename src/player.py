# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, health=100, maxHealth=100, weapon=None, armor=None, inventory=[]):
        self.name = name
        self.location = location
        self.health = health
        self.maxHealth = maxHealth
        self.weapon = weapon
        self.armor = armor
        self.inventory = inventory
    def __str__(self):
        p = f"Player: {self.name}, Health: {self.health}/{self.maxHealth}"
        w = "None" if (self.weapon == None) else self.weapon.name
        a = "None" if (self.armor == None) else self.armor.name
        e = f"Weapon: {w}, Armor: {a}"
        i = f"Inventory: {len(self.inventory)} items"
        l = f"{self.location}"
        return f"{p}\n{e}\n{i}\n\n{l}\n"
