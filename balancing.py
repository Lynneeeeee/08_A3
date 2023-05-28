from __future__ import annotations

import ratio
from threedeebeetree import Point


def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    x_coordinates = [point[0] for point in my_coordinate_list]
    results = []

    p = ratio.Percentiles()
    for x in x_coordinates:
        p.add_point(x)

    percentile_values = p.ratio(0, 0)
    for value in percentile_values:
        for point in my_coordinate_list:
            if point[0] == value:
                results.append(point)
                break

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