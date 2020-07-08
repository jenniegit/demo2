#-*- codeing = utf-8 -*-
#@Time : 2020/7/6 15:21
#@Author : 小白
#@File : demo3.py
#@Software : PyCharm

'''
password = input("请输入密码：")
print("您刚刚输入的密码是：",password)
'''
'''
password = int(input("请输入密码："))
print("您刚刚输入的密码是：",password)
print(type(password))
'''
'''
for i in range(5):
    print(i)
'''
'''
for i in range(0,13,3):
    print(i)
'''

'''
for i in range (-10,-100,-30):
    print(i)
'''

'''
a = ["aa","bb","cc","dd"]
for i in range(len(a)):
    print(i,a[i])
'''
'''
i = 0
while i < 5 :
    print("当前是第%d次执行循环"%(i+1))
    print("i=%d"%i)
    i += 1
'''

'''
#1-100求和
n = 100
sum = 0
conter = 1
while conter <= n:
    sum = sum + conter
    conter += 1
print("1到%d 的和为%d"%(n,sum))
'''
'''
#求和1-100
i = 1 #初始化i
sumNum = 0  #初始化和
while i <= 100:
    sumNum = sumNum + i #第一次为和为0+1，sumNum变成1，第二次就用1+i，依此类推
    i += 1  #i循环一次加一
print(sumNum)   #打印最后结果
'''
'''
sum = 0
for i in range(1,101):
    sum = sum + i
    i += 1
print (sum)
'''

#1到100求和
'''
n = 100
sum = 0
conter = 1
while conter <= 100:
    sum = conter + sum
    conter += 1
print(sum)
'''

'''
sum = 0
for i in range(1,101):
    sum = sum + i
    i += 1
    print (sum)
'''
'''
for i in range(1,101):
    print(i)
'''

