import tkinter as tk
import random

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)
adventurer_image = tk.PhotoImage(file="adventurer.gif")
adventurer_image_canvas_object = canvas1.create_image(125, 125, image=adventurer_image)
number = random.randint(1, 100)


def input_name(the_name):

    input = entry1.get()

    label1 = tk.Label(root, text=f'Hello,{input}, Adventurer!')
        #print("\a\a\a")
    canvas1.create_window(200, 230, window=label1)


button1 = tk.Button(text='Please enter your name, adventurer:  ', command=lambda: input_name(input))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
