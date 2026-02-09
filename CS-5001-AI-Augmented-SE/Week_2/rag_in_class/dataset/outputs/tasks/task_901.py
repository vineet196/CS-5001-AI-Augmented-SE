def smallest_multiple(n: int) -> int:
    """Return the smallest positive number divisible by all integers from 1 to n.

    Args:
        n: The upper bound of the range (inclusive).

    Returns:
        The smallest multiple of all numbers from 1 to n.
        Returns None for n <= 0 or n > 100 (arbitrary upper limit for practicality).
    """
    if n <= 0 or n > 100:
        return None
    if n <= 2:
        return n

    i = n * 2
    factors = [number for number in range(n, 1, -1) if number * 2 > n]

    while True:
        divisible = True
        for a in factors:
            if i % a != 0:
                divisible = False
                i += n
                break
        if divisible:
            return i
