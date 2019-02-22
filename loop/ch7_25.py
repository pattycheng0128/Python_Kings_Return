num = int(input("請輸入>1的整數做質數測試:"))

if num == 2:
    print("%d是質數" % num)
else:
    for n in range(2, num):
        if num % 2 == 0:
            print("%d不是質數" % num)
            break
    else:
        print("%d是質數" % num)