# daily_commit.py
import os
from datetime import datetime
import random

FILENAME = "log.txt"

def make_commit():
    now = datetime.now()
    with open(FILENAME, "a") as file:
        file.write(f"Commit at {now}\n")
    os.system("git add .")
    os.system(f"git commit -m 'Daily commit: {now.strftime('%Y-%m-%d %H:%M:%S')}'")
    os.system("git push")

if __name__ == "__main__":
    make_commit()
