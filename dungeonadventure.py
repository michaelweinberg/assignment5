import tkinter as tk

from assignment5.assignment5.adventurer import Adventurer
from assignment5.assignment5.map import Map
from tkinter.messagebox import showinfo
import time

"""white"""
def draw_cell(canvas, row, col, color="#F2F2F2"):
    x0, y0 = col * cell_width, row * cell_width
    x1, y1 = x0 + cell_width, y0 + cell_width
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color, width=0)

def draw_maze(canvas, map, moves):
    for y in range(rows):
        for x in range(cols):
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


"""green"""
def draw_hero(canvas, map, moves, hero):
    hero_move = moves[-1]
    pre_move = moves[-2]
    hero.hero_move(moves)
    print(hero.get_health())
    draw_cell(canvas, hero_move.get_y(), hero_move.get_x(), "#232323")
    if pre_move == map.start_point:
        draw_cell(canvas, pre_move.get_y(), pre_move.get_x(), "#eee83f")
    elif pre_move == map.destination:
        draw_cell(canvas, pre_move.get_y(), pre_move.get_x(), "#cf52eb")
    elif pre_move != map.start_point and pre_move != map.destination:
        if pre_move.get_value() == 4 or pre_move.get_value() == 5:
            draw_cell(canvas, pre_move.get_y(), pre_move.get_x(), "#ee3f4d")
        else:
            draw_cell(canvas, pre_move.get_y(), pre_move.get_x(), "#F2F2F2")
    check_reach()

def check_reach():
    if movement_list[-1] == map.destination:
        if hero.get_pillars():
            print("Congratulations!")
            # x0, y0 = width / 2 - 200, 30
            # x1, y1 = x0 + 400, y0 + 40
            # canvas.create_rectangle(x0, y0, x1, y1, fill='#F2F2F2', outline='#525288', width=3)
            # canvas.create_text(width / 2, y0 + 20,
            #                    text="Congratulations! You reach the goal!",
            #                    fill="#525288")
            exit()
        else:
            print("not enough pillars")


def generate_maze():
    global movement_list
    map.do_recursive_division()
    map.set_room()
    movement_list = [map.start_point]
    draw_maze(canvas, map, movement_list)


def move_west(event):
    x = hero.get_x()
    y = hero.get_y()
    print("hero(y,x)", y, x)
    room = map.get_room(y, x-1)
    if map.is_movable(room):
        hero.set_x(x-1)
        movement_list.append(room)
        draw_hero(canvas, map, movement_list, hero)
        print("west",  "y", y, "x", x, room.get_value())
    else:
        return

def move_east(event):
    x = hero.get_x()
    y = hero.get_y()
    print("hero(y,x)", y, x)
    room = map.get_room(y, x+1)
    if map.is_movable(room):
        hero.set_x(x+1)
        movement_list.append(room)
        draw_hero(canvas, map, movement_list, hero)
        print("east",  "y", y, "x", x, room.get_value())
    else:
        return

def move_south(event):
    x = hero.get_x()
    y = hero.get_y()
    print("hero(y,x)", y, x)
    room = map.get_room(y+1, x)
    if map.is_movable(room):
        hero.set_y(y+1)
        movement_list.append(room)
        draw_hero(canvas, map, movement_list, hero)
        print("south",  "y", y, "x", x, room.get_value())
    else:
        return

def move_north(event):
    x = hero.get_x()
    y = hero.get_y()
    print("hero(y,x)", y, x)
    room = map.get_room(y-1, x)
    if map.is_movable(room):
        hero.set_y(y-1)
        movement_list.append(room)
        print("north", "y", y, "x", x, room.get_value())
        draw_hero(canvas, map, movement_list, hero)
    else:
        return

def vision_of_map():
    map.show_map()

if __name__ == "__main__":
    cell_width = 50
    rows = 15
    cols = 19
    height = cell_width * rows
    width = cell_width * cols
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
    print("start point(y,x)", map.start_point.get_y(),map.start_point.get_x())

    windows.bind("w", move_north)
    windows.bind("s", move_south)
    windows.bind("d", move_east)
    windows.bind("a", move_west)
    windows.mainloop()
