import time

from color_convert import hex_to_rgb
from html_preview import export_html_file
from palette import generate_nes_palette


def export_pal_file(palette, output_filename):
    print(f"Generating {output_filename}...")
    pal_data = bytearray()

    for hex_color in palette:
        r, g, b = hex_to_rgb(hex_color)
        pal_data.append(r)
        pal_data.append(g)
        pal_data.append(b)

    with open(output_filename, "wb") as f:
        f.write(pal_data)


def main():
    start_time = time.perf_counter()

    palette = generate_nes_palette()
    export_pal_file(palette, "palette.pal")
    export_html_file(palette, "preview.html")

    end_time = time.perf_counter()

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print("Done!")


if __name__ == "__main__":
    main()
