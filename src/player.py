# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    # function dedicated to the movement
    def move_to(self, direction, current_location):
        attribtue = direction + '_to'

        # make sure room exsists in that direction
        if hasattr(current_location, attribtue):
            return getattr(current_location, attribtue)
        # if you cant go that way
        else:
            print("\n")
            print("There's nothing that way.")

        return current_location

