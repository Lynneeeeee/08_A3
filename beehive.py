from dataclasses import dataclass
from heap import MaxHeap
from typing import List

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0


class HeapBeehive:
    """Wrapper around Beehive to make it work in a MaxHeap"""

    def __init__(self, beehive: Beehive, value: float):
        self.beehive = beehive
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.value == other.value


class BeehiveSelector:
    def __init__(self, max_beehives: int):
        self.max_beehives = max_beehives
        self.beehives_heap = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: List[Beehive]):
        self.beehives_heap = MaxHeap(self.max_beehives)
        for hive in hive_list:
            self.add_beehive(hive)

    def add_beehive(self, hive: Beehive):
        hive_value = min(hive.capacity, hive.volume) * hive.nutrient_factor
        self.beehives_heap.add(HeapBeehive(beehive=hive, value=hive_value))


    def harvest_best_beehive(self):
        if self.beehives_heap.length == 0:
            return None

        best_beehive_wrapper = self.beehives_heap.get_max()  # use get_max instead of extract_max
        best_beehive = best_beehive_wrapper.beehive
        honey_harvested = min(best_beehive.capacity, best_beehive.volume)
        best_beehive.volume -= honey_harvested
        emeralds_earned = honey_harvested * best_beehive.nutrient_factor

        if best_beehive.volume > 0:
            self.add_beehive(best_beehive)

        return emeralds_earned
    # def __init__(self, max_beehives: int):
    #     """
    #         Initializes a maximum number of beehives.
    #
    #         :param max_beehives: The maximum number of beehives that can be managed.
    #         :complexity: O(1)
    #     """
    #
    #     self.max_beehives = max_beehives
    #     self.beehives = []
    #
    # def set_all_beehives(self, hive_list: list[Beehive]):
    #     """
    #         Sets all the beehives in the manager with the given list of beehives.
    #         Only the top `max_beehives` beehives, sorted by potential emerald yield, will be stored.
    #
    #         :param hive_list: The list of Beehive objects to set.
    #         :complexity: O(M), where M is the length of `hive_list`.
    #     """
    #     sorted_beehives = sorted(hive_list, key=lambda hive: min(hive.capacity, hive.volume) * hive.nutrient_factor, reverse=True)
    #     self.beehives = sorted_beehives[:self.max_beehives]
    #
    # def add_beehive(self, hive: Beehive):
    #
    #     """
    #         Adds a new beehive to the manager, maintaining a maximum of `max_beehives` beehives.
    #         If the number of beehives exceeds the maximum, the beehive with the lowest potential yield is replaced.
    #
    #         :param hive: The Beehive object to add.
    #         :complexity: O(log N), where N is the number of beehives in `self.beehives`.
    #     """
    #
    #     self.beehives.append(hive)
    #     self.beehives.sort(key=lambda hive: min(hive.capacity, hive.volume) * hive.nutrient_factor, reverse=True)
    #     if len(self.beehives) > self.max_beehives:
    #         self.beehives.pop()
    #
    # def harvest_best_beehive(self):
    #
    #     """
    #         Harvests honey from the beehive with the highest potential yield.
    #         The beehive is removed from the manager if its honey volume becomes zero.
    #
    #         :return: The number of emeralds earned from the harvested honey.
    #         :complexity: O(log N), where N is the number of beehives in `self.beehives`.
    #     """
    #     if len(self.beehives) > 0:
    #         # Sort the beehives by potential emerald yield
    #         self.beehives.sort(key=lambda hive: min(hive.capacity, hive.volume) * hive.nutrient_factor, reverse=True)
    #
    #         # Pop the first hive (with max potential yield)
    #         hive = self.beehives.pop(0)
    #
    #         # Calculate honey to harvest and update hive's volume
    #         honey_harvested = min(hive.capacity, hive.volume)
    #         hive.volume -= honey_harvested
    #
    #         # If the hive still has honey, add it back to the list
    #         if hive.volume > 0:
    #             self.beehives.append(hive)
    #
    #         # Return the number of emeralds earned
    #         return honey_harvested * hive.nutrient_factor
    #     else:
    #         return 0.0
    #

