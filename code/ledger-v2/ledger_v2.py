import json
import shutil
from datetime import date


def load_records() -> list:
    """Load the ledger from ledger.json, or create it if it doesn't exist."""
    try:
        with open("ledger.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        with open("ledger.json", "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)
        return []
    except json.JSONDecodeError:
        print("Error: ledger.json is corrupted. Creating a backup and starting fresh.")
        shutil.copy("ledger.json", "ledger.json.bak")
        with open("ledger.json", "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)
        return []
def save_records(ledger: list) -> None:
    """Persist the ledger to ledger.json after every change."""
    with open("ledger.json", "w", encoding="utf-8") as f:   # open 管编码（016 坑）
        json.dump(ledger, f, ensure_ascii=False, indent=2)  # dump 管转义；indent 让文件可读
def add(ledger: list, amount: float, category: str, note: str) -> None:
    """Add a new entry to the ledger."""
    today = date.today().isoformat() # noqa: DTZ011  # 本地日期即可，无需时区
    ledger_entry = {"date": today, "amount": amount, "category": category, "note": note}
    ledger_id = max(r["id"] for r in ledger) + 1 if ledger else 1
    ledger_entry["id"] = ledger_id
    ledger.append(ledger_entry)
    save_records(ledger)
def list_entries(ledger: list) -> None:
    """List all entries in the ledger."""
    for entry in ledger:
        print(f"ID: {entry['id']}, Date: {entry['date']}, Amount: {entry['amount']}, Category: {entry['category']}, Note: {entry['note']}")
def by(ledger: list, category: str) -> None:
    """Filter entries by category."""
    filtered_entries = [entry for entry in ledger if entry["category"] == category]
    list_entries(filtered_entries)
def total(ledger: list) -> None:
    """Calculate the total amount of all entries."""
    total_earning = sum(entry["amount"] for entry in ledger if entry["amount"] > 0)
    total_expense = sum(entry["amount"] for entry in ledger if entry["amount"] < 0)
    print(f"Total Earnings: {total_earning}, Total Expenses: {total_expense}, Net Total: {total_earning + total_expense}")
def delete(ledger: list, entry_id: int) -> None:
    """Delete an entry from the ledger by ID."""
    ledger[:] = [entry for entry in ledger if entry["id"] != entry_id]
    save_records(ledger)
def edit(ledger: list, entry_id: int, new_note: str) -> None:
    """Edit an entry in the ledger by ID."""
    for entry in ledger:
        if entry["id"] == entry_id and new_note:
            entry["note"] = new_note   
    save_records(ledger)
def month_str(ledger: list,date:str) -> None:
    """Filter entries by month."""
    filtered_entries = [entry for entry in ledger if entry["date"].startswith(date)]
    if not filtered_entries:
        print(f"No entries found for {date}.")
    else:
        total(filtered_entries)
        print(sum(1 for _ in filtered_entries if _["amount"] > 0), "Earnings and", sum(1 for _ in filtered_entries if _["amount"] < 0), "Expenses.")
def top(ledger: list,category:str) -> None:
    """Show top entries by category."""
    filtered_entries = [e for e in ledger if e["category"]==category]
    if not filtered_entries:
        print(f"No entries found for category '{category}'.")
        return
    total(filtered_entries)
    print(sum(1 for _ in filtered_entries))
def handle_command(cmd: str, ledger: list) -> None:
    parts = cmd.split(maxsplit=3)
    if not parts:
        return
    action = parts[0]
    if action == "add":
        if len(parts)<3:
            print("用法：add <amount> <category> <note>")    
            return
        try:             # parts[1]=金额 parts[2]=分类 parts[3]=备注
            amount = float(parts[1])        # ← 转换放这里（带 try/except）
        except ValueError:
            print("金额无效，用法：add <amount> <category> <note>")
            return
        add(ledger, amount, parts[2], parts[3] if len(parts) > 3 else "")
    elif action == "list":
        list_entries(ledger)
    elif action == "total":
        total(ledger)
    elif action == "by":
        if len(parts) < 2:
            print("用法：by <category>")
            return                # parts[1]=分类
        by(ledger, parts[1])
    elif action == "delete":
        if len(parts) < 2:
            print("用法：delete <id>")
            return
        try:
            entry_id = int(parts[1])
        except ValueError:
            print("ID 无效")
            return            # parts[1]=id
        delete(ledger, entry_id)
    elif action == "edit":              # parts[1]=id parts[2]=新备注
        if len(parts)<3:
            print("用法：edit <id> <新备注>")
            return
        try:
            entry_id=int(parts[1])
        except ValueError:
            print("invalid ID")
            return
        edit(ledger, entry_id, parts[2])
    elif action == "month":             # parts[1]=YYYY-MM
        month_str(ledger, parts[1])
    elif action == "top":               # parts[1]=分类
        top(ledger, parts[1])
    else:
        print("Unknown command")
def main() -> None:
    ledger = load_records()
    while True:
        cmd = input("> ")
        if cmd == "exit":
            break
        try:
            handle_command(cmd, ledger)          # 兜底在这里
        except Exception as e:# noqa: BLE001  # 主循环兜底：任何意外都继续
            print(f"出错：{e}")
if __name__ == "__main__":
    main()
