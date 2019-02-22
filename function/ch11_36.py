mylist = [4, 3, 9, 6]

oddlist = list(filter(lambda x: (x % 2 == 1), mylist))
print(oddlist)