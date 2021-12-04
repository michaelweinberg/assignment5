
import random
from enum import Enum
from random import randint


class Map_entry_type(Enum):
    map_empty = 0
    map_block = 1
    map_entrance = 2
    map_exit = 3
    map_healing_potion = 4
    map_pit = 5
    map_pillar_abstraction = 6
    map_pillar_encapsulation = 7
    map_pillar_inheritance = 8
    map_pillar_polymorphism = 9
    map_character = 10

# class Wall_direction(Enum):
#     wall_left = 0
#     wall_up = 1
#     wall_right = 2
#     wall_down = 3

class Map():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]
        self.start_point = None
        self.destination = None
        self.end_point = None
        self.healing_potion = None
        self.pit = None
        self.pillar_abstraction = None
        self.pillar_encapsulation = None
        self.pillar_inheritance = None
        self.pillar_polymorphism = None

    def set_map(self, x, y, value):
        if value == Map_entry_type.map_empty:
            self.map[y][x] = 0
        elif value == Map_entry_type.map_block:
            self.map[y][x] = 1
        elif value == Map_entry_type.map_entrance:
            self.map[y][x] = 2
        elif value == Map_entry_type.map_exit:
            self.map[y][x] = 3
        elif value == Map_entry_type.map_healing_potion:
            self.map[y][x] = 4
        elif value == Map_entry_type.map_pit:
            self.map[y][x] = 5
        elif value == Map_entry_type.map_pillar_abstraction:
            self.map[y][x] = 6
        elif value == Map_entry_type.map_pillar_encapsulation:
            self.map[y][x] = 7
        elif value == Map_entry_type.map_pillar_inheritance:
            self.map[y][x] = 8
        elif value == Map_entry_type.map_pillar_polymorphism:
            self.map[y][x] = 9
        elif value == Map_entry_type.map_character:
            self.map[y][x] = 10

    def is_movable(self, x, y):
        return self.map[y][x] != 1

    def is_valid(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return True

    def show_map(self):
        for row in self.map:
            show_spot = ""
            for entry in row:
                if entry == 0:
                    show_spot += "  "
                elif entry == 1:
                    show_spot += " □"
                elif entry == 2:
                    show_spot += " S"
                elif entry == 3:
                    show_spot += " N"
                elif entry == 4:
                    show_spot += " H"
                elif entry == 5:
                    show_spot += " X"
                elif entry == 6:
                    show_spot += " A"
                elif entry == 7:
                    show_spot += " E"
                elif entry == 8:
                    show_spot += " I"
                elif entry == 9:
                    show_spot += " P"
                elif entry == 10:
                    show_spot += " ▲"
            print(show_spot)

    def set_room(self):
        """set all the special rooms with names"""
        coordinate_of_room = []
        for x in range(1, self.width):
            for y in range(1, self.height):
                if self.is_movable(x, y):
                    point = (x, y)
                    coordinate_of_room.append(point)
        # self.start_point = random.choice(coordinate_of_room)
        # selected_rooms.append(self.start_point)
        # excluded.add(self.start_point)
        num_to_select = 8
        selected_rooms = random.sample(coordinate_of_room, num_to_select)
        self.start_point = selected_rooms[0]
        self.destination = selected_rooms[1]
        self.healing_potion = selected_rooms[2]
        self.pit = selected_rooms[3]
        self.pillar_abstraction = selected_rooms[4]
        self.pillar_encapsulation = selected_rooms[5]
        self.pillar_inheritance = selected_rooms[6]
        self.pillar_polymorphism = selected_rooms[7]
        self.set_map(self.start_point[0], self.start_point[1], Map_entry_type.map_entrance)
        self.set_map(self.destination[0], self.destination[1], Map_entry_type.map_exit)
        self.set_map(self.healing_potion[0], self.healing_potion[1], Map_entry_type.map_healing_potion)
        self.set_map(self.pit[0], self.pit[1], Map_entry_type.map_pit)
        self.set_map(self.pillar_abstraction[0], self.pillar_abstraction[1], Map_entry_type.map_pillar_abstraction)
        self.set_map(self.pillar_encapsulation[0], self.pillar_encapsulation[1], Map_entry_type.map_pillar_encapsulation)
        self.set_map(self.pillar_inheritance[0], self.pillar_inheritance[1], Map_entry_type.map_pillar_inheritance)
        self.set_map(self.pillar_polymorphism[0], self.pillar_polymorphism[1], Map_entry_type.map_pillar_polymorphism)


def do_recursive_division(map):
    """draw four margin wall lines"""
    for x in range(0, map.width):
        map.set_map(x, 0, Map_entry_type.map_block)
        map.set_map(x, map.height-1, Map_entry_type.map_block)
    for y in range(0, map.height):
        map.set_map(0, y, Map_entry_type.map_block)
        map.set_map(map.width-1, y, Map_entry_type.map_block)
    recursive_division(map, 1, 1, map.width-2, map.height-2, Map_entry_type.map_block)

def recursive_division(map, x, y, width, height, wall_value):
    """recursive division algorithm"""
    def get_wall_index(start, length):
        """start must be an odd number, length must be an even number"""
        if length >= 3:
            wall_index = randint(start+1, start+length-2)
            if wall_index % 2 == 1:
                wall_index -= 1
            return wall_index

    def generate_holes(map, x, y, width, height, wall_x, wall_y):
        holes = []
        hole_entrys = [(randint(x, wall_x-1), wall_y), (randint(wall_x+1, x+width-1), wall_y), (wall_x,randint(y, wall_y-1)),(wall_x, randint(wall_y+1, y+height-1))]
        margin_entrys = [(x, wall_y), (x+width-1, wall_y), (wall_x, y), (wall_x, y+height-1)]
        adjacent_entrys = [(x-1, wall_y), (x+width, wall_y), (wall_x, y-1), (wall_x, y+height)]
        for i in range(4):
            adj_x, adj_y = (adjacent_entrys[i][0], adjacent_entrys[i][1])
            if map.is_valid(adj_x, adj_y) and map.is_movable(adj_x, adj_y):
                map.set_map(margin_entrys[i][0], margin_entrys[i][1], Map_entry_type.map_empty)
            else:
                holes.append(hole_entrys[i])
        ignore_hole = randint(0, len(holes)-1)
        for i in range(0, len(holes)):
            if i != ignore_hole:
                map.set_map(holes[i][0], holes[i][1], Map_entry_type.map_empty)

    if width <= 1 or height <= 1:
        return
    """generate a row and a column wall index, must be number"""
    wall_x, wall_y = (get_wall_index(x, width), get_wall_index(y, height))
    """set horizontal and vertical lines to wall"""
    for i in range(x, x+width):
        map.set_map(i, wall_y, wall_value)
    for i in range(y, y+height):
        map.set_map(wall_x, i, wall_value)
    """create three holes"""
    generate_holes(map, x, y, width, height, wall_x, wall_y)
    recursive_division(map, x, y, wall_x-x, wall_y-y, wall_value)
    recursive_division(map, x, wall_y+1, wall_x-x, y+height-wall_y-1, wall_value)
    recursive_division(map, wall_x+1, y, x+width-wall_x-1, wall_y-y, wall_value)
    recursive_division(map, wall_x+1, wall_y+1, x+width-wall_x-1, y+height-wall_y-1, wall_value)

def run():
    width_map = 11"""always odd numbers"""
    height_map = 15"""always odd numbers"""
    map = Map(width_map, height_map)
    do_recursive_division(map)
    map.set_room()
    map.show_map()

if __name__ == "__main__":
    run()
