fstream1 = open("test1.txt", mode="w") # 取代先前的資料
print("Test Hello", file=fstream1)
fstream1.close()
fstream2 = open("test2.txt", mode="a") # 取代先前的資料
print("Test Hello", file=fstream2)
fstream2.close()