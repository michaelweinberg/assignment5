import tkinter as tk
from tkinter import BOTTOM, TOP
from tkinter import LEFT
from tkinter import *

from PIL import Image, ImageTk
import random
from room import Room

from adventurer import Adventurer
from map import Map

from dungeon import Dungeon
from tkinter.messagebox import showinfo
import time
import copy
import math


def text(canvas, row, col):
    x0, y0 = col * cell_width, row * cell_width
    x1, y1 = x0 + cell_width, y0 + cell_width
    canvas.create_text(x0, y0, x1, y1, fill="darkblue", font="Times 20 italic bold", text="0")


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


def draw_hero(canvas, map, moves):
    move = moves[-1]
    draw_maze(canvas, map, moves)
    draw_cell(canvas, move.get_y(), move.get_x(), "#232323")
    if check_reach():
        exit()


def check_reach():
    if movement_list[-1] == map.destination:
        if hero.get_pillars():
            print("Congratulations!")
            return True


def generate_maze():
    global movement_list
    map.do_recursive_division()
    map.set_room()
    movement_list = [map.start_point]
    draw_maze(canvas, map, movement_list)


def move_west():
    x = hero.get_x()
    y = hero.get_y()
    print("hero(y,x)", y, x)
    room = map.get_room(y, x - 1)
    if map.is_movable(room):
        hero.set_x(x - 1)
        movement_list.append(room)
        # draw_maze(canvas, map, movement_list)
        draw_hero(canvas, map, movement_list)
        print("west", "y", y, "x", x, room.get_value())
    else:
        return


def move_east():
    x = hero.get_x()
    y = hero.get_y()
    print("hero(y,x)", y, x)
    room = map.get_room(y, x + 1)
    if map.is_movable(room):
        hero.set_x(x + 1)
        movement_list.append(room)
        # draw_maze(canvas, map, movement_list)
        draw_hero(canvas, map, movement_list)
        print("east", "y", y, "x", x, room.get_value())
    else:
        return


def move_south():
    x = hero.get_x()
    y = hero.get_y()
    print("hero(y,x)", y, x)
    room = map.get_room(y + 1, x)
    if map.is_movable(room):
        hero.set_y(y + 1)
        movement_list.append(room)
        # draw_maze(canvas, map, movement_list)
        draw_hero(canvas, map, movement_list)
        print("south", "y", y, "x", x, room.get_value())
    else:
        return


def move_north():
    x = hero.get_x()
    y = hero.get_y()
    print("hero(y,x)", y, x)
    room = map.get_room(y - 1, x)
    if map.is_movable(room):
        hero.set_y(y - 1)
        movement_list.append(room)
        print("north", "y", y, "x", x, room.get_value())
        # draw_maze(canvas, map, movement_list)
        draw_hero(canvas, map, movement_list)
    else:
        return


#method to initiate game
def start_game():
    def get_input(entry):
        #entry1 = tk.Entry(start_canvas)
        input = entry.get()
        label2 = tk.Label(top_frame,
                          text=f'Hello,{input}, Adventurer!\n  '
                               f'Please use the control panel to navigate.\n  '
                               f'Your mission is to collect all 4 pillars of OO\n'
                          )
        label2.grid(row=3,column=0)
        #start_canvas.create_window(200, 230, window=label2)

    top = tk.Toplevel(windows)
    top.geometry("400x400")
    top.title("You Have Started the Game! ")
    top_frame = tk.Frame(top)
    top_frame.pack()
    # start_canvas = tk.Canvas(top_frame, background='cyan', width=400, height=400)
    # start_canvas.grid()
    adventurer_image = Image.open("adventurer.gif")
    tk_image = ImageTk.PhotoImage(adventurer_image)
    label1 = tk.Label(top_frame, image=tk_image)
    label1.image = tk_image
    label1.grid(row=0, column=0)
    entry1 = tk.Entry(top_frame)
    entry1.grid(row=1, column=0)

    button1 = tk.Button(top_frame, text='Please enter your name, adventurer:  ', command=lambda: get_input(entry1))
    button1.grid(row=2, column=0)

# def start_game():
#     top = tk.Toplevel(windows)
#     top.geometry("400x400")
#     top.title("You Have Started the Game! ")
#     top_frame = tk.Frame(top)
#     top_frame.grid()
#     start_canvas = tk.Canvas(top_frame, background="cyan", width=400, height=400)
#     start_canvas.pack()
#
#     entry1 = tk.Entry(start_canvas)
#     start_canvas.create_window(200, 140, window=entry1)
#
#     adventurer_image = tk.PhotoImage(file="adventurer.gif")
#     adventurer_image_canvas_object = start_canvas.create_image(125, 125, image=adventurer_image)
#     adventurer_image_canvas_object.pack(side=CENTER)
#     #number = random.randint(1, 100)
#
#
#
#     button1 = tk.Button(top_frame, text='Please enter your name, adventurer:  ', command=lambda: get_input(input))
#     button1.pack()
#     start_canvas.create_window(200, 180, window=button1)


# def start_game():
#     top = tk.Toplevel(windows)
#     top.geometry("400x400")
#     top.title("You Have Started the Game! ")
#     top_frame = tk.Frame(top)
#     top_frame.pack()
#     entry1 = tk.Entry(top_frame)
#     entry1.pack()
#
#     button1 = tk.Button(top_frame, text='Please enter your name, adventurer:  ', command=get_input)
#     button1.pack()
#     start_canvas = tk.Canvas(top_frame, background='cyan', width=400, height=400)
#     start_canvas.pack()
#     adventurer_image = tk.PhotoImage(file="adventurer.gif")
#     adventurer_image_canvas_object = start_canvas.create_image(125, 125, image=adventurer_image)
#     adventurer_image_canvas_object.pack(side=CENTER)







#method to help display room info
# def display_roominfo(y,x):
#     room = map.get_room(y,x)
#     print(room.__str__())


if __name__ == "__main__":
    cell_width = 40
    rows = 15
    cols = 19
    height = cell_width * rows
    width = cell_width * cols
    move_counter, total_counter = 0, 0
    global entry1
    global top_frame

    windows = tk.Tk()
    windows.title("CovidAdventure")
    windows.resizable(0, 0)
    t0 = time.time()

    # big maze canvas
    canvas = tk.Canvas(windows, background="#F2F2F2", width=width, height=height)
    canvas.pack()

    # frame for legend
    frame_legend = tk.Frame(windows, highlightbackground="blue", highlightthickness=1, width=width / 4, height=175,
                            bd=0)
    frame_legend.pack(fill=tk.Y, side=tk.LEFT)

    # start game button in legend frame
    start_button = tk.Button(frame_legend, text="Start Game", fg="black", bg="yellow", command=start_game)
    start_button.pack()

    tk.Label(frame_legend,
             text="LEGEND OF DUNGEON: ",
             fg="black",
             font="Times").pack()
    tk.Label(frame_legend,
             text="Yellow = 'Start'",
             fg="yellow",
             bg="black",
             font="Times").pack()
    tk.Label(frame_legend,
             text="Purple = 'Exit'",
             fg="purple",
             font="Times").pack()
    tk.Label(frame_legend,
             text="Red = 'Pit'",
             fg="red",
             font="Times").pack()
    tk.Label(frame_legend,
             text="Black = Hero",
             fg="black",
             font="Times").pack()



    # control panel frame
    frame_controlpanel = tk.Frame(windows, highlightbackground="green", highlightthickness=1, width=width / 4,
                                  height=175, bd=0)
    frame_controlpanel.pack(fill=tk.Y, side=tk.LEFT)

    north_button = tk.Button(frame_controlpanel, text="North", fg="cyan", command=move_north)
    north_button.grid(row=2, column=3)

    west_button = tk.Button(frame_controlpanel, text="West", fg="red", command=move_west)
    west_button.grid(row=3, column=2)

    center_button = tk.Button(frame_controlpanel, text="Control Panel", fg="green")
    center_button.grid(row=3, column=3)

    east_button = tk.Button(frame_controlpanel, text="East", fg="blue", command=move_east)
    east_button.grid(row=3, column=4)

    # bottom_frame = Frame(frame_controlpanel, width=width)
    # bottom_frame.pack(side=BOTTOM)

    south_button = tk.Button(frame_controlpanel, text="South", fg="black", command=move_south)
    south_button.grid(row=4, column=3)

    # room info frame
    frame_roominfo = tk.Frame(windows, highlightbackground="green", highlightthickness=1, width=width / 4, height=175,
                               bd=0)
    frame_roominfo.pack()

    tk.Label(frame_roominfo, anchor=tk.NW, height=40,
             text="Room Info",
             fg="blue",
             font="Times").grid()

    # roominfo_button = tk.Button(frame_roominfo, anchor=tk.N, height=40, text="Room Info", fg="green", font="Times",
    #                              command=lambda: display_roominfo(hero.get_y(), hero.get_x()))
    # roominfo_button.pack(side=TOP)

    # hero stats, take potion, take vision potion frame
    frame_herostats = tk.Frame(windows, highlightbackground="green", highlightthickness=1, width=width / 4, height=175,
                                bd=0)
    frame_herostats.pack(side=RIGHT)

    tk.Label(frame_herostats, anchor=tk.NW, height=40,
             text="Hero Stats",
             fg="blue",
             font="Times").grid()
    tk.Label(frame_herostats, anchor=tk.S, height=40,
             text="Take Potion/Vaccine",
             fg="blue",
             font="Times").grid()


    map = Map(cols, rows)
    generate_maze()
    hero = Adventurer(map.start_point.get_y(), map.start_point.get_x())
    movement_list = [map.start_point]
    print("start point(y,x)", map.start_point.get_y(), map.start_point.get_x())
    # draw_maze(canvas, map, movement_list)

    # windows.bind("w", move_north)
    # windows.bind("s", move_south)
    # windows.bind("d", move_east)
    # windows.bind("a", move_west)
    windows.mainloop()
