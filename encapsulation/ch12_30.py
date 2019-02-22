"""__repr和__str__用法一樣"""

class Name():
    
    def __init__(self,name):
        self.uname=name
        
    def __str__(self):
        return '%s' % self.uname
    __repr__ = __str__

a=Name("hung")
print(a)


