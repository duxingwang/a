
34

描述
Lily上课时使用字母数字图片教小朋友们学习英语单词，每次都需要把这些图片按照大小（ASCII码值从小到大）排列收好。请大家给Lily帮忙，通过代码解决。
Lily使用的图片使用字符"A"到"Z"、"a"到"z"、"0"到"9"表示。

数据范围：每组输入的字符串长度满足 1 \le n \le 1000 \1≤n≤1000 

输入描述：
一行，一个字符串，字符串中的每个字符表示一张Lily使用的图片。

输出描述：
Lily的所有图片按照从小到大的顺序输出

import sys

print(''.join(sorted(input())))


HJ1
字符串最后一个单词的长度
简单

import sys
print(len(input().split()[-1]))


HJ2
计算某字符出现次数
简单
import sys
#import re

#print(input().upper().count()input().upper()))
a=input().upper()
b=input().upper()
#c=a.count(b)
print(a.count(b))

#print(input().lower().count(input().lower()))
HJ4
字符串分隔
简单import sys

l=input()
for i in range(0,len(l),8):
    print("{:0<8s}".format(l[i:8+i]))

#[i:8+i] list[] 数组 
#:0<8s 8s 8位 string 精度 < 左对齐，补0
HJ5import sys

# while True:
#     try:
#         strs = input()
#         strs = int(strs,16)
#         print (strs)
#     except:
#         break    
print(int(input(),16))



进制转换
简单
HJ6import sys
import math

num = int(input())
for i in range(2,int(num**0.5)+1):
    while num%i==0:
        print(i,end=' ')
        num=num/i
if(num>=2):
    print(int(num))









质数因子
简单
HJ8
合并表记录
简单import sys

c = int(input())
s = {}

for i in range(c):
    key,value=map(int,input().split())
    if key in s.keys():
        s[key]+=value
    else:
        s[key]=value
for key in sorted(s.keys()):
    print("%s %s"%(key,s[key]))


 
   
HJ10
字符个数统计
简单import sys
print(len(set(input())))
HJ11
数字颠倒
简单import sys
#print("".join(reversed(list(input())))) 
print("".join(reversed(input()))) 
# print(''.join(input()[::-1]))
HJ12
字符串反转
简单import sys

# print("".join(reversed(input())))
# print("".join(reversed(list(input()))))
# print(input()[::-1])
print(''.join(input()[::-1]))

HJ13
句子逆序
简单import sys


#print(' '.join(reversed(input().split())))
# print(' '.join(input().split()[::-1]))


print(' '.join(input().split()[::-1]))
HJ14
字符串排序
简单import sys
s = []

for i in range(int(input())):
    s.append(input())
print('\n'.join(sorted(s)))        

HJ15
求int型正整数在内存中存储时1的个数
简单import sys
print(bin(int(input())).count('1'))


HJ21
简单密码
简单import sys

dic = {
    "a": "2",
    "b": "2",
    "c": "2",
    "d": "3",
    "e": "3",
    "f": "3",
    "g": "4",
    "h": "4",
    "i": "4",
    "j": "5",
    "k": "5",
    "l": "5",
    "m": "6",
    "o": "6",
    "n": "6",
    "p": "7",
    "q": "7",
    "r": "7",
    "s": "7",
    "t": "8",
    "u": "8",
    "v": "8",
    "w": "9",
    "x": "9",
    "y": "9",
    "z": "9",
    "A": "b",
    "B": "c",
    "C": "d",
    "D": "e",
    "E": "f",
    "F": "g",
    "G": "h",
    "H": "i",
    "I": "j",
    "J": "k",
    "K": "l",
    "L": "m",
    "M": "n",
    "N": "o",
    "O": "p",
    "P": "q",
    "Q": "r",
    "R": "s",
    "S": "t",
    "T": "u",
    "U": "v",
    "V": "w",
    "W": "x",
    "X": "y",
    "Y": "z",
    "Z": "a",
}
for i in input():
    if i in dic:
        print(dic[i], end="")
    else:
        print(i, end="")

HJ22
汽水瓶
简单import sys
while True:
    try:
        n = int(input())
        if n==0:
            break
        else:
            b=n//2
        print(b)

  
    except:
        break

HJ23
删除字符串中出现次数最少的字符
简单import sys

s = input()
dic = {}
for i in s:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
m=min(dic.values())
# print(m)
for i in s:
    if dic[i] == m:
        s=s.replace(i,'')
print(s)

HJ31
单词倒排
简单import sys
n = input()
for i in n:

    if not i.isalpha():
        n = n.replace(i,' ')

print(' '.join(n.split()[::-1]))
HJ34
图片整理
简单import sys

print(''.join(sorted(input())))

HJ35
蛇形矩阵

import sys

n = int(input())
a = [[0]*n for _ in range(n)]
for i in range(0, n):
    for j in range(0,n):
        if i == 0:
            # print( (i+1) * (i + 2) / 2)
            a = (j+1)*(j+2)/2
            print()
        else:
            a[i][j] = a[i - 2][j + 1] - 1
            # a = a.append(a[i - 1][j])
            print(a[i][j], end=" ")
            
            
简单
HJ37
统计每个月兔子的总数
简单


import sys
n = int(input())
n1 = 1
n3 = n2 = 2
if n <= 2:
    print(1)
for i in range (2,n):
    n3 = n2
    n2 = n1 + n2
    n1 = n3
print(n3)        

HJ40
统计字符
简单import sys
s=input()
al=di=sp=ot=0
for i in s:
    if i.isalpha():
        al+=1
    elif i.isspace():
        sp+=1
    elif i.isdigit():
        di+=1
    else:
        ot+=1
print(al)
print(sp)
print(di)
print(ot)

HJ51
输出单向链表中倒数第k个结点
简单import sys

# n,m,o=int(input()),input().split(),int(input())
# print(m[len(m)-o])

# class linknode:
#     def __init__(self,val):
#         self.val=val
#         self.next=None
# a = int(input())        
# b = input().split()        
# c = int(input())        
# one = f_node=linknode(b[0])
# for i in b[1:]:
#     one.next = linknode(i)
#     one = one.next
# two = f_node
# for j in range(a-c):
#     two = two.next
# print(two.val) 

while True:
    try:        
        class linknode:
            def __init__(self,val):
                self.val=val
                self.next=None
        a = int(input())        
        b = input().split()        
        c = int(input())        
        one = f_node=linknode(b[0])
        for i in b[1:]:
            one.next = linknode(i)
            one = one.next
        two = f_node
        for j in range(a-c):
            two = two.next
        print(two.val)
    except: break    


HJ53
杨辉三角的变形
简单import sys
# 打印10行规律就出来，分别在2324位置
a = int(input())
if a in range(1, 3):
    print(-1)
elif (a - 2) % 4 == 1:
    print(2)
elif (a - 2) % 4 == 2:
    print(3)
elif (a - 2) % 4 == 3:
    print(2)
elif (a - 2) % 4 == 0:
    print(4)

HJ54
表达式求值
简单import sys

# eval() 函数用来执行一个字符串表达式，并返回表达式的值
print(int(eval(input())))

HJ56
完全数计算
简单import sys

# s=int(input())
# #s=5*10**5
# c=0
# for i in range(1,s):
#     n = 0
#     for j in range(1,i//2+1):
#         if i%j == 0:
#             n+=j
#     if i == n:
# #        print(i,end=' ')
#         c+=1        
# print(c)
#6,28,496,8128

# while True:
#     try:
#         a = int(input())
#         print(len(list(filter(lambda x: x < a, [6, 28, 496, 8128]))))
#     except:
#         break

while True:
    try:
        a = int(input())
        print(len(list(filter(lambda x:x<a,[6, 28, 496, 8128]))))
    except: 
        break


HJ60
查找组成一个偶数最接近的两个素数
简单import sys

def isa(x):
    for i in range(2,int(pow(x,0.5))+1):
        if x%i == 0:
            return False
        else:
            continue
    return True

s = int(input())
m,n,min = 0,0,s
for j in range (2,s):
    if isa(j) and isa(s - j) and 0 <= s-2*j <min :
        m,n=j,s-j
        min=s - 2 * j
print(m)
print(n)
HJ61
放苹果
简单import sys

def a(m,n):
    if m in range(0,2) or n == 1:
        return 1
    if m<n:
        return a(m,m)
    else:
        return a(m,n-1) + a(m-n,n)
# b,c=map(int,input().split())

bb=(input().split())
b= int(bb[0])
c= int(bb[1])
print(a(b,c))        

# 实现思路
# 我们递归的最终结果是要返回solution(m,n)
# 递归退出条件：
# 如果没有苹果，则说明放置已经完成，方案已定，只能为1
# 如果有一个苹果，则放在剩下哪一个盘子中都是一样的，因此方案数也是1
# 如果只有一个盘子，则手上的苹果必须全部放在这一个盘子中，因此方案数也是1
# 如果盘子数量大于苹果数量
# 则必定有n-m个盘子空着，所以必定的事件不会影响方案数
# 如果盘子数量小于等于苹果数量
# 则考虑是不是要放满所有的盘子
# 如果要空一个盘子，则有solution(m,n-1)种方案
# 如果不要空这些盘子，则相当于所有盘子里至少会放一个苹果，那就相当于每个盘子都拿掉一个苹果，放了也白放不影响方案数量，因此有solution(m-n,n)种方案         
HJ62
查找输入整数二进制中1的个数
简单import sys
while True:
    try:
        print(bin(int(input())).count('1'))
    except: break    




HJ72
百钱买百鸡问题
简单import sys

# for i in range (0,21):
#     for j in range(0,34):
#         for k in range(1,101):
#             if i + j + k == 100 and i * 5 + j * 3 + k * 1/3 == 100:
#                 print(i,j,k)

for i in range(0, 21):
    for j in range(0, 34):
        k = 100 - i -j
        if i* 5 + j * 3 + k * 1/3 == 100:
            print(i,j,k)

HJ73
计算日期到天数转换
简单import sys
import datetime
print(datetime.datetime(*map(int,input().split())).strftime("%j").lstrip("0"))

HJ76
尼科彻斯定理
简单import sys
n=int(input())
s=[]
for i in range(0,n):
    s.append(str(n*n-n+1+2*i))
    s.append('+')
s.pop()
print(''.join(s))    


#    本来不知道可以用数学公式直接推导，在设计程序过程中发现了这个公式。
#         对于数字n来说，其是由n个连续奇数相加得到的，因此第一反应是求出来n3次方然后除以n，可以得到一个位于中间的数字n2，但是发现n2与n的奇偶性相同，需要进行处理。那就先假设，当n2是奇数的时候不处理，当n2是偶数的时候进行-1操作。
#         到这，就开始想怎么求出这个数前后的数字，分别计算前后感觉有点麻烦，就想着能不能直接计算出第一个数字，然后后面通过一个循环，在第一个数字的基础上加上i*2就行了。试了几次，发现了规律，第一个数字就是n2-n+1。
#         后面就直接根据公式编bug了。
# 2 2 2 8 4


HJ80
整型数组合并
简单import sys

a, b, c, d = input(), input().split(), input(), input().split()
print("".join(map(str, sorted(map(int, set(b + d))))))

#set 升序去重合并， 题目要求的，示例 要求 排序 sorted
HJ81
字符串字符匹配
简单import sys

a,b=set(input()),set(input())
print("true" if a&b==a else "false")
# python两行代码解决，思路：
# 使用set，集合的交。

HJ83
二维数组操作
简单import sys


def creat_table(x, y):
    if 0 <= x <= 9 and 0 <= y <= 9:
        global mytable
        mytable = [[i + j for j in range(y)] for i in range(x)]
        print("0")
    else:
        print("-1")


def func(x, a):
    return True if x < a else False


def change_table(x1, y1, x2, y2):
    # if all(map(func, [x1, x2], [a, a])) and all(map(func, [y1, y2], [b, b])) and a+1 <=9 and b+1 <=9:
    if all(map(func, [x1, x2], [a, a])) and all(map(func, [y1, y2], [b, b])):
        mytable[x1][y1], mytable[x2][y2] = mytable[x2][y2], mytable[x1][y1]
        print("0")
    else:
        print("-1")


def insert_row(x):
    if func(x, a) and a + 1 <= 9:
        mytable.insert(x - 1, [j for j in range(b)])
        mytable.pop()

        print("0")
    else:
        print("-1")


def insert_corl(x):
    if func(x, b) and b + 1 <= 9:
        for i in range(a):
            mytable[i].insert(i, x - 1)
            mytable[i].pop()
        print("0")
    else:
        print("-1")


def search(x, y):
    # if func(x, a) and a + 1 <= 9 and func(y, b) and b + 1 <= 9:    
    if func(x, a)  and func(y, b):
        print("0")
    else:
        print("-1")


while True:
    try:
        a, b = map(int, input().split())
        creat_table(a, b)
        c1, c2, d1, d2 = map(int, input().split())
        change_table(c1, c2, d1, d2)
        e = int(input())
        insert_row(e)
        f = int(input())
        insert_corl(f)
        g1, g2 = map(int, input().split())
        search(g1, g2)
    except:
        break

HJ84
统计大写字母个数
简单import sys

print(sum(map(str.isupper,input().strip())))

HJ85
最长回文子串
简单import sys

l = input()
m = 0
for i in range (len(l)):
    for j in range(i,len(l)):
        if l[i:j+1] == l[i:j+1][::-1] and j - i +1 > m:
            m = j -i +1
print(m)            
HJ86
求最大连续bit数
简单import sys

# l=int(input())
print(len(max(bin(int(input()))[2:].split('0'))))
HJ87
密码强度等级
简单import sys
while 1:
    try:
        ia = input()
        f1 = 0
        if len(ia)<=4:
            f1 = 5
        elif len(ia) >= 8:
            f1 = 25
        else:
            f1 = 10

        alo=alu=di=ot=oot=0
        f2=f3=f4=0
        for i in range(len(ia)):
            if ia[i].isupper():
                alu += 1
            elif ia[i].islower():
                alo += 1            
            elif ia[i].isdigit():
                di += 1
            elif ia[i].isascii():
                ot += 1    
            else :
                oot += 1

        # print(ot,end='ot')
        al = alu+alo
        if al == 0:
            f2 = 0
        elif alu > 0 and alo >0:
            f2 = 20
        else :
            f2 = 10

        if di == 0:
            f3 = 0
        elif di == 1:
            f3 = 10
        else :
            f3 = 20      

        # print(,end='ot')
        if ot == 0:
            f4 = 0
        elif ot == 1:
            f4 = 10
        else :
            f4 = 25

        f5 = 0
        if alu >0 and alo >0 and di >0 and  ot > 0:
            f5=5        
        elif al >0 and di >0 and  ot > 0:
            f5=3        
        # elif al >0 and di >0:
        #     f5=2
        else :
            f5=2    

        sum =0
        sum = f1 + f2 +f3+ f4+ f5
        # print(f1,f2,f3,f4,f5,end=' ')

        # print(sum,end=' ')
        if sum >= 90:
            print("VERY_SECURE")
        elif sum >= 80:
            print("SECURE")                  
        elif sum >= 70:
            print("VERY_STRONG")        
        elif sum >= 60:
            print("STRONG")        
        elif sum >= 50:
            print("AVERAGE")        
        elif sum >= 25:
            print("WEAK") 
        else :
            print("VERY_WEAK")      
    
    
    except: break


HJ91
走方格的方案数
简单import sys

def dg(n,m):
    if n<0 or m < 0:
        return 0
    elif n == 0 or m == 0:
        return 1
    else:
        return dg(n-1,m) + dg(n,m-1)
#起点x到终点y的走法 等于 终点y 到x 的走法
#沿着横方向走一步，剩余 dg(n-1,m)种走法 
#沿着纵方向走一步，剩余 dg(n,m-1)种走法 
#走到边界 n or m = 0 就只有沿着边界方向1种走法


n,m=map(int,input().split())
print(dg(n,m))


HJ94
记票统计
简单import sys

a1 = int(input())
a2 = input().split()
a3 = int(input())
a4 = input().split()
# print(a1,a2,a3,a4)

b1=s=c=0

for i in range (a1):
    # print(i,'i')    
    b1 = a4.count(a2[i])
    s = s + b1
    print(a2[i],':',b1)
s=a3-s
print('Invalid :' ,s)    




HJ96
表示数字
简单import sys

import re
s = input().strip()
print(re.sub(r'([0-9]{1,})',r'*\1*',s))
#r-此顶4个\,代表原生的意思，否则不生效，re.sub 1,2,3 类似于 sed 1 需要被替换的字符，2，替换的，3 对象
HJ97
记负均正
简单import sys


def ooo(x, y):
    a, b,c = [], [],[]
    for i in num_list:
        if i > 0:
            a.append(i)
        elif i < 0:
            b.append(i)
        else :
            c.append(i)

    # if sum(c) == 0:
    #     print("0 0.0")

    if len(a) == 0:
        print("0 0.0")
    else:
        print(len(b), round(sum(a) / len(a), 1))


n = int(input())
# print (n)
num_list = list(map(int, input().split()))

if n == 0 :
# if n == 0 or n == 3:
    print("0 0.0")
else:
    ooo(n, num_list)

HJ99
自守数
简单import sys

n = int(input())
c = 0
d = 0
for i in range(0, n + 1):
    d = 0
    d=i*i
    if str(i) == str(d)[-len(str(i)):]:
        c += 1
print(c)
#d = i*i str(d)=str(i*i)
#[-len(str(i)):]截取最后str(i)位匹配,str 让人类看懂
HJ100
等差数列
简单import sys

s=int(input())
# w=3*s+2 
#第一项 2+(3*0) 2+3(3*1)=5 3 2+3+3(3*2)=8  
# L=range(2,w,3)
ii=ss=0
# print(s)
for i in range(0,s):
    # print(i,end=' ')
    ii=2+i*3
    ss=ss+ii
print(ss)
# print(sum(L)) 
HJ102
字符统计
简单import sys

s = input()
s1 = sorted(set(s))
s2=sorted(s1,key=lambda x:s.count(x),reverse=True)
print(''.join(s2))
#sorted（a,key,reverse=） ascii 顺序排序， a 操作对象 key 规则，reverse= true or false 降序 or 升序


HJ105
记负均正II
简单import sys

a=[]
os=[]
ob=[]

while 1:
    try:
        i = int(input())
        if i>=0:
            ob.append(i)
        else:
            os.append(i)   
    except EOFError: break

#这个题需要注意对文件结束的处理。以往的题目都是有确定数量的输入，可以在try里按既定数量获取input()，这一题是不定长的输出，只能判断文件结束符。方法见except
#重点重点重点，在python中对文件结束符的判断，可以用except EOFError来获取。没有碰到结束符之前，只记录输入，碰到结束符之后，处理输出。



print(len(os))
   
print(round(sum(ob)/len(ob),1) if ob else 0.0)  
    


HJ106
字符逆序
简单import sys

# string = str(input().strip()) 
# print(string[::-1])

print(str(input().strip())[::-1])
HJ108
求最小公倍数
简单
#include <stdio.h>

int main() {
    int a, b;
    while (scanf("%d %d", &a, &b) != EOF) { // 注意 while 处理多个 case
        // 64 位输出请用 printf("%lld")
        printf("%d\n", a + b);
    }
    return 0;
}
