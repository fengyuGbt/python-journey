# 造数据：python -c "open('scores.txt','w').write('Alice,85\nBob,92\nbad line\nCara,76\n')"
def read_scores(path):
    ...  # 每行 "name,score"（split(",")），坏行跳过，返回 {"name": score}
    scores = {}
    with open(path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 2:
                name, score = parts
                try:
                    scores[name] = int(score)
                except ValueError:
                    continue
    return scores
# 验收：read_scores("scores.txt") → {'Alice': 85, 'Bob': 92, 'Cara': 76}
print(read_scores("scores.txt"))
