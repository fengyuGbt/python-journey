from pathlib import Path
import shutil

src = Path("messy2")
files = [f for f in src.iterdir() if f.is_file()]   # 快照：先收清单（目录被 is_file 过滤）

for file in files:                                   # 处理：随便 mkdir / move
    dst = src / "归档"
    dst.mkdir(exist_ok=True)
    shutil.move(file, dst / file.name)
