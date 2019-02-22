msg1 = "Hello!"
msg2 = "How are you~"
msg = msg1 + "\n" + msg2
input_quite = ""  # 預設為空字串

while input_quite != "q":
    input_quite = input(msg)
    if input_quite != "q":  # 輸入不是q才輸出訊息
        print(input_quite)