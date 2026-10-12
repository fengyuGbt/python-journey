import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--dir", default=".", help="Directory to search for files")
parser.add_argument("--prefix", default="file", help="File prefix to search for")
parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without renaming files")

args = parser.parse_args()
p = Path(args.dir).expanduser()
if not p.is_dir():
    print(f"Error: {args.dir} is not a valid directory.")
    exit(1)
for i, file in enumerate(sorted(p.iterdir()),start=1):
    if not file.is_file():
        continue
    newname = f"{args.prefix}_{i}{file.suffix}"
    if args.dry_run:
        print(f"Dry run: {file.name} would be renamed to {newname}")
    else:
        file.rename(file.with_name(newname))
        print(f"Renamed {file.name} to {newname}")