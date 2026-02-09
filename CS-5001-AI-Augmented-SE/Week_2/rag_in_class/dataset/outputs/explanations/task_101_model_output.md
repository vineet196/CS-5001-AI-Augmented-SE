# Model output for task_101

## Model
- devstral-small-2:24b-cloud

## Original Code:

def kth_element(arr, n, k):
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]

## Refactored Code:

```python
def kth_element(arr: list, n: int, k: int) -> int:
    """
    Sorts the array in ascending order and returns the k-th smallest element (1-based index).

    Args:
        arr: List of integers to be sorted.
        n: Length of the array.
        k: The 1-based index of the element to return.

    Returns:
        The k-th smallest element in the sorted array.

    Raises:
        IndexError: If k is out of bounds after sorting.
    """
    # Perform bubble sort to sort the array in-place
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Return the k-th smallest element (1-based index)
    return arr[k - 1]
```

- Fixed the syntax error in the swap operation (changed `==` to `=`).
- Added type hints for better code clarity and type checking.
- Added a docstring to explain the function's purpose, arguments, and return value.
- Maintained the in-place sorting behavior as required.
- Ensured the function returns the k-th smallest element using 1-based indexing.
- The function now raises an `IndexError` if `k` is out of bounds, which is the expected behavior for Python lists.
