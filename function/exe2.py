def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y
print("請輸入運算")
print("1.加法")
print("2.減法")
print("3.乘法")
print("4.除法")

op = int(input("請輸入選擇:"))
a = int(input("請輸入a:"))
b = int(input("請輸入b:"))

# 程式運算
if op == 1:
    print("a+b=", add(a, b))
elif op == 2:
    print("a-b=", sub(a, b))
elif op == 3:
    print("a*b=", mul(a, b))
elif op == 4:
    print("a/b=", div(a, b))
else:
    print("輸入錯誤")