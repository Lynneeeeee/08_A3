from __future__ import annotations
from threedeebeetree import Point
from ratio import Percentiles
from bst import TreeNode
def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    def sort_by_axis(points: list[Point], depth: int = 0) -> TreeNode:
        if not points:
            return None

        # Select axis based on depth so that axis cycles through all valid values
        axis = depth % 3

        # Sort points list and choose median as root
        points.sort(key=lambda point: point[axis])

        median = len(points) // 2  # choose median

        # Create node and construct subtrees
        node = TreeNode(points[median])
        node.left = sort_by_axis(points[:median], depth + 1)
        node.right = sort_by_axis(points[median + 1:], depth + 1)

        return node

    def balance_tree(node: TreeNode):
        if node is None:
            return

        # Count the number of points on each side of the axis
        count_left = count_points(node.left)
        count_right = count_points(node.right)

        # If the size ratio exceeds 1:7, split the points
        if count_left > 17 * count_right or count_right > 17 * count_left:
            split_points(node)

        # Recursively balance the left and right subtrees
        balance_tree(node.left)
        balance_tree(node.right)

    def count_points(node: TreeNode) -> int:
        if node is None:
            return 0
        return 1 + count_points(node.left) + count_points(node.right)

    def split_points(node: TreeNode):
        points = collect_points(node)
        node.left = None
        node.right = None

        sort_by_axis(points, node.axis)

        median = len(points) // 2
        node.key = points[median][0]  # Update the key of the node
        node.item = points[median]  # Update the item of the node

        node.left = sort_by_axis(points[:median], node.depth + 1)
        node.right = sort_by_axis(points[median + 1:], node.depth + 1)

    def collect_points(node: TreeNode) -> list[Point]:
        if node is None:
            return []
        return [node.item] + collect_points(node.left) + collect_points(node.right)

    root = sort_by_axis(my_coordinate_list)
    balance_tree(root)
    return collect_points(root)