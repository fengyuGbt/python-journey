with open("squares.txt","w", encoding="utf-8") as file:
    for i in range(1, 101):
        file.write(f"{i**2}\n")