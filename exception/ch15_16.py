import traceback

def passWord(pwd):
    pwdlen = len(pwd)
    if pwdlen < 5:
        raise Exception("密碼長度不足")
    if pwdlen > 8:
        raise Exception("密碼長度太長")
    print("密碼長度正確")

for password in ("aaaa", "bbbbbbbbb", "ccccc"):
    try:
        passWord(password)
    except Exception as err:
        errlog = open("error15_16.txt", "a")
        errlog.write(traceback.format_exc())
        errlog.close()
        print("將錯誤寫入error.txt")
        print("密碼長度異常發生:", str(err))