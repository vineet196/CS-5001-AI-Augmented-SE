def count_Hexadecimal(L: int, R: int) -> int:
    """
    Counts the number of integers in the range [L, R] that contain at least one hexadecimal digit (A-F).

    Args:
        L: The lower bound of the range (inclusive).
        R: The upper bound of the range (inclusive).

    Returns:
        The count of integers in the range [L, R] that contain at least one hexadecimal digit (A-F).
    """
    count = 0
    for i in range(L, R + 1):
        if 10 <= i <= 15:
            count += 1
        elif i > 15:
            k = i
            while k != 0:
                if k % 16 >= 10:
                    count += 1
                    break  # No need to check further digits once a hex digit is found
                k = k // 16
    return count
