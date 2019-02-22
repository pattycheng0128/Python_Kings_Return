fn = "test.txt"
with open(fn) as file_Obj:
    for line in file_Obj:
        # print(line)
        print(line.rstrip())
