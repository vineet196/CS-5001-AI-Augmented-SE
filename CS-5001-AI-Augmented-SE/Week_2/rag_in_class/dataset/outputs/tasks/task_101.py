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
