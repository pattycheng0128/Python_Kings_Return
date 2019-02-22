def printmsg():
    msg = "Local Variable"
    print("在printmsg()裡，這是區域變數", msg)

def printing():
    print(msg)

msg = "Global Variable"
print("主程式，這是全域變數", msg)
printmsg()
printing()
