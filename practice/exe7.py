ch = input("請輸入字元")

if (ord(ch) >= ord("A")) and (ord(ch) <= ord("Z")):
    print(ch.lower())
elif (ord(ch) >= ord("a")) and (ord(ch) <= ord("z")):
    print(ch.upper())
elif (ord(ch) >= ord("0")) and (ord(ch) <= ord("9")):
    print(int(ch))
else:
    print("輸入錯誤")