import math


def hex_to_rgb(hex_value):
    hex_value = hex_value.lstrip("#")
    r = int(hex_value[0:2], 16)
    g = int(hex_value[2:4], 16)
    b = int(hex_value[4:6], 16)
    return r, g, b


def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def srgb_to_linear(channel):
    c = channel / 255.0
    if c <= 0.04045:
        return c / 12.92
    return ((c + 0.055) / 1.055) ** 2.4


def linear_to_srgb(c):
    if c <= 0.0031308:
        srgb = c * 12.92
    else:
        srgb = 1.055 * (c ** (1 / 2.4)) - 0.055
    return round(min(max(srgb, 0.0), 1.0) * 255)


def rgb_to_oklch(r, g, b):
    lr, lg, lb = srgb_to_linear(r), srgb_to_linear(g), srgb_to_linear(b)

    l = 0.4122214708 * lr + 0.5363325363 * lg + 0.0514459929 * lb
    m = 0.2119034982 * lr + 0.6806995451 * lg + 0.1073969566 * lb
    s = 0.0883024619 * lr + 0.2817188376 * lg + 0.6299787005 * lb

    l_, m_, s_ = l ** (1 / 3), m ** (1 / 3), s ** (1 / 3)

    lightness = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_
    a = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    b_lab = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_

    chroma = math.hypot(a, b_lab)
    hue = math.degrees(math.atan2(b_lab, a)) % 360
    return lightness, chroma, hue


def oklch_to_rgb(lightness, chroma, hue_degrees):
    hue_rad = math.radians(hue_degrees)

    # lower chroma if gamut is too high
    for _ in range(20):
        a = chroma * math.cos(hue_rad)
        b_lab = chroma * math.sin(hue_rad)

        l_ = lightness + 0.3963377774 * a + 0.2158037573 * b_lab
        m_ = lightness - 0.1055613458 * a - 0.0638541728 * b_lab
        s_ = lightness - 0.0894841775 * a - 1.2914855480 * b_lab

        l, m, s = l_**3, m_**3, s_**3

        lr = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
        lg = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
        lb = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s

        if all(-0.001 <= channel <= 1.001 for channel in (lr, lg, lb)):
            break
        chroma *= 0.9  # nudge toward gray and try again

    return linear_to_srgb(lr), linear_to_srgb(lg), linear_to_srgb(lb)


def oklch_to_hex(lightness, chroma, hue_degrees):
    r, g, b = oklch_to_rgb(lightness, chroma, hue_degrees)
    return f"#{r:02x}{g:02x}{b:02x}"
