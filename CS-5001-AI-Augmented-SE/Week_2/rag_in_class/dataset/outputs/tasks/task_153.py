def parabola_vertex(a: float, b: float, c: float) -> tuple[float, float]:
    """
    Calculate the vertex of a parabola given by the equation y = ax^2 + bx + c.

    Args:
        a: Coefficient of x^2 (must not be zero)
        b: Coefficient of x
        c: Constant term

    Returns:
        A tuple (x, y) representing the vertex coordinates of the parabola.

    Raises:
        ValueError: If a is zero (not a quadratic equation)
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation")

    x_vertex = -b / (2 * a)
    y_vertex = ((4 * a * c) - (b ** 2)) / (4 * a)

    return (x_vertex, y_vertex)
