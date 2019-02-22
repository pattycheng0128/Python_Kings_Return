mylist = [25, 18, 12, 22, 31, 17, 26, 19, 18, 10]
nbaliat = list(filter(lambda x: (x > 20), mylist))
print(nbaliat)

"""傳統寫法
def nbalist(x):
    if (x > 20):
        return x
    
list = [25, 18, 12, 22, 31, 17, 26, 19, 18, 10]
filter_obj = filter(nbalist, list)

for item in filter_obj:
    print(item)"""