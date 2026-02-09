from typing import List, Union

def sum_list(lst1: List[Union[int, float]], lst2: List[Union[int, float]]) -> List[Union[int, float]]:
    """Sum corresponding elements of two lists of equal length.

    Args:
        lst1: First list of numbers.
        lst2: Second list of numbers.

    Returns:
        List of summed elements. Modifies the input lists in-place.

    Raises:
        ValueError: If the input lists have different lengths.
    """
    if len(lst1) != len(lst2):
        raise ValueError("Input lists must have the same length")

    for i in range(len(lst1)):
        lst1[i] += lst2[i]

    return lst1
