import json

def save_json(path, data):
    ...  # with + encoding="utf-8" + ensure_ascii=False（016 坑：dump 管转义、open 管编码）
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

def load_json(path):
    ...  # with + encoding="utf-8" + json.load
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
# 验收：save_json("data.json", {"name": "爱丽丝"}); load_json("data.json")
#       → {'name': '爱丽丝'}（且 cat data.json 中文无转义）
save_json("data.json", {"name": "爱丽丝"})
print(load_json("data.json"))
