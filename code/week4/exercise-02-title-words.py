def title_words(text):
    words = text.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return " ".join(words)
# 验收：title_words("hello world") → "Hello World"

if __name__ == "__main__":
    text = "hello world"
    print(title_words(text))
    print(text)
