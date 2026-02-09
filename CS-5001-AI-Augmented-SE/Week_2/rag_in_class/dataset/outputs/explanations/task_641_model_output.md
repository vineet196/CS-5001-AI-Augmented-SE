# Model output for task_641

## Model
- devstral-small-2:24b-cloud

## Original Code:

def is_nonagonal(n): 
	return int(n * (7 * n - 5) / 2) 

## Refactored Code:

```python
def is_nonagonal(n: int) -> int:
    """Calculate the nth nonagonal number.

    The nth nonagonal number is given by the formula: n * (7n - 5) / 2.

    Args:
        n: A positive integer representing the position in the nonagonal number sequence.

    Returns:
        The nth nonagonal number as an integer.
    """
    return int(n * (7 * n - 5) / 2)
```

- Preserved the original function name and signature to maintain interface contract
- Added type hints for better code clarity and early error detection
- Included a docstring explaining the purpose and formula of the function
- Maintained the exact same mathematical formula and return type (int)
- No changes to the core logic or behavior, ensuring functional parity
- The function remains a pure calculation without side effects
- Edge cases (like n=0) are handled the same way as the original implementation
