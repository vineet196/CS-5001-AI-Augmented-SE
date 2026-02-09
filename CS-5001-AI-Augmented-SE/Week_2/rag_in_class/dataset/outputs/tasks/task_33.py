def decimal_To_Binary(N: int) -> int:
    """
    Convert a decimal number to its binary representation as an integer.

    Args:
        N: The decimal number to convert (must be non-negative).

    Returns:
        The binary representation of N as an integer (e.g., 5 -> 101).
        Returns 0 if N is 0.
    """
    if N == 0:
        return 0

    B_Number = 0
    cnt = 0
    while N != 0:
        rem = N % 2
        c = 10 ** cnt
        B_Number += rem * c
        N //= 2
        cnt += 1
    return B_Number
