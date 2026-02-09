# Model output for task_252

## Model
- devstral-small-2:24b-cloud

## Original Code:

import cmath  
def convert(numbers):    
  num = cmath.polar(numbers)  
  return (num) 

## Refactored Code:

```python
import cmath
from typing import Union, Tuple

def convert(numbers: Union[complex, float]) -> Tuple[float, float]:
    """
    Convert a complex number or real number to its polar form (magnitude and phase in radians).

    Args:
        numbers: A complex number or a real number to be converted.

    Returns:
        A tuple (magnitude, phase) where:
        - magnitude is the distance from the origin to the point in the complex plane.
        - phase is the angle in radians between the positive real axis and the point.

    Note:
        For real numbers, the phase will be 0.0 if the number is positive and π (pi) if negative.
    """
    num = cmath.polar(numbers)
    return num
```

- Maintained the original function name and interface contract.
- Added type hints for better code clarity and type safety.
- Preserved the exact behavior of the original function, including handling of both complex and real numbers.
- Added a docstring to explain the function's purpose, arguments, and return values.
- Ensured the function returns a tuple of floats (magnitude and phase in radians) as per the original behavior.
- No changes to the core logic or algorithm, ensuring functional parity with the original implementation.
