def copy_valid_lines(src, dst):
    ...  # 读 src，把"非空且以数字开头"的行写入 dst
    with open(src, 'r') as f_src, open(dst, 'w') as f_dst:
        for line in f_src:
            if line.strip() and line.lstrip()[0].isdigit():
                f_dst.write(line)
# 验收：src 内容 "abc\n123 def\n\n456\nxyz\n" → dst 内容 "123 def\n456\n"
with open('src.txt', 'w') as f:
    f.write("abc\n123 def\n\n456\nxyz\n")
print(copy_valid_lines('src.txt', 'dst.txt'))  # 假设 src.txt 已存在并包含测试内容
