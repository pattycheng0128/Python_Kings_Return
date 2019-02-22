username = "admin"
password = "123456"
user = input("請輸入帳號:")
pwd = input("請輸入密碼:")

if user == username and pwd == password:
    print("帳號和密碼驗證正確")
else:
    print("帳號和密碼輸入錯誤")
