numset = {1, 2, 3}
deep_numset = numset
deep_numset.add(10)
print("深度拷貝numset:", numset)
print("深度拷貝deep_numset", deep_numset)

print("-------------------------")
# 淺拷貝，不會影響另一個集合
shallow_numset = numset.copy()
shallow_numset.add(100)
print("淺拷貝numset:", numset)
print("淺拷貝shallow_numset", shallow_numset)