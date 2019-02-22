fields = ["Name", "Age", "country"]
info = ["Penny", "30", "Taiwan"]
zipData = zip(fields, info)
print(type(zipData))
player = list(zipData)
print(player)

# unzip
f, i = zip(*player)
print("fields:", f)
print("info:", i)