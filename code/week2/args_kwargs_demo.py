# *args and **kwargs - L2 Day 3
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

def build_query(**kwargs):
    query = {k: v for k, v in kwargs.items() if v is not None}
    result = ""
    for key, value in query.items():
        result += f"{key}={value}&"
    return result.rstrip("&")

print(sum_all(1, 2, 3, 4, 5))          # 15
print(build_query(name="Alice", age=30))  # name=Alice&age=30
