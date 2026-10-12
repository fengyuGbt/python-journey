import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--dir",default=".", help="Directory to search for Python files")
parser.add_argument("--ext", default=".py", help="File extension to search for")
parser.add_argument("--keyword", default="class", help="Keyword to search for")
args = parser.parse_args()

p = Path(args.dir).expanduser()
ext = args.ext if args.ext.startswith(".") else "." + args.ext
if not p.is_dir():
    print(f"{p} is not a directory")
    exit(1)
EXCLUDE = {".venv", ".git", "__pycache__", "node_modules", ".mypy_cache", ".pytest_cache"}
for file in p.rglob(f"*{ext}"):
    if any(part in EXCLUDE for part in file.parts):
        continue
    try:
        content = file.read_text(errors="ignore")
    except OSError:
        continue
    if args.keyword in content:
        print(file.name)