from __future__ import annotations
from threedeebeetree import Point


def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    def make_ordering_aux(points: list[Point], depth: int) -> list[Point]:
        if not points:
            return []

        # choose axis based on depth so that axis cycles through x, y, z
        axis = depth % 3

        # sort point list and choose median as root
        points.sort(key=lambda point: point[axis])
        median = len(points) // 2

        # create node and construct subtrees
        return [points[median]] + make_ordering_aux(points[:median], depth + 1) + make_ordering_aux(points[median + 1:],
                                                                                                    depth + 1)

    return make_ordering_aux(my_coordinate_list, 0)

