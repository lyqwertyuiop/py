# 分数计算.py

#导入
import re

#公倍数捆绑包
#最大公约数
def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m
#最小公倍数
def lcm(m, n):
    return m * n // gcd(m, n)

#求一些分数分母的最小公倍数
def anl(mom,long_,now,num_now):
    if(now == long_):
        return num_now
    num_now = lcm(num_now,mom[now])
    return anl(mom,long_,now+1,num_now)

#通分
def tong(son1, mom1,son2, mom2):
    num = lcm(mom1, mom2)
    son1 *= num // mom1
    son2 *= num // mom2
    one_fen = [son1, son2, num]
    return one_fen
        

#约分
def yue(son, mom):
    common = gcd(abs(son), mom)
    son //= common
    mom //= common
    one_fen = [son, mom]
    return one_fen

#分数类
class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("分母不能为0")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        common = gcd(abs(self.numerator), self.denominator)
        self.numerator //= common
        self.denominator //= common
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        num = lcm(self.denominator, other.denominator)
        new_num = self.numerator * (num // self.denominator) + other.numerator * (num // other.denominator)
        return Fraction(new_num, num)

    def __sub__(self, other):
        num = lcm(self.denominator, other.denominator)
        new_num = self.numerator * (num // self.denominator) - other.numerator * (num // other.denominator)
        return Fraction(new_num, num)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("除数不能为0")
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

#表达式解析
def evaluate_expression(expression):
    # 移除空格
    expression = expression.replace(" ", "")
    
    # 分割数字和运算符
    tokens = re.findall(r'\d+/\d+|\d+|[+\-*/]', expression)
    
    # 转换为分数
    def to_fraction(token):
        if '/' in token:
            num, den = map(int, token.split('/'))
            return Fraction(num, den)
        else:
            return Fraction(int(token))
    
    # 运算符优先级
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    # 两个栈
    values = []
    ops = []
    
    i = 0
    while i < len(tokens):
        if tokens[i] not in ['+', '-', '*', '/']:
            values.append(to_fraction(tokens[i]))
        elif tokens[i] == '-' and (i == 0 or tokens[i-1] in ['+', '-', '*', '/']):
            # 处理负数
            i += 1
            if i < len(tokens):
                values.append(Fraction(-int(tokens[i])))
        else:
            while ops and precedence.get(ops[-1], 0) >= precedence.get(tokens[i], 0):
                op = ops.pop()
                b = values.pop()
                a = values.pop()
                if op == '+':
                    values.append(a + b)
                elif op == '-':
                    values.append(a - b)
                elif op == '*':
                    values.append(a * b)
                elif op == '/':
                    values.append(a / b)
            ops.append(tokens[i])
        i += 1
    
    while ops:
        op = ops.pop()
        b = values.pop()
        a = values.pop()
        if op == '+':
            values.append(a + b)
        elif op == '-':
            values.append(a - b)
        elif op == '*':
            values.append(a * b)
        elif op == '/':
            values.append(a / b)
    
    return values[0]

#使用
#输入表达式
expr = input("请输入分数表达式（例如：1/2 + 3/4 * 5/6）：")
try:
    result = evaluate_expression(expr)
    print(f"结果：{result}")
except Exception as e:
    print(f"错误：{e}")



