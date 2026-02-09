def parallel_lines(line1: tuple[float, float], line2: tuple[float, float]) -> bool:
    """
    Check if two lines are parallel by comparing their slopes.

    Args:
        line1: A tuple representing the first line in (y2-y1, x2-x1) format.
        line2: A tuple representing the second line in (y2-y1, x2-x1) format.

    Returns:
        bool: True if the lines are parallel, False otherwise.
    """
    return line1[0] * line2[1] == line2[0] * line1[1]
