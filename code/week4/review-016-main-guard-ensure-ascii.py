import json

def save_data(data):
    with open("people.json", "w", encoding="utf-8") as f:   # ← 坑 B：ensure_ascii 不是 open 的参数！
        json.dump(data, f,ensure_ascii=False)

def load_data():
    with open("people.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    data = [{"name": "爱丽丝", "age": 30}, {"name": "鲍勃", "age": 25}]
    save_data(data)
    print(load_data())

if __name__ == "__main__":
    main()