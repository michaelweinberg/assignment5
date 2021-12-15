import tkinter as tk
from dungeon import Dungeon
from adventurer import Adventurer
# from dungeonadventure import DungeonAdventure


class DungeonController:

    def __init__(self, dungeon, adventure):
        self.__dungeon = dungeon
        self.__view = adventure
        # self.__dungeon.get_hero() = Adventurer(self.__dungeon.get_map().start_point.get_y(), self.__dungeon.get_map().start_point.get_x())
        # self.__dungeon.__dungeon_adventure = dungeon_adventure

    def draw_hero(self):
        hero_move = self.__dungeon.get_movement_list()[-1]
        pre_move = self.__dungeon.get_movement_list()[-2]
        self.hero_move(self.__dungeon.get_movement_list())
        print(self.__dungeon.get_hero().get_health())
        self.__dungeon.draw_cell(hero_move.get_y(), hero_move.get_x(), "#232323")
        if pre_move == self.__dungeon.get_map().start_point:
            self.__dungeon.draw_cell(pre_move.get_y(), pre_move.get_x(), "#eee83f")
        elif pre_move == self.__dungeon.get_map().destination:
            self.__dungeon.draw_cell(pre_move.get_y(), pre_move.get_x(), "#cf52eb")
        elif pre_move != self.__dungeon.get_map().start_point and pre_move != self.__dungeon.get_map().destination:
            if pre_move.get_value() == 4 or pre_move.get_value() == 5:
                self.__dungeon.draw_cell(pre_move.get_y(), pre_move.get_x(), "#ee3f4d")
            else:
                self.__dungeon.draw_cell(pre_move.get_y(), pre_move.get_x(), "#F2F2F2")
        self.check_reach()

    def check_reach(self):
        if self.__dungeon.get_movement_list()[-1] == self.__dungeon.get_map().destination:
            if self.__dungeon.get_hero().get_pillars():
                print("Congratulations!")
                exit()
            else:
                print("not enough pillars")

    def move_west(self):
        x = self.__dungeon.get_hero().get_x()
        y = self.__dungeon.get_hero().get_y()
        print("hero(y,x)", y, x)
        room = self.__dungeon.get_map().get_room(y, x - 1)
        if self.__dungeon.get_map().is_movable(room):
            self.__dungeon.get_hero().set_x(x - 1)
            self.__dungeon.get_movement_list().append(room)
            self.draw_hero()
            print("west", "y", y, "x", x, room.get_value())
        else:
            return

    def move_east(self):
        x = self.__dungeon.get_hero().get_x()
        y = self.__dungeon.get_hero().get_y()
        print("hero(y,x)", y, x)
        room = self.__dungeon.get_map().get_room(y, x + 1)
        if self.__dungeon.get_map().is_movable(room):
            self.__dungeon.get_hero().set_x(x + 1)
            self.__dungeon.get_movement_list().append(room)
            self.draw_hero()
            print("east", "y", y, "x", x, room.get_value())
        else:
            return

    def move_south(self):
        x = self.__dungeon.get_hero().get_x()
        y = self.__dungeon.get_hero().get_y()
        print("hero(y,x)", y, x)
        room = self.__dungeon.get_map().get_room(y + 1, x)
        if self.__dungeon.get_map().is_movable(room):
            self.__dungeon.get_hero().set_y(y + 1)
            self.__dungeon.get_movement_list().append(room)
            self.draw_hero()
            print("south", "y", y, "x", x, room.get_value())
        else:
            return

    def move_north(self):
        x = self.__dungeon.get_hero().get_x()
        y = self.__dungeon.get_hero().get_y()
        print("hero(y,x)", y, x)
        room = self.__dungeon.get_map().get_room(y - 1, x)
        if self.__dungeon.get_map().is_movable(room):
            self.__dungeon.get_hero().set_y(y - 1)
            self.__dungeon.get_movement_list().append(room)
            print("north", "y", y, "x", x, room.get_value())
            self.draw_hero()
        else:
            return

    def hero_move(self, moves):
        hero_move = moves[-1]
        if hero_move.get_value() == 6:
            self.__dungeon.get_hero().add_pillar("abstraction")
            hero_move.set_value(0)
        if hero_move.get_value() == 7:
            self.__dungeon.get_hero().add_pillar("encapsulation")
            hero_move.set_value(0)
        if hero_move.get_value() == 8:
            self.__dungeon.get_hero().add_pillar("inheritance")
            hero_move.set_value(0)
        if hero_move.get_value() == 9:
            self.__dungeon.get_hero().add_pillar("polymorphism")
            hero_move.set_value(0)
        if hero_move.get_value() == 4:
            self.__dungeon.get_hero().add_health()
        if hero_move.get_value() == 5:
            self.__dungeon.get_hero().min_health()
            if self.__dungeon.get_hero().get_health() <= 0:
                self.__view.show_dead()

