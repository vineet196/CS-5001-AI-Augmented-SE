def even_bit_toggle_number(n: int) -> int:
    """
    Toggles the even-positioned bits (1-based index) of the integer n.
    For example, the 2nd, 4th, 6th, etc. bits are toggled.

    Args:
        n: The integer whose even-positioned bits are to be toggled.

    Returns:
        The integer with even-positioned bits toggled.
    """
    res = 0
    count = 0
    temp = n
    while temp > 0:
        if count % 2 == 1:  # Check if the bit position is even (1-based)
            res |= (1 << count)
        count += 1
        temp >>= 1
    return n ^ res
