def add_record(records: list, amount: float, category: str, note: str) -> None:
    """
    添加一条记录到 records 列表中，记录包含金额、类别和备注
    """
    records.append({"amount": amount, "category": category, "note": note})


def list_records(records: list) -> None:
    """
    列出所有记录
    """
    for record in records:
        print(
            f"Amount: {record['amount']}, Category: {record['category']}, Note: {record['note']}"
        )


def total_amount(records: list) -> float:
    """
    计算所有记录的总金额
    """
    return sum(record["amount"] for record in records)


def filter_by_category(records: list, category: str) -> None:
    """
    根据类别过滤记录
    """
    filtered_records = [record for record in records if record["category"] == category]
    if not filtered_records:
        print(f"No records found for category: {category}")
        return
    for record in filtered_records:
        print(
            f"Amount: {record['amount']}, Category: {record['category']}, Note: {record['note']}"
        )


def main() -> None:
    """主循环：input → split 解析 → 分发 → exit 用 break"""
    records: list = []
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
            note = parts[3] if len(parts) > 3 else ""
            add_record(records, amount, category, note)
        elif parts[0] == "list":
            list_records(records)
        elif parts[0] == "total":
            total = total_amount(records)
            print(f"Total amount: {total}")
        elif parts[0] == "by":
            if len(parts) < 2:
                print("Usage: by <category>")
                continue
            category = parts[1]
            if not category:
                print("Please specify a category.")
                continue
            filter_by_category(records, category)
        else:
            print("Unknown command. Please use add/list/total/by/exit.")


if __name__ == "__main__":
    main()
