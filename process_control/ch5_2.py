num = input("輸出任意數字:")
x = int(num)
# if x < 0:
#     x = abs(x)
if int(x) < 0: x = abs(x) # 3和4行可以用一行代替
print("絕對值是%d" % int(x))