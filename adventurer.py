
class Adventurer:

    def __init__(self, y, x):
        self.__x = x
        self.__y = y
        self.__health = 100
        self.__is_dead = False
        self.__number_vaccine = 0
        self.__number_vision_potion = 0
        self.__pillar_found = None

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

    def set_health(self, health_reset):
        self.__health = health_reset

    def show_hero(self, maze):
        position = maze.get_room(self.__y, self.__x)
        position.set_value(10)