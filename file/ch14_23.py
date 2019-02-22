fn = "test.txt"
with open(fn) as file_Obj:
    data = file_Obj.read()
    newdata = data.replace("癌症","cancer")
    print(newdata)
