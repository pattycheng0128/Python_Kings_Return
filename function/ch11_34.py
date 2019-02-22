def oddfn(x):
    return x if(x % 2 == 1) else None

mylist = [4, 3, 9, 6, 44, 33]
filter_object = filter(oddfn, mylist)

# 印出奇數串列
# print("奇數串列", [item for item in filter_object])
# 和下列這行一樣
for item in filter_object:
    print(item)