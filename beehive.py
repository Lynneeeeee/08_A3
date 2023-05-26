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
        self.beehives = sorted(hive_list[:self.max_beehives], key=lambda hive: min(hive.capacity, hive.volume) * hive.nutrient_factor, reverse=True)

    def add_beehive(self, hive: Beehive):
        if len(self.beehives) < self.max_beehives:
            self.beehives.append(hive)
            self.beehives.sort(key=lambda hive: min(hive.capacity, hive.volume) * hive.nutrient_factor, reverse=True)
        else:
            if min(hive.capacity, hive.volume) * hive.nutrient_factor > min(self.beehives[-1].capacity,
                                                                            self.beehives[-1].volume) * self.beehives[
                -1].nutrient_factor:
                self.beehives.pop()
                self.beehives.append(hive)
                self.beehives.sort(key=lambda hive: min(hive.capacity, hive.volume) * hive.nutrient_factor,
                                   reverse=True)


    def harvest_best_beehive(self):
        if len(self.beehives) > 0:
            # Sort the beehives by potential emerald yield
            self.beehives.sort(key=lambda hive: min(hive.capacity, hive.volume) * hive.nutrient_factor, reverse=True)

            # Pop the first hive (with max potential yield)
            hive = self.beehives.pop(0)

            # Calculate honey to harvest and update hive's volume
            honey_harvested = min(hive.capacity, hive.volume)
            hive.volume -= honey_harvested

            # If the hive still has honey, add it back to the list
            if hive.volume > 0:
                self.beehives.append(hive)

            # Return the number of emeralds earned
            return honey_harvested * hive.nutrient_factor
        else:
            return 0.0



