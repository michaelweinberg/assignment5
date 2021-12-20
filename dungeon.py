from adventurer import Adventurer
from map import Map

"""This class functionas as the main model of the program.  In this class we create all child component classes 
needed to execute the program - On init we create the map for our dungeon by creating a randomly generated Map
and a hero (Adventurer) object to traverse the Map."""
class Dungeon():
    def __init__(self, cols, rows, canvas):
        self.__cols = cols
        self.__rows = rows
        self.__map = Map(cols, rows)
        self.__map.do_recursive_division()
        self.__map.set_room()
        self.__movement_list = [self.__map.start_point]
        self.__canvas = canvas
        self.__hero = Adventurer(self.__map.start_point.get_y(), self.__map.start_point.get_x())
        self.draw_maze()

    def get_map(self):
        return self.__map

    def get_hero(self):
        return self.__hero

    def get_movement_list(self):
        return self.__movement_list

    def get_canvas(self):
        return self.__canvas

    def draw_cell(self, row, col, color="#F2F2F2"):
        cell_width = 40
        x0, y0 = col * cell_width, row * cell_width
        x1, y1 = x0 + cell_width, y0 + cell_width
        self.__canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color, width=0)

    def draw_maze(self):
        for y in range(self.__rows):
            for x in range(self.__cols):
                if self.__map.get_room(y, x).get_value() == 0:
                    self.draw_cell(y, x)
                elif self.__map.get_room(y, x).get_value() == 1:
                    self.draw_cell(y, x, "#525288")
                    """blue"""
                elif self.__map.get_room(y, x).get_value() == 2:
                    self.draw_cell(y, x, "#eee83f")
                    """yellow"""
                elif self.__map.get_room(y, x).get_value() == 3:
                    self.draw_cell(y, x, "#cf52eb")
                    """purple"""
                elif self.__map.get_room(y, x).get_value() == 4:
                    self.draw_cell(y, x, "#ee3f4d")
                    """red"""
                elif self.__map.get_room(y, x).get_value() == 5:
                    self.draw_cell(y, x, "#ee3f4d")
                elif self.__map.get_room(y, x).get_value() == 6:
                    self.draw_cell(y, x, "#ee3f4d")
                elif self.__map.get_room(y, x).get_value() == 7:
                    self.draw_cell(y, x, "#ee3f4d")
                elif self.__map.get_room(y, x).get_value() == 8:
                    self.draw_cell(y, x, "#ee3f4d")
                elif self.__map.get_room(y, x).get_value() == 9:
                    self.draw_cell(y, x, "#ee3f4d")

    def get_cols(self):
        return self.__cols

    def set_cols(self, cols):
        self.__cols = cols

    def get_row(self):
        return self.__rows

    def set_rows(self, rows):
        self.__rows = rows


