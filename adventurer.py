
"""Child class of the Dungeon model where we define our adventure and initiate health, vaccines points, list of pillars
collected and position within the Map"""
class Adventurer():

    def __init__(self, y, x):
        self.__name = ""
        # self.__dungeon = dungeon
        self.__x = x
        self.__y = y
        self.__health = 100
        self.__is_dead = False
        self.__number_vaccine = 0
        self.__number_vision_potion = 0
        self.__pillars = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_health(self):
        return self.__health

    def add_health(self):
        self.__health += 10 * self.__number_vaccine
        self.__number_vaccine = 0

    def min_health(self):
        self.__health -= 50
        print(self.__health)
        print("Health minus", self.__health)
        if self.__health <= 0:
            print("Our hero is dead")
    # def set_vaccine_points(self, vaccine_points):
    #     self.__number_vaccine += vaccine_points
    #
    # def use_vaccine(self):
    #     # currently just use all the vaccine, could change this
    #     self.__health += self.__number_vaccine
    #     self.__number_vaccine = 0

    def get_pillars(self):
        if len(self.__pillars) == 4:
            return True
        else:
            return False

    def add_pillar(self, pillar):
        if pillar not in self.__pillars:
            self.__pillars.append(pillar)

    def get_number_vaccine(self):
        return self.__number_vaccine

    def add_vaccine(self):
        self.__number_vaccine += 1

    def get_number_vision_potion(self):
        return self.__number_vision_potion

    def set_number_vision_potion(self, potions):
        self.__number_vision_potion += potions

    def get_number_pillars(self):
        return self.__pillars

    def add_pillar(self, pillar_to_add):
        self.__pillars.append(pillar_to_add)

    # def die(self):
    #     self.__dungeon_adventure.remove_observer()
    #     print("Our hero has died")

    # def hero_move(self, moves):
    #     hero_move = moves[-1]
    #     if hero_move.get_value() == 6:
    #         self.add_pillar("abstraction")
    #         hero_move.set_value(0)
    #     if hero_move.get_value() == 7:
    #         self.add_pillar("encapsulation")
    #         hero_move.set_value(0)
    #     if hero_move.get_value() == 8:
    #         self.add_pillar("inheritance")
    #         hero_move.set_value(0)
    #     if hero_move.get_value() == 9:
    #         self.add_pillar("polymorphism")
    #         hero_move.set_value(0)
    #     if hero_move.get_value() == 4:
    #         self.add_health()
    #     if hero_move.get_value() == 5:
    #         self.min_health()
