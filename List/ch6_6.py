# 當list裡有參雜字串和數字時，要指定索引範圍才不會造成錯誤
James = ["Lebron James", 22, 19, 31, 18]
print("最高得分:", max(James[1:4]))
print("最低得分:", min(James[1:4]))
print("得分總計:", sum(James[1:4]))