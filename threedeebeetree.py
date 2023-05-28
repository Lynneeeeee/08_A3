from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I
    subtree_size: int = 1
    children: list[BeeNode | None] = field(default_factory=lambda: [None] * 8)

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        """
            This method returns the child that corresponds to the provided point.
            The point is a 3D coordinate.

            :param point: 3D coordinate to determine which child node to return.
            :return: The child node that corresponds to the provided point.
            :complexity: O(1)
        """
        x, y, z = point
        octant = 0
        if x < self.key[0]:
            octant += 1
        if y < self.key[1]:
            octant += 2
        if z < self.key[2]:
            octant += 4
        return self.children[octant]


class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
            :complexity: O(1)
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        """
            Attempts to get the tree node associated with a given key.
            If the key is not found, a KeyError is raised.

            :param key: The key of the node to get.
            :return: The node associated with the given key.
            :raises KeyError: If the key is not found in the tree.
            :complexity: best O(log N), where N is the number of nodes in the tree
                         worst case O(N).
        """

        if self.root is None:
            raise KeyError('Key not found: {0}'.format(key))
        current = self.root
        while current:  # Loop until find the specific node
            if key == current.key:
                return current

            x, y, z = key
            octant = 0
            if x < current.key[0]:
                octant += 1
            if y < current.key[1]:
                octant += 2
            if z < current.key[2]:
                octant += 4

            child = current.children[octant]
            if child is None:
                raise KeyError('Key not found: {0}'.format(key))
            current = child

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
            Inserts an item into the tree at the position determined by the key. If the current node is None, a new node
            is created.
            If there already exists a node at the determined position, the method is recursively called on the child node.

            :param current: The current node in the tree during the traversal.
            :param key: The key of the node to insert.
            :param item: The item to insert in the tree.
            :return: The node after insertion.
            :complexity: O(log N), where N is the number of nodes in the tree.
                        worst case, O(N).
        """
        if current is None:
            self.length += 1
            return BeeNode(key, item)

        x, y, z = key
        octant = 0
        if x < current.key[0]:
            octant += 1
        if y < current.key[1]:
            octant += 2
        if z < current.key[2]:
            octant += 4

        child = current.children[octant]
        if child is None:
            current.children[octant] = BeeNode(key, item)
            self.length += 1
        else:
            current.children[octant] = self.insert_aux(child, key, item)

        subtree_size = 0
        for child in current.children:  # Add the subtree size of each child to the total
            if child:
                subtree_size += child.subtree_size
        current.subtree_size = subtree_size + 1
        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        for child in current.children:
            if child is not None:
                return False
        return True

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
