# Model output for task_395

## Model
- devstral-small-2:24b-cloud

## Original Code:

def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

## Refactored Code:

```python
from typing import Optional

def first_non_repeating_character(str1: str) -> Optional[str]:
    """Return the first non-repeating character in the string.

    Args:
        str1: Input string to search for the first non-repeating character.

    Returns:
        The first non-repeating character as a string, or None if all characters repeat.
    """
    char_order = []
    char_count = {}

    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            char_order.append(char)

    for char in char_order:
        if char_count[char] == 1:
            return char

    return None
```

- Maintained the original function name and interface contract
- Added type hints for better code clarity and type safety
- Improved variable naming for better readability (e.g., `ctr` → `char_count`)
- Preserved the exact logic flow and behavior of the original implementation
- Ensured the function returns `None` for empty strings or strings with all repeating characters
- Added a docstring to explain the function's purpose, arguments, and return value
- Kept the in-place modification of the `char_order` list as in the original
- Maintained the original algorithm's time complexity (O(n) for both passes through the string)
- Verified that the function handles edge cases (empty string, all repeating characters) correctly
- Ensured the function returns the first non-repeating character in the order it appears in the input string
