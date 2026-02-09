def digit_distance_nums(n1: int, n2: int) -> int:
    """Calculate the sum of the digits of the absolute difference between two numbers.

    Args:
        n1: First integer
        n2: Second integer

    Returns:
        Sum of digits in the absolute difference between n1 and n2
    """
    difference = abs(n1 - n2)
    return sum(int(digit) for digit in str(difference))
