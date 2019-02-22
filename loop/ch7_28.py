msg1 = "Hello"
msg2 = "Every"
msg = msg1 + " " + msg2
active = True
while active:
    input_msg = input(msg)
    if input_msg != "q":
        print(input_msg)
    else:
        active = False
