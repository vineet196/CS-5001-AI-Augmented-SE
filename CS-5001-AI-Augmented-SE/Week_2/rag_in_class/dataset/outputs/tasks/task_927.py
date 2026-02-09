class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None

def max_height(node: Node | None) -> int:
    """
    Calculate the maximum height of a binary tree.

    Args:
        node: The root node of the binary tree. If None, the tree is empty.

    Returns:
        The maximum height of the tree. For an empty tree (node is None), returns 0.
    """
    if node is None:
        return 0
    left_height = max_height(node.left)
    right_height = max_height(node.right)
    return max(left_height, right_height) + 1
