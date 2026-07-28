import sqlite3
from collections import defaultdict

from color_convert import hex_to_rgb, rgb_to_hex
from data_download import download_data

DB_PATH = "colors.db"
TABLE_NAME = "colors"


def fetch_prompt_values(db_path, table_name):
    download_data()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT prompt, value FROM {table_name}")

    count = 0
    prompt_values = defaultdict(list)
    for prompt, value in cursor.fetchall():
        count += 1
        prompt_values[prompt].append(value)

    print(f"{count} total submissions processed")
    conn.close()
    return prompt_values


def average_hex_per_prompt(prompt_values):
    averages = {}
    for prompt, hex_values in prompt_values.items():
        rgb_values = [hex_to_rgb(v) for v in hex_values]

        r_avg = round(sum(r for r, g, b in rgb_values) / len(rgb_values))
        g_avg = round(sum(g for r, g, b in rgb_values) / len(rgb_values))
        b_avg = round(sum(b for r, g, b in rgb_values) / len(rgb_values))

        averages[prompt] = rgb_to_hex(r_avg, g_avg, b_avg)

    return averages


def main():
    prompt_values = fetch_prompt_values(DB_PATH, TABLE_NAME)
    averages = average_hex_per_prompt(prompt_values)

    # display values
    for prompt, avg_hex in sorted(averages.items()):
        count = len(prompt_values[prompt])
        print(f"{prompt:10s} n={count:3d}  {avg_hex}")


if __name__ == "__main__":
    main()
