import tkinter as tk
from dungeon import Dungeon
from adventurer import Adventurer
from tkinter import messagebox
# from dungeonadventure import DungeonAdventure


class DungeonController:

    def __init__(self, dungeon, adventure):
        self.__dungeon = dungeon
        self.__view = adventure
        # self.__dungeon.get_hero() = Adventurer(self.__dungeon.get_map().start_point.get_y(), self.__dungeon.get_map().start_point.get_x())
        # self.__dungeon.__dungeon_adventure = dungeon_adventure

    def get_dungeon(self):
        return self.__dungeon

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
        elif self.__dungeon.get_hero().get_health() <= 0:
            print("hero is dead!")
            messagebox.showinfo("Room Info", f"{self.__dungeon.get_hero().get_name()}\n"
                                             f"Game Over!Your health points have fallen below 0.\n")
            exit()

    def move_west(self):
        x = self.__dungeon.get_hero().get_x()
        y = self.__dungeon.get_hero().get_y()
        print("hero(y,x)", y, x)
        room = self.__dungeon.get_map().get_room(y, x - 1)
        if self.__dungeon.get_map().is_movable(room):
            self.__dungeon.get_hero().set_x(x - 1)
            self.__dungeon.get_movement_list().append(room)
            self.room_info()
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
            self.room_info()
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
            self.room_info()
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
            self.room_info()
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
            self.__dungeon.get_hero().add_vaccine()
        if hero_move.get_value() == 5:
            self.__dungeon.get_hero().min_health()
            if self.__dungeon.get_hero().get_health() <= 0:
                self.__view.show_dead()

    # method to get room info
    def room_info(self):
        #currently not showing there's a potion there after you enter the room - hero already scooped it and then the display is showing no potion
        current_room = self.__dungeon.get_map().get_room(self.__dungeon.get_hero().get_y(), self.__dungeon.get_hero().get_x())
        if current_room.get_value() == 0:
            return None
            # room_description = "Nothing"
        elif current_room.get_value() == 2:
            room_description = "Entrance/Start"
            return None
        elif current_room.get_value() == 3:
            room_description = "Exit"
        elif current_room.get_value() == 4:
            room_description = "Vaccine"
            messagebox.showinfo("Room Info", f"{self.__dungeon.get_hero().get_name()} Your Room Has:\n"
                                             f"{room_description}\n"
                                             f"your can use it to increase your health.")
        elif current_room.get_value() == 5:
            room_description = "Pit of People"
            messagebox.showinfo("Room Info", f"{self.__dungeon.get_hero().get_name()} Your Room Has:\n"
                                             f"{room_description}\n"
                                             f"your health will decrease by 50.")
            if self.__dungeon.get_hero().get_health() <= 0:
                messagebox.showinfo("Game Over!", f"Your health points have fallen below 0.\n"
                                                  f"You have died.  Please exit out of the game!")
                self.check_reach()
        elif current_room.get_value() == 6:
            room_description = "Pillar:  Abstraction"
            messagebox.showinfo("Room Info", f"{self.__dungeon.get_hero().get_name()} Your Room Has:\n"
                                             f"{room_description}")
        elif current_room.get_value() == 7:
            room_description = "Pillar:  Encapsulation"
            messagebox.showinfo("Room Info", f"{self.__dungeon.get_hero().get_name()} Your Room Has:\n"
                                             f"{room_description}")
        elif current_room.get_value() == 8:
            room_description = "Pillar:  Inheritance"
            messagebox.showinfo("Room Info", f"{self.__dungeon.get_hero().get_name()} Your Room Has:\n"
                                             f"{room_description}")
        elif current_room.get_value() == 9:
            room_description = "Pillar:  Polymorphism"
            messagebox.showinfo("Room Info", f"{self.__dungeon.get_hero().get_name()} Your Room Has:\n"
                                             f"{room_description}")

        # messagebox.showinfo("Room Info", f"{self.__dungeon.get_hero().get_name()} Your Room Has:\n"
        #                               f"{room_description}")
        #
        # if current_room.get_value() >= 4:
        #     messagebox.showinfo("There is something in this room!", f"You use/pick up this item.\n"
        #                                                             f"If it is a pit, you fall in and lose 50 health points.")
        #
        # if current_room.get_value() == 5:
        #     if self.__dungeon.get_hero().get_health() <= 0:
        #         messagebox.showinfo("Game Over!", f"Your health points have fallen below 0.\n"
        #                                           f"You have died.  Please exit out of the game!")



    # def hero_stats(self):
    #     messagebox.showinfo("Hero Stats", f"{self.__dungeon.get_hero().get_name()} Your Hero Stats are:\nHealth Points: {self.__dungeon.get_hero().get_health()}\n"
    #                                       f"Number of Vaccines:  {self.__dungeon.get_hero().get_number_vaccine()}\n"
    #                                       f"Number of Vision Potions:  {self.__dungeon.get_hero().get_number_vision_potion()}\n"
    #                                       f"Pillars of OO Collected:  {self.__dungeon.get_hero().get_number_pillars()}")
    #
    # def yes_callback(self):
    #
    #     self.__dungeon.get_hero().add_health()
    #     messagebox.showinfo("Taking Vaccine",
    #                         f"{self.__dungeon.get_hero().get_name()} Your Health Points are: {self.__dungeon.get_hero().get_health()} ")
    #
    # def no_callback(self):
    #
    #     messagebox.showinfo("Not taking vaccine", "Show User Health Points (unaltered)")

    # def vaccine_buttons(self):
    #
    #     top2 = tk.Toplevel(windows)
    #     top2.geometry("500x500")
    #     top2.title("Would you like to take the vaccine? ")
    #     top2_frame = tk.Frame(top2)
    #     top2_frame.pack()
    #     canvas2 = tk.Canvas(top2, width=400, height=400)
    #     canvas2.pack()
    #
    #     tk.Label(canvas2, text='Would you like to take the vaccine ? ').pack()
    #
    #     vaccine_image = Image.open("vaccine.gif")
    #     tk_image2 = ImageTk.PhotoImage(vaccine_image)
    #     label2 = tk.Label(top2_frame, image=tk_image2)
    #     label2.image = tk_image2
    #     label2.grid(row=0, column=0)
    #
    #     number = random.randint(1, 100)
    #
    #     bottom2_frame = Frame(top2)
    #     bottom2_frame.pack(side=BOTTOM)
    #
    #     green_button = Button(bottom2_frame, text="Yes", fg="green", command=dc.yes_callback())
    #     green_button.pack(side=LEFT)
    #
    #     red_button = Button(bottom2_frame, text="No", fg="red", command=dc.no_callback())
    #     red_button.pack(side=RIGHT)
    #
    # def get_input(self, entry):
    #     self.__dungeon.get_hero().set_name(entry.get())
    #     label2 = tk.Label(top_frame,
    #                       text=f'Hello,{adventurer_name}, Adventurer!\n  '
    #                            f'Please use the control panel to navigate.\n  '
    #                            f'Your mission is to collect all 4 pillars of OO and stay alive!\n'
    #                       )
    #     label2.grid(row=3, column=0)
    #     #start_canvas.create_window(200, 230, window=label2)

