from typing import List, Any

def remove_elements(list1: List[Any], list2: List[Any]) -> List[Any]:
    """Remove elements from list1 that are present in list2.

    Args:
        list1: The list from which elements will be removed.
        list2: The list containing elements to be removed from list1.

    Returns:
        A new list containing elements from list1 that are not in list2.
    """
    return [x for x in list1 if x not in list2]
