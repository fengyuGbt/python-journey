def safe_float(s):
    ...  # 转换成功返回 float，失败返回 None
    try:
        return float(s)
    except (ValueError, TypeError):
        return None 
# 验收：safe_float("3.14") → 3.14；safe_float("abc") → None
print(safe_float("3.14"))
print(safe_float("abc"))
