from map import Map
from room import Room

class Dungeon:

        def __init__(self, width, height):

            self.__maze = Map(width, height)
            self.__x_y_position = [0, 0]
            self.__exit_position = [4, 1]

        def traverse(self, x, y):
            found_exit = False
            if 1 == 1:
                self.__x_y_position[0] += x
                self.__x_y_position[1] += y
                self.print_position()
                if (self.__x_y_position[0] == self.__exit_position[0]
                        and self.__x_y_position[1] == self.__exit_position[1]):
                    print("we found the exit")
                    return True
            else:#tried to move into an invalid room
                return False
            return found_exit

        def is_valid_room(self, row, col):
            return True
            # return 0 <= row < self.__rowCount and col >= 0 and col < self.__colCount and self.__maze[row][
            #     col].can_enter()

        def print_position(self):
                print("X position is " + str(self.__x_y_position[0]) + " Y position is " + str(self.__x_y_position[1]))

