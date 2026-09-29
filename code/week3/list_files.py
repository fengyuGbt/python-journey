from pathlib import Path

p = Path("~/learning").expanduser()
p.exists()
for file in p.iterdir():
    if file.suffix == ".py":
        print(file.name)