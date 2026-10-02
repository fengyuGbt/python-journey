import json

from ledger import add_record, filter_by_category, list_records, total_amount

DATA_FILE = "ledger.json"

def load_records():
    """启动时加载：文件存在就读，不存在就返回空列表"""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_records(records):
    """每次变更后保存"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False)

# add_record / list_records / total_amount / filter_by_category 照抄你的 ledger.py

def main():
    records = load_records()          # ← 1. 启动时加载，不再 = []
    while True:
        input_str = input("Enter command (add/list/total/by/exit): ")
        if input_str == "exit":
            break
        parts = input_str.split(maxsplit=3)
        if parts[0] == "add":
            if len(parts) < 3:
                print("Usage: add <amount> <category> <note>")
                continue
            try:
                amount = float(parts[1])
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                continue
            category = parts[2]
            note = parts[3] if len(parts) > 3 else ""                        # ← 2. 校验照旧
            add_record(records, amount, category, note)
            save_records(records)      # ← 3. 一变更一保存
        elif parts[0] == "list":
            list_records(records)
        elif parts[0] == "total":
            print(f"Total amount: {total_amount(records)}")
        elif parts[0] == "by":
            if len(parts) < 2:
                print("Usage: by <category>")
                continue
            if not parts[1]:
                print("Please specify a category.")
                continue
            filter_by_category(records, parts[1])   
        else:
            print("Unknown command. Please use add/list/total/by/exit.")            

if __name__ == "__main__":
    main()
