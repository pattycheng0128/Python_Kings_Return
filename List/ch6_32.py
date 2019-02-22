James = [["James", "SF", "2018/11/20"], 23, 17, 40]
games = len(James)  # 計算串列長度
score_max = max(James[1:games])  # 最高得分
i = James.index(score_max)  # 最高得分的場次
name = James[0][0]
position = James[0][1]
born = James[0][2]
print("姓名:", name)
print("位置:", position)
print("生日:", born)
print("在第%d場得最高分%d" % (i, score_max))
