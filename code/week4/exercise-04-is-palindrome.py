def is_palindrome(s):
    ...  # 忽略大小写和空格
    s = s.replace(" ", "").lower()
    return s == s[::-1]
# 验收：is_palindrome("A man a plan a canal Panama") → True
#       is_palindrome("hello") → False
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))
