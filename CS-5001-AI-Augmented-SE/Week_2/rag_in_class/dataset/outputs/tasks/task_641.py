def is_nonagonal(n: int) -> int:
    """Calculate the nth nonagonal number.

    The nth nonagonal number is given by the formula: n * (7n - 5) / 2.

    Args:
        n: A positive integer representing the position in the nonagonal number sequence.

    Returns:
        The nth nonagonal number as an integer.
    """
    return int(n * (7 * n - 5) / 2)
