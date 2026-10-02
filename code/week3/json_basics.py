import json

data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
with open("people.json", "w", encoding="utf-8") as file:
    json.dump(data, file,ensure_ascii=False)

with open("people.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print(loaded_data)