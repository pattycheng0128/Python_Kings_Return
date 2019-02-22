#傳回多筆資料的應用
def mutifunction(x,y):
    add = x+y
    sub = x-y
    mul = x*y
    div = x/y
    return add, sub, mul, div
add, sub, mul, div = mutifunction(4,2)
print("加法:", add)
print("減法:", sub)
print("乘法:", mul)
print("除法:", div)