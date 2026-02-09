def number_of_substrings(s: str) -> int:
    """Calculate the number of possible substrings in a given string.

    Args:
        s: Input string for which to count substrings.

    Returns:
        The number of substrings as an integer. Returns 0 for empty strings.
    """
    str_len = len(s)
    return int(str_len * (str_len + 1) / 2)
