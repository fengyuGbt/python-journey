# nonlocal counter closure - L2 Day 4
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

p = make_counter()
print(p())   # 1
print(p())   # 2
print(p())   # 3

q = make_counter()
print(q())   # 1 — new instance, independent state
print(p())   # 4 — p continues where it left off
