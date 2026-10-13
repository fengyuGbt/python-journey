import argparse
from pathlib import Path
import shutil
import logging

CATEGORIES = {
"图片": {".jpg", ".png", ".gif", ".webp"},
"文档": {".pdf", ".docx", ".txt", ".md"},
"压缩包": {".zip", ".tar", ".gz"},
"代码": {".py", ".js", ".html",".css"},
}

def classify(file):
    for category, extensions in CATEGORIES.items():
        if file.suffix in extensions:
            return category
    return "其他"

def move_files(file,dst,dry_run=False):
    try:
        if dry_run:
            print(f"Dry run: {file.name} would be moved to {dst/file.name}")
        else:
            target = dst / file.name
            if target.exists():
                target = dst / f"{file.stem}_{file.suffix.lstrip('.')}{file.suffix}"
                logging.warning(f"{file.name} already exists, renaming to {target.name}")
            shutil.move(file, target)
            logging.info(f"Moved {file.name} -> {target}")
    except Exception as e:
        logging.error(f"Error moving file {file.name}: {e}")
        print(f"Error moving file {file.name}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default=".", help="Directory to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview without moving files")
    parser.add_argument("--log", help="Log file path.")
    args = parser.parse_args()

    src = Path(args.dir).expanduser()
    
    if not src.is_dir():
        print(f"Error: {src} is not a valid directory.")   
        exit(1)

    if args.log:
        logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.FileHandler(args.log, mode="w", encoding="utf-8"), logging.StreamHandler()],
    )

    files = [f for f in src.iterdir() if f.is_file()]   # 快照：只收文件，收完遍历就结束

    for file in files:                                   # 处理阶段：随便 mkdir / move
        dst = src / classify(file)
        dst.mkdir(exist_ok=True)
        move_files(file, dst, args.dry_run)


