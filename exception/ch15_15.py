def passWord(pwd):
    pwdlen = len(pwd)
    if pwdlen < 5:
        raise Exception("密碼長度不足")
    if pwdlen > 8:
        raise Exception("密碼長度太長")
    print("密碼長度正確")


for password in ("aaaa", "bbbbbbbbbb", "cccccc"):
    try:
        passWord(password)
    except Exception as err:
        print("密碼長度檢查異常:", str(err))
