R = 3
C = 3

def min_cost(cost: list[list[int]], m: int, n: int) -> int:
    """
    Calculate the minimum cost path from the top-left corner to the bottom-right corner
    of a grid, moving only right or down.

    Args:
        cost: 2D list representing the cost matrix where cost[i][j] is the cost at cell (i,j)
        m: Number of rows in the cost matrix (0-based index)
        n: Number of columns in the cost matrix (0-based index)

    Returns:
        The minimum cost to reach the bottom-right corner from the top-left corner
    """
    # Initialize the total cost matrix with zeros
    total_cost = [[0 for _ in range(C)] for _ in range(R)]

    # Base case: starting cell
    total_cost[0][0] = cost[0][0]

    # Fill the first column (only moving down)
    for i in range(1, m + 1):
        total_cost[i][0] = total_cost[i - 1][0] + cost[i][0]

    # Fill the first row (only moving right)
    for j in range(1, n + 1):
        total_cost[0][j] = total_cost[0][j - 1] + cost[0][j]

    # Fill the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # The minimum cost to reach (i,j) is the minimum of:
            # - coming from top (i-1,j)
            # - coming from left (i,j-1)
            # - coming from top-left diagonal (i-1,j-1)
            total_cost[i][j] = min(total_cost[i - 1][j - 1], total_cost[i - 1][j], total_cost[i][j - 1]) + cost[i][j]

    return total_cost[m][n]
