def parse_command(cmd: str) -> list:
    """解析命令行，返回动作和参数列表"""
    return cmd.split(maxsplit=3)

def handle(cmd: str) -> str:
    parts = parse_command(cmd)
    if not parts:
        return "no command provided"
    if parts[0] == "add":
        if len(parts) < 4:
            return "Usage: add <amount> <category> <note>"
        amount, category, note = parts[1], parts[2], parts[3]
        return f"added {amount} to {category}: {note}"
    elif parts[0] == "by":
        if len(parts) < 2:          # ← 坑 A
            return "Usage: by <category>"
        category = parts[1]            # ← 坑 B（复制残留）
        return f"filtering by {category}"
    else:
        return "unknown command"

if __name__ == "__main__":
    for cmd in ["add 30 餐饮 午饭", "by", "by 餐饮", "add abc", ""]:
        print(f"{cmd!r:>20} -> {handle(cmd)}")