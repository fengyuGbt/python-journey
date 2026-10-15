def word_count_file(path):
    ...  # 一个 with 一个循环，返回 (行数, 单词总数)
    line_count = 0
    word_count = 0
    with open(path, 'r') as f:
        for line in f:
            line_count += 1
            word_count += len(line.split())
        return (line_count, word_count)
# 验收（造数据：python -c "open('notes.txt','w').write('hello world\npython is fun\n')"）：
# word_count_file("notes.txt") → (2, 5)
print(word_count_file("notes.txt"))
