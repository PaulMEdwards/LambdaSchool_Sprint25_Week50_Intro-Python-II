# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
    def __repr__(self):
        print(f"name: {self.name}\ndesc: {self.description}\nitems: {str(self.items)}")
    def __str__(self):
        return f"You find yourself in the {self.name}\n{self.description}.\n\nThere are {len(self.items)} items nearby."
