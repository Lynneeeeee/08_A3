from __future__ import annotations
import math
from typing import Generic, TypeVar, List
from math import ceil
from bst import BinarySearchTree
from node import TreeNode

T = TypeVar("T")
I = TypeVar("I")


class Percentiles(Generic[T]):

    def __init__(self) -> None:
        """
            Initializes an instance of the class with an empty Binary Search Tree.
            :complexity: O(1)
        """
        self.bst = BinarySearchTree()

    def add_point(self, item: T):
        """
           Inserts an item into the Binary Search Tree.
           :param item: The item to be added to the Binary Search Tree.
           :complexity:  O(log n), when the tree is balanced.
        """
        self.bst[item] = item
    
    def remove_point(self, item: T):
        """
            Deletes an item from the Binary Search Tree.
            :param item: The item to be removed from the Binary Search Tree.
            :complexity: O(log n), when the tree is balanced.
        """
        del self.bst[item]

    def ratio(self, x: float, y: float) -> List[T]:
        """
            x and y are given as percentages between 0 and 100.
            The function finds all elements that are larger than at least x% of the elements
            and smaller than at least y% of the elements.

            Params:
            x – Percentage value for the lower limit.
            y – Percentage value for the upper limit.
            Returns:
            List of elements that are larger than at least x% of the elements and smaller than at least y% of the elements.
            :complexity: O(log n + O), where O is the number of points returned by the function.
        """

        n = len(self.bst)
        lower_rank = int(math.ceil((n) * x / 100)) + 1
        upper_rank = n - int(math.ceil((n) * y / 100)) - 1 + 1

        results = []
        for rank in range(lower_rank, upper_rank + 1):
            node_item = self.bst.kth_smallest(rank, self.bst.root).item
            results.append(node_item)

        return results


if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
