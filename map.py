import random

from assignment5.assignment5.adventurer import Adventurer
from assignment5.assignment5.map_entry_type import Map_entry_type
from assignment5.assignment5.room import Room


class Map:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__map = [[Room(y, x) for x in range(self.__width)] for y in range(self.__height)]
        self.start_point = Room(None, None)
        self.destination = Room(None, None)
        self.__healing_potion = Room(None, None)
        self.__pit = Room(None, None)
        self.__pillar_abstraction = Room(None, None)
        self.__pillar_encapsulation = Room(None, None)
        self.__pillar_inheritance = Room(None, None)
        self.__pillar_polymorphism = Room(None, None)
        self.__hero = None

    def set_width(self):
        pass

    def get_width(self):
        return self.__width

    def set_height(self):
        pass

    def get_height(self):
        return self.__height

    def set_map(self, room, value):
        if value == Map_entry_type.map_empty:
            room.set_empty()
        elif value == Map_entry_type.map_block:
            room.set_block()
        elif value == Map_entry_type.map_entrance:
            room.set_entrance()
        elif value == Map_entry_type.map_exit:
            room.set_exit()
        elif value == Map_entry_type.map_healing_potion:
            room.set_healing_potion()
        elif value == Map_entry_type.map_pit:
            room.set_pit()
        elif value == Map_entry_type.map_pillar_abstraction:
            room.set_pillar_abstraction()
        elif value == Map_entry_type.map_pillar_encapsulation:
            room.set_pillar_encapsulation()
        elif value == Map_entry_type.map_pillar_inheritance:
            room.set_pillar_inheritance()
        elif value == Map_entry_type.map_pillar_polymorphism:
            room.set_pillar_polymorphism()

    def is_movable(self, room):
        print("room value", room.get_value())
        return room.get_value() != 1

    def is_valid(self, y, x):
        if x < 0 or x >= self.__width or y < 0 or y >= self.__height:
            return False
        return True

    def show_map(self):
        for row in self.__map:
            show_spot = ""
            for room in row:
                if room.get_value() == 0:
                    show_spot += "  "
                elif room.get_value() == 1:
                    show_spot += " □"
                elif room.get_value() == 2:
                    show_spot += " S"
                elif room.get_value() == 3:
                    show_spot += " N"
                elif room.get_value() == 4:
                    show_spot += " H"
                elif room.get_value() == 5:
                    show_spot += " X"
                elif room.get_value() == 6:
                    show_spot += " A"
                elif room.get_value() == 7:
                    show_spot += " E"
                elif room.get_value() == 8:
                    show_spot += " I"
                elif room.get_value() == 9:
                    show_spot += " P"
                elif room.get_value() == 10:
                    show_spot += " ▲"
            print(show_spot)

    def set_room(self):
        """set all the special rooms with names"""
        rooms = []
        for x in range(self.__width):
            for y in range(self.__height):
                if self.is_movable(self.__map[y][x]):
                    rooms.append(self.__map[y][x])
        special_room = random.sample(rooms, 8)
        self.start_point = special_room[0]
        self.destination = special_room[1]
        self.__healing_potion = special_room[2]
        self.__pit = special_room[3]
        self.__pillar_abstraction = special_room[4]
        self.__pillar_encapsulation = special_room[5]
        self.__pillar_inheritance = special_room[6]
        self.__pillar_polymorphism = special_room[7]
                    # rooms.append(self.__map[y][x])
        # self.start_point = random.choice(rooms)
        # self.destination = random.choice(rooms)
        # self.__healing_potion = random.choice(rooms)
        # self.__pit = random.choice(rooms)
        # self.__pillar_abstraction = random.choice(rooms)
        # self.__pillar_encapsulation = random.choice(rooms)
        # self.__pillar_inheritance = random.choice(rooms)
        # self.__pillar_polymorphism = random.choice(rooms)
        self.set_map(self.start_point, Map_entry_type.map_entrance)
        self.set_map(self.destination, Map_entry_type.map_exit)
        self.set_map(self.__healing_potion, Map_entry_type.map_healing_potion)
        self.set_map(self.__pit, Map_entry_type.map_pit)
        self.set_map(self.__pillar_abstraction, Map_entry_type.map_pillar_abstraction)
        self.set_map(self.__pillar_encapsulation, Map_entry_type.map_pillar_encapsulation)
        self.set_map(self.__pillar_inheritance, Map_entry_type.map_pillar_inheritance)
        self.set_map(self.__pillar_polymorphism, Map_entry_type.map_pillar_polymorphism)
        # special_rooms = set()
        # for i in range(0, 30):
        #     room = random.choice(rooms)
        #     if room in special_rooms:
        #         continue
        #     special_rooms.add(room)
        # for j in range(2, 9):
        #     room = special_rooms.pop()
        #     room.set_value(j)
            # self.set_map(room, j)
            # self.set_map(special_rooms.pop(), 2)
            # self.set_map(special_rooms.pop(), 3)
            # self.set_map(special_rooms.pop(), 4)
            # self.set_map(special_rooms.pop(), 5)
            # self.set_map(special_rooms.pop(), 6)
            # self.set_map(special_rooms.pop(), 7)
            # self.set_map(special_rooms.pop(), 8)
            # self.set_map(special_rooms.pop(), 9)
        # self.set_map(special_rooms.pop(), Map_entry_type.map_entrance)
        # self.set_map(special_rooms.pop(), Map_entry_type.map_exit)
        # self.set_map(special_rooms.pop(), Map_entry_type.map_healing_potion)
        # self.set_map(special_rooms.pop(), Map_entry_type.map_pit)
        # self.set_map(special_rooms.pop(), Map_entry_type.map_pillar_abstraction)
        # self.set_map(special_rooms.pop(), Map_entry_type.map_pillar_encapsulation)
        # self.set_map(special_rooms.pop(), Map_entry_type.map_pillar_inheritance)
        # self.set_map(special_rooms.pop(), Map_entry_type.map_pillar_polymorphism)
        # self.__start_point = special_rooms.pop()
        # self.__destination = special_rooms.pop()
        # self.__healing_potion = special_rooms.pop()
        # self.__pit = special_rooms.pop()
        # self.__pillar_abstraction = special_rooms.pop()
        # self.__pillar_encapsulation = special_rooms.pop()
        # self.__pillar_inheritance = special_rooms.pop()
        # self.__pillar_polymorphism = special_rooms.pop()
        # self.set_map(self.__start_point, Map_entry_type.map_entrance)
        # self.set_map(self.__destination, Map_entry_type.map_exit)
        # self.set_map(self.__healing_potion, Map_entry_type.map_healing_potion)
        # self.set_map(self.__pit, Map_entry_type.map_pit)
        # self.set_map(self.__pillar_abstraction, Map_entry_type.map_pillar_abstraction)
        # self.set_map(self.__pillar_encapsulation, Map_entry_type.map_pillar_encapsulation)
        # self.set_map(self.__pillar_inheritance, Map_entry_type.map_pillar_inheritance)
        # self.set_map(self.__pillar_polymorphism, Map_entry_type.map_pillar_polymorphism)

    def get_room(self, y, x):
        room = self.__map[y][x]
        return room

    def do_recursive_division(self):
        """draw four margin wall lines"""
        for x in range(0, self.__width):
            self.set_map(self.get_room(0, x), Map_entry_type.map_block)
            self.set_map(self.get_room(self.__height - 1, x), Map_entry_type.map_block)

        for y in range(0, self.__height):
            self.set_map(self.get_room(y, 0), Map_entry_type.map_block)
            self.set_map(self.get_room(y, self.__width - 1), Map_entry_type.map_block)
        self.recursive_division(1, 1, self.__width - 2, self.__height - 2, Map_entry_type.map_block)

    def generate_holes(self, x, y, width, height, wall_x, wall_y):
        holes = []
        hole_entrys = [(random.randint(x, wall_x - 1), wall_y), (random.randint(wall_x + 1, x + width - 1), wall_y),
                       (wall_x, random.randint(y, wall_y - 1)),
                       (wall_x, random.randint(wall_y + 1, y + height - 1))]
        margin_entrys = [(x, wall_y), (x + width - 1, wall_y), (wall_x, y), (wall_x, y + height - 1)]
        adjacent_entrys = [(x - 1, wall_y), (x + width, wall_y), (wall_x, y - 1), (wall_x, y + height)]
        for i in range(4):
            adj_x, adj_y = (adjacent_entrys[i][0], adjacent_entrys[i][1])
            if self.is_movable(self.__map[adj_y][adj_x]):
                self.set_map(self.__map[margin_entrys[i][1]][margin_entrys[i][0]], Map_entry_type.map_empty)
            else:
                holes.append(hole_entrys[i])
        ignore_hole = random.randint(0, len(holes) - 1)
        for i in range(0, len(holes)):
            if i != ignore_hole:
                self.set_map(self.__map[holes[i][1]][holes[i][0]], Map_entry_type.map_empty)

    def get_wall_index(self, start, length):
        """start must be an odd number, length must be an even number"""
        if length >= 3:
            wall_index = random.randint(start + 1, start + length - 2)
            if wall_index % 2 == 1:
                wall_index -= 1
            return wall_index

    def recursive_division(self, x, y, width, height, wall_value):
        """recursive division algorithm"""
        if width <= 1 or height <= 1:
            return
        """generate a row and a column wall index, must be number"""
        wall_x, wall_y = (self.get_wall_index(x, width), self.get_wall_index(y, height))
        """set horizontal and vertical lines to wall"""
        for i in range(x, x + width):
            self.set_map(self.get_room(wall_y, i), wall_value)
        for i in range(y, y + height):
            self.set_map(self.get_room(i, wall_x), wall_value)
        """create three holes"""
        self.generate_holes(x, y, width, height, wall_x, wall_y)
        self.recursive_division(x, y, wall_x - x, wall_y - y, wall_value)
        self.recursive_division(x, wall_y + 1, wall_x - x, y + height - wall_y - 1, wall_value)
        self.recursive_division(wall_x + 1, y, x + width - wall_x - 1, wall_y - y, wall_value)
        self.recursive_division(wall_x + 1, wall_y + 1, x + width - wall_x - 1, y + height - wall_y - 1, wall_value)


def run():
    width_map = 11
    height_map = 15
    map = Map(width_map, height_map)
    map.do_recursive_division()
    map.set_room()
    map.show_map()
    hero = Adventurer(10, 10)
    hero.get_health()
    print(hero.get_health())

if __name__ == "__main__":
    run()