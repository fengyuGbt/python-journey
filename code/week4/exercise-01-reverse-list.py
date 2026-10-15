lst = [1, 2, 3, 4, 5]

def reverse_slice(lst):
    return lst[::-1]  # 方法一：切片
def reverse_inplace(lst):
    lst.reverse()  # 方法二：就地 reverse
    return lst
# 验收：两种方法都输出 [5,4,3,2,1]

if __name__ == "__main__":
    print(reverse_inplace(lst))
    print(reverse_slice(lst))
    