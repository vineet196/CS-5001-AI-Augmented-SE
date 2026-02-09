def binary_to_integer(test_tup: tuple) -> str:
    """Convert a tuple of binary digits to its integer representation as a string.

    Args:
        test_tup: A tuple of integers representing binary digits (0 or 1).

    Returns:
        A string representation of the integer value of the binary tuple.
    """
    if not test_tup:
        return "0"

    binary_str = "".join(str(ele) for ele in test_tup)
    integer_value = int(binary_str, 2)
    return str(integer_value)
