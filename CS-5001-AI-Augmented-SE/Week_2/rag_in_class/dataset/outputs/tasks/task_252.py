import cmath
from typing import Union, Tuple

def convert(numbers: Union[complex, float]) -> Tuple[float, float]:
    """
    Convert a complex number or real number to its polar form (magnitude and phase in radians).

    Args:
        numbers: A complex number or a real number to be converted.

    Returns:
        A tuple (magnitude, phase) where:
        - magnitude is the distance from the origin to the point in the complex plane.
        - phase is the angle in radians between the positive real axis and the point.

    Note:
        For real numbers, the phase will be 0.0 if the number is positive and π (pi) if negative.
    """
    num = cmath.polar(numbers)
    return num
