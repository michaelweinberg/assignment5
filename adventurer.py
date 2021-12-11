class Adventurer:

    def __init__(self, y, x):
        self.__x = x
        self.__y = y
        self.__health = 100
        self.__is_dead = False
        self.__number_vaccine = 0
        self.__number_vision_potion = 0
        self.__pillars = []

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

    def set_health(self, health):
        self.__health += health
        if self.__health <= 0:
            self.die()

    def set_vaccine_points(self, vaccine_points):
        self.__number_vaccine += vaccine_points

    def use_vaccine(self):
        # currently just use all the vaccine, could change this
        self.__health += self.__number_vaccine
        self.__number_vaccine = 0

    def get_pillars(self):
        if len(self.__pillars) == 4:
            return True
        else:
            return False

    def add_pillar(self, pillar):
        if pillar not in self.__pillars:
            self.__pillars.append(pillar)

    def die(self):
        self.__dungeon_adventure.remove_observer()
        print("Our hero has died")
