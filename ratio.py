from __future__ import annotations
from typing import Generic, TypeVar, List
from math import ceil
from bst import BinarySearchTree
from node import TreeNode

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.elements = BinarySearchTree()
    
    def add_point(self, item: T):
        self.elements[item] = item
    
    def remove_point(self, item: T):
        del self.elements[item]

    def ratio(self, x, y):
        total_elements = len(self.elements)
        x_rank = int(ceil(total_elements * x / 100))
        y_rank = int(ceil(total_elements * y / 100))

        result = []
        self._traverse_in_order(self.elements.root, x_rank, y_rank, result)
        return result

    def _traverse_in_order(self, current: TreeNode, x_rank: int, y_rank: int, result: List[T]) -> None:
        if current is None or len(result) >= y_rank:
            return

        if current.left:
            left_size = current.left.subtree_size
        else:
            left_size = 0

        if left_size >= x_rank:
            self._traverse_in_order(current.left, x_rank, y_rank, result)

        if len(result) < y_rank:
            result.append(current.item)

        if left_size < y_rank:
            self._traverse_in_order(current.right, x_rank - left_size - 1, y_rank - left_size - 1, result)


if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
