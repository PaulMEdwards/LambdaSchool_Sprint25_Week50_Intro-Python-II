# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        print(f"name: {self.name}\ndesc: {self.description}\n")
    def __str__(self):
        print(f"You find yourself in the {self.name} room which appears as {self.description}")
