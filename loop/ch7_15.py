n = int(input("請輸入整數:"))
sum = 0
for i in range(n+1):
    sum += i
print("從1到%d的總和是:" % n, sum)