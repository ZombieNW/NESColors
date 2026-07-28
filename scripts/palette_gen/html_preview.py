from color_convert import hex_to_rgb


def get_text_color(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return "#000" if luminance > 0.5 else "#fff"


def export_html_file(palette, output_filename):
    print(f"Generating {output_filename}...")

    html_rows = []
    for row_idx in range(0, len(palette), 16):
        row_colors = palette[row_idx : row_idx + 16]
        cells = []
        for color in row_colors:
            text_color = get_text_color(color)
            cell = f'            <td style="background-color: {color}; color: {text_color};">{color}</td>'
            cells.append(cell)

        html_rows.append("        <tr>\n" + "\n".join(cells) + "\n        </tr>")

    table_body = "\n".join(html_rows)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color Table</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }}
        table {{
            border-collapse: collapse;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #ffffff;
        }}
        td {{
            width: 60px;
            height: 60px;
            text-align: center;
            vertical-align: middle;
            font-size: 10px;
            font-family: monospace;
            padding: 4px;
        }}
    </style>
</head>
<body>

    <table>
{table_body}
    </table>

</body>
</html>
"""

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_content)
