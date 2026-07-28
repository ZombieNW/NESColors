from color_convert import hex_to_rgb
from palette import generate_nes_palette


def export_pal_file(palette, output_filename):
    pal_data = bytearray()

    for hex_color in palette:
        r, g, b = hex_to_rgb(hex_color)
        pal_data.append(r)
        pal_data.append(g)
        pal_data.append(b)

    with open(output_filename, "wb") as f:
        f.write(pal_data)


def main():
    palette = generate_nes_palette()
    export_pal_file(palette, "palette.pal")


if __name__ == "__main__":
    main()
