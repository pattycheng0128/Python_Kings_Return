i = 1
while i <= 9:  # 外層迴圈
    j = 1
    while j <= 9:  # 內層迴圈
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end=" ")
        j += 1
    print()
    i += 1