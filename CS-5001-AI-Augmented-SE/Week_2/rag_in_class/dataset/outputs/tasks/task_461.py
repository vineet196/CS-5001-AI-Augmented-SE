def upper_ctr(s: str) -> int:
    """Count the number of uppercase letters in the input string.

    Args:
        s: Input string to analyze.

    Returns:
        int: Number of uppercase letters in the string.
             Returns 0 for empty strings.
    """
    count = 0
    for char in s:
        if 'A' <= char <= 'Z':
            count += 1
    return count
