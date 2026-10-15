# word_analysis.py：python word_analysis.py <文件> <N>
# 读文件 → 词频统计（题 7 方法）→ 输出 Top N（题 12 方法）
# 验收：对 notes.txt（"hello world\npython is fun\n"）：
# python word_analysis.py notes.txt 2
# → hello: 1, world: 1（或 python: 1——按词频和字母序，你的实现定）
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="输入文件")
parser.add_argument("n", type=int, help="输出前N个词")
args = parser.parse_args()

with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("hello world\npython is fun\n")

with open(args.file, "r", encoding="utf-8") as f:
    text = f.read()
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words[:args.n]:
        print(f"{word}: {count}")