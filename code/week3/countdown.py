from datetime import date

while True:
    user_input = input("请输入一个日期（格式：YYYY-MM-DD），或输入 'exit' 退出: ")
    if user_input.lower() == 'exit':
        print("程序已退出。")
        break
    try:
        target_date = date.fromisoformat(user_input)
        today = date.today()
        if target_date < today:
            print("输入的日期已经过去了，请输入一个未来的日期。")
            continue
        if target_date == today:
            print("输入的日期就是今天！")
            continue
        delta = target_date - today
        print(f"距离 {target_date} 还有 {delta.days} 天。")
    except ValueError:
        print("输入的日期格式不正确，请使用 YYYY-MM-DD 格式。")
