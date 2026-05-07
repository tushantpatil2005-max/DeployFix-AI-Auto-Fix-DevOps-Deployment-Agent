import json
from rich.console import Console

console = Console()


def save_json(data, path="output/sample_fix.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def pretty_print(data):
    console.print(data)