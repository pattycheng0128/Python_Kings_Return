fn = "test2.txt"
str1 = "I Love Python."
str2 = "Learn Python from the best book."

with open(fn,'w') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')
