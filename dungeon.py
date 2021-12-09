from room import Room
from maze import Maze

class Dungeon:

        def __init__(self, row_count, col_count):

            self.__maze = Maze.build(row_count, col_count)
            self.__x_y_position = [0, 0]

        def traverse(self, row, col):
            found_exit = False
            if self.is_valid_room(row, col):
                self.__maze[row][col].set_visited(True)
                #check for exit
                if self.__maze[row][col].is_exit():
                    return True
                #not an exit so try another room
                found_exit = self.traverse(row + 1, col)#south
                self.__x_y_position[1] -= 1
                if not found_exit:
                    found_exit = self.traverse(row, col + 1)
                    self.__x_y_position[1] += 1#east
                if not found_exit:
                    found_exit = self.traverse(row - 1, col)
                    self.__x_y_position[1] += 1#north
                if not found_exit:
                    found_exit = self.traverse(row, col-1)
                    self.__x_y_position[0] -= 1#west
                if not found_exit:
                    self.__maze[row][col].set_visited(True)

            else:#tried to move into an invalid room
                return False
            return found_exit

        def is_valid_room(self, row, col):
            return 0 <= row < self.__rowCount and col >= 0 and col < self.__colCount and self.__maze[row][
                col].can_enter()

