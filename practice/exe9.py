class InformationEngineering():

    def __init__(self):
        self.student = ["Ken", "Lulu", "Lily", "Penny", "John"]

    def studentlist(self):
        print("目前學生名單:", self.student)
        print("輸入1:新增資料,2:移除資料,其他:離開選單")
        try:
            num = int(input("請選擇要修改的選單:"))
            if num == 1:
                name = input("請輸入要新增的學生姓名")
                self.student.append(name)
                print("目前學生名單:", self.student)
            elif num == 2:
                name = input("請輸入要移除的學生姓名")
                self.student.remove(name)
                print("目前學生名單:", self.student)
            else:
                print("離開選單")
        except Exception:
            print("您輸入錯誤的內容或大小寫有誤")


test = InformationEngineering()
test.studentlist()