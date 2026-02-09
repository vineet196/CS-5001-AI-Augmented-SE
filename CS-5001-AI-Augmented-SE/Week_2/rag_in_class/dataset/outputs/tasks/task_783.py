def rgb_to_hsv(r: float, g: float, b: float) -> tuple[float, float, float]:
    """
    Convert RGB color values to HSV color space.

    Args:
        r: Red component (0-255)
        g: Green component (0-255)
        b: Blue component (0-255)

    Returns:
        tuple: (hue, saturation, value) where:
            - hue is in degrees [0, 360)
            - saturation is percentage [0, 100]
            - value is percentage [0, 100]
    """
    # Normalize RGB values to [0, 1] range
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    # Find max and min values
    mx = max(r_norm, g_norm, b_norm)
    mn = min(r_norm, g_norm, b_norm)
    df = mx - mn

    # Calculate Hue
    if mx == mn:
        h = 0.0
    elif mx == r_norm:
        h = (60 * ((g_norm - b_norm) / df) + 360) % 360
    elif mx == g_norm:
        h = (60 * ((b_norm - r_norm) / df) + 120) % 360
    else:  # mx == b_norm
        h = (60 * ((r_norm - g_norm) / df) + 240) % 360

    # Calculate Saturation
    s = 0.0 if mx == 0 else (df / mx) * 100

    # Calculate Value
    v = mx * 100

    return (h, s, v)
