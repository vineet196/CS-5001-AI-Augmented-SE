from typing import List, Union

def filter_oddnumbers(nums: List[int]) -> Union[List[int], bool]:
    """
    Filters out all even numbers from the input list and returns a list of odd numbers.
    If the input list is empty or contains no odd numbers, returns False.

    Args:
        nums: List of integers to filter

    Returns:
        List of odd integers from the input, or False if no odd numbers found
    """
    odd_nums = [x for x in nums if x % 2 != 0]
    return odd_nums if odd_nums else False
