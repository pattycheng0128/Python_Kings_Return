"""isinstance用來判斷兩個物件是否一樣"""


class Grandfather():
    pass

class Father(Grandfather):
    pass

class Ivan(Father):

    def fn(self):
        pass

# 呼叫
grandfather = Grandfather()
father = Father()
ivan = Ivan()
#測試iva
print("ivan屬於Ivan類別:",isinstance(ivan, Ivan))
print("ivan屬於Father類別:",isinstance(ivan, Father))
print("ivan屬於Grandfather類別:",isinstance(ivan, Grandfather))
#測試father
print("father屬於Father類別:",isinstance(father, Father))
print("father屬於ivan類別:",isinstance(father, Ivan))
print("father屬於Grandfather類別:",isinstance(father, Grandfather))
#測試grandfather
print("grandfather屬於Grandfather類別",isinstance(grandfather, Grandfather))
print("grandfather屬於Father類別",isinstance(grandfather, Father))
print("grandfather屬於Ivan類別",isinstance(grandfather, Ivan))
