import abc
from abc import ABCMeta


class Observer(metaclass=ABCMeta):

    @abc.abstractmethod
    def update(self, observable, new_data):
        pass
