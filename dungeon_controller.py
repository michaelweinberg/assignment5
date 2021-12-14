from dungeon import Dungeon
from adventurer import Adventurer
# from dungeonadventure import DungeonAdventure


class DungeonController:

    def __init__(self, dungeon):
        self.__dungeon = dungeon
        self.__hero = Adventurer(self.__dungeon.get_map().start_point.get_y(), self.__dungeon.get_map().start_point.get_x())
        # self.__dungeon.__dungeon_adventure = dungeon_adventure


    def draw_hero(self):
        hero_move = self.__dungeon.get_movement_list()[-1]
        pre_move = self.__dungeon.get_movement_list()[-2]
        self.__hero.hero_move(self.__dungeon.get_movement_list())
        print(self.__hero.get_health())
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
            if self.__hero.get_pillars():
                print("Congratulations!")
                exit()
            else:
                print("not enough pillars")

    def move_west(self):
        x = self.__hero.get_x()
        y = self.__hero.get_y()
        print("hero(y,x)", y, x)
        room = self.__dungeon.get_map().get_room(y, x - 1)
        if self.__dungeon.get_map().is_movable(room):
            self.__hero.set_x(x - 1)
            self.__dungeon.get_movement_list().append(room)
            self.draw_hero()
            print("west", "y", y, "x", x, room.get_value())
        else:
            return

    def move_east(self):
        x = self.__hero.get_x()
        y = self.__hero.get_y()
        print("hero(y,x)", y, x)
        room = self.__dungeon.get_map().get_room(y, x + 1)
        if self.__dungeon.get_map().is_movable(room):
            self.__hero.set_x(x + 1)
            self.__dungeon.get_movement_list().append(room)
            self.draw_hero()
            print("east", "y", y, "x", x, room.get_value())
        else:
            return

    def move_south(self):
        x = self.__hero.get_x()
        y = self.__hero.get_y()
        print("hero(y,x)", y, x)
        room = self.__dungeon.get_map().get_room(y + 1, x)
        if self.__dungeon.get_map().is_movable(room):
            self.__hero.set_y(y + 1)
            self.__dungeon.get_movement_list().append(room)
            self.draw_hero()
            print("south", "y", y, "x", x, room.get_value())
        else:
            return

    def move_north(self):
        x = self.__hero.get_x()
        y = self.__hero.get_y()
        print("hero(y,x)", y, x)
        room = self.__dungeon.get_map().get_room(y - 1, x)
        if self.__dungeon.get_map().is_movable(room):
            self.__hero.set_y(y - 1)
            self.__dungeon.get_movement_list().append(room)
            print("north", "y", y, "x", x, room.get_value())
            self.draw_hero()
        else:
            return

    # def start_game():
    #     def get_input(entry):
    #         # entry1 = tk.Entry(start_canvas)
    #         input = entry.get()
    #         label2 = tk.Label(top_frame,
    #                           text=f'Hello,{input}, Adventurer!\n  '
    #                                f'Please use the control panel to navigate.\n  '
    #                                f'Your mission is to collect all 4 pillars of OO\n'
    #                           )
    #         label2.grid(row=3, column=0)
    #         # start_canvas.create_window(200, 230, window=label2)
    #
    #     top = tk.Toplevel(windows)
    #     top.geometry("400x400")
    #     top.title("You Have Started the Game! ")
    #     top_frame = tk.Frame(top)
    #     top_frame.pack()
    #     # start_canvas = tk.Canvas(top_frame, background='cyan', width=400, height=400)
    #     # start_canvas.grid()
    #     adventurer_image = Image.open("adventurer.gif")
    #     tk_image = ImageTk.PhotoImage(adventurer_image)
    #     label1 = tk.Label(top_frame, image=tk_image)
    #     label1.image = tk_image
    #     label1.grid(row=0, column=0)
    #     entry1 = tk.Entry(top_frame)
    #     entry1.grid(row=1, column=0)
    #
    #     button1 = tk.Button(top_frame, text='Please enter your name, adventurer:  ', command=lambda: get_input(entry1))
    #     button1.grid(row=2, column=0)
