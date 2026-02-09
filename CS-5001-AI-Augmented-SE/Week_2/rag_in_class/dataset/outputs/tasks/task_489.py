def frequency_Of_Largest(n: int, arr: list[int]) -> int:
    """
    Calculate the frequency of the largest element in the array.

    Args:
        n: Length of the array.
        arr: List of integers.

    Returns:
        Frequency of the largest element in the array.
    """
    if n == 0 or not arr:
        return 0

    max_val = arr[0]
    freq = 1

    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
            freq = 1
        elif arr[i] == max_val:
            freq += 1

    return freq
