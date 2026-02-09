def median_numbers(a: float, b: float, c: float) -> float:
    """Return the median of three numbers.

    Args:
        a: First number
        b: Second number
        c: Third number

    Returns:
        The median value of the three input numbers
    """
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c
