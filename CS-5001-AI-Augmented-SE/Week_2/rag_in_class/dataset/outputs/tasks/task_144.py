def sum_Pairs(arr: list[int], n: int) -> int:
    """
    Calculate the sum of pairs in the array based on the given formula.

    Args:
        arr: List of integers to process.
        n: The length of the array to consider.

    Returns:
        The computed sum based on the formula: sum += i*arr[i] - (n-1-i) * arr[i]
    """
    total = 0
    for i in range(n - 1, -1, -1):
        total += i * arr[i] - (n - 1 - i) * arr[i]
    return total
