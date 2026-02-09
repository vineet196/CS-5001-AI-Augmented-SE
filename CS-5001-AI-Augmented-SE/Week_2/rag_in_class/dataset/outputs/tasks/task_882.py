def parallelogram_perimeter(base: float, height: float) -> float:
    """
    Calculate the perimeter of a parallelogram given its base and height.

    Args:
        base: Length of the base of the parallelogram (in any consistent unit).
        height: Height of the parallelogram (in the same unit as base).

    Returns:
        The perimeter of the parallelogram (2 * (base + height)).

    Note:
        The formula for the perimeter of a parallelogram is 2 * (base + height).
        This function assumes the input dimensions are valid (positive numbers).
    """
    perimeter = 2 * (base + height)
    return perimeter
