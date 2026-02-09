class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None

def get_height(root: Node | None) -> int:
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1

def is_tree_balanced(root: Node | None) -> bool:
    if root is None:
        return True
    lh = get_height(root.left)
    rh = get_height(root.right)
    if (abs(lh - rh) <= 1) and is_tree_balanced(root.left) and is_tree_balanced(root.right):
        return True
    return False
