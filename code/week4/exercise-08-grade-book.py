def grade_book(scores):
    ...  # >=90 A, >=80 B, >=70 C, >=60 D, else F
    for k,v in scores.items():
        if v >= 90:
            scores[k] = 'A'
        elif v >= 80:
            scores[k] = 'B'
        elif v >= 70:
            scores[k] = 'C'
        elif v >= 60:
            scores[k] = 'D'
        else:
            scores[k] = 'F'
    return scores
# 验收：grade_book({"Alice": 85, "Bob": 92, "Cara": 76})
#       → {"Alice": "B", "Bob": "A", "Cara": "C"}
print(grade_book({"Alice": 85, "Bob": 92, "Cara": 76}))
