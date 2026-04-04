# 方程组计算器
# 功能：
# 1) 线性方程组（手工求解或借助 sympy）
# 2) 通用方程组（非线性，必须安装 sympy）
# 3) 支持变量名自定义

import math

try:
    from sympy import symbols, Eq, solve
    has_sympy = True
except ImportError:
    has_sympy = False


def solve_linear_system_manual(var_names, coeffs, constants):
    # Gauss 消元（浮点）
    n = len(var_names)
    A = [row[:] for row in coeffs]
    b = constants[:]

    for i in range(n):
        # 找到主元
        pivot = i
        while pivot < n and abs(A[pivot][i]) < 1e-12:
            pivot += 1
        if pivot == n:
            continue
        if pivot != i:
            A[i], A[pivot] = A[pivot], A[i]
            b[i], b[pivot] = b[pivot], b[i]

        # 归一化
        pivot_val = A[i][i]
        if abs(pivot_val) < 1e-12:
            continue
        for j in range(i, n):
            A[i][j] /= pivot_val
        b[i] /= pivot_val

        for k in range(n):
            if k == i:
                continue
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            b[k] -= factor * b[i]

    # 检查无解/多解
    for i in range(n):
        if all(abs(A[i][j]) < 1e-9 for j in range(n)) and abs(b[i]) > 1e-9:
            return None, '无解'

    rank = sum(1 for i in range(n) if any(abs(A[i][j]) > 1e-9 for j in range(n)))
    if rank < n:
        return None, '有无穷多解或参数解，请使用 SymPy 进一步分析'

    sol = {var_names[i]: b[i] for i in range(n)}
    return sol, None


def solve_linear_system():
    print('=== 线性方程组求解 ===')
    n = int(input('请输入未知数个数 n (例如 2): ').strip())
    var_input = input('请输入变量名（用空格分隔，留空则自动 x1 x2 ...）: ').strip()
    if var_input == '':
        var_names = [f'x{i+1}' for i in range(n)]
    else:
        var_names = var_input.split()
        if len(var_names) != n:
            print('变量名数与 n 不匹配，已退出。')
            return

    print('请逐个输入方程，例如 2*x1 + 3*x2 = 5')
    eqs = []
    for i in range(n):
        eqs.append(input(f'第 {i+1} 个方程: ').strip())

    if has_sympy:
        try:
            syms = symbols(' '.join(var_names))
            eq_list = []
            for eq in eqs:
                if '=' not in eq:
                    raise ValueError('方程需要包含 =')
                left, right = eq.split('=')
                local_vars = {name: sym for name, sym in zip(var_names, syms)}
                eq_list.append(Eq(eval(left, {}, local_vars), eval(right, {}, local_vars)))
            sol = solve(eq_list, syms, dict=True)
            if not sol:
                print('无解或无法解析（空）')
                return
            if len(sol) > 1:
                print('多组解：')
            for solution in sol:
                print({str(k): v for k, v in solution.items()})
            return
        except Exception as e:
            print('SymPy 求解失败，会尝试手工线性求解:', e)

    # 手工求解（仅线性）
    coeffs = []
    constants = []
    for eq in eqs:
        if '=' not in eq:
            print('方程格式错误，必须包含 =')
            return
        left, right = eq.split('=')
        # 解析简单系数
        try:
            rhs = float(eval(right, {}, {}))
        except Exception:
            print('无法解析右侧常数:', right)
            return

        row = [0.0] * n
        # 将左侧表示为系数
        expr = left
        for idx, name in enumerate(var_names):
            expr = expr.replace(name, f'({{var{idx}}})')
        for idx, name in enumerate(var_names):
            # 依次求系数
            try:
                cs = eval(expr.format(**{f'var{idx}': 1.0, **{f'var{j}': 0.0 for j in range(n) if j != idx}}), {}, {})
            except Exception:
                cs = 0.0
            row[idx] = cs
        coeffs.append(row)
        constants.append(rhs)

    sol, err = solve_linear_system_manual(var_names, coeffs, constants)
    if err:
        print(err)
    else:
        print('解：')
        for k, v in sol.items():
            print(f'{k} = {v}')


def solve_general_system():
    if not has_sympy:
        print('未安装 sympy，无法求解通用方程组。请先安装 sympy (pip install sympy)')
        return

    print('=== 通用方程组求解（可非线性/高次） ===')
    var_input = input('请输入变量名，空格分隔（例如 x y z）: ').strip()
    if not var_input:
        print('变量名不能为空。')
        return
    var_names = var_input.split()
    syms = symbols(' '.join(var_names))

    m = int(input('请输入方程数量 m: ').strip())
    eqs = []
    print('请逐个输入方程（例如 x**2 + y - 3 = 0）')
    for i in range(m):
        eq = input(f'方程 {i+1}: ').strip()
        if '=' not in eq:
            print('方程必须包含 =')
            return
        left, right = eq.split('=')
        local_vars = {name: sym for name, sym in zip(var_names, syms)}
        eqs.append(Eq(eval(left, {}, local_vars), eval(right, {}, local_vars)))

    try:
        sol = solve(eqs, syms, dict=True)
        if not sol:
            print('无解或符号解不可用。')
            return
        for idx, s in enumerate(sol, 1):
            print(f'解 #{idx}:', {str(k): v for k, v in s.items()})
    except Exception as e:
        print('求解失败:', e)


def main():
    print('=== 方程组计算器 v1.0 ===')
    while True:
        print('\n请选择功能:')
        print('1. 线性方程组求解')
        print('2. 通用方程组求解（需要 sympy）')
        print('3. 退出')
        choice = input('> ').strip()
        if choice == '1':
            solve_linear_system()
        elif choice == '2':
            solve_general_system()
        elif choice == '3':
            print('再见！')
            break
        else:
            print('无效选项，请重新输入。')


if __name__ == '__main__':
    main()
