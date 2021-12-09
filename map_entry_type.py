from enum import Enum


class Map_entry_type(Enum):
    map_empty = 0
    map_block = 1
    map_entrance = 2
    map_exit = 3
    map_healing_potion = 4
    map_pit = 5
    map_pillar_abstraction = 6
    map_pillar_encapsulation = 7
    map_pillar_inheritance = 8
    map_pillar_polymorphism = 9
    map_character = 10