msg1 = "Hello"
msg2 = "Every"
msg = msg1 + " " + msg2
while True:
    input_msg = input(msg)
    if input_msg == "q":
        break
    else:
        print(input_msg)
