class Room:
    def __init__(self, y, x):
        self.__coordinate_x = x
        self.__coordinate_y = y
        self.__value = 0
        self.__name = None
        self.__do = None
        self.__is_visited = False

    def get_x(self):
        return self.__coordinate_x

    def get_y(self):
        return self.__coordinate_y

    def __str__(self):
        return "This is a" + self.__name + self.__do

    def is_visited(self):
        self.__is_visited = True

    def set_empty(self):
        self.__value = 0
        self.__name = "empty spot"

    def set_block(self):
        self.__value = 1
        self.__name = "block"

    def set_entrance(self):
        self.__value = 2
        self.__name = "start"

    def set_exit(self):
        self.__value = 3
        self.__name = "exit"

    def set_healing_potion(self):
        self.__value = 4
        self.__name = "healing potion"

    def set_pit(self):
        self.__value = 5
        self.__name = "pit"

    def set_pillar_abstraction(self):
        self.__value = 6
        self.__name = "abstraction"

    def set_pillar_encapsulation(self):
        self.__value = 7
        self.__name = "encapsulation"

    def set_pillar_inheritance(self):
        self.__value = 8
        self.__name = "inheritance"

    def set_pillar_polymorphism(self):
        self.__value = 9
        self.__name = "polymorphism"

    def get_value(self):
        return self.__value

    def set_value(self, num):
        self.__value = num

    #
    # def get_health_chance(self):
    #     return self.__healthChance
    #
    # def __str__(self):
    #     item_count = 0;
    #     if self.__healthPotion:
    #         item_count += 1
    #     if self.__visionPotion:
    #         item_count += 1
    #     if item_count > 1:
    #         return "M"
    #
    #     return "Health potion: " + str(self.__healthPotion) + "\n" \
    #            + "Vision potion: " + str(self.__visionPotion) + "\n" \
    #            + "Pillar: " + str(self.__pillar) + "\n" \
    #            + "Pit: " + str(self.__pit) + "\n" \
    #            + "Impassable: " + str(self.__impassable) + "\n" \
    #            + "Entrance: " + str(self.__entrance) + "\n" \
    #            + "Exit: " + str(self.__exit) + "\n\n"
    #
    # def set_health(self, add_potion):
    #     self.__healthPotion = add_potion
    #
    # def can_enter(self):
    #     return not self.__impassable
    #
    # def is_exit(self):
    #     return self.__exit
    #
    # def set_entrance(self):
    #     self.__entrance = True
    #
    # def set_impassible(self, is_impassable):
    #     self.__impassable = is_impassable
    #
    # def set_exit(self):
    #     self.__exit = True
    #
