from typing import List, Any

def remove_column(list1: List[List[Any]], n: int) -> List[List[Any]]:
    """
    Removes the nth column from each sublist in the input list in-place.

    Args:
        list1: A list of lists where each sublist represents a row.
        n: The index of the column to remove (0-based).

    Returns:
        The modified list with the nth column removed from each sublist.
    """
    for row in list1:
        if n < len(row):
            del row[n]
    return list1
