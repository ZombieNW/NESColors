from average_colors import (
    DB_PATH,
    TABLE_NAME,
    average_hex_per_prompt,
    fetch_prompt_values,
)
from color_convert import (
    hex_to_rgb,
    oklch_to_hex,
    rgb_to_oklch,
)

ROW_LIGHTNESS = [0.5, 0.75, 1.00, 1.5]

COLUMN_MAP = {
    "Gray": 0,
    "Azure": 1,
    "Blue": 2,
    "Violet": 3,
    "Magenta": 4,
    "Rose": 5,
    "Red": 6,
    "Orange": 7,
    "Yellow": 8,
    "Lime": 9,
    "Green": 10,
    "Teal": 11,
    "Cyan": 12,
}


def dim_hex_by_half(hex_value):
    r, g, b = hex_to_rgb(hex_value)
    r = r // 2
    g = g // 2
    b = b // 2
    return f"#{r:02x}{g:02x}{b:02x}"


def get_base_colors():
    prompt_values = fetch_prompt_values(DB_PATH, TABLE_NAME)
    averages = average_hex_per_prompt(prompt_values)

    base_colors = {}
    for prompt, hex_val in averages.items():
        if prompt in COLUMN_MAP:
            col_index = COLUMN_MAP[prompt]
            base_colors[col_index] = hex_val

    # hardcode remaining columns
    base_colors[13] = dim_hex_by_half(base_colors[0])  # $xD: Dark Gray
    base_colors[14] = "#000000"  # $xE: Black/Unused
    base_colors[15] = "#000000"  # $xF: Black/Unused

    return base_colors


def apply_filter(hex_color, row):
    if hex_color == "#000000":
        return "#000000"

    r, g, b = hex_to_rgb(hex_color)
    l, c, h = rgb_to_oklch(r, g, b)

    # changing luminance
    if row == 3:
        l = l + (1.0 - l) * 0.5  # pastel "formula"
    else:
        l = min(1.0, l * ROW_LIGHTNESS[row])

    return oklch_to_hex(l, c, h)


def generate_nes_palette():
    base_colors = get_base_colors()
    palette = []

    print("Generating palette colors...")
    for row in range(4):
        for col in range(16):
            color = base_colors.get(col, "#000000")
            final_color = apply_filter(color, row)
            palette.append(final_color)

    return palette
