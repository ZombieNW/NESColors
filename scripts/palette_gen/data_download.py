import os
import subprocess

from dotenv import load_dotenv

load_dotenv()

remote_path = os.getenv("REMOTE_DB_PATH")


def download_data():
    if remote_path:
        subprocess.run(["scp", remote_path, "colors.db"], check=True)
