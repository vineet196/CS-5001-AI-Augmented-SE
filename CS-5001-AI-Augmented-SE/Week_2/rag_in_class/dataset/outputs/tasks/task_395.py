from typing import Optional

def first_non_repeating_character(str1: str) -> Optional[str]:
    """Return the first non-repeating character in the string.

    Args:
        str1: Input string to search for the first non-repeating character.

    Returns:
        The first non-repeating character as a string, or None if all characters repeat.
    """
    char_order = []
    char_count = {}

    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            char_order.append(char)

    for char in char_order:
        if char_count[char] == 1:
            return char

    return None
