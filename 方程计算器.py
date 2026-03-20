# 方程计算器
# 支持：
# 1) 线性方程 ax + b = 0
# 2) 二次方程 ax^2 + bx + c = 0
# 3) 通用方程（需要 sympy 库，可输入像 2*x+3=7 这样的方程）

import math

try:
    from sympy import symbols, Eq, solve
    has_sympy = True
except ImportError:
    has_sympy = False


def solve_linear():
    print("解一元一次方程 ax + b = 0")
    a = float(input("请输入 a = ").strip())
    b = float(input("请输入 b = ").strip())
    if a == 0:
        if b == 0:
            print("有无穷多解")
        else:
            print("无解")
    else:
        x = -b / a
        print(f"解: x = {x}")


def solve_quadratic():
    print("解一元二次方程 ax^2 + bx + c = 0")
    a = float(input("请输入 a = ").strip())
    b = float(input("请输入 b = ").strip())
    c = float(input("请输入 c = ").strip())
    if a == 0:
        print("a = 0，退化为线性方程")
        if b == 0:
            if c == 0:
                print("有无穷多解")
            else:
                print("无解")
        else:
            x = -c / b
            print(f"线性解: x = {x}")
        return
    d = b * b - 4 * a * c
    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2 * a)
        r2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"两个实根: x1 = {r1}, x2 = {r2}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"重根: x = {x}")
    else:
        re = -b / (2 * a)
        im = math.sqrt(-d) / (2 * a)
        print(f"两个复根: x1 = {re}+{im}j, x2 = {re}-{im}j")


def solve_general():
    if not has_sympy:
        print("未安装 sympy，无法使用通用方程求解。请安装 sympy（pip install sympy）后重试。")
        return
    eq_str = input("请输入方程（例如 2*x+3=7 或 x**2-4*x+3=0）: ")
    x = symbols('x')
    try:
        left, right = eq_str.split('=')
        eq = Eq(eval(left, {}, {'x': x}), eval(right, {}, {'x': x}))
        sol = solve(eq, x)
        print(f"求解结果: {sol}")
    except Exception as e:
        print("解析方程时出错，请检查输入格式。", e)


def main():
    print("=== 方程计算器 v1.0 ===")
    while True:
        print("\n请选择功能:")
        print("1. 线性方程 ax + b = 0")
        print("2. 二次方程 ax^2 + bx + c = 0")
        print("3. 通用方程（需要 sympy）")
        print("4. 退出")
        choice = input("> ").strip()
        if choice == '1':
            solve_linear()
        elif choice == '2':
            solve_quadratic()
        elif choice == '3':
            solve_general()
        elif choice == '4':
            print("再见！")
            break
        else:
            print("无效选项，请重新输入。")


if __name__ == '__main__':
    main()