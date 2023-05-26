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
        self.bst = BinarySearchTree()

    def add_point(self, item: T):
        self.bst[item] = item
    
    def remove_point(self, item: T):
        del self.bst[item]

    def ratio(self, x: float, y: float) -> List[T]:

        results = []

        # for i in range(x_idx, n - y_idx):
        #     node = self.bst.kth_smallest(i, self.bst.root)
        #     results.append(node.item)
        #
        # return results
        """
                x and y are given as percentages between 0 and 100.
                The function finds all elements that are larger than at least x% of the elements
                and smaller than at least y% of the elements.
                """
        """
                x and y are given as percentages between 0 and 100.
                The function finds all elements that are larger than at least x% of the elements
                and smaller than at least y% of the elements.
                """

        n = len(self.bst)
        lower_rank = int(math.ceil((n - 1) * x / 100))
        upper_rank = int(math.floor((n - 1) * y / 100))
        return [self.bst.kth_smallest(rank, self.bst.root).item for rank in range(lower_rank, upper_rank + 1)]

if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
