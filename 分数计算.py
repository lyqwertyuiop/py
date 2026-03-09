# 分数计算.py

#导入

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
    common = gcd(son, mom)
    son /= common
    mom /= common
    one_fen = [son, mom]
    return one_fen

#计算
class know:
    def __init__(self):
        pass
    
    def add(self, son1, mom1, son2, mom2):
        now_fen = tong(son1, mom1, son2, mom2)
        new_fen = [now_fen[0]+now_fen[1], now_fen[2]]
        return yue(new_fen[0], new_fen[1])
    
    def sub(self, son1, mom1, son2, mom2):
        now_fen = tong(son1, mom1, son2, mom2)
        new_fen = [now_fen[0]-now_fen[1], now_fen[2]]
        return yue(new_fen[0], new_fen[1])
    
    def mul(self, son1, mom1, son2, mom2):
        new_fen = [son1*son2, mom1*mom2]
        return yue(new_fen[0], new_fen[1])
    
    def div(self, son1, mom1, son2, mom2):
        new_fen = [son1*mom2, mom1*son2]
        return yue(new_fen[0], new_fen[1])
    
        

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
#输出列表
#每个列表每个元素都是一个中间的结果，如：1/2 + 1/2 + 1/2，则这个3个列表为:[1,1][0,1][0,2]
zn = []
sn = []
mn = []

#计算与推进
if time == 1:
    # 如果只有一个分数，直接输出
    zn.append(y[0])
    sn.append(s[0])
    mn.append(m[0])
else:
    for i in range(time-1):
        what = input(f"请输入第{i+1}个符号（加1、减2、乘3、除4、退出0）：")

        if what == '0':
            print("退出程序！")
            break

        #这里因为列表无法修改元素的同时删除元素，所以只能新建一个列表来存储每步运算的结果
        '''
        计算步骤
        1.先把整数部分转化为分数部分
        2.通分
        3.计算
        4.约分（如果分子>分母则转化为带分数）
        '''

        #1
        for j in range(time):
            s[j] += y[j]*m[j]
            y[j] = 0
        
        #2-4
        if i == 0:
            if what == '1':
                now_fen = tong(s[i], m[i], s[i+1], m[i+1])
                new_fen = [now_fen[0]+now_fen[1], now_fen[2]]
                new_fen = yue(new_fen[0], new_fen[1])
                zn.append(int(new_fen[0]//new_fen[1]))
                sn.append(int(new_fen[0]%new_fen[1]))
                mn.append(int(new_fen[1]))
            elif what == '2':
                now_fen = tong(s[i], m[i], s[i+1], m[i+1])
                new_fen = [now_fen[0]-now_fen[1], now_fen[2]]
                new_fen = yue(new_fen[0], new_fen[1])
                zn.append(int(new_fen[0]//new_fen[1]))
                sn.append(int(new_fen[0]%new_fen[1]))
                mn.append(int(new_fen[1]))
            elif what == '3':
                new_fen = [s[i]*s[i+1], m[i]*m[i+1]]
                new_fen = yue(new_fen[0], new_fen[1])
                zn.append(int(new_fen[0]//new_fen[1]))
                sn.append(int(new_fen[0]%new_fen[1]))
                mn.append(int(new_fen[1]))
            elif what == '4':
                new_fen = [s[i]*m[i+1], m[i]*s[i+1]]
                new_fen = yue(new_fen[0], new_fen[1])
                zn.append(int(new_fen[0]//new_fen[1]))
                sn.append(int(new_fen[0]%new_fen[1]))
                mn.append(int(new_fen[1]))
            else:
                print("输入错误，请重新输入！")
        else:
            current_son = zn[i-1] * mn[i-1] + sn[i-1]
            if what == '1':
                now_fen = tong(current_son, mn[i-1], s[i+1], m[i+1])
                new_fen = [now_fen[0]+now_fen[1], now_fen[2]]
                new_fen = yue(new_fen[0], new_fen[1])
                zn.append(int(new_fen[0]//new_fen[1]))
                sn.append(int(new_fen[0]%new_fen[1]))
                mn.append(int(new_fen[1]))
            elif what == '2':
                now_fen = tong(current_son, mn[i-1], s[i+1], m[i+1])
                new_fen = [now_fen[0]-now_fen[1], now_fen[2]]
                new_fen = yue(new_fen[0], new_fen[1])
                zn.append(int(new_fen[0]//new_fen[1]))
                sn.append(int(new_fen[0]%new_fen[1]))
                mn.append(int(new_fen[1]))
            elif what == '3':
                new_fen = [current_son * s[i+1], mn[i-1] * m[i+1]]
                new_fen = yue(new_fen[0], new_fen[1])
                zn.append(int(new_fen[0]//new_fen[1]))
                sn.append(int(new_fen[0]%new_fen[1]))
                mn.append(int(new_fen[1]))
            elif what == '4':
                new_fen = [current_son * m[i+1], mn[i-1] * s[i+1]]
                new_fen = yue(new_fen[0], new_fen[1])
                zn.append(int(new_fen[0]//new_fen[1]))
                sn.append(int(new_fen[0]%new_fen[1]))
                mn.append(int(new_fen[1]))
            else:
                print("输入错误，请重新输入！")
            

        




#输出结果
print(f"结果：{zn[-1]} {sn[-1]}/{mn[-1]}")



'''
File: 分数计算.py
Author: LY
Date: 2026-03-08 16:51
LastEditTime: 2026-03-08 17:21
LastEditors: LY
Description: 分数计算器

'''