# Model output for task_161

## Model
- devstral-small-2:24b-cloud

## Original Code:

def remove_elements(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result

## Refactored Code:

```python
from typing import List, Any

def remove_elements(list1: List[Any], list2: List[Any]) -> List[Any]:
    """Remove elements from list1 that are present in list2.

    Args:
        list1: The list from which elements will be removed.
        list2: The list containing elements to be removed from list1.

    Returns:
        A new list containing elements from list1 that are not in list2.
    """
    return [x for x in list1 if x not in list2]
```

- Maintained the original function name and interface contract
- Added type hints for better code clarity and type checking
- Preserved the exact behavior of removing elements from list1 that are present in list2
- Kept the list comprehension for efficient filtering
- Ensured the function returns a new list without modifying the input lists
- Added a docstring to explain the function's purpose and parameters
- No changes to the core logic or return type
- The function handles all edge cases (empty lists, non-existent elements) as per the original implementation
