def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

# 程式運算
while True:
    print("===算式運算===")
    print("1.加法 2.減法 3.乘法 4.除法")
    op = input("請輸入選擇(q 結束):")
    if op == "q":
        break
    else:
        op = int(op)  # 轉型
    a = int(input("請輸入a:"))
    b = int(input("請輸入b:"))
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

