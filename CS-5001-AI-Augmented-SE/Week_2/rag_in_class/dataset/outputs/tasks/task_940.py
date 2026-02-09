from typing import List, Optional

def heap_sort(arr: List[int]) -> List[int]:
    """Sorts the input list in-place using heap sort algorithm.

    Args:
        arr: List of integers to be sorted in ascending order.

    Returns:
        The sorted list (same as input list after in-place modification).
    """
    if not arr:
        return arr

    heapify(arr)
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        shift_down(arr, 0, end - 1)
        end -= 1
    return arr

def heapify(arr: List[int]) -> None:
    """Converts the input list into a max-heap in-place.

    Args:
        arr: List of integers to be converted into a max-heap.
    """
    start = len(arr) // 2 - 1  # Start from the last non-leaf node
    while start >= 0:
        shift_down(arr, start, len(arr) - 1)
        start -= 1

def shift_down(arr: List[int], start: int, end: int) -> None:
    """Performs the shift-down operation to maintain the max-heap property.

    Args:
        arr: List representing the heap.
        start: Index of the current root node.
        end: Index of the last element in the heap.
    """
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break
