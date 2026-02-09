# Model output for task_153

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

## Refactored Code:

```python
def parabola_vertex(a: float, b: float, c: float) -> tuple[float, float]:
    """
    Calculate the vertex of a parabola given by the equation y = ax^2 + bx + c.

    Args:
        a: Coefficient of x^2 (must not be zero)
        b: Coefficient of x
        c: Constant term

    Returns:
        A tuple (x, y) representing the vertex coordinates of the parabola.

    Raises:
        ValueError: If a is zero (not a quadratic equation)
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation")

    x_vertex = -b / (2 * a)
    y_vertex = ((4 * a * c) - (b ** 2)) / (4 * a)

    return (x_vertex, y_vertex)
```

- Maintained the original function name and interface contract
- Added type hints for better code clarity and type checking
- Added input validation to handle the edge case where a=0 (which would make it not a quadratic equation)
- Improved variable naming for better readability
- Maintained the exact same mathematical calculations
- Added docstring to explain the function's purpose and behavior
- The function still returns a tuple of (x, y) coordinates as in the original
- Preserved the exact same return type and structure
- Added error handling for invalid input (a=0) which would have caused division by zero in the original
- The mathematical formulas remain unchanged to maintain exact functional parity
