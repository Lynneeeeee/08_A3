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
    """
    Wrapper around Beehive to make it work in a MaxHeap
    The volume attribute represents the potential yield of a beehive.
    """

    def __init__(self, beehive: Beehive, volume: float):
        self.beehive = beehive
        self.volume = volume

    def __lt__(self, other):
        return self.volume < other.volume

    def __le__(self, other):
        return self.volume <= other.volume

    def __gt__(self, other):
        return self.volume > other.volume

    def __ge__(self, other):
        return self.volume >= other.volume

    def __eq__(self, other):
        return self.volume == other.volume


class BeehiveSelector:
    def __init__(self, max_beehives: int):
        """
            Initialize a BeehiveSelector with a maximum number of beehives that can be managed.
            :param max_beehives: The maximum number of beehives that can be managed.
            :complexity: O(1)
        """
        self.max_beehives = max_beehives
        self.beehives_heap = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: List[Beehive]):
        """
            Sets all the beehives in the manager with the given list of beehives.
            :param hive_list: The list of Beehive objects to set.
            :complexity: O(N), where N is the length of hive_list.
        """
        self.beehives_heap = MaxHeap(self.max_beehives)
        for hive in hive_list:
            self.add_beehive(hive)

    def add_beehive(self, hive: Beehive):
        """
            Adds a new beehive to the manager, maintaining the `max_beehives` limit.
            :param hive: The Beehive object to add.
            :complexity: O(log N), where N is the number of beehives in the heap.
        """
        hive_volume = min(hive.capacity, hive.volume) * hive.nutrient_factor
        self.beehives_heap.add(HeapBeehive(beehive=hive, volume=hive_volume))

    def harvest_best_beehive(self):
        """
            Harvests honey from the beehive with the highest potential yield.
            The beehive is removed from the heap if its honey volume becomes zero.
            :return: The number of emeralds earned from the harvested honey.
            :complexity: O(log N), where N is the number of beehives in the heap.
        """
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
