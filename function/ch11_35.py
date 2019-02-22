def oddfn(x):
    return x if(x % 2 == 1) else None

mylist = [4, 3, 9, 6, 44, 33]
filter_object = filter(oddfn, mylist)

# 印出奇數串列
oddlist = [item for item in filter_object]
print(oddlist)
