password = "123456"
pwd = input("請輸入密碼")
if pwd != password and pwd == "":
    print("密碼有誤或密碼未輸入")
elif pwd == password:
    print("密碼驗證正確")
else:
    print("其他錯誤")