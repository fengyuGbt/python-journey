# 造数据：python -c "open('data.txt','w').write('1\n2\n3\nabc\n4\n')"
def sum_numbers(path):
    ...  # 读每行转 int，坏行跳过（try/except），返回总和
    total = 0
    with open(path, 'r') as f:
        for line in f:
            try:
                total += int(line.strip())
            except ValueError:
                continue
    return total        
# 验收：sum_numbers("data.txt") → 10
print(sum_numbers("data.txt"))
