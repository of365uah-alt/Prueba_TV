
class room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def set_description(self, description):
        self.description = description
    def get_description(self):       
        return self.description
    
    def set_north(self, north):
        self.north = north 
    def get_north(self):        
        return self.north
    
    def set_south(self, south):
        self.south = south
    def get_south(self):        
        return self.south

    def set_east(self, east):
        self.east = east
    def get_east(self):        
        return self.east

    def set_west(self, west): 
        self.west = west
    def get_west(self):        
        return self.west

def main():
    room_list = [
        room("You are in a bedroom. There is a door to the east.", None, None, 1, None),
        room("You are in a hallway. There are doors to the west and east and a path to the north.", 4, None, 2, 0),
        room("You are in a dinning room. There are doors to the north and west.", 5, None, None, 1),
        room("You are in garage. You can only go back (to east).",None,None,4,None),
        room("You are in a hallway. There are doors to the west, east and north and a path to the south.", 6, 1, 5, 3),
        room("You are in a kitchen. There are doors to the south and west.", None, 2, None, 4),
        room("You are in a balcony. There is a door to the south but you can jump if you want.", None, 4, None, None)
    ]
    current_room = 0
    done = False
    while not done:
        print()
        print(room_list[current_room].get_description())
        print("Where do you want to go?\n(n/s/e/w or quit(q))")
        command = str(input("> ")).lower()

        if command == "n" or command == "north":
            next_room = room_list[current_room].get_north()
            if next_room is not None:
                current_room = next_room
            else:
                print("You can't go that way.")

        elif command == "s":
            next_room = room_list[current_room].get_south()
            if next_room is not None:
                current_room = next_room
            else:
                print("You can't go that way.")

        elif command == "e":
            next_room = room_list[current_room].get_east()
            if next_room is not None:
                current_room = next_room
            else:
                print("You can't go that way.")

        elif command == "w":
            next_room = room_list[current_room].get_west()
            if next_room is not None:
                current_room = next_room
            else:
                print("You can't go that way.")

        elif command == "q":
            if current_room == 0:
                print("You go to sleep.")
            if current_room == 1:
                print("You go to the bathroom and drown yourself in the bathtub.")
            if current_room == 2:
                print("You eat some bad food and die of food poisoning.")
            if current_room == 3:
                print("You hop on a bike and flee.")
            if current_room == 4:
                print("You take a shotgun and you make a reference to Kurt Cobain.")
            if current_room == 5:
                print("You take a knife and end your suffering.")
            if current_room == 6:
                print("You jump off the balcony and die.")
            done = True

        else:
            print("I don't understand that command.")

main()