import math
from typing import Union

def area_pentagon(a: float) -> float:
    """
    Calculate the area of a regular pentagon with side length 'a'.

    Args:
        a: Side length of the pentagon (must be positive)

    Returns:
        Area of the pentagon as a float

    Formula:
        Area = (sqrt(5*(5 + 2*sqrt(5))) * a^2) / 4
    """
    if a <= 0:
        raise ValueError("Side length must be positive")

    area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (a ** 2)) / 4.0
    return area
