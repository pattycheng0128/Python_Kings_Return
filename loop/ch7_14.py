# sum = 0
# # for i in range(11):
# #     sum += i
# # print(sum)

n = int(input("請輸入整數:"))
number = list(range(n+1))
sum = 0
for i in number:
    sum += i
print("從1到%d的總和" % n, sum)