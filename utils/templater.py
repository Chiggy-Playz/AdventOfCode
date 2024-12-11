from datetime import datetime, timedelta
from os import listdir, mkdir, path
import subprocess
from time import sleep
from typing import Annotated

import requests

from .paths import root_path

try:
    import typer
except ImportError:
    print("You need to have `typer` installed")

app = typer.Typer()


@app.command()
def create(
    day: Annotated[int, typer.Argument(help="Day to create files for")] = 0,
    year: Annotated[int, typer.Option("--y", help="Year folder in which files will be created")] = 0,
    skip_time_check: Annotated[bool, typer.Option(help="Skip time check before next day start.")] = False,
):
    year = year or datetime.now().year
    year_path = root_path / str(year)
    input_folder_path = year_path / "inputs"
    token = None

    if not path.exists(year_path):
        mkdir(year_path)
        mkdir(input_folder_path)

    if day == 0:
        files = listdir(year_path)
        # Find last day
        days = sorted([file for file in files if "day" in file], key=lambda s: int(s.strip("day.py")))
        if not days:
            day = 1
        else:
            day = int(days[-1].strip("day.py")) + 1
            if day == 26:
                print("Uhhhh cya next year!")
                return

    if not skip_time_check:
        now = datetime.now()
        day_unlock_at = datetime(year=year, month=12, day=day, hour=10, minute=30, second=1)
        if now < day_unlock_at:
            td = day_unlock_at - now
            td = timedelta(seconds=td.total_seconds() // 1)
            if td > timedelta(hours=1):
                print("Very far away from start. Exiting...")
                return
            print(f"Day {day} not started yet. Waiting for ", end="")
            while (td.total_seconds() + 1) > 0:
                print(f"Day not started yet. Waiting for {td}", end="\r")
                td = td - timedelta(seconds=1)
                sleep(1)
            print("\nDownloading...")

    day_path = year_path / f"day{day:02}.py"
    input_folder_path = year_path / "inputs"
    input_path = input_folder_path / f"day{day:02}.txt"
    input_test_path = input_folder_path / f"day{day:02}.test.txt"

    with open(root_path / "utils/template.py") as f:
        template_code = f.read()

    if path.exists(root_path / "utils/token"):
        with open(root_path / "utils/token") as f:
            token = f.read()

    if not path.exists(day_path):
        with open(day_path, "w") as f:
            f.write(template_code)
    else:
        print("Skipping template creation")

    if token is None:
        return

    response = requests.get(url=f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": token})
    if not response.ok:
        print("Couldn't fetch input...")
        return

    with open(input_path, "w") as file:
        file.write(response.text)
    open(input_test_path, "a").close()

    print("Done!")
    subprocess.run(["code", "-r", str(day_path)], shell=True)
    subprocess.run(["code", "-r", str(input_test_path)], shell=True)


if __name__ == "__main__":
    app()
