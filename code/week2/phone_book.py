# Phone book CLI - L2 Day 1
# Final clean version: add/query/delete/list with no scaffolding comments.
# See lessons/010 for the "clean code" habit (no leftover hints, no commented-out code).
phone_book = {}

while True:
    command = input("a-添加 q-查询 d-删除 l-列出 e-退出: ")
    if command == "a":
        name = input("名字: ")
        number = input("电话: ")
        phone_book[name] = number
    elif command == "q":
        name = input("查谁: ")
        print(phone_book.get(name, "查无此人"))
    elif command == "d":
        name = input("删谁: ")
        if phone_book.pop(name, None) is None:
            print("查无此人")
        else:
            print(f"{name} 已删除")
    elif command == "l":
        for name, number in phone_book.items():
            print(f"{name}: {number}")
    elif command == "e":
        break
    else:
        print("无效命令")
