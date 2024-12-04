from datetime import datetime
from os import path, mkdir

import requests
from paths import root_path
from typing import Annotated

try:
    import typer
except ImportError:
    print("You need to have `typer` installed")

app = typer.Typer()


@app.command()
def create(
    day: Annotated[int, typer.Argument(help="Day to create files for")],
    year: Annotated[int, typer.Option(help="Year folder in which files will be created")] = 0,
    overwrite: Annotated[bool, typer.Option(help="Overwrite already created files. Dangerous.")] = False,
):
    year = year or datetime.now().year
    token = None

    year_path = root_path / str(year)
    day_path = year_path / f"day{day}.py"
    input_folder_path = year_path / "inputs"
    input_path = input_folder_path / f"day{day}.txt"
    input_test_path = input_folder_path / f"day{day}.test.txt"

    with open(root_path / "utils/template.py") as f:
        template_code = f.read()

    if path.exists(root_path / "utils/token"):
        with open(root_path / "utils/token") as f:
            token = f.read()

    if not path.exists(year_path):
        mkdir(year_path)
        mkdir(input_folder_path)

    for filepath in (day_path, input_path, input_test_path):
        if path.exists(filepath) and not overwrite:
            print(f"{filepath} already exists. Use --overwrite to overwrite existing file")
            return
        # Create the file
        open(filepath, "a").close()

    with open(day_path, "w") as f:
        f.write(template_code)

    if token is None:
        return

    response = requests.get(url=f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": token})
    if not response.ok:
        raise print("Couldn't fetch input")
    with open(input_path, "w") as file:
        file.write(response.text)

    print("Created 3 files!")


if __name__ == "__main__":
    app()
