soldier0 = {'tag': 'red', 'score': 3, 'ypos': 30, 'xpos': 100, 'speed': 'high'}
print("小兵的x、y座標:", soldier0['xpos'], soldier0["ypos"])
if soldier0["speed"] == "slow":  # 慢
    x_move = 1
elif soldier0["speed"] == "medium":  # 中
    x_move = 3
else:
    x_move = 5  # 快

soldier0["xpos"] += x_move
print("小兵的x、y座標:", soldier0['xpos'], soldier0["ypos"])
