from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random

def buttons():
    def yes_callback():
        messagebox.showinfo("Taking Vaccine", "Show Health Points (incremented)")
    def no_callback():
        messagebox.showinfo("Not taking vaccine", "Show Health Points (unaltered)")

    root = tk.Tk()
    frame = Frame(root)
    frame.pack()

    canvas1 = tk.Canvas(root, width=400, height=400)
    canvas1.pack()

    label1 = tk.Label(text='Would you like to take the vaccine ? ')
    canvas1.create_window(200, 180, window=label1)

    #canvas1.create_window(200, 140, window=entry1)
    vaccine_image = tk.PhotoImage(file="vaccine.gif")
    vaccine_image_canvas_object = canvas1.create_image(200, 200, image=vaccine_image)
    number = random.randint(1, 100)

    bottom_frame = Frame(root)
    bottom_frame.pack(side=BOTTOM)

    green_button = Button(frame, text="Yes", fg="green", command=yes_callback)
    green_button.pack(side=LEFT)

    red_button = Button(frame, text="No", fg="red", command=no_callback)
    red_button.pack(side=RIGHT)


    root.mainloop()

buttons()
