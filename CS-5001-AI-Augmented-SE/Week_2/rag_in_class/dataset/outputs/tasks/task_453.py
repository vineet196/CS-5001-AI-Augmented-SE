import math
from typing import Union

def sumofFactors(n: int) -> Union[int, None]:
    """
    Calculate the sum of factors of a given integer n.

    Args:
        n: An integer to calculate the sum of its factors.

    Returns:
        The sum of factors of n if n is even, otherwise 0.
        Returns None for empty lists (though n is an integer, this is for consistency with the constraint).
    """
    if n % 2 != 0:
        return 0

    res = 1
    temp_n = n  # Preserve original n for potential logging/debugging

    for i in range(2, int(math.sqrt(n)) + 1):
        count = 0
        curr_sum = 1
        curr_term = 1

        while n % i == 0:
            count += 1
            n = n // i
            if i == 2 and count == 1:
                curr_sum = 0
            curr_term *= i
            curr_sum += curr_term

        res *= curr_sum

    if n >= 2:
        res *= (1 + n)

    return res
