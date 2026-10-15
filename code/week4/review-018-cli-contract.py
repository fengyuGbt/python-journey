import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--dir", default=".", help="Directory to search")
parser.add_argument("--ext", default="py", help="File extension to search for")
parser.add_argument("--keyword", default="def", help="Keyword to search for")
args = parser.parse_args()

p = Path(args.dir).expanduser()
                     # ← 坑 1：调用不接返回值 = 死代码
if not p.exists():
    print(f"Directory {p} does not exist.")
    exit(1)

args.ext = args.ext if args.ext.startswith(".") else f".{args.ext}"    

for file in p.iterdir(): 
                 # 一层就够，非递归
    if file.suffix != args.ext:              # ← 坑 2：suffix 是 ".py"，args.ext 是 "py"，永远不相等！
        continue                              # ← 坑 3：就算相等，也是"匹配就跳过"——逻辑反了
    try:
        content = file.read_text(errors="ignore")
    except OSError:
        continue
    if args.keyword in content:
        print(file.name)
