from typing import List, Union

def mul_consecutive_nums(nums: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Multiplies each pair of consecutive numbers in the input list.

    Args:
        nums: List of numbers (int or float)

    Returns:
        List of products of consecutive pairs. Returns empty list if input has less than 2 elements.
    """
    if len(nums) < 2:
        return []

    result = [a * b for a, b in zip(nums[:-1], nums[1:])]
    return result
