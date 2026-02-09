# Model output for task_367

## Model
- devstral-small-2:24b-cloud

## Original Code:

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def get_height(root): 
	if root is None: 
		return 0
	return max(get_height(root.left), get_height(root.right)) + 1
def is_tree_balanced(root): 
	if root is None: 
		return True
	lh = get_height(root.left) 
	rh = get_height(root.right) 
	if (abs(lh - rh) <= 1) and is_tree_balanced( 
	root.left) is True and is_tree_balanced( root.right) is True: 
		return True
	return False

## Refactored Code:

```python
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
```

- Maintained original function names and interface contracts
- Added type hints for better code clarity and type safety
- Removed redundant `is True` checks in boolean conditions
- Preserved exact behavior for all edge cases (None root, balanced/unbalanced trees)
- Ensured in-place modification is not applicable (functions work with immutable tree structure)
- Maintained exact return types (bool for is_tree_balanced, int for get_height)
- Kept original algorithm logic and mathematical operations unchanged
- Improved code formatting and readability while preserving functionality
- Added proper None type annotations for optional Node parameters
