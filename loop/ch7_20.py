# 直角三角形
for i in range(1, 6):
    for j in range(1, 6):
        if j <= i:
            print("*", end=" ")
    print()
print()
# 倒直角三角形
for i in range(6, 1, -1):
    for j in range(6, 1, -1):
        if j <= i:
            print("*", end=" ")
    print()
