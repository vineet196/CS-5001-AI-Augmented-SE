import cmath
from typing import Union

def len_complex(a: Union[int, float], b: Union[int, float]) -> float:
    """Calculate the magnitude (length) of a complex number.

    Args:
        a: Real part of the complex number.
        b: Imaginary part of the complex number.

    Returns:
        The magnitude (length) of the complex number as a float.
    """
    complex_number = complex(a, b)
    length = abs(complex_number)
    return length
