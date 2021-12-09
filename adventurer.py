class Adventurer:

    def __init__(self):
        self.__health = 100
        self.__is_dead = False
        self.__number_vaccine = 0
        self.__number_vision_potion = 0
        # self.__dungeon_adventure = dungeon_adventure
        self.__pillars = []

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health += health
        if self.__health <= 0:
            self.die()

    def get_vaccine_points(self):
        return self.__number_vaccine

    def set_vaccine_points(self, vaccine_points):
        self.__number_vaccine += vaccine_points

    def use_vaccine(self):
        #currently just use all the vaccine, could change this
        self.__health += self.__number_vaccine
        self.__number_vaccine = 0

    def get_pillars(self):
        return self.__pillars

    def add_pillar(self, pillar):
        self.__pillars.append(pillar)

    def die(self):
        self.__dungeon_adventure.remove_observer()
        print("Our hero has died")





