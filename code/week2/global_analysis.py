# global vs local scope analysis - L2 Day 4
x = 10

def outer():
    x = 20
    def inner():
        return x
    return inner()

def change():
    global x
    x = 99

print(outer())   # 20 — LEGB: inner finds outer's x=20
print(x)         # 10 — global x untouched (so far)
change()         # global declaration: x = 99 writes to the global
print(x)         # 99 — the assignment modified the global
