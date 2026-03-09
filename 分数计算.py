# 分数计算.py

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
def tong(son, mom):
        long_num = len(son)
        all_num_lcm = anl(mom,long_num,0,1)
        
        for i in range(long_num):
            mom[i] = all_num_lcm
            son[i] = son[i] * (all_num_lcm // mom[i])

#约分
def yue(son, mom):
    common = gcd(son, mom)
    son /= common
    mom /= common
    one_fen = [son, mom]
    return one_fen

#计算
class know:
    def __init__(self):
        pass
    
    def add(self, son, mom):
        tong(son, mom)
        sum_son = 0
        for i in range(len(son)):
            sum_son += son[i]
        return yue(sum_son, mom[0])

    def sub(self, son, mom):
        tong(son, mom)
        sum_son = 0
        for i in range(len(son)):
            sum_son -= son[i]
        return yue(sum_son, mom[0])

    def mul(self, son, mom):
        sum_son = 1
        sum_mom = 1
        for i in range(len(son)):
            sum_son *= son[i]
            sum_mom *= mom[i]
        return yue(sum_son, sum_mom)

    def div(self, son, mom):
        sum_son = 1
        sum_mom = 1
        for i in range(len(son)):
            sum_son *= son[i]
            sum_mom *= mom[i]
        return yue(sum_son, sum_mom)

#使用
#输入
#分数输入法 整数 分子 分母 （换行）
y = []
s = []
m = []
time = int(input("请输入分数的个数："))
for i in range(time):
    y.append(int(input(f"请输入第{i+1}个分数的整数部分：")))
    s.append(int(input(f"请输入第{i+1}个分数的分子：")))
    m.append(int(input(f"请输入第{i+1}个分数的分母：")))
    print(f"第{i+1}个分数：{y[i]} {s[i]}/{m[i]}\n")
#需求
what = input("请输入需要进行的运算（加1、减2、乘3、除4、退出0）：")
    
k = know()
if what == "1":
    result = k.add(s, m)
    print(f"结果：{result[0]}/{result[1]}\n")
elif what == "2":
    result = k.sub(s, m)
    print(f"结果：{result[0]}/{result[1]}\n")
elif what == "3":
    result = k.mul(s, m)
    print(f"结果：{result[0]}/{result[1]}\n")
elif what == "4":
    result = k.div(s, m)
    print(f"结果：{result[0]}/{result[1]}\n")
elif what == "0":
    print("退出程序。\n")
    exit()
else:
    print("无效的输入，请重新输入。\n")
    
        
       



'''
File: 分数计算.py
Author: LY
Date: 2026-03-08 16:51
LastEditTime: 2026-03-08 17:21
LastEditors: LY
Description: 分数计算器

'''