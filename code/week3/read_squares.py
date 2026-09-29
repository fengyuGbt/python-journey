with open("squares.txt","r",encoding="utf8") as f:
    total = 0
    count = 0
    for line in f:
        total += int(line.strip())
        count += 1
print(total)
print(count)