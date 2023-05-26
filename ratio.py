from __future__ import annotations
from typing import Generic, TypeVar, List
from math import ceil
from bst import BinarySearchTree
from node import TreeNode

T = TypeVar("T")
I = TypeVar("I")


class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.bst = BinarySearchTree[T, T]()
    
    def add_point(self, item: T):
        self.bst[item] = item
    
    def remove_point(self, item: T):
        if item in self.bst:
            del self.bst[item]

    def ratio(self, x: float, y: float) -> List[T]:
        n = len(self.bst)
        x_idx = int(n * (x / 100.0)) + 1
        y_idx = int(n * (y / 100.0)) - 1

        results = []

        # for i in range(x_idx, n - y_idx):
        #     node = self.bst.kth_smallest(i, self.bst.root)
        #     results.append(node.item)
        #
        # return results
        if x_idx > y_idx:
            return results

        for i in range(x_idx, n - y_idx + 1):
            try:
                node = self.bst.kth_smallest(i, self.bst.root)
                results.append(node.item)
            except ValueError:
                break

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
