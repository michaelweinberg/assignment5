from assignment5.assignment5.map import Map
from assignment5.assignment5.room import Room


def run():
    width_map = 11
    height_map = 11
    map = Map(width_map, height_map)
    map.do_recursive_division()
    map.set_room()
    map.show_map()

if __name__ == "__main__":
    run()


# class Dungeon:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height
#         self.__maze = Map(self.__width, self.__height)
#         self.__maze.do_recursive_division()
#         self.__maze.set_room()
#         self.__maze.show_map()


