"""列出類別物件與物件內方法的資料型態"""
class Grandfather():
    pass


class Father(Grandfather):
    pass


class Ivan(Father):

    def fn(self):
        pass


grandfather = Grandfather()
father = Father()
ivan = Ivan()
print("grandfather",type(grandfather))
print("grandfather",type(father))
print("grandfather",type(ivan))
