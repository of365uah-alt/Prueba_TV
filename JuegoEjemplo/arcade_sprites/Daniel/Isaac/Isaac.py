from pytiled_parser import Property

class Room:

    def __init__(self, description, north, south, east, west):

        self._description = description

        self._north = north
        self._south = south
        self._east = east
        self._west = west

    @property
    def description(self):
        return self._description

    @property
    def north(self):
        return self._north

    @property
    def south(self):
        return self._south

    @property
    def east(self):
        return self._east

    @property
    def west(self):
        return self._west

    def get_adjacent_room(self, cmd_dir: str):

        d = cmd_dir.lower()

        if d == "n":
            return self.north

        if d == "s":
            return self.south

        if d == "e":
            return self.east

        if d == "w":
            return self.west

        return None

def main():

    current_room = 0
    done = False

    room_list = [
        Room("You are in the bedroom 1. There is a passage to the east.", None, None, 1, None),
        Room("You are in the south hallway. There is a passage to the north, east and west.", 4, None, 2, 0),
        Room("You are in the dining room. There is a passage to the north and west.", 5, None, None, 1),
        Room("You are in the bedroom 2. There is a passage to the east.", None, None, 4, None),
        Room("You are in the north hallway. There is a passage to the north, south, east and west.", 6, 1, 5, 3),
        Room("You are in the kitchen. There is a passage to the south and west.", None, 2, None, 4),
        Room("You are in the balcony. There is a passage to the south.", None, 4, None, None)
    ]

    while not done:

        room = room_list[current_room]

        print(room.description)

        print("Where do you want to go? (\"n/s/e/w\", \"q\" to quit)")
        cmd = input("> ").lower()

        if cmd == "q":

            if current_room == 6:
                print("You jump off the balcony and got impaled on a spear!")

            done = True
            continue

        adjacent = room.get_adjacent_room(cmd)

        if adjacent is None:
            print("You cant go that way!")
        else:
            current_room = adjacent

main()