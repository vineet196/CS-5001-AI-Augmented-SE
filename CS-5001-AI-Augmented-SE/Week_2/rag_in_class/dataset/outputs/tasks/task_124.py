import cmath
from typing import Union

def angle_complex(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Calculate the phase angle (in radians) of the complex number formed by a and b.

    Args:
        a: Real part of the complex number.
        b: Imaginary part of the complex number.

    Returns:
        The phase angle in radians.
    """
    complex_number = complex(a, b)
    angle = cmath.phase(complex_number)
    return angle
