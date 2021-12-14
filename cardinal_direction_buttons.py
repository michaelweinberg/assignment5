from tkinter import *
from tkinter import messagebox


def buttons():
    def west_callback():
        messagebox.showinfo("Going West", "Pillars, Pits, Healing Potions")
    def center_callback():
        messagebox.showinfo("You Are Here", "Hero Stats")
    def east_callback():
        messagebox.showinfo("Going East", "Pillars, Pits, Healing Potions")
    def south_callback():
        messagebox.showinfo("Going South", "Pillars, Pits, Healing Potions")
    def north_callback():
        messagebox.showinfo("Going North", "Pillars, Pits, Healing Potions")

    root = Tk()
    frame = Frame(root)
    frame.pack()

    bottom_frame = Frame(root)
    bottom_frame.pack(side=BOTTOM)

    north_button = Button(frame, text="North", fg="cyan", command=north_callback)
    north_button.pack(side=TOP)

    west_button = Button(frame, text="West", fg="red", command=west_callback)
    west_button.pack(side=LEFT)

    center_button = Button(frame, text="You Are Here", fg="green", command=center_callback)
    center_button.pack(side=LEFT)

    east_button = Button(frame, text="East", fg="blue", command=east_callback)
    east_button.pack(side=LEFT)

    south_button = Button(bottom_frame, text="South", fg="black", command=south_callback)
    south_button.pack(side=BOTTOM)
    #print('hello')
    root.mainloop()

buttons()
