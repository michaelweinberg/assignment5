from assignment5.assignment5.adventurer import Adventurer
from map import Map

class Dungeon:
    def __init__(self, cols, rows, canvas):
        self.__cols = cols
        self.__rows = rows
        self.__map = Map(cols, rows)
        self.__map.do_recursive_division()
        self.__map.set_room()
        self.__hero = Adventurer(self.__map.start_point.get_y(), self.__map.start_point.get_x())
        self.__movement_list = [self.__map.start_point]
        self.__canvas = canvas

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

    def draw_hero(self):
        hero_move = self.__movement_list[-1]
        pre_move = self.__movement_list[-2]
        self.__hero.hero_move(self.__movement_list)
        print(self.__hero.get_health())
        self.draw_cell(hero_move.get_y(), hero_move.get_x(), "#232323")
        if pre_move == self.__map.start_point:
            self.draw_cell(pre_move.get_y(), pre_move.get_x(), "#eee83f")
        elif pre_move == self.__map.destination:
            self.draw_cell(pre_move.get_y(), pre_move.get_x(), "#cf52eb")
        elif pre_move != self.__map.start_point and pre_move != self.__map.destination:
            if pre_move.get_value() == 4 or pre_move.get_value() == 5:
                self.draw_cell(pre_move.get_y(), pre_move.get_x(), "#ee3f4d")
            else:
                self.draw_cell(pre_move.get_y(), pre_move.get_x(), "#F2F2F2")
        self.check_reach()

    def check_reach(self):
        if self.__movement_list[-1] == self.__map.destination:
            if self.__hero.get_pillars():
                print("Congratulations!")
                exit()
            else:
                print("not enough pillars")

    def move_west(self):
        x = self.__hero.get_x()
        y = self.__hero.get_y()
        print("hero(y,x)", y, x)
        room = self.__map.get_room(y, x - 1)
        if self.__map.is_movable(room):
            self.__hero.set_x(x - 1)
            self.__movement_list.append(room)
            self.draw_hero()
            print("west", "y", y, "x", x, room.get_value())
        else:
            return

    def move_east(self):
        x = self.__hero.get_x()
        y = self.__hero.get_y()
        print("hero(y,x)", y, x)
        room = self.__map.get_room(y, x + 1)
        if self.__map.is_movable(room):
            self.__hero.set_x(x + 1)
            self.__movement_list.append(room)
            self.draw_hero()
            print("east", "y", y, "x", x, room.get_value())
        else:
            return

    def move_south(self):
        x = self.__hero.get_x()
        y = self.__hero.get_y()
        print("hero(y,x)", y, x)
        room = self.__map.get_room(y + 1, x)
        if self.__map.is_movable(room):
            self.__hero.set_y(y + 1)
            self.__movement_list.append(room)
            self.draw_hero()
            print("south", "y", y, "x", x, room.get_value())
        else:
            return

    def move_north(self):
        x = self.__hero.get_x()
        y = self.__hero.get_y()
        print("hero(y,x)", y, x)
        room = self.__map.get_room(y - 1, x)
        if self.__map.is_movable(room):
            self.__hero.set_y(y - 1)
            self.__movement_list.append(room)
            print("north", "y", y, "x", x, room.get_value())
            self.draw_hero()
        else:
            return
