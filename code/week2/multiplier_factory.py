# Multiplier factory closure - L2 Day 4
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_2 = make_multiplier(2)
times_3 = make_multiplier(3)
times_10 = make_multiplier(10)
print(times_2(5))    # 10
print(times_3(4))    # 12
print(times_10(7))   # 70
