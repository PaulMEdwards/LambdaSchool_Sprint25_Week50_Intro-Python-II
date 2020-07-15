# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, health=100, weapon=None, armor=None):
        self.name = name
        self.location = location
        self.health = health
        self.weapon = weapon
        self.armor = armor
    def __str__(self):
        p = f"Player: {self.name}, Health: {self.health}"
        w = "None" if (self.weapon == None) else self.weapon.name
        a = "None" if (self.armor == None) else self.armor.name
        e = f"Weapon: {w}, Armor: {a}"
        r = f"Location: {self.location.name}\n{self.location.description}"
        return f"{p}\n{e}\n{r}\n"
