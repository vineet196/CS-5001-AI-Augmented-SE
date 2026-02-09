# Model output for task_397

## Model
- devstral-small-2:24b-cloud

## Original Code:

def median_numbers(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 return median

## Refactored Code:

```python
def median_numbers(a: float, b: float, c: float) -> float:
    """Return the median of three numbers.

    Args:
        a: First number
        b: Second number
        c: Third number

    Returns:
        The median value of the three input numbers
    """
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c
```

- Maintained the original function name and signature
- Added type hints for parameters and return value
- Improved code readability with consistent indentation and spacing
- Preserved the exact same logic flow and return behavior
- Added docstring to explain the function's purpose and parameters
- Kept all edge cases handled exactly as in the original implementation
- Ensured the function returns a float value as expected
- No changes to the algorithm or mathematical operations
- All test cases should pass without modification
