import tkinter as tk

from assignment5.assignment5.adventurer import Adventurer
from assignment5.assignment5.map import Map
from dungeon import Dungeon
from tkinter.messagebox import showinfo
import time
import copy
import math

"""white"""
def draw_cell(canvas, col, row, color="#F2F2F2"):
    x0, y0 = col * cell_width, row * cell_width
    x1, y1 = x0 + cell_width, y0 + cell_width
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color, width=0)

"""green"""
def draw_hero(canvas, col, row, color="#a1e6aa"):
    x0, y0 = col * cell_width, row * cell_width
    x1, y1 = (x0 + cell_width), (y0 + cell_width)
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color, width=0)

def draw_maze(canvas, map, moves):
    for x in range(cols):
        for y in range(rows):
            if map.get_room(y, x).get_value() == 0:
                draw_cell(canvas, y, x)
            elif map.get_room(y, x).get_value() == 1:
                draw_cell(canvas, y, x, "#525288")
                """blue"""
            elif map.get_room(y, x).get_value() == 2:
                draw_cell(canvas, y, x, "#eee83f")
                """yellow"""
            elif map.get_room(y, x).get_value() == 3:
                draw_cell(canvas, y, x, "#cf52eb")
                """purple"""
            elif map.get_room(y, x).get_value() == 4:
                draw_cell(canvas, y, x, "#ee3f4d")
                """red"""
            elif map.get_room(y, x).get_value() == 5:
                draw_cell(canvas, y, x, "#ee3f4d")
            elif map.get_room(y, x).get_value() == 6:
                draw_cell(canvas, y, x, "#ee3f4d")
            elif map.get_room(y, x).get_value() == 7:
                draw_cell(canvas, y, x, "#ee3f4d")
            elif map.get_room(y, x).get_value() == 8:
                draw_cell(canvas, y, x, "#ee3f4d")
            elif map.get_room(y, x).get_value() == 9:
                draw_cell(canvas, y, x, "#ee3f4d")
            # elif map.get_room(y, x).get_value() == 10:
            #     draw_hero(canvas, y, x, "#232323")
            #     """grey"""
    for move in moves:
        map.get_room(move.get_y(), move.get_x()).set_value(10)
        draw_hero(canvas, move.get_y(), move.get_x(), "#232323")

def update_maze(canvas, map, moves):
    canvas.delete("all")
    map = copy.copy(map)
    for move in moves:
        map.get_room(move.get_y, move.get_x).set_value(0)
    x = moves[-1].get_x()
    y = moves[-1].get_y()
    draw_hero(canvas, x, y, "#232323")

def check_reach():
    if movement_list[-1] == map.destination:
        print("Congratulations!")

def generate_maze():
    global movement_list
    map.do_recursive_division()
    map.set_room()
    movement_list = [map.start_point]
    draw_maze(canvas, map, movement_list)


def move_west(event):
    x = hero.get_x()
    y = hero.get_y()
    room = map.get_room(y, x-1)
    if map.is_movable(room):
        hero.set_x(x-1)
        movement_list.append(room)
        draw_maze(canvas, map, movement_list)
        print("west", movement_list, room.get_value())
    else:
        return

def move_east(event):
    x = hero.get_x()
    y = hero.get_y()
    room = map.get_room(y, x+1)
    if map.is_movable(room):
        hero.set_x(x+1)
        movement_list.append(room)
        draw_maze(canvas, map, movement_list)
        print("east", movement_list, room.get_value())
    else:
        return

def move_south(event):
    x = hero.get_x()
    y = hero.get_y()
    room = map.get_room(y+1, x)
    if map.is_movable(room):
        hero.set_y(y+1)
        movement_list.append(room)
        draw_maze(canvas, map, movement_list)
        print("south", movement_list, room.get_value())
    else:
        return

def move_north(event):
    x = hero.get_x()
    y = hero.get_y()
    room = map.get_room(y-1, x)
    if map.is_movable(room):
        hero.set_y(y-1)
        movement_list.append(room)
        print("north", movement_list, room.get_value())
        draw_maze(canvas, map, movement_list)
    else:
        return

if __name__ == "__main__":
    cell_width = 50
    rows = 15
    cols = 19
    height = cell_width * cols
    width = cell_width * rows
    move_counter, total_counter = 0, 0

    windows = tk.Tk()
    windows.title("CovidAdventure")
    windows.resizable(0, 0)
    t0 = time.time()

    canvas = tk.Canvas(windows, background="#F2F2F2", width=width, height=height)
    canvas.pack()

    map = Map(cols, rows)
    generate_maze()
    hero = Adventurer(map.start_point.get_y(), map.start_point.get_x())
    movement_list = [map.start_point]
    # draw_maze(canvas, map, movement_list)

    windows.bind("w", move_north)
    windows.bind("s", move_south)
    windows.bind("d", move_east)
    windows.bind("a", move_west)
    windows.mainloop()
