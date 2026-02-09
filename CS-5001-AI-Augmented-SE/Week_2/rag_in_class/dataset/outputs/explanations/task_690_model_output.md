# Model output for task_690

## Model
- devstral-small-2:24b-cloud

## Original Code:

def mul_consecutive_nums(nums):
    result = [b*a for a, b in zip(nums[:-1], nums[1:])]
    return result

## Refactored Code:

```python
from typing import List, Union

def mul_consecutive_nums(nums: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Multiplies each pair of consecutive numbers in the input list.

    Args:
        nums: List of numbers (int or float)

    Returns:
        List of products of consecutive pairs. Returns empty list if input has less than 2 elements.
    """
    if len(nums) < 2:
        return []

    result = [a * b for a, b in zip(nums[:-1], nums[1:])]
    return result
```

- Maintained the original function name and interface contract
- Added type hints for better code documentation and type checking
- Improved docstring to clearly explain the function's purpose and behavior
- Added explicit check for edge case (list with less than 2 elements)
- Preserved the original list comprehension logic for multiplying consecutive pairs
- Ensured the function returns an empty list for edge cases (as per original behavior)
- Kept the same return type (list of numbers) for all cases
- Maintained exact functional parity with the original implementation
