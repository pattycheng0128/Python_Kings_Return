import traceback

def division(x, y):
    try:
        return x/y
    except:
        errlog = open("error15_17.txt", "a")
        errlog.write(traceback.format_exc())
        errlog.close()
        print("將錯誤寫入完成")
        print("異常發生")

print(division(6, 2))
print(division(5, 0))
print(division("a", "b"))

