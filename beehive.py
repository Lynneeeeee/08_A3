from dataclasses import dataclass
from heap import MaxHeap

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.max_beehives = max_beehives
        self.beehives = []

    def set_all_beehives(self, hive_list: list[Beehive]):
        self.beehives = sorted(hive_list[:self.max_beehives], key=lambda hive: hive.volume, reverse=True)


    def add_beehive(self, hive: Beehive):
        if len(self.beehives) < self.max_beehives:
            self.beehives.append(hive)
            self.beehives.sort(key=lambda hive: hive.volume, reverse=True)
        else:
            if hive.volume > self.beehives[-1].volume:
                self.beehives.pop()
                self.beehives.append(hive)
                self.beehives.sort(key=lambda hive: hive.volume, reverse=True)

    def harvest_best_beehive(self):
        if len(self.beehives) > 0:
            hive = self.beehives.pop(0)
            honey_harvested = min(hive.capacity, hive.volume)
            emeralds = honey_harvested * hive.nutrient_factor
            hive.volume -= honey_harvested
            if hive.volume > 0:
                self.beehives.insert(0, hive)
            return emeralds
        else:
            return 0.0