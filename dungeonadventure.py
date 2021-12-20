import tkinter as tk
from tkinter import BOTTOM, TOP
from tkinter import LEFT
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring

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
from dungeon_controller import DungeonController


"""This file contains all view code and visual layout logic for our program.  All visual components are defined here
as well as function calls for the buttons"""
class View:

    @staticmethod
    def show_health(health):
        print("Health in view:", health)

    @staticmethod
    def show_dead():
        print("Our hero is dead")


#method to initiate game
def start_game():
    def get_input(entry):
        dc.get_dungeon().get_hero().set_name(entry.get())
        label2 = tk.Label(top_frame,
                          text=f'Hello,{dc.get_dungeon().get_hero().get_name()}, Adventurer!\n  '
                               f'Please use the control panel to navigate.\n  '
                               f'Your mission is to collect all 4 pillars of OO and stay alive!\n'
                          )
        label2.grid(row=3,column=0)
        top.destroy()
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

    button1 = tk.Button(top_frame, text='Please confirm your name, adventurer!', command=lambda: get_input(entry1))
    button1.grid(row=2, column=0)


if __name__ == "__main__":
    cell_width = 40
    rows = 15
    cols = 19
    height = cell_width * rows
    width = cell_width * cols
    move_counter, total_counter = 0, 0
    global entry1
    global top_frame
    global adventurer_name
    global hero

    windows = tk.Tk()
    windows.title("CovidAdventure")
    windows.resizable(0, 0)
    t0 = time.time()

    # big maze canvas
    canvas = tk.Canvas(windows, background="#F2F2F2", width=width, height=height)
    canvas.pack()


    dungeon = Dungeon(cols, rows, canvas)
    # dungeon.draw_maze()
    dc = DungeonController(dungeon, View())

    def north():
        dungeon.move_north()
    def south():
        dungeon.move_south()
    def east():
        dungeon.move_east()
    def west():
        dungeon.move_west()


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


    north_button = tk.Button(frame_controlpanel, text="North", fg="cyan", command=dc.move_north)
    north_button.grid(row=2, column=3)

    west_button = tk.Button(frame_controlpanel, text="West", fg="red", command=dc.move_west)
    west_button.grid(row=3, column=2)

    center_button = tk.Button(frame_controlpanel, text="Control Panel", fg="green")
    center_button.grid(row=3, column=3)


    east_button = tk.Button(frame_controlpanel, text="East", fg="blue", command=dc.move_east)
    east_button.grid(row=3, column=4)


    south_button = tk.Button(frame_controlpanel, text="South", fg="black", command=dc.move_south)
    south_button.grid(row=4, column=3)

    # right bottom frame
    frame_right = tk.Frame(windows, highlightbackground="green", highlightthickness=1, width=width / 2, height=175,
                               bd=0)
    frame_right.pack()


    # room info, hero stats, take potion, take vision potion buttons in right bottom frame
    tk.Button(frame_right,
             text="Room Info",
             fg="blue",
             font="Times", command=dc.room_info).grid(row=0, column=0)

    def hero_stats():
        messagebox.showinfo("Hero Stats",
                            f"{dc.get_dungeon().get_hero().get_name()} Your Hero Stats are:\nHealth Points: {dungeon.get_hero().get_health()}\n"
                            f"Number of Vaccines:  {dc.get_dungeon().get_hero().get_number_vaccine()}\n"
                            f"Number of Vision Potions:  {dc.get_dungeon().get_hero().get_number_vision_potion()}\n"
                            f"Pillars of OO Collected:  {dc.get_dungeon().get_hero().get_number_pillars()}")

    tk.Button(frame_right,
             text="Hero Stats",
             fg="blue",
             font="Times",
             command=hero_stats).grid(row=0, column=1)


    def vaccine_buttons():
        def no_callback():
            messagebox.showinfo("Not taking vaccine",
                                f"{dc.get_dungeon().get_hero().get_name()} Your Health Points are: {dc.get_dungeon().get_hero().get_health()}")

        def yes_callback():
            dc.get_dungeon().get_hero().add_health()
            messagebox.showinfo("Taking Vaccine",
                                f"{dc.get_dungeon().get_hero().get_name()} Your Health Points are: {dc.get_dungeon().get_hero().get_health()} ")

        top2 = tk.Toplevel(windows)
        top2.geometry("500x500")
        top2.title("Would you like to take the vaccine? ")
        top2_frame = tk.Frame(top2)
        top2_frame.pack()
        canvas2 = tk.Canvas(top2, width=400, height=400)
        canvas2.pack()

        tk.Label(canvas2, text='Would you like to take the vaccine ? ').pack()

        vaccine_image = Image.open("vaccine.gif")
        tk_image2 = ImageTk.PhotoImage(vaccine_image)
        label2 = tk.Label(top2_frame, image=tk_image2)
        label2.image = tk_image2
        label2.grid(row=0, column=0)

        number = random.randint(1, 100)

        bottom2_frame = Frame(top2)
        bottom2_frame.pack(side=BOTTOM)

        green_button = Button(bottom2_frame, text="Yes", fg="green", command=yes_callback)
        green_button.pack(side=LEFT)

        red_button = Button(bottom2_frame, text="No", fg="red", command=no_callback)
        red_button.pack(side=RIGHT)

    tk.Button(frame_right,
             text="Take Potion/Vaccine",
             fg="blue",
             font="Times",
             command=vaccine_buttons).grid(row=1, column=0)

    tk.Button(frame_right,
              text="Use Vision Potion",
              fg="blue",
              font="Times").grid(row=1, column=1)

    windows.mainloop()
