class Observable:

    def __init__(self):
        self.__observers = []

    def notify_observers(self, new_data):
        for observer in self.__observers:
            observer.update(self, new_data)

    def add_observer(selfs, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)