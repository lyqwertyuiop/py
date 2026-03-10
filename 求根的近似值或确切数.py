number = float(input("请输入一个数："))
gen = int(input("请输入一个整数（根的次数）："))
if gen <= 1:
    print("根的次数必须大于1")
    exit(0)
if number < 0 and gen % 2 == 0:
    print("负数的偶次根不存在")
    exit(0)

# 使用牛顿法求根
guess = abs(number) ** (1 / gen)  # 初始猜测
epsilon = 1e-10
max_iter = 1000
for _ in range(max_iter):
    f = guess ** gen - abs(number)
    f_prime = gen * guess ** (gen - 1)
    if abs(f_prime) < epsilon:
        break
    new_guess = guess - f / f_prime
    print(f"相邻两个数：{guess}, {new_guess}")  # 添加打印相邻两个数
    if abs(new_guess - guess) < epsilon:
        break
    guess = new_guess

# 检查是否为确切数
if abs(guess ** gen - abs(number)) < epsilon:
    # 计算确切根
    exact_root = round(guess)
    if abs(exact_root ** gen - abs(number)) < epsilon:
        if number < 0:
            exact_root = -exact_root
        print(f"确切结果：{exact_root}")
    else:
        if number < 0:
            guess = -guess
        print(f"近似结果：{guess}")
else:
    if number < 0:
        guess = -guess
    print(f"近似结果：{guess}")
