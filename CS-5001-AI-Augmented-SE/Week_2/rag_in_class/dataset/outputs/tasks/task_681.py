def smallest_Divisor(n: int) -> int:
    """
    Returns the smallest divisor of n greater than 1.
    For even numbers, returns 2.
    For odd numbers, checks divisibility starting from 3, incrementing by 2.
    If n is prime, returns n itself.

    Args:
        n: Integer to find the smallest divisor for (must be >= 2)

    Returns:
        int: Smallest divisor of n greater than 1
    """
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n
