# 1. **难度选择**：简单（1–50，最多 10 次）/ 中等（1–100，7 次）/ 困难（1–200，5 次）
# 2. **计分**：剩余次数 × 10 分，每局结束显示得分
# 3. **历史记录**：每局结束打印 "本局猜了 N 次"
# 4. **非法输入**：非数字、超出范围 → 提示后重输，**不扣次数、不崩溃**（用 `try/except` + `while`）
# 5. **函数拆分**：至少 3 个函数（如 `choose_difficulty()`、`play_round(secret, max_guesses)`、`main()`）
# 6. **循环玩**：每局结束问 "再来一局？"，输入 `y` 继续

import random


def choose_difficulty() -> tuple[int, int, int]:
    """
    让用户选择难度级别，并返回相应的随机数、上限和最大猜测次数。
    返回：
        tuple: (secret_number, upper_limit, max_guesses)
    """
    while True:
        level = input("请选择难度（1-简单，2-中等，3-困难）：")
        if level == "1":
            return random.randint(1, 50), 50, 10
        elif level == "2":
            return random.randint(1, 100), 100, 7
        elif level == "3":
            return random.randint(1, 200), 200, 5
        else:
            print("无效选择，请输入 1、2 或 3。")


def play_round(secret: int, upper: int, max_guesses: int) -> None:
    """
    进行一轮猜数字游戏。
    参数：
        secret (int): 要猜的数字
        upper (int): 数字的上限
        max_guesses (int): 最大猜测次数
    """
    remaining_guesses = max_guesses
    while remaining_guesses > 0:
        try:
            guess = int(input(f"请输入一个数字（1-{upper}）："))
        except ValueError:
            print("输入无效，请输入一个数字。")
            continue
        if guess < 1 or guess > upper:
            print(f"输入超出范围，请输入一个数字在 1 到 {upper} 之间。")
            continue
        remaining_guesses -= 1
        if guess < secret:
            print("太小了！")
        elif guess > secret:
            print("太大了！")
        else:
            print(f"恭喜你，猜对了！你用了 {max_guesses - remaining_guesses} 次机会。")
            print(f"本局得分：{remaining_guesses * 10} 分")
            return
    print(f"很遗憾，机会用完了。正确答案是 {secret}。")
    print("本局得分：0 分")


def main():
    """
    主函数，控制游戏流程。
    1. 选择难度
    2. 进行猜数字游戏
    3. 游戏结束后询问是否再来一局
    """
    while True:
        secret, upper, guesses = choose_difficulty()
        play_round(secret, upper, guesses)
        if input("再来一局？(y/n)：").lower() != "y":
            break


main()
