class ROCidCheck():
    # 身分證驗證
    def __init__(self, uname):
        self.name = uname  # 驗證者姓名
        self.__id = ""  # 驗證者身分證字號

    def roc_check(self, rocid):
        id_len = len(rocid)  # 計算長度
        # 身份證字號中key對應的value表
        roc_list = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14,
                    "F": 15, "G": 16, "H": 17, "I": 34, "J": 18, "K": 19,
                    "M": 21, "N": 22, "O": 35, "P": 23, "Q": 24, "T": 27, "U": 28,
                    "V": 29, "W": 32, "X": 30, "Z": 33, "L": 20, "R": 25, "S": 26, "Y": 31}
        # 檢查身份證字號長度必須為10
        if id_len != 10:
            print(self.name.title(), "輸入的身分證有誤，請重新確認")
        else:
            id_key = rocid[0]
            if id_key in roc_list:
                # 轉換對應的value
                id_value = roc_list[id_key]
                # 先計算英文的部分
                n1 = int(id_value / 10)
                n2 = id_value % 10
                # 計算數字的部分要轉型
                # 公式驗證
                id_check = n1 * 1 + n2 * 9 + int(rocid[1]) * 8 + int(rocid[2]) * 7 + \
                           int(rocid[3]) * 6 + int(rocid[4]) * 5 + int(rocid[5]) * 4 + int(rocid[6]) * 3 + \
                           int(rocid[7]) * 2 + int(rocid[8]) * 1 + int(rocid[9]) * 1
                if id_check % 10 == 0:
                    print(self.name.title(), "您的身分證驗證正確")
                else:
                    print(self.name.title(), "您的身分證驗證錯誤")
            else:
                print("第一個字母輸入有誤")


# 建立物件並呼叫
name = ROCidCheck("patty")
check = input("請輸入身份證字號:")
name.roc_check(check)


