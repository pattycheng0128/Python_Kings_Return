"""___str__可以協助返回易讀取的字串"""
class Name():
    
    def __init__(self, name):
        self.uname = name

    def __str__(self):
        return "%s" % self.uname
    
a = Name("Lala")
print(a)