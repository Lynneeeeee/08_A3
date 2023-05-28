from __future__ import annotations
import ratio, bst
from threedeebeetree import Point


class tempNode:
    """
        A temporary Node class used for make_ordering.
        Has a key and a value.
    """
    def __init__(self, k, v):
        self.k = k
        self.v = v

    def __lt__(self, other):
        return self.k < other.k

    def __gt__(self, other):
        return self.k > other.k

    def __eq__(self, other):
        return self.k == other.k


def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    """
        Find and return an order which splits its children by a size ratio
        :param my_coordinate_list: A list of points
        :return: The list after sorting
        :complexity: O(nlog(n)×log(n)), n is the number of points in the list
    """
    px = ratio.Percentiles()
    py = ratio.Percentiles()
    pz = ratio.Percentiles()
    bstX = bst.BinarySearchTree()
    for i, p in enumerate(my_coordinate_list):
        px.add_point(tempNode(p[0], i))
        py.add_point(tempNode(p[1], i))
        pz.add_point(tempNode(p[2], i))

    #  Find idx at the position of 12.6%
    x_idx = px.ratio(12.6, 12.6)
    y_idx = py.ratio(12.6, 12.6)
    z_idx = pz.ratio(12.6, 12.6)
    x_list = set([p.v for p in x_idx])
    y_list = set([p.v for p in y_idx])
    z_list = set([p.v for p in z_idx])

    potential = list(x_list & y_list & z_list)
    idx = potential[0]
    key = my_coordinate_list[idx]
    children = [[] for _ in range(8)]
    for current in my_coordinate_list:
        if current == key : continue
        octant = sum((1 if key[i] < current[i] else 0) << i for i in range(3))
        children[octant].append(current)

    results = [key]

    for l in children:
        if len(l) > 17:  # If subtree length > 17, recursively call make_ordering()
            l = make_ordering(l[:])
        results += l

    return results


if __name__ == "__main__":
    points = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (2, 3, 1),
        (5, 6, 4),
        (8, 9, 7),
    ]
    new_ordering = make_ordering(points)
    for point in new_ordering:
        print(point)
