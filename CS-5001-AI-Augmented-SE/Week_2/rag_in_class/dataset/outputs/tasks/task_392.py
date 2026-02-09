def get_max_sum(n: int) -> int:
    """
    Calculate the maximum sum for a given integer n using a dynamic programming approach.
    The sum for each integer i is the maximum of i itself or the sum of the maximum sums
    of its divisors (i/2, i/3, i/4, i/5).

    Args:
        n: The integer for which to calculate the maximum sum.

    Returns:
        The maximum sum for the integer n.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    res = [0, 1]  # Base cases: res[0] = 0, res[1] = 1

    for i in range(2, n + 1):
        # Calculate the sum of the maximum sums of the divisors
        sum_divisors = res[i // 2] + res[i // 3] + res[i // 4] + res[i // 5]
        # The current value is the maximum of i or the sum of its divisors
        res.append(max(i, sum_divisors))

    return res[n]
